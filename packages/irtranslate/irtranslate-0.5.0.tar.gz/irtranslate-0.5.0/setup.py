from setuptools import setup, find_packages

setup(
    name="irtranslate",
    version="0.5.0",
    author="Ali Shirgol",
    author_email="ali.shirgol.coder@gmail.com",
    description="یک کتابخانه ترجمه ساده با تشخیص زبان",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alishirgol",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
