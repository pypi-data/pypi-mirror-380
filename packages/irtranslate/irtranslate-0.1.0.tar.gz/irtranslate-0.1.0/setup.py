from setuptools import setup, find_packages

setup(
    name="irtranslate",
    version="0.1.0",
    description="A simple translator library without API key",
    author="Ali Shirgol",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
