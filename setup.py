#!/usr/bin/env python
# coding: utf-8

from distutils.core import setup

setup(
    name="ip2loc",
    version="0.1.2",
    description="获取域名或者IP的所在地",
    author="numbbbbb",
    author_email="lj925184928@gmail.com",
    packages=["ip2loc", ],
    package_data={'ip2loc': ['17monipdb.dat'], },
    url="https://github.com/numbbbbb/python-ip",
    license="WTFPL",
    long_description=open("README.md").read(),
)
