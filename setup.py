from setuptools import setup, find_packages

VERSION = '0.0.4'
DESCRIPTION = 'personaldata Python package'
LONG_DESCRIPTION = 'Python package.'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="personaldata",
    version=VERSION,
    author="zosialaa",
    author_email="zofia.lapinska@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=open("requirements.txt").readlines(),

    keywords=['python', 'personaldata'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)
