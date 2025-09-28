from setuptools import setup, find_packages

setup(
    name="Instaweb",
    version="1.4",
    description="Instagram Web automation and utilities",
    long_description="Instaweb is a Python package to interact with Instagram web features programmatically.",
    long_description_content_type="text/markdown",
    author="Lariot & Horte",
    author_email="lariot.antsa@gmail.com",
    url="https://github.com/Trade999/Instaweb",
    packages=find_packages(),
    install_requires=[
        "requests", "bs4"
    ],
    entry_points={
        'console_scripts': [
            'instaweb-cli=Instaweb.main:main',
        ]
    },
    python_requires=">=3.6",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)