# Import setuptools module
import setuptools

# Parse the readme markdown file
with open("../README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="readsettings",
    version="2.0.0",
    author="Richie Bendall",
    author_email="richiebendall@gmail.com",
    description=
    "Easily create, edit and remove a customized settings file which you can use for storing all of the settings for your application.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/Richienb/readsettings-python",
    packages=setuptools.find_packages(),
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
)
