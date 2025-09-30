from setuptools import setup, find_packages

setup(
    name="autofuse",
    version="0.1.0",
    packages=find_packages(),
    author="graph-infra-community",
    author_email="joozhan@163.com",
    description="A minimal Python package that prints Hello World",
    long_description="A super kernel simple package that demonstrates how to create and publish a Python package to PyPI.",
    long_description_content_type="text/plain",
    url="https://gitcode.com/cann/graph-infra",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)