import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matrix",
    version="0.0.1",
    author="e.sineokov",
    author_email="e.sineokov@gmail.com",
    description="get matrix text from url and transform to list of list",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/esineokov/avitohomework",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)