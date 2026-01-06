from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath: str)-> List[str]: 
    ''' 
    fetches txt file path from filepath, extract all libraries and gives them in list format
    '''
    requirements: List[str] = []

    with open(filepath) as file: 
        for library in file.readlines():
            requirements.append(library.replace("\n", ""))

    if "-e ." in requirements: 
        requirements.remove("-e .")

    return requirements

setup(
    name='student-performance-tracker', 
    version='0.0.1', 
    author = "Deepak",
    author_email="deepakkrishna2206@gmail.com",
    packages=find_packages(), 
    install_requires=get_requirements('requirements.txt')
)
