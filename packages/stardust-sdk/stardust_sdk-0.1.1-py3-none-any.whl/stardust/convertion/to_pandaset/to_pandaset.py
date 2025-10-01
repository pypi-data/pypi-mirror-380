from pathlib import Path
from typing import Union

import numpy as np
import pandas as pd

# from stardust.utils.convert import read_rosetta


def get_demo():
    """

    Returns: pandaset format

    """
    columns = ['uuid', 'label', 'yaw', 'stationary', 'camera_used', 'position.x',
               'position.y', 'position.z', 'dimensions.x', 'dimensions.y',
               'dimensions.z', 'attributes.object_motion', 'cuboids.sibling_id',
               'cuboids.sensor_id', 'attributes.pedestrian_behavior',
               'attributes.pedestrian_age', 'attributes.rider_status']
    demo = {key: np.NaN for key in columns}
    demo["camera_used"] = -1
    demo["cuboids.sensor_id"] = -1
    demo["cuboids.sibling_id"] = '-'
    return demo


def _frame_handle(frame_obj, save_path: Path):
    """

    Args:
        frame_obj: sdk frame object
        save_path: data saving path

    Returns:

    """

    task_id = frame_obj.task_info.task_id
    frame_num = frame_obj.task_info.frame_num
    res = []
    input_objs = frame_obj.annotation.input_lst
    for box_id, box_3d in frame_obj.annotation.box3d_lst.items():
        demo = get_demo()
        demo["uuid"] = box_id
        demo["yaw"] = box_3d.rotation[-1]
        demo['position.x'], demo['position.y'], demo['position.z'] = box_3d.center
        demo['dimensions.x'], demo['dimensions.y'], demo['dimensions.z'] = box_3d.size
        for child_id in box_3d.children:
            if input_objs.get(child_id) is None:
                continue
            children_obj = input_objs[child_id]
            attribute_name = children_obj.name
            if attribute_name not in demo.keys():
                continue
            value = children_obj.value
            if value == "False":
                value = False
            elif value == "True":
                value = True
            demo[attribute_name] = value
        res.append(demo)
    output_dir = save_path / f"pandaset/{task_id}/annotations/cuboids"
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
    df = pd.DataFrame(res)
    df.to_pickle(output_dir / f"{frame_num:0>2}.pkl")


def to_pandaset(sdk_generator, save_path: Union[Path, str]):
    """
    Args:
        sdk_generator: sdk builder
        save_path: save path

    Returns: None

    """

    if not isinstance(save_path, Path):
        save_path = Path(save_path)
    for frame_obj in sdk_generator:
        _frame_handle(frame_obj, save_path)


if __name__ == '__main__':
    rosetta_data = '/Users/mac/Downloads/rosetta_data'
    project_id = 2661
    # export rosetta data and cut frames
    sd_generator = read_rosetta(project_id=project_id,
                             input_path=rosetta_data,
                             )
    to_pandaset(sd_generator, Path('/Users/mac/Downloads/rosetta_data'))
