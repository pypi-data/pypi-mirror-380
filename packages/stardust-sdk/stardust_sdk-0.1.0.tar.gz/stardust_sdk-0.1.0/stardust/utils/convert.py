from typing import Dict, Iterable, List, Optional
from numbers import Number
import re
from pathlib import Path
import json
import glob
import shutil

from stardust.components.annotations import Box2D, Box3D, Input, Line, Point, Polygon, Text
from stardust.components.attachment import Image, PointCloud
from stardust.components.frame import Annotation, Frame, Media, Prediction, TaskInfo
from stardust.rosetta.rosetta_data import RosettaData as Export
from stardust.ms.ms import MS

__all__ = [
    "read_rosetta", "read_ms"
]


def _serialize(obj):
    dic = dict()
    if hasattr(obj, "__dict__"):
        for key, val in obj.__dict__.items():
            if str(key).startswith("__") and str(key).endswith("__"):
                continue
            if str(key) in ("id", "shapely_polygon"):
                continue
            dic[key] = _serialize(val)
    elif isinstance(obj, (str, Number)):
        return obj
    elif isinstance(obj, Dict):
        for key, val in obj.items():
            dic[key] = _serialize(val)
    elif isinstance(obj, Iterable):
        return [_serialize(val) for val in obj]
    return dic


