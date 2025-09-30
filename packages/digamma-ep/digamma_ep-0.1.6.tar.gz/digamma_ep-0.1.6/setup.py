from setuptools import setup, find_packages

setup(
    name="digamma-ep",
    version="0.1.6",
    description="Symbolic audit framework for model divergence and integrity",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Cerene-Salt",
    author_email="cesarestudante16@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
