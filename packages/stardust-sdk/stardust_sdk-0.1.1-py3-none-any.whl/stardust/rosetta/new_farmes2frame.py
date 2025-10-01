import os
import json
import numpy as np
from glob import glob
from tqdm import tqdm
from typing import Union, Optional
from concurrent.futures import ProcessPoolExecutor, as_completed

from stardust.rosetta.new_structure import Slot
from stardust.rosetta.mapping_structure import SlotMapping
from stardust.components.camera import Camera
from stardust.utils.frames import *


# Definition of sequential frames
class Frames:
    sequence_type_list = ["IMAGE_SEQUENCE", "IMAGE_SET_SEQUENCE", "POINTCLOUD_SEQUENCE", "POINTCLOUD_SET_SEQUENCE"]

    @classmethod
    def read_json(cls, path: str):
        with open(path) as fp:
            cls._ = json.load(fp)

    def __init__(self, path: str):
        self.read_json(path)
        self.path = path
        record: dict = self._['taskParams']['record']
        self.attachment_type: str = record['attachmentType']
        assert self.attachment_type in self.sequence_type_list, 'Not supported'
        self.projectId: int = self._['projectId']
        self.datasetId: int = self._['datasetId']
        self.poolId: int = self._['poolId']
        self.taskId: int = self._['taskId']
        self.status: int = self._['status']
        self.attachment: list = record['attachment']
        self.attachment_length: int = len(record['attachment'])
        self.metadata: dict = record.get('metadata', {})
        self.operators: list = self._['taskParams']['operators']
        self.result_annotations: list = self._['result']['annotations']
        self.result_hints: list = self._['result'].get('hints', [])
        self.result_metadata: dict = self._['result'].get('metadata', {})
        self.error_info: str = f'project{self.projectId}_pool{self.poolId}_task{self.taskId}'

    def frame_structure(self, frame_number) -> dict:
        return {
            "projectId": self.projectId,
            "datasetId": self.datasetId,
            "poolId": self.poolId,
            "taskId": self.taskId,
            "status": self.status,
            "taskParams": {
                "record": {
                    "attachmentType": self.attachment_type.replace("_SEQUENCE", ""),
                    "attachment": self.attachment[frame_number],
                    "metadata": self.metadata
                },
                "operators": self.operators
            }
        }

    @property
    def empty_operators(self):
        return [slot_structure(_) for _ in self.operators]

    def operators_record(self, operators: Optional[list] = None, operators_record: Optional[dict] = None):
        if not operators:
            operators = self.operators
        if operators_record is None:
            operators_record = {}
        for op in operators:
            if op['type'] != 'slotChildren':
                continue
            operators_record.setdefault(op['key'], op['slotSpecification'].get('imageSourceMapping', []))
            self.operators_record(op['children'], operators_record)
        return operators_record

    def annotation_type_factory(self, annotation, frame_number, operators=None) -> callable:
        func = Factory(annotation,
                       frame_number,
                       self.attachment,
                       operators)
        return func.factory(annotation['type'])

    def _normal_frames_split(self, frame_number) -> list:
        normal_annotation_frame_data = []
        for annotation in self.result_annotations:
            normal_annotation_frame_data.append(self.annotation_type_factory(annotation, frame_number))
        return normal_annotation_frame_data

    def _reflection_frames_split(self, frame_number) -> list:
        reflection_annotation_frame_data = []
        operators = self.operators_record()
        for annotation in self.result_annotations:
            reflection_annotation_frame_data.append(self.annotation_type_factory(annotation, frame_number, operators))
        return reflection_annotation_frame_data

    def _frames_split(self, frame_number) -> list:
        if self.result_metadata:
            invalid_frame = self.result_metadata.get('invalidFrame', [])
            if frame_number in invalid_frame:
                frame_annotations = self.empty_operators
            else:
                if self.result_metadata.get('interpolateMethod', '') == 'mapping-first':
                    frame_annotations = self._reflection_frames_split(frame_number)
                else:
                    frame_annotations = self._normal_frames_split(frame_number)
        else:
            frame_annotations = self._normal_frames_split(frame_number)
        return frame_annotations

    def frames_split(self):
        for frame_number in range(self.attachment_length):
            new_path = frame_name(self.path, frame_number)
            new_path = os.path.join(os.path.dirname(new_path), str(self.taskId), os.path.basename(new_path))
            os.makedirs(os.path.dirname(new_path), exist_ok=True)
            with open(new_path, "w") as fw:
                frame_data = self.frame_structure(frame_number)
                try:
                    frame_annotations = self._frames_split(frame_number)
                except Exception as e:
                    print(f'{self.error_info}_frame{frame_number} split failed: {e}')
                    frame_annotations = self.empty_operators
                frame_data['result'] = {
                    'annotations': frame_annotations,
                    'hints': self.result_hints,
                    'metadata': self.result_metadata
                }
                fw.write(json.dumps(frame_data, ensure_ascii=False))
        os.remove(self.path)


