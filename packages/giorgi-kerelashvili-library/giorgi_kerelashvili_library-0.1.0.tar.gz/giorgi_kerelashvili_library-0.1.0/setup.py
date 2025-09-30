# setup.py
from setuptools import setup, find_packages

setup(
    name='giorgi_kerelashvili_library',  # The name of your package
    version='0.1.0',   # The initial version
    description='A simple package with a Base class',  # Description of the package
    long_description=open('README.md').read(),  # Optional: long description from a README file
    long_description_content_type='text/markdown',  # The content type of the README
    author='Your Name',  # Your name or organization
    author_email='your_email@example.com',  # Your email
    url='https://github.com/yourusername/mypackage',  # URL for your project, e.g., GitHub repo
    packages=find_packages(),  # Automatically find packages in the current directory
    classifiers=[  # Some classifiers for PyPI
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version
)