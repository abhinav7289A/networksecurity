'''
The setup.py file is an essential part of the apckkaging 
and distributing Python Projects. It is used by setupstools (or ditutils in older python version) to define the configuration
of your project, such as its metadata, dependenciesm, and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # read lines from the file
            lines = file.readlines()
            # process each lines
            for line in lines:
                requirement = line.strip()
                ## ifnore empty lines -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement) 
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst

print(get_requirements())

setup(
    name="Network Security",
    version="0.0.1",
    author="Abhinav",
    author_email="abhinavbhatia7289@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)