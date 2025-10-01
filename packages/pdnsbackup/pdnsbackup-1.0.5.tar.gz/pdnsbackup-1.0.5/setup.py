#!/usr/bin/python

import setuptools
  
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    
KEYWORDS = ('powerdns pdns database backup')

setuptools.setup(
    name="pdnsbackup",
    version="1.0.5",
    author="Denis MACHARD",
    author_email="d.machard@gmail.com",
    description="Backup tool for PowerDNS database",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/dmachard/python-pdnsbackup",
    packages=['pdnsbackup'],
    include_package_data=True,
    platforms='any',
    keywords=KEYWORDS,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
    entry_points={'console_scripts': ['pdnsbackup = pdnsbackup:run']},
    install_requires=[
        "pyyaml",
        "aiomysql",
        "python-dotenv",
        "boto3",
        "prometheus-client",
    ]
)