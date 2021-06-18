"""Setup file"""

import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="vitamin_d_fitbit",
    version="0.1.0",
    author="Lars Korpel",
    author_email="lars.korpel@hotmail.nl",
    description="Vitamin-D external fitbit",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://gitlab.fdmci.hva.nl/IoT/2020-2021-jan-jul/digitallife-vitamined/core-backend",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        "flask",
        "python-dotenv",
        "flask-cors",
        "requests",
    ],
    entry_points = {
        'console_scripts': ['vitamin_d_fitbit=vitamin_d_fitbit.__main__:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
