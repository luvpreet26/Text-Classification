import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="text classification",
    version="0.0.1",
    author="Luvpreet Kaur",
    author_email="luvpreetkaur@yahoo.com",
    description="Text classification using sklearn, keras",
    long_description=long_description,
    long_description_content_type="text/markdown",  
    packages=setuptools.find_packages(),
    install_requires = [
    "future~=0.16",
    "numpy~=1.14",
    "scikit-learn~=0.19.0",
    "keras ~= 2.2.4"
     ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
print("\nWelcome to Text classification")
