from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file : 
            lines=file.readlines()

            for line in lines:
                requirement = line.strip()
                ## ignore -e . and empty lines
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
          print("requirements.txt fiel not found")

    return requirement_lst

setup(
    name="NetworkSecurity" , 
    version="0.0.1",
    author = "Andres Ruiz",
    author_email="andresruuiz95@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)