class Convertor:
    def __init__(self) -> None:
        self.project_id = None
        self.input_path = None
        self.pattern = re.compile(r'_(\d+)\.json')

    def yield_rosetta_json(self):
        """
        yield json file from local path which is download from rosetta

        Returns:

        """

        if not (rosetta_json_lst := glob.glob(os.path.join(self.input_path, f"{self.project_id}/json/**/*.json"))):
            rosetta_json_lst = glob.glob(os.path.join(self.input_path, f"{self.project_id}/json/*.json"))

        for file in rosetta_json_lst:
            try:
                with open(file, 'r', encoding='utf-8') as jf:
                    _ = json.load(jf)
                    self.file_name = str(file)
                    __ = Path(file).stem.rsplit("_", 1)[1]
                    if self.pattern.search(str(file)):
                        self.frame_num = int(Path(file).stem.rsplit("_", 1)[1])
                    else:
                        self.frame_num = 0
                    yield _
            except json.decoder.JSONDecodeError as e:
                print(e)
                continue
            except Exception as e:
                raise e

    def factory_children(self, children: "rosetta children",
                         parent_id: str = None):
        """
        Start processing operation subentries, recursion

        Args:
            children:
                rosetta children
            slot_id:
                rosetta slot id

        Returns:
            Dictionary, where key is the id of children and value is the type
        """
        children_lst = dict()
        label_kind = None
        for child in children:
            if child['type'] == "input":
                input_obj = Input.gen_input(child, parent_id)
                children_lst[input_obj.id] = "input"
                if isinstance(input_obj.name, str) and input_obj.name.lower() in ("type", "category"):
                    label_kind = input_obj.value
                self.label_result.input_lst.setdefault(input_obj.id, input_obj)
            elif child['type'] == "slotChildren":
                self.factory_slot_children(child['slotsChildren'], parent_id, children_lst)
            elif child['type'] == "slot":
                self.factory_slots(child['slots'], parent_id, children_lst)
            else:
                raise ValueError
        return children_lst, label_kind

    def factory_slot(self, slot: "rosetta slot",
                     children_lst: Dict = None,
                     parent_id: str = None,
                     label_kind: str = None,
                     team_id: int = None) -> Optional[str]:
        """
        Processing label box

        Args:
            slot:
                rosetta slot
            children_lst:
                rosetta children
            parent_id:
                Upper floor ID
        Returns:
            str， id
        """
        obj_type = slot['type']
        if obj_type == "box3d":  # 3D bounding box
            box3d = Box3D.gen_box3d(slot, children_lst, parent_id, label_kind, team_id=team_id)
            if not box3d:
                return
            self.label_result.box3d_lst.setdefault(box3d.id, box3d)
            return box3d.id
        elif obj_type == "box2d":  # 2D bounding box
            box2d = Box2D.gen_box(slot, children_lst, parent_id, label_kind, team_id=team_id)
            if not box2d:
                return
            self.label_result.box2d_lst.setdefault(box2d.id, box2d)
            return box2d.id
        elif obj_type == "cuboid":  # Mapped cuboid
            pass
        elif obj_type == "line":  # 2D line
            line = Line.gen_line(slot, children_lst, parent_id, label_kind, team_id=team_id)
            if not line:
                return
            self.label_result.line_lst.setdefault(line.id, line)
            return line.id
        elif obj_type == "polygon":  # Polygon
            polygon = Polygon.gen_polygon(slot, children_lst, parent_id, label_kind, team_id=team_id)
            if not polygon:
                return
            self.label_result.polygon_lst.setdefault(polygon.id, polygon)
            return polygon.id
        elif obj_type == "point":  # 2D keypoint
            point = Point.gen_point(slot, children_lst, parent_id, label_kind, team_id=team_id)
            if not point:
                return
            self.label_result.key_point_lst.setdefault(point.id, point)
        elif obj_type == "text":  # Text annotation
            text = Text.gen_text(slot, children_lst, parent_id, label_kind, team_id=team_id)
            if not text:
                return
            self.label_result.text_lst.setdefault(text.id, text)
        else:
            print(f'Unsupported structure: {obj_type}')
            pass
            # raise ValueError('Unsupported structure')

    def factory_slots(self, slot_lst: "rosetta slots json",
                      parent_id: str = None,
                      children_lst: Dict = {}) -> None:
        """
        Start processing the tag box list

        Args:
            slot_lst:
                rosetta slot
            parent_id:
                Upper floor ID
            children_lst:
                rosetta children

        Returns:

        """
        for slot in slot_lst:
            slot_id = self.factory_slot(slot, list(), parent_id=parent_id, team_id=slot.get("teamId", None))
            if slot_id:
                children_lst[slot_id]: slot['type']

    def factory_slot_children(self, sc_lst: "slotsChildren or slots",
                              parent_id: str = None,
                              children_lst: Dict = {}) -> None:
        """
        Start processing the annotation instance

        Args:
            children_lst:
                rosetta children
            sc_lst:
                rosetta slot
            parent_id:
                Upper floor ID

        Returns:

        """
        for sc in sc_lst:
            try:
                slot_id = sc['slot']['id']
                if sc.get("children"):
                    _children_lst, label_kind = self.factory_children(sc['children'], slot_id)
                    self.factory_slot(sc['slot'], _children_lst, parent_id, label_kind,
                                      team_id=sc['slot'].get("teamId", None))
                    if slot_id:
                        children_lst[slot_id] = sc['slot']['type']
                else:
                    self.factory_slot(sc['slot'], list(), parent_id, team_id=sc['slot'].get("teamId", None))
            except Exception as e:
                raise e
                continue

    def factory_anns(self, ann_lst: List) -> None:
        """
        Annotated configuration

        Args:
            ann_lst:
                Annotated result list
        Returns:

        """
        for ann in ann_lst:
            ann_type = ann['type']
            if ann_type == "input":
                input = Input.gen_input(ann)
                self.label_result.input_lst.setdefault(input.id, input)
            elif ann_type == "slotChildren":
                self.factory_slot_children(ann['slotsChildren'])
            elif ann_type == "slot":
                self.factory_slots(ann['slots'])
            elif ann_type == "childrenOnly":
                pass

    def factory_label_file(self, label_type: str,
                           label_file,
                           **kwargs) -> Media:
        """
        Start processing annotation file, single frame

        Args:
            label_type:
                Annotated type, image, point cloud
            label_file:
                Mark file
        Returns:
                a Media instance
        """
        if "POINTCLOUD" in label_type:
            pcd_url = label_file['url'] if isinstance(label_file, Dict) else label_file
            meta_point = PointCloud(
                uri=pcd_url,
                name=None,
                file_path=Path(pcd_url)
            )
            meta_images = list()
            if "imageSources" in label_file:
                for image in label_file['imageSources']:
                    meta_images.append(Image.gen_image(image))
            media = Media(point_cloud=meta_point, image=meta_images)
        elif "IMAGE" in label_type:
            image_url = label_file['url'] if isinstance(label_file, Dict) else label_file
            media = Media(
                point_cloud=None,
                image=Image(uri=image_url,
                            width=kwargs['size'].get("width") if kwargs.get("size") else None,
                            height=kwargs['size'].get("height") if kwargs.get("size") else None
                            )
            )
        else:
            media = {}

        return media

    def factory_rosetta(self, data: Dict) -> Frame:
        """
        Start processing, all single frame data

        Args:
            data: rosetta data

        Returns:
            a Frame instance

        """
        label_file = data['taskParams']['record']['attachment']
        label_type = data['taskParams']['record']['attachmentType']

        # Rosetta metadata
        self.task_info = TaskInfo(
            task_id=data['taskId'],
            project_id=data['projectId'],
            pool_id=data['poolId'],
            frame_num=self.frame_num
        )

        # Prepare annotation file metadata
        self.media = self.factory_label_file(label_type=label_type,
                                             label_file=label_file,
                                             size=data['taskParams']['record']['metadata'].get("size") \
                                                 if data['taskParams']['record'].get('metadata') else None
                                             )

        # Human annotations
        self.label_result = Annotation()
        # Parse annotation results
        self.factory_anns(data['result']['annotations'])
        annotation = self.label_result

        # Model-generated predictions
        self.label_result = Prediction()

        # Process pre-annotations if present
        if not data['taskParams']['record']['metadata']:
            # return None  # Kept for legacy compatibility consideration
            prediction = None
        else:
            if pres_data := data['taskParams']['record']['metadata'].get("preprocessedData"):
                if pres_data.get("annotations"):
                    self.factory_anns(pres_data['annotations'])
            prediction = self.label_result

        return Frame(media=self.media,
                     task_info=self.task_info,
                     annotation=annotation,
                     prediction=prediction
                     )

    def convert_rosetta(self) -> Dict:
        """
        Start to do the conversion work, yield a single frame of data

        Returns:

        """
        for json_data in self.yield_rosetta_json():
            yield self.factory_rosetta(json_data)

    def export_rosetta(self, pool_lst=[], split_name='old', env_name='top') -> None:
        """
        export rosetta project data

        Args:
            pool_lst:
                A list of pools to export
        Returns:

        """
        Export(self.project_id, self.input_path, env_name).export(pool_lst, split_name=split_name)

    def read_rosetta(self, project_id,
                     input_path,
                     pool_lst,
                     export_type=None,
                     **kwargs):
        """
        start to convert data, your choice can be: SDK、 json，default to be SDK，
        if you want to export other formats, please refer to stardust.conversion

        Args:
            project_id:
                rosetta project
            input_path:
                path to store json data exported from Rosetta
            pool_lst:
                pool list from your rosetta project
            export_type:
                expected export data type，SDK or json

        Returns:

        """

        assert project_id and isinstance(project_id, int)

        self.project_id = project_id
        self.input_path = input_path

        # Export data from Rosetta
        if os.path.exists(os.path.join(self.input_path, str(self.project_id), "json")):
            print("Start to fetch annotation results")
            shutil.rmtree(os.path.join(self.input_path, str(self.project_id)))

        self.export_rosetta(pool_lst, split_name=kwargs.get("split"), env_name=kwargs.get("env_name"))

        # Yield results as a generator
        for frame_obj in self.convert_rosetta():
            if not frame_obj:
                continue
            if export_type == "json":
                yield _serialize(frame_obj)
            else:
                yield frame_obj

    def read_ms(self, export_type=None, **kwargs):
        """
        Read data from MorningStar.

        Args:
            export_type:
                Desired export type
            ms_data:
                MorningStar response payload

        Returns:
                Frame objects

        Known gaps:
            taskinfo missing
            annotation file missing
            relationship between frames and annotation file
        """
        # Fetch dataset from MorningStar
        ms_data = MS().export_dataset(**kwargs)
        assert ms_data

        # Each dataset yields instances that are processed sequentially
        for instance_lst in ms_data:
            for index, instance in enumerate(instance_lst):
                self.frame_num = index
                res = self.factory_rosetta(instance)
                if export_type == "json":
                    yield _serialize(res)
                else:
                    yield res


