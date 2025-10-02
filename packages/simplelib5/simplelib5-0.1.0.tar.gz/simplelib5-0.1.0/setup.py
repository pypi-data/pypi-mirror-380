from setuptools import setup

setup(
    name='simplelib5',  # Name of your library
    version='0.1.0',  # Version number
    description='A simple example Python library',  # A short description
    long_description=open('README.md').read(),  # Long description (optional, often the README.md file)
    long_description_content_type='text/markdown',
    py_modules=['simplelib5'],  # Specify the module(s) to include
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python version requirement
)
