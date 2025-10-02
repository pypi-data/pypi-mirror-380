from setuptools import setup, find_packages

setup(
    name="h0rn3t_sp1d3r",          # Package name on PyPI
    version="1.0.0",               # Start with 0.1.0
    author="h0rn3t_sp1d3r",
    author_email="tg@gmail.com",
    description="A short description of your module",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/H0rn3t-Sp1d3rs",  # Optional
    packages=find_packages(),
    install_requires=[              # Any dependencies
        "requests",
        "colorama",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
