# -*- coding: utf-8 -*-
"""
Setup script for agushuju package
Compatible with both Python 2 and Python 3
"""
import sys
import os

# Python 2/3 compatibility for setuptools import
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
    from distutils.util import convert_path
    
    def find_packages(where='.', exclude=()):
        """Simple find_packages implementation for Python 2.6"""
        packages = []
        for root, dirs, files in os.walk(where):
            if '__init__.py' in files:
                package = root.replace(os.sep, '.').replace(where + '.', '')
                if package and not any(package.startswith(ex) for ex in exclude):
                    packages.append(package)
        return packages

# Read the README file
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        try:
            # Python 3
            with open(readme_path, 'r', encoding='utf-8') as f:
                return f.read()
        except TypeError:
            # Python 2
            with open(readme_path, 'r') as f:
                return f.read().decode('utf-8')
    return "爱股数据（别名：A股数据），一个集A股、期货与一体的量化交易数据服务平台。"

# Determine Python version and set appropriate dependencies
def get_dependencies():
    python_version = sys.version_info[:2]
    
    if python_version < (3, 0):
        # Python 2.7
        return [
            "requests>=2.20.0,<3.0.0",
            "pandas>=0.24.0,<1.0.0",
        ]
    elif python_version < (3, 6):
        # Python 3.5
        return [
            "requests>=2.20.0",
            "pandas>=0.24.0,<1.0.0",
        ]
    else:
        # Python 3.6+
        return [
            "requests>=2.25.0",
            "pandas>=1.1.0",
        ]

# Get package version
def get_version():
    version_file = os.path.join(os.path.dirname(__file__), 'src', 'agushuju', '__init__.py')
    try:
        # Python 3
        with open(version_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('__version__'):
                    return line.split('=')[1].strip().strip('"\'')
    except TypeError:
        # Python 2
        with open(version_file, 'r') as f:
            for line in f:
                if line.startswith('__version__'):
                    return line.split('=')[1].strip().strip('"\'')
    return "0.1.2"

setup(
    name="agushuju",
    version=get_version(),
    description="爱股数据（别名：A股数据），一个集A股、期货与一体的量化交易数据服务平台。",
    long_description=read_readme(),
    # long_description_content_type="text/markdown",  # Not supported in Python 2.7
    author="安徽爱股科技有限公司",
    author_email="jinguxun@qq.com",
    url="https://github.com/agukeji/agushuju",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_dependencies(),
    python_requires=">=2.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["agushuju", "爱股数据", "A股数据","aigushuju", "agudata", "api", "sdk", "token"],
    zip_safe=False,
)
