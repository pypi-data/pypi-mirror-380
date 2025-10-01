"""
Frame splitting utilities.
"""
import os
import json
import numpy
from tqdm import tqdm
from glob import glob
from concurrent.futures.thread import ThreadPoolExecutor

from stardust.rosetta.frame_tools import FrameCapture
from stardust.rosetta.structure import Slot, Input


def get_input(children, frame_number):
    attribute_input = Input(children, frame_number)
    for _ in ['frame_list', 'target']:
        if hasattr(attribute_input, _):
            delattr(attribute_input, _)
    return vars(attribute_input)


def get_slot(slot, frame_number, capture):
    if slot['type'] in FrameCapture.slot_type_list:
        attribute_slot = Slot(slot, frame_number, capture)
        if capture.get_slot_structure(attribute_slot):
            return attribute_slot
        else:
            return False
    elif slot['type'] == 'slot':
        attribute_slot = FrameCapture.get_annotation_struct(slot, 'slots')
        for slot_line in slot['slots']:
            if slot_line['type'] in FrameCapture.slot_type_list:
                slot_dict = Slot(slot_line, frame_number, capture)
                if capture.get_slot_structure(slot_dict):
                    if hasattr(slot_dict, 'capture'):
                        delattr(slot_dict, 'capture')
                    attribute_slot['slots'].append(vars(slot_dict))
        return attribute_slot


def get_slots_children(annotation, frame_number, capture: FrameCapture):
    slots_children_dict = capture.get_annotation_struct(annotation, 'slotsChildren')
    for i in annotation['slotsChildren']:
        result_slot = get_slot(i['slot'], frame_number, capture)
        if not result_slot:
            continue
        children_list = []  # Collect child annotations
        for children in i['children']:
            if children['type'] == 'input':
                result_children = get_input(children, frame_number)
            elif children['type'] == 'slot':
                result_children = get_slot(children, frame_number, capture)
            elif children['type'] == 'slotChildren':
                result_children = get_slots_children(children, frame_number, capture)
            else:
                raise ValueError(f'The children result type {children["type"]} is missing')
            children_list.append(result_children)

        if result_slot:
            if hasattr(result_slot, 'capture'):
                delattr(result_slot, 'capture')
            slots_children_dict['slotsChildren'].append({
                'slot': vars(result_slot),
                'children': children_list})
    return slots_children_dict


def get_children_only(annotation, frame_number, capture):
    children_only_dict = {
        "key": annotation['key'],
        "label": annotation['label'],
        "type": annotation['type'],
        "childrenOnly": []}
    for i in annotation['childrenOnly']:

        children_list = []  # Collect child annotations
        for children in i['children']:
            if children['type'] == 'input':
                result_children = get_input(children, frame_number)
            elif children['type'] == 'slot':
                result_children = get_slot(children, frame_number, capture)
            elif children['type'] == 'slotChildren':
                result_children = get_slots_children(children, frame_number, capture)
            else:
                result_children = {}
                print(f"result_children {children['type']} attribute missing")
            children_list.append(result_children)
        children_only_dict['childrenOnly'].append({
            'id': i['id'],
            'label': i['label'],
            'children': children_list})
    return children_only_dict


def frames_split_task(file_path):
    try:
        frame = FrameCapture(file_path)
    except AssertionError:
        return True
    else:
        for frame_number in range(frame.attachment_length):
            with open(file_path.replace('.json', f'_{str(frame_number).rjust(4, "0")}.json'), "w") as fw:
                frame_data = {
                    "projectId": frame.projectId,
                    "datasetId": frame.datasetId,
                    "poolId": frame.poolId,
                    "taskId": frame.taskId,
                    "status": frame.status,
                    "taskParams": {
                        "record": {
                            "attachmentType": frame.attachment_type.replace("_SEQUENCE", ""),
                            "attachment": frame.attachment[frame_number],
                            "metadata": frame.metadata
                        },
                        "operators": frame.operators
                    }
                }
                annotation_frame_data = []
                for annotation in frame.annotations:
                    try:
                        if annotation['type'] == 'slotChildren':
                            _ = get_slots_children(annotation, frame_number, frame)
                        elif annotation['type'] == 'childrenOnly':
                            _ = get_children_only(annotation, frame_number, frame)
                        elif annotation['type'] == 'input':
                            _ = get_input(annotation, frame_number)
                        elif annotation['type'] == 'slot':
                            _ = get_slot(annotation, frame_number, frame)
                        else:
                            raise ValueError(f'The annotation result type {annotation["type"]} is missing')
                    except numpy.core._exceptions.UFuncTypeError:
                        print(f'{frame_number} encountered invalid boxes')
                    except ValueError as e:
                        print(f'{frame_number} {e}')
                    else:
                        annotation_frame_data.append(_)
                frame_data['result'] = {
                    'annotations': annotation_frame_data,
                }
                fw.write(json.dumps(frame_data, ensure_ascii=False))
        os.remove(file_path)
        return True


