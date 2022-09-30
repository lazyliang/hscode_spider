# -*- coding: utf-8 -*-
"""
    Setup for PyPi
"""

from setuptools import setup

setup(
    name='code',
    version='1.0.0',
    author='lazyliang',
    author_email='liangli0128@gmail.com',
    url='https://github.com/lazyliang/hscode_spider',
    description=u'税関コード問合せデータベース',
    packages=['hscode'],
    keywords=['hscode', 'python3', 'ciq'],
    license='MIT',
    install_requires=[
        "requests",
        "beautifulsoup4",
        "lxml"
    ],
    entry_points={
        'console_scripts': [
            'hscode=main:main'
        ]
    },
    zip_safe=True
)
