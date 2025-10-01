import os
import numpy as np

from stardust.utils.convert import read_rosetta


def object_class(val, label):
    for child in val.children:
        if child in label.input_lst.keys() and label.input_lst[child].name == 'category':
            box_class = label.input_lst[child].value
            if isinstance(box_class, list):
                return '/'.join(box_class[0])
            else:
                return box_class
    return 'unknown'


def camera_map(camera_param):
    return {cam.name: cam.camera_param.cam2lidar_rt.I.T for cam in camera_param}


def box_center_in_image(cam, center):
    center = np.c_[center.reshape(1, 3), np.array([1])]
    center = np.dot(center, cam).tolist()[0][:3]
    return center


def kitti_export(stardust_data: "Frame", save_path: str):
    """
    rosetta to kitti

    Args:
        stardust_data:
            Frame class
        save_path:
            Save path
    """
    while True:
        try:
            json_data = next(stardust_data)
        except AssertionError:
            pass
        except StopIteration:
            break
        else:
            try:
                camera_info = camera_map(json_data.media.image)
            except Exception as e:
                raise ValueError(f'Camera parameters are invalid: {e}')
            txt_name = os.path.basename(json_data.media.point_cloud.uri).replace('pcd', 'txt')
            os.makedirs(save_path, exist_ok=True)
            with open(os.path.join(save_path, txt_name), 'w') as wp:
                annotation = json_data.annotation
                for key, value in annotation.box2d_lst.items():
                    # category, truncation, occlusion, observation angle, 2D top-left, 2D bottom-right, 3D dimensions, 3D position, yaw, score
                    kitti_data = [None] * 16
                    kitti_data[4:6] = value.x1, value.y1
                    kitti_data[6:8] = value.x2, value.y2
                    box3d_info = annotation.box3d_lst.get(value.parent, None)
                    if box3d_info:
                        kitti_data[0] = object_class(box3d_info, annotation)
                        kitti_data[8:11] = box3d_info.size
                        kitti_data[11:14] = box_center_in_image(camera_info[value.source], np.array(box3d_info.center))
                        kitti_data[14] = box3d_info.rotation[-1]
                    else:
                        kitti_data[0] = object_class(value, annotation)
                    wp.write(' '.join(np.array(kitti_data, dtype=str).tolist()))
                    wp.write("\n")
    print(f"Exported KITTI files saved to: {save_path}")


if __name__ == '__main__':
    project_id = 1507
    input_path = f'/Users/mac/Desktop/{project_id}'

    _json_data = read_rosetta(project_id=project_id,
                              input_path=input_path,
                              )
    kitti_export(_json_data, os.path.join(input_path, 'kitti'))
