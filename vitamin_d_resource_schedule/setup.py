"""Setup file"""

import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="vitamin_d_resource_schedule",
    version="0.1.0",
    author="Joost Sijm",
    author_email="joost.sijm3@hva.nl",
    description="Vitamin-D resource schedule",
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
        "flask_mongoengine",
    ],
    entry_points = {
        'console_scripts': ['vitamin_d_resource_schedule=vitamin_d_resource_schedule.__main__:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