class Factory:
    def __init__(
            self,
            annotation: dict,
            frame_number: int,
            attachment: list,
            operators: Optional[list],
            reflection: bool = False
    ):
        self.annotation = annotation
        self.frame_number = frame_number
        self.attachment = attachment
        self.operators = operators
        self.reflection = reflection

    def image_source(self):
        now_attachment = self.attachment[self.frame_number].get('imageSources', [])
        assert now_attachment, 'now_attachment must not be empty'
        return {
            n['name']: {
                'camera': Camera(
                    camera_type=n['camera']['type'],
                    heading=tuple(n['camera']['heading'].values()),
                    position=tuple(n['camera']['position'].values()),
                    intrinsic=tuple(n['camera']['intrinsic'].values()),
                    radial=tuple(n['camera']['radial'].values()),
                    tangential=tuple(n['camera']['tangential'].values())
                ),
                'width': n['width'],
                'height': n['height']
            } for n in now_attachment
        }

    def annotation_slots_children(self, annotation: Optional[dict] = None):
        if not annotation:
            annotation = self.annotation
        slot_children_dict = slot_structure(annotation)
        for slot_children in annotation.get('slotsChildren', []):
            slot_ = self.annotation_slot(slot_children['slot'])
            children_ = []
            children_record = []
            for children in slot_children['children']:
                if self.operators and children['key'] in self.operators[annotation['key']]:
                    children_result = self.factory(children['type'], children, slot_)
                else:
                    children_result = self.factory(children['type'], children)
                children_record.append(empty(children_result))
                children_.append(children_result)
            if isinstance(slot_.label, bool) and np.all(np.array(children_record)):
                continue
            slot_children_dict['slotsChildren'].append({
                'slot': vars(slot_),
                'children': children_
            })
        return slot_children_dict

    def annotation_children_only(self, annotation: Optional[dict] = None):
        if not annotation:
            annotation = self.annotation
        children_only_dict = slot_structure(annotation)
        for children_only in annotation['childrenOnly']:
            children_ = []
            for children in children_only['children']:
                children_.append(self.factory(children['type'], children))
            else:
                children_only_dict['childrenOnly'].append({
                    'id': children_only['id'],
                    'label': children_only['label'],
                    'teamId': children_only.get('teamId', None),
                    'children': children_})
        return children_only_dict

    def annotation_slot(self, annotation: Optional[dict] = None, father: object = None):
        if not annotation:
            annotation = self.annotation
        if annotation['type'] == 'slot':
            slot_dict = slot_structure(annotation)
            for slot_obj in annotation['slots']:
                if father:
                    slot = SlotMapping(slot_obj, father, self.frame_number, self.image_source())
                else:
                    slot = Slot(slot_obj, self.frame_number, self.attachment)
                if isinstance(slot.label, bool):
                    continue
                slot_dict['slots'].append(vars(slot))
            return slot_dict
        else:
            attribute_slot = Slot(annotation, self.frame_number, self.attachment)
            return attribute_slot

    def annotation_input(self, annotation: Optional[dict] = None):
        if not annotation:
            annotation = self.annotation
        input_dict = slot_structure(annotation)
        try:
            input_dict['input'].update(vars(Slot(annotation, self.frame_number))['input'])
        except TypeError:
            return input_dict
        return input_dict

    def factory(self, annotation_type, annotation: dict = None, slot: object = None) -> callable:
        if not annotation:
            annotation = self.annotation
        if annotation_type == 'slotChildren':
            return self.annotation_slots_children(annotation)
        if annotation_type == 'childrenOnly':
            return self.annotation_children_only(annotation)
        if annotation_type == 'slot':
            return self.annotation_slot(annotation, slot)
        else:
            return self.annotation_input(annotation)


def _to_split(path):
    try:
        frames = Frames(path)
    except AssertionError:
        os.rename(path, frame_name(path))
    else:
        frames.frames_split()
    return True


def to_split(input_path):
    file_paths = [file for file in glob(f'{input_path}/**', recursive=True) if file.endswith('.json')]
    bar = tqdm(total=len(file_paths))
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(_to_split, file_path) for file_path in file_paths]
        for future in as_completed(futures):
            if future.result():
                bar.update(1)


if __name__ == '__main__':
    import open3d as o3d
    paths = '/Users/stardust/Downloads/2073'

    # paths = glob('/Users/stardust/Downloads/1953/*.json')
    # frames_ = Frames(paths[0])

    import time

    s = time.time()
    # frames_.frames_split()
    to_split("/Users/mac/Documents/pyproject/sd_sdk/stardust_sdk/Stardust_SDK/data/2201/2201")
    # o = frames.operators_record()
    # print(o)1
    end = time.time()
    print(end - s)
