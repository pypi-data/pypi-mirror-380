import json
import uuid
import time
import os

current_path = os.path.dirname(__file__)


# TODO: integrate with ossutil helpers
def ToAnnotationTool(data_path: str, task_type: str):
    """
    Visual result of algorithm with AnnotationTool

    Args:
        data_path: str
            The path of algorithm output which should be a json file
        task_type: str
            The type of visual task, the task can be chosen from 'object_detection', 'lane_detection' and 'tracking' for now

    Returns:
        str: 
            URL of AnnotationTool

    Examples:
        .. code-block:: python

            from stardust.visualization.visual import ToAnnotationTool
            vis_url = ToAnnotationTool('tracking_test.json', 'tracking')
    """
    assert task_type in ['object_detection', 'lane_detection', 'tracking']
    assert data_path.endswith('.json')
    with open(data_path, 'r') as f:
        input_data = json.load(f)

    log_time = time.strftime('%Y%m%d-%H%M%S', time.localtime())
    base_path = os.path.join(current_path, 'base', f'{task_type}.json')
    with open(base_path, 'r') as f:
        output = json.load(f)

    output['taskParams']['value']['record']['metadata'] = {
        'uniqueIdentifier': str(uuid.uuid4())
    }

    output['taskParams']['value']['record']['attachment'] = input_data['attachment']

    if task_type == 'object_detection':
        result_type = input_data['results']['type']
        annotations = input_data['results'][result_type]
        for obj_info in annotations:
            slot = obj_info['slot']
            children = obj_info['children']
            output['taskResult']['annotations'][0]['slotsChildren'].append(
                {
                    "slot":
                        {
                            "id": slot['id'],
                            "box": slot['box'],
                            "type": "box3d",
                            "label": "Point Cloud Box"},
                    "children": [{
                        "key": "box2d-[b274c]",
                        "type": "slot",
                        "label": "Mapped Bounding Box",
                        "slots": []}]}
            )
    elif task_type == 'lane_detection':
        result_type = input_data['results']['type']
        annotations = input_data['results'][result_type]
        for obj_info in annotations:
            output['taskResult']['annotations'][0]['slots'].append(
                {
                    "id": obj_info['id'],
                    "vertices": obj_info['vertices'],
                    "type": "line",
                    "label": "lane line"}
            )
    elif task_type == 'tracking':
        fallback_box_key = '3D\u6846'
        box_key = '3D box' if '3D box' in input_data['results'] else fallback_box_key
        fallback_rect_key = '\u77e9\u5f62\u6846'
        rect_key = 'Mapped Bounding Box' if 'Mapped Bounding Box' in input_data['results'].get(box_key, {}) else fallback_rect_key
        result_type = input_data['results'][box_key]['type']
        box3d = input_data['results'][box_key][result_type]
        for obj_info in box3d:
            slot = obj_info['slot']
            children = obj_info['children']
            output['taskResult']['annotations'][0]['slotsChildren'].append(
                {
                    "slot":
                        {
                            "id": slot['id'],
                            "box": slot['box'],
                            "timeSeries": slot['timeSeries'],
                            "type": "box3d",
                            "label": "Point Cloud Box"}}
            )
            if rect_key in children:
                for child in children[rect_key]['slot']:
                    child['label'] = 'Mapped Bounding Box'
                output['taskResult']['annotations'][0]['slotsChildren'][-1].update(children=[{
                    "key": "box2d-[b274c]",
                    "type": "slot",
                    "label": "Mapped Bounding Box",
                    "slots": children[rect_key]['slot']}])
            else:
                output['taskResult']['annotations'][0]['slotsChildren'][-1].update(children=[{}])
    os.makedirs(f'./results/{task_type}', exist_ok=True)
    local_path = f'./results/{task_type}/{log_time}.json'
    with open(local_path, 'w') as f:
        json.dump(output, f, ensure_ascii=False)
    oss_path = f'oss://stardust-data/Clients/J-ceshi/path-test/Production/666/{task_type}/{log_time}.json'
    vis_path = oss_path[oss_path.find('Clients'):]
    vis_url = f'https://dev.rosettalab.top/annotate#fromLink/https://stardust-data.rosettalab.top/{vis_path}'
    print(vis_url)
    os.system(f'ossutil cp -rf {local_path} {oss_path} -e oss-cn-hangzhou.aliyuncs.com')
    return vis_url
