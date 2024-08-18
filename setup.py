from setuptools import setup, find_packages

setup(
    name= 'OBD_Tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'consol_scripts':[
            'obd-diagnostics=obd_diagnostics.cli:main',
        ]
    }
    description= 'A OBD scanning tool'
    author='James Hall'
    author_email='techdetectivejames@gmail.com'




)