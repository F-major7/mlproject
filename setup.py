from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirement(file_path:str)->List[str]:
    '''
    returns the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements] # to remove \n element from the path in requirements.txt
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name = 'mlproject',
    version = '1.0.0',
    author = 'Parth',
    authonr_email = 'parthsarthi142@gmail.com',
    packages = find_packages(), # finds all the packages to be used in the project
    #install_requires = ['numpy', 'pandas', 'seaborn']
    install_requires = get_requirement('requirements.txt') #instead of tyyping each library, we will update path in requirement file
)