"""
cert2temp - SSL Certificate Temporary Folder Management Utility
"""

from setuptools import setup, find_packages
import os

# Read version information
def read_version():
    version_file = os.path.join(os.path.dirname(__file__), 'cert2temp', '__version__.py')
    namespace = {}
    with open(version_file, 'r', encoding='utf-8') as f:
        exec(f.read(), namespace)
    return namespace['__version__']

# Read README file
def read_readme():
    readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_file):
        with open(readme_file, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

# Read requirements
def read_requirements():
    req_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(req_file):
        with open(req_file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="cert2temp",
    version="0.1.0",
    author="Minicom",
    author_email="3387910@naver.com",
    description="SSL Certificate Temporary Folder Management Utility",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/minicom365/cert2temp",
    project_urls={
        "Bug Reports": "https://github.com/minicom365/cert2temp/issues",
        "Source": "https://github.com/minicom365/cert2temp",
    },
    packages=find_packages(exclude=["tests*", "docs*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security",
        "Topic :: System :: Networking",
    ],
    keywords="ssl certificate temp temporary folder path unicode ascii",
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": ["pytest", "pytest-cov", "black", "flake8"],
        "test": ["pytest", "pytest-cov"],
    },
    include_package_data=True,
    zip_safe=False,
)