def read_rosetta(
        project_id: int = None,
        input_path: str = None,
        pool_lst: Optional[List[int]] = None,
        export_type=None,
        **kwargs):
    """
    Start converting data. Options include SDK and json outputs (default SDK).
    For additional formats, see stardust.conversion.

    Args:
        project_id:
            Rosetta project identifier
        input_path:
            Path used to store JSON exported from Rosetta
        pool_lst:
            Pool list from your Rosetta project
        export_type:
            Expected output type: SDK or json

    Returns:

    """
    assert project_id and input_path
    return Convertor().read_rosetta(project_id, input_path, pool_lst, export_type, **kwargs)


def read_ms(*args, **kwargs):
    """
    Export MorningStar data

    Args:
        dataset_id:
            Data set ID
        version_num:
            Version number
        slice_id:
            Slice ID
        page_no:
            Slice paging
        page_size:
            Amount of data per page

    Returns:
        generator object

    Examples:
        .. code-block:: python

            from stardust.utils.convert import read_ms
            from stardust.convertion.to_pandaset import to_pandaset

            # Derived data
            gen_data = read_ms(
                dataset_id=351787480925605888,
                version_num=18
            )
            # scale format
            to_pandaset(gen_data, export_path:"Input save directory")


    """
    return Convertor().read_ms(*args, **kwargs)


if __name__ == '__main__':
    current_dir = os.getcwd()
    base_dir = os.path.dirname(os.path.dirname(current_dir))

    project_id = 1354
    pool_lst = [33750, ]
    # Input path is the directory where Rosetta JSON files are stored
    input_path = f"{base_dir}/data/"

    os.makedirs(input_path, exist_ok=True)

    gen_data = read_rosetta(project_id=project_id,
                            input_path=input_path,
                            pool_lst=pool_lst,
                            export_type="json"
                            )

    os.makedirs(os.path.join(input_path, "output"), exist_ok=True)
    # with open(f"{os.path.join(input_path, f'{project_id}', 'output')}/{project_id}.json", 'w', encoding='utf-8') as f:
    from pprint import pprint

    for data in gen_data:
        # pprint(len(data['annotation']['box3d_lst']))
        pass
        # json.dump(data, f, ensure_ascii=False, indent=2)
        # break
        # load_dataset(data, "/Users/mac/Desktop/1835")
        # break
