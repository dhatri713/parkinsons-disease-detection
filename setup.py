from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str)->List[str]:
    '''
    returns a list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    
    return requirements

setup(
    name = 'parkinsons-disease-detection',
    version = '0.0.1',
    author = 'Dhatri',
    author_email = 'dhatrimanaswini@gmail.com',
    packages = find_packages(),
    #install_requires = ['numpy', 'pandas', 'seaborn']
    install_requires = get_requirements("requirements.txt")
)