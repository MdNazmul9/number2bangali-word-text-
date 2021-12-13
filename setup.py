from setuptools import setup, find_packages
VERSION = '0.0.5'
DESCRIPTION = 'Convert Number to Bangla Word Text'

# Setting up
setup(
    name="numberbanglaword",
    version=VERSION,
    author="Md. Nazmul Hossain",
    author_email="<nazmul.cse48@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python','numberbanglaword','number2bangali-word-text','number2word-text','number-to-bangali-word-text','number-to-word-text','number-to-bangla-text' ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
