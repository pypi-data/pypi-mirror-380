import os
import json
from pathlib import Path

from stardust.convertion.to_coco.coco_demo import COCO_ANNS
from stardust.utils.convert import read_rosetta

_all_input = set()
_input_parent_map = dict()
_input_value_id_map = dict()
_g_input_id = 1
_g_box_id = 1


# COCO demo scaffold
def _coco_demo():
    return COCO_ANNS


def func_category(input: "sdk input"):
    if input.input_type == "select":
        return input.value
    elif input.input_type == "nested":
        return [input.value[0], input.value[1]]


# Convert Stardust data into COCO structure
def sd_to_coco(demo: "coco format",
               data: "sdk format",
               frame_num,
               ensure_match=False):
    global _g_input_id
    global _g_box_id

    demo["images"].append({
        "license": 1,
        "file_name": Path((image := data.media.image).uri).name,
        "coco_url": image.uri.replace("oss://stardust-data/Clients/", "https://stardust-data.oss-cn-hangzhou.aliyuncs.com/Clients/"),
        "height": 2160,
        "width": 3840,
        "date_captured": None,
        "flickr_url": None,
        "id": frame_num + 1
    })

    for index, (_id, ann) in enumerate(data.annotation.input_lst.items()):
        # Skip fields without a value
        if not ann.value:
            continue

        # Keep only category-style inputs
        if ann.name not in ("category", "Type", "type", "portrait_id"):
            continue

        # Map box2d entries back to their input field (1:1 mapping)
        category_id = int(f"{frame_num}{index}")
        if ann.parent:
            _input_parent_map.setdefault(ann.parent, (_id, category_id))

        # Category value
        assert ann
        category = func_category(ann)

        # Only register each value once
        if category in _all_input:
            continue
        _all_input.add(category)
        _input_value_id_map.setdefault(category, _g_input_id)

        # Append category definition
        demo["categories"].append({
            "supercategory": category,
            "id": _g_input_id,
            "name": category,
            # "origin_id": ann.id
        })

        _g_input_id += 1

    for index, (_id, ann) in enumerate(data.annotation.box2d_lst.items()):
        if ensure_match and not _input_parent_map.get(_id):
            continue

        # Retrieve the input annotation object
        _input_obj = data.annotation.input_lst.get(_input_parent_map[_id][0])
        if not _input_obj:
            continue
        category = func_category(_input_obj)

        _children = ann.children
        segmentation = list()
        area = ann.area
        if polygon_lst := data.annotation.polygon_lst:
            for _child in _children:
                if polygon_lst.get(_child):
                    _segem = list()
                    points = polygon_lst[_child].points
                    segmentation = list()
                    for i in points:
                        _segem.extend([round(i[0], 2), round(i[1], 2)])
                    area = polygon_lst[_child].area
                    segmentation.append(_segem)
        demo["annotations"].append({
            "segmentation": segmentation,
            "area": area,
            "iscrowd": 0,
            "image_id": frame_num + 1,
            "bbox": [round(ann.x1, 2), round(ann.y1, 2), ann.width, ann.height],
            "category_id": _input_value_id_map[category] if _input_parent_map.get(_id) else None,
            # "id": int(f"{frame_num}{index}")
            "id": _g_box_id,
            # "origin_id": ann.id
        })
        _g_box_id += 1


# Stardust exports yield a generator
def coco_export(sd_generator: "sdk generator",
                save_path: "coco output path"):
    # COCO demo payload
    demo = _coco_demo()

    # Convert Stardust frames to COCO annotations
    for index, json_data in enumerate(sd_generator):
        sd_to_coco(demo, json_data, index, ensure_match=True)

    # Persist COCO annotations
    if os.path.exists(save_path):
        os.remove(save_path)
    with open(save_path, 'w', encoding='utf-8') as sf:
        json.dump(demo, sf, ensure_ascii=False)

    print(f"Exported COCO file saved to: {save_path}")


if __name__ == '__main__':
    # Example usage:

    # Data directory
    base_dir = "/Users/mac/Documents/pyproject/sd_sdk/stardust_sdk/Stardust_SDK/data"
    # Rosetta project ID
    project_id = 2066

    # Prepare directories
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    input_path = f"{base_dir}/{project_id}"

    # Convert from Rosetta to Stardust
    sd_generator = read_rosetta(project_id=project_id,
                                input_path=input_path,
                                )

    # COCO output path
    os.makedirs(f"{base_dir}/{project_id}/output/", exist_ok=True)
    res_save_path = f"{base_dir}/{project_id}/output/{project_id}_coco.json"

    # Run conversion
    coco_export(sd_generator, res_save_path)
