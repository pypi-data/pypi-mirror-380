from setuptools import setup, find_packages

setup(
    name='digamma-ep',
    version = "0.1.5",
    author='Cerene Rúbio',
    author_email='teu@email.com',
    description='Symbolic audit framework for model divergence and integrity',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.8',
)
