from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.read().splitlines()
        requirements = [req.strip() for req in requirements if req.strip() and req != HYPHEN_E_DOT]
    
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Michael',
    author_email='mnsihnimo.gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  # Make sure to filter out `-e .`
)

