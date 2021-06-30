# -*- coding: utf-8 -*-
"""
"""

from setuptools import setup, find_packages
from pathlib import Path

HERE = Path(__file__).resolve().parent

setup(
    author="Brénainn Woodsend",
    author_email='bwoodsend@gmail.com',
    python_requires='>=3.6',
    description="Sphinx theme used for Tomial projects. "
                "Sits on top of the Sphinx readthedocs theme.",
    install_requires=["sphinx", "sphinx_rtd_theme"],
    license="MIT license",
    package_data={"sphinx_rtd_theme_configuration": ['_static/*']},
    name='sphinx_rtd_theme_configuration',
    packages=find_packages(include=['sphinx_rtd_theme_configuration',
                                    'sphinx_rtd_theme_configuration.*']),
    url='https://github.com/bwoodsend/tomial_rtd_theme',
    version="0.1.0",
    zip_safe=False,
)
