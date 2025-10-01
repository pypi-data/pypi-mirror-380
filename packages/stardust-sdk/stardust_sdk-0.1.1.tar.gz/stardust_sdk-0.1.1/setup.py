import os, shutil
from setuptools import setup, find_packages
from distutils.cmd import Command

# Remove the build directory produced during packaging
# CUR_PATH = os.path.dirname(os.path.abspath(__file__))
# path = os.path.join(CUR_PATH, 'build')
# if os.path.isdir(path):
#     print('INFO del dir ', path)
#     shutil.rmtree(path)

import configparser


def generate_config_file():
    # Create a ConfigParser instance
    config = configparser.ConfigParser()

    # Populate configuration sections
    config['OssUser'] = {
        'key': 'LTAI4GHWdWdjGDE4Gx1Efbyt',
        'secret': 'SffMd625UN8ceXLj0RlRG8oyF8BkjU',
        'bucket': 'stardust-data',
        'endpoint': 'https://oss-cn-hangzhou.aliyuncs.com',
        'prefix_url': 'https://stardust-data.oss-cn-hangzhou.aliyuncs.com'
    }

    config['RosUser'] = {
        'username': '13693170335',
        'password': 'Start123!'
    }

    config['RosConfig'] = {
        'env_prod': 'https://server.rosettalab.top',
        'env_dev': 'https://dev-server.rosettalab.top'
    }

    # Write configuration to disk
    with open('config222.ini', 'w') as configfile:
        config.write(configfile)


class CustomCommand(Command):
    description = 'Custom command description'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("Executing custom command...")  # Custom command implementation
        # Create a ConfigParser instance
        config = configparser.ConfigParser()

        # Populate configuration sections
        config['OssUser'] = {
            'key': 'LTAI4GHWdWdjGDE4Gx1Efbyt',
            'secret': 'SffMd625UN8ceXLj0RlRG8oyF8BkjU',
            'bucket': 'stardust-data',
            'endpoint': 'https://oss-cn-hangzhou.aliyuncs.com',
            'prefix_url': 'https://stardust-data.oss-cn-hangzhou.aliyuncs.com'
        }

        config['RosUser'] = {
            'username': '13693170335',
            'password': 'Start123!'
        }

        config['RosConfig'] = {
            'env_prod': 'https://server.rosettalab.top',
            'env_dev': 'https://dev-server.rosettalab.top'
        }

        # Write configuration to disk
        with open('config222.ini', 'w') as configfile:
            config.write(configfile)


# Call helper to generate the config file
# generate_config_file()


setup(
    name='stardust-sdk',  # Package name - changed to avoid conflict with existing 'stardust' package
    author='stardust.ai',
    author_email='support@stardust.ai',
    version='0.1.1',  # Package version - using semantic versioning
    description='Stardust SDK for AI/ML data processing and annotation workflows',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/stardustai/Stardust-SDK',
    project_urls={
        'Bug Reports': 'https://github.com/stardustai/Stardust-SDK/issues',
        'Source': 'https://github.com/stardustai/Stardust-SDK',
        'Documentation': 'https://sdk-docs.stardust.ai/',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='ai ml computer-vision annotation data-processing stardust',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'stardust': ['config.ini', "visualization/base/*.json"],
    },
    entry_points={
        'console_scripts': [
            'stardust = stardust.command.export:main',
        ],
    },
    install_requires=[
        'numpy>=1.24.0',
        'opencv-python>=4.8.0',
        'open3d>=0.17.0',
        'requests>=2.31.0',
        'matplotlib>=3.7.0',
        'pillow>=10.0.0',
        'aiohttp>=3.9.0',
        'httpx>=0.27.0',
        'jsonlines>=4.0.0',
        'numba>=0.58.0',
        'pandas>=2.1.0',
        'retry>=0.9.0',
        'scipy>=1.11.0',
        'shapely>=2.0.0',
        'tqdm>=4.66.0',
        'uvloop>=0.19.0',
    ],
    python_requires=">=3.9",
    extras_require={
        'dev': [
            'pytest>=7.0',
            'pytest-cov>=4.0',
            'black>=23.0',
            'flake8>=6.0',
        ],
    },
)
