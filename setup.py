from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT = "-e ."

def get_req(file_path:str)->List[str]:
    ''' 
    this funtion will return the list of req
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
name = 'AI _ML PROJ', 
version = '0.0.1',
author = "rachit",
author_email = 'rachitgupta049@gmail.com',
packages = find_packages(),
install_requires = get_req('requirements.txt')
)