import os
from setuptools import setup, find_packages
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    


setup(
        # the name must match the folder name 'verysimplemodule'
        name="iman", 
        version='2.0.3',
        author="Iman Sarraf",
        author_email="imansarraf@gmail.com",
        description='Python package for daily Tasks',
        long_description=read('README.rst'),
        packages=find_packages(),
        include_package_data=True,
        package_data={
        "iman": ["svad/data/*.*"],  # Include all files in iman/data
        },
        # add any additional packages that 
        # needs to be installed along with your package.
        install_requires=['scipy','numpy','six','matplotlib','joblib'], 
        
        keywords=['python', 'iman'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
        ]
        

)