def frames_split(input_path):
    file_paths = [file for file in glob(f'{input_path}/**', recursive=True) if file.endswith('.json')]
    bar = tqdm(total=len(file_paths))
    with ThreadPoolExecutor(max_workers=4) as executor:
        executors = executor.map(frames_split_task, file_paths)
        for exe in executors:
            if exe:
                bar.update(1)


# Each instance is split frame-by-frame
def func_ms(ms_data: "ms_data"):
    """
    Iterate over all instances; each may contain a sequence of frames.

    Args:
        ms_data:

    Returns:
        All frames for each instance

    """

    result_lst = list()
    for instance in ms_data['data']['data']:
        if "SEQUENCE" not in instance['record']['attachmentType']:
            result_lst.append([{
                "poolId": None,
                "taskId": None,
                "datasetId": instance['datasetId'],
                "dataInstanceId": instance['dataInstanceId'],
                "projectId": instance['projectId'],
                "algoId": instance['algoId'],
                "versionNum": instance['versionNum'],
                "datasetName": instance['datasetName'],
                "taskParams": {
                    "record": {
                        "attachmentType": instance['record']['attachmentType'].replace("_SEQUENCE", ""),
                        "attachment": instance['record']['attachment'],
                        "metadata": instance['record']['metadata']
                    }
                },
                "result": {
                    "annotations": instance['annotation']
                }
            }, ])

        else:
            frame_numbers = len(instance['record']['attachment'])
            current_instance_data_lst = list()  # Container for all frames of the current instance

            # Iterate per frame
            for frame_number in range(frame_numbers):
                ret_data = {
                    "poolId": None,
                    "taskId": None,
                    "datasetId": instance['datasetId'],
                    "dataInstanceId": instance['dataInstanceId'],
                    "projectId": instance['projectId'],
                    "algoId": instance['algoId'],
                    "versionNum": instance['versionNum'],
                    "datasetName": instance['datasetName'],
                    "taskParams": {
                        "record": {
                            "attachmentType": instance['record']['attachmentType'].replace("_SEQUENCE", ""),
                            "attachment": instance['record']['attachment'][frame_number],
                            "metadata": instance['record']['metadata']
                        }
                    },
                    "result": {
                        "annotations": list()
                    }
                }
                annotation_frame_data = []
                for annotation in instance['annotation']:
                    try:
                        if annotation['type'] == 'slotChildren':
                            _ = get_slots_children(annotation, frame_number, FrameCapture)
                        elif annotation['type'] == 'childrenOnly':
                            _ = get_children_only(annotation, frame_number, FrameCapture)
                        elif annotation['type'] == 'input':
                            _ = get_input(annotation, frame_number)
                        elif annotation['type'] == 'slot':
                            _ = get_slot(annotation, frame_number, frame)
                        else:
                            raise ValueError(f'The annotation result type {annotation["type"]} is missing')
                    except numpy.core._exceptions.UFuncTypeError:
                        print(f'{frame_number} encountered invalid boxes')
                    except ValueError as e:
                        print(f'{frame_number} {e}')
                    else:
                        annotation_frame_data.append(_)
                        break
                ret_data['result']['annotations'] = annotation_frame_data
                current_instance_data_lst.append(ret_data)

            result_lst.append(current_instance_data_lst)

    return result_lst


if __name__ == '__main__':
    for pid in (1953, 2011, 2026):
        # pid = 1337
        dir_path = f'/Users/mac/Documents/pyproject/Chacer/rosetta/{pid}/'

        frames_split(dir_path)
