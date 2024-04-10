from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'bridge_support'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='administrator',
    maintainer_email='azarcon3@illinois.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tf2_bridger = bridge_support.tf2_bridger:main',
            'elevation_map_modifier = bridge_support.elevation_map_modifier:main'
        ],
    },
)
