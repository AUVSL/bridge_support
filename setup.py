from setuptools import find_packages, setup

package_name = 'bridge_support'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='administrator',
    maintainer_email='soumilgupta2@gmail.com',
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
