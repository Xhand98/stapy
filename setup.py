from setuptools import setup, find_packages
import os

def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name), encoding='utf-8') as f:
        return f.read()

setup(
    name='steam_api',  # Replace with your library name
    version='0.7',  # Starting version of your library
    description='A library for interacting with the Steam API',  # Brief description
    author='Hendrick',  # Your name
    author_email='hendrickherrera9@example.com',  # Your corrected email address
    url='https://github.com/Xhand98/steam-api',  # URL to your project
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[
        'httpx',  # List of dependencies
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # License type
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
