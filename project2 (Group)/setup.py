from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='massive data',
    author='yudi',
    license='MIT',
    entry_points = '''
                [console_scripts]
                get_raw=src.data.get_raw:main
    ''',
)
