from setuptools import setup, find_packages

setup(
    name="python-ml-app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here. For example:
        # 'numpy==1.21.0',
        # 'pandas==1.3.0',
        # 'scikit-learn==0.24.2',
    ],
    entry_points={
        'console_scripts': [
            # If you want to create any command-line scripts, list them here.
            # For example, if you have a script 'myscript' in a module 'my_module', list it as:
            # 'myscript=my_module:main_func',
        ],
    },
    # Metadata for the project
    description="A sample Python ML project",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/raviteja869/python-ml-app",  # project home page
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
    ],
    keywords="sample python ml project",
)

