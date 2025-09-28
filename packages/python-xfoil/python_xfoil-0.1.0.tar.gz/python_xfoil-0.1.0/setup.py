from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="python-xfoil",
    version="0.1.0",
    author="cc-aero",
    author_email="",  # Add your email here
    description="A Python interface for XFOIL aerodynamic analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cc-aero/pythonxfoil",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires=">=3.6",
    install_requires=[],
)
