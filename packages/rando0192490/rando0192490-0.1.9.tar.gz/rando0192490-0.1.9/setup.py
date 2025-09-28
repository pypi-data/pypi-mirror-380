from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rando0192490",  # Package name for pip install bloxpy
    version="0.1.9",
    author="wangzhou",
    author_email="wangzhou@gmail.com",
    description="Test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wangzhou/test",  # Replace with your repo URL
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
        "pycryptodome",
    ],
    entry_points={
        'console_scripts': [
            'your-package-init = bloxapi.cli:init_function',
        ],
    },
)