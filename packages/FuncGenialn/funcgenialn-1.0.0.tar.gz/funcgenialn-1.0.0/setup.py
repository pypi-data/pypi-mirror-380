import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FuncGenialn",  
    version="1.0.0",  
    author="NEFOR",  
    author_email="N7FOR8572@gmail.com",  
    description="A simple library for speed control in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nefoceo/genialtools",  
    packages=setuptools.find_packages(), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
)
