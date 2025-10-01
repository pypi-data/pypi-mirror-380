import os
import json
import shutil
import argparse
from tqdm import tqdm
from stardust.convertion import *
from stardust.utils.convert import read_rosetta


def _export(args):
    # Rosetta project ID
    project_id = int(args.project_id)
    # Pool identifiers for the project
    pool_lst = args.pool
    # Export data type
    e_type = args.type
    # Output directory
    save_path = args.output

    # Prepare the output directory
    if os.path.exists(save_path):
        shutil.rmtree(save_path, ignore_errors=True)
    os.makedirs(save_path)
    save_path = os.path.join(save_path, str(project_id))

    # Export Stardust structure
    if e_type == "stardust":
        # Convert Rosetta export to Stardust format
        sd_generator = read_rosetta(project_id=project_id,
                                    pool_lst=pool_lst,
                                    input_path=save_path,
                                    export_type="json",
                                    )
        res_save_path = os.path.join(save_path, f"{project_id}_sd.jsonl")
        with open(res_save_path, 'w', encoding='utf-8') as f:
            for sd_data in tqdm(sd_generator, desc="Processing", unit="item"):
                json.dump(sd_data, f)
                f.write('\n')
        print(f"project id: {project_id}, saved to {res_save_path}")

    # Export COCO structure
    elif e_type == "coco":
        # Convert Rosetta export to Stardust format first
        sd_generator = read_rosetta(project_id=project_id,
                                    pool_lst=pool_lst,
                                    input_path=save_path,
                                    )
        res_save_path = os.path.join(save_path, f"{project_id}_coco.json")
        coco_export(sd_generator, res_save_path)

    # Export KITTI structure
    elif e_type == "kitti":
        # Decide whether frames need to be separated
        _json_data = read_rosetta(project_id=project_id,
                                  pool_lst=pool_lst,
                                  input_path=save_path,
                                  )
        kitti_path = os.path.join(save_path, 'kitti')
        kitti_export(_json_data, kitti_path)

    elif e_type == "rosetta":
        # Decide whether frames need to be separated
        _json_data = read_rosetta(project_id=project_id,
                                  pool_lst=pool_lst,
                                  input_path=save_path,
                                  )
        next(_json_data)


    else:
        print("Unsupported export structure")


def _algo(args):
    print(f'Running algorithm command with args: {args}')


def parse_integer_list(string):
    try:
        # Split comma-separated values and convert to integers
        integer_list = [int(num) for num in string.split(',')]
        return integer_list
    except ValueError:
        # Raise if any value cannot be converted
        raise argparse.ArgumentTypeError("Invalid integer list: {}".format(string))


def main():
    # Create the top-level parser
    parser = argparse.ArgumentParser(description='Stardust command line tool')

    # Define sub-commands
    subparsers = parser.add_subparsers(title='Commands', required=True, dest='command')

    # Export command supporting stardust, coco, kitti, pandaset outputs
    comd_export = subparsers.add_parser('export', help='Export data from Rosetta')
    comd_export.add_argument('--type', "-t", default="stardust", help='Supported export formats: stardust, rosetta, coco, kitti, pandaset')
    comd_export.add_argument('--output', "-o", required=True, help='Output directory for exported data')
    comd_export.add_argument('--project_id', '-p', required=True, help='Rosetta project ID')
    comd_export.add_argument('--pool', '-pool', required=True, help='Comma separated pool IDs for the project', type=parse_integer_list)
    comd_export.set_defaults(func=_export)

    # Placeholder for algorithm-related commands
    comd_algo = subparsers.add_parser('algo', help='Algorithm utilities')
    comd_algo.add_argument('arg1', help='Placeholder parameter')
    comd_algo.set_defaults(func=_algo)

    # Parse CLI arguments
    args = parser.parse_args()

    # Dispatch to the appropriate handler
    args.func(args)


if __name__ == '__main__':
    main()
