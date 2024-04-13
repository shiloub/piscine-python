from setuptools import setup, find_packages
from readme_renderer.markdown import render

long_description = ""
with open('README.md', encoding='utf-8') as file:
  long_description = file.read()

setup(
  name = "ft_package",
  version = "0.0.1",
  summary ="a simple test package"
#   Home-page: 
  author="amontant",
  author_email="general03@XXXXXX.com",
  license='MIT',
  description='The framework to use in python project',
  url="https://gitlab.server.com/general03/myPck.git",
  packages=find_packages(exclude=["testing"]),
  install_requires=[
    'requests'
  ],
  python_requires='>=3.7',
  classifiers=[
    "Programming Language :: Python :: 3",
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3.7",
    "Topic :: Security"
  ],
)