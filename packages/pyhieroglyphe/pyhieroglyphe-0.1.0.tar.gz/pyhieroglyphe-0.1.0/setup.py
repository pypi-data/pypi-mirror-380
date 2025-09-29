from setuptools import setup, find_packages

setup(
    name="pyhieroglyphe",            # Nom unique sur PyPI
    version="0.1.0",
    packages=find_packages(),
    description="Librairie de traduction français → hiéroglyphes",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="editor4001",
    author_email="30leodomingue@gmail.com",
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
