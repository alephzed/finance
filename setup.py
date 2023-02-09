from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A finance package to support discount cash flow and other valuations'
LONG_DESCRIPTION = 'A finance package to support discount cash flow and other valuations'

# Setting up
setup(
    name="vidstream",
    version=VERSION,
    author="Herringbone Techmologies",
    author_email="<mail@none.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['beautifulsoup4'],
    keywords=['python', 'finance', 'capm', 'dcf'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)