# Import setuptools module
import setuptools

# Parse the readme markdown file
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

# Setup module
setuptools.setup(
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    version_format='{tag}',
    setup_requires=['setuptools-git-version'])
