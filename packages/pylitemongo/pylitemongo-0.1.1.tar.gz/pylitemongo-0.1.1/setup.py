from setuptools import setup, find_packages

setup(
    name="pylitemongo",              
    version="0.1.1",                 
    description="MongoDB-like document store using SQLite",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/salvatorpy/pylitemongo",  
    packages=find_packages(),
    install_requires=[],            
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)