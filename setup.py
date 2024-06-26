import os

from setuptools import setup, find_packages

VERSION_FILE = 'VERSION'


def get_version():
    """Returns the current  dictionary version"""

    current_dir = os.path.dirname(os.path.realpath(__file__))
    version_path = os.path.join(current_dir, VERSION_FILE)
    try:
        with open(version_path, 'r') as version_fd:
            return version_fd.read().strip()
    except FileNotFoundError:
        return '0.0.0'

setup(
    name='gdcdictionary',
    version=get_version(),
    packages=find_packages(),
    install_requires=[
        'dictionaryutils',
    ],
    dependency_links=[
       "git+https://github.com/uc-cdis/dictionaryutils.git@1.2.0#egg=dictionaryutils",
    ],
    package_data={
        "gdcdictionary": [
            "schemas/*.yaml",
            "schemas/projects/*.yaml",
            "schemas/projects/*/*.yaml",
        ]
    },
)
