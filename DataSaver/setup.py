import setuptools

with open("README.md", "r") as fhandle:
    long_description = fhandle.read() # Your README.md file will be used as the long description!

setuptools.setup(
    name="Showierdata9978", # Put your username here!
    version="0.0.1", # The version of your package!
    author="Gavin", # Your name here!
    author_email="melfang36@outlook.com", # Your e-mail here!
    description="A small example package", # A short description here!
    long_description=long_description,
    long_description_content_type="text/markdown",
    website = "https://github.com/ShowierData/Data-Saver-Py-",
    packages=setuptools.find_packages(), # A list of all packages for Python to distribute!
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], # Enter meta data into the classifiers list!
    python_requires='>=3.6', # The version requirement for Python to run your package!
)
setuptools