from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT= '-e .'

def get_requirements(file_path:str)->List[str]:
    """Reads the requirements.txt file and returns a list of dependencies."""
    requirements=[]
    try:
        with open(file_path) as file_obj:
          requirements=file_obj.readlines()

        requirements=[
            req.strip() for req in requirements if req.strip() and not req.startswith("-e")
            ]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please provide a valid requirements.txt file.")
        

    return requirements        


setup(
name='endtoendmlgit',
version='0.0.1',
author='Dami',
author_email= 'omisdami@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)