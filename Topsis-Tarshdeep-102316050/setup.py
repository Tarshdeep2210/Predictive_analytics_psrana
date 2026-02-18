from setuptools import setup, find_packages

setup(
    name="Topsis-Tarshdeep-102316050",
    version="0.2",
    author="Tarshdeep Kaur",
    author_email="tarshdeepkaur1@gmail.com",
    description="TOPSIS implementation for multi-criteria decision making",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Tarshdeep2210/Topsis-Tarshdeep-102316050",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "topsis-cli=topsis.topsis:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
