# Stardust SDK

Stardust SDK helps data and machine learning teams orchestrate the lifecycle of high quality sensor datasets: exporting
annotations, converting formats, validating metrics, and closing the loop on model performance.

## Overview

Stardust-SDK is a Python toolkit created by [Stardust.ai](https://stardust.ai/en-US/) for preparing training data. It
connects raw annotations from [Rosetta](https://rosettalab.top/ "Stardust Official Website") and MorningStar to
common computer vision formats, analytics, and visualization utilities so that models can be trained and debugged
faster.

## Features

- Export labeled data from Rosetta or MorningStar in the Stardust data format and transform it into COCO, KITTI, or
  PandaSet with minimal code.
- Visualize predictions for key perception tasks such as object detection, tracking, and lane detection.
- Evaluate model quality with built-in metrics including precision, recall, and F1, or plug in custom callbacks.
- Validate camera and lidar calibration matrices before they reach production pipelines.

## Installation

### Option 1: Install from PyPI (Recommended)

```bash
pip install stardust-sdk
```

### Option 2: Install from GitHub

```bash
pip install git+https://github.com/stardustai/Stardust-SDK.git
```

### Option 3: Development Installation

1. Create and activate a Python 3.9 (or newer) environment.

    ```bash
    conda create -n stardust_sdk python=3.9 -y
    conda activate stardust_sdk
    ```

2. Clone this repository.

    ```bash
    git clone https://github.com/stardustai/Stardust-SDK.git
    cd Stardust-SDK
    ```

3. Install dependencies and the package in editable mode.

    ```bash
    pip install -r requirements.txt
    pip install -e .
    ```

## Quick Start

### Export Stardust JSON

Use `read_rosetta` to load labeled frames from Rosetta and stream them to a JSON file.

```python
import json
from stardust.utils.convert import read_rosetta

gen_data = read_rosetta(
    project_id=1694,
    input_path="/path/to/export",
    pool_lst=[48904],  # optional
    export_type="json"  # optional
)

with open("your_file.json", "w", encoding="utf-8") as sf:
    for json_data in gen_data:
        json.dump(json_data, sf, ensure_ascii=False)
        break
```

### Convert to KITTI

Transform Stardust JSON into KITTI files with the high level conversion helper.

```python
import os
from stardust.utils.convert import read_rosetta
from stardust.convertion.to_kitti.to_kitti import kitti_export


gen_json_data = read_rosetta(
    project_id=1507,
    input_path="/path/to/export"
)

kitti_export(
    gen_json_data,
    os.path.join("/path/to/export", "kitti")
)  # outputs into input_path/kitti
```

### Compute Metrics

Compare model predictions against human labels and review the results.

```python
from pprint import pprint
from stardust.utils.convert import read_rosetta
from stardust.metric.object_detection import compute_metric

project_id = 1507
json_datas = read_rosetta(project_id=project_id, input_path="/path/to/export")
metric = compute_metric(json_datas, 0.5, "IoU", "results")
pprint(metric)
```

### Project 3D Points

Confirm calibration by projecting 3D point clouds onto camera images.

```python
import numpy as np
import open3d as o3d
from stardust.geometry.ops3d import pointcloud2img
from stardust.utils.convert import read_rosetta


pcd_path = "/path/to/point_cloud.pcd"
frames_jsons = read_rosetta(
    project_id=1507,
    input_path="/path/to/export",
    export_type="json"
)

pcd = o3d.io.read_point_cloud(pcd_path)
pcd_pts = np.asarray(pcd.points)

for frame in frames_jsons:
    frame_info = frame["media"]
    img_pixel = pointcloud2img(frame_info, cam_idx=1, points_3d=pcd_pts)
    # img_pixel now contains the projection of the point cloud onto image 1
```

## Data Model

Each exported frame contains synchronized metadata and annotations. The top level structure is:

```json
{
  "media": "Media metadata for all sensor files",
  "task_info": "TaskInfo describing the labeling job context",
  "annotation": "Human annotation results",
  "prediction": "Model-generated pre-annotations"
}
```

Key components are documented in the API reference:

- Media: [docs/statics/frame.html#stardust.components.frame.Media](http://120.26.78.19:9001/frame.html#stardust.components.frame.Media)
- Annotation: [docs/statics/frame.html#stardust.components.frame.Annotation](http://120.26.78.19:9001/frame.html#stardust.components.frame.Annotation)
- TaskInfo: [docs/statics/frame.html#stardust.components.frame.TaskInfo](http://120.26.78.19:9001/frame.html#stardust.components.frame.TaskInfo)

Refer to the documentation site for a complete schema and additional examples.

## Documentation

Latest API and workflow guides: [docs](http://120.26.78.19:9001/index.html).

## Contributing

We welcome pull requests and feature proposals. Please review the
[contributing guidelines](https://www.google.com/) before submitting code.

## Roadmap

- Streamlined data warehouse migration support.
- Hard example discovery tooling for model debugging.
- Active learning workflow integration.

## Community

Have questions or feedback? Join the discussion on Discord: https://discord.gg/gaaENMpK
