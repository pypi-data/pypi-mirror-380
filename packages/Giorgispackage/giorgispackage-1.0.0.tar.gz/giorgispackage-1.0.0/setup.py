from setuptools import setup, find_packages
from MyPackages.PythonAssignment1 import Base

setup(
    name='Giorgispackage',
    version='1.0.0',    
    description='A sample Python package',
    author='Giorgi',
    packages=find_packages(),
    python_requires='>=3.6'
)


obj = Base(5)
print(obj.get_value())  # Output: 5

obj.add_to_value(3)
print(obj.get_value())  # Output: 8

print(obj.set_value(10))  # Output: None