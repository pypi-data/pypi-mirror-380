from setuptools import setup, find_packages
import os


version = None
with open(os.path.join(os.path.dirname(__file__), 'dumbjuice', '__version__.py')) as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip('"')
            break
setup(
    name="dumbjuice",
    description="DumbJuice is a Python module that simplifies the process of packaging small Python programs into self-contained installable packages. These packages can be shared with non-technical users, who only need to run a single install.bat file to install Python, set up a virtual environment, install necessary dependencies, and create a shortcut to the program on their desktop.",
    long_description=open("README.md","r",encoding="utf-8").read(),
    long_description_content_type='text/markdown', # since readme.md contains markup
    author="Lorithai",
    author_email="lorithai@gmail.com",
    url="https://github.com/lorithai/dumbjuice",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Adjust to your license
        'Operating System :: OS Independent',
    ],


    version=version,
    packages=find_packages(include=['dumbjuice', 'dumbjuice.*']),
        package_data={
        'dumbjuice.assets': ['djicon.ico'],
        'dumbjuice.bin': ['makensis.exe', 'plugins/inetc.dll'],
    },
    include_package_data=True,  # Ensures non-Python files are included
    install_requires=["pillow==11.3.0", "requests" ,"beautifulsoup4==4.13.5","packaging"
        
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'dumbjuice-build = dumbjuice.build:build',
            'dumbjuice-create_ico = dumbjuice.create_ico_entry:main'
        ],
    },
)