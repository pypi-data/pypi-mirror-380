from setuptools import setup, find_packages

setup(
    name="visualizerai",
    version="0.2.0",
    author="Saurabh Chandrakant Zarekar",
    author_email="your_email@example.com",
    description="A Python library for effortless data visualization using Pandas DataFrames",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Saurabh-Zarekar/visualizerai",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
