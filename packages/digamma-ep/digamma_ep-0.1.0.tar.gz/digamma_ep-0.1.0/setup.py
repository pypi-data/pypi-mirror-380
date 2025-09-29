from setuptools import setup, find_packages

setup(
    name='digamma-ep',
    version='0.1.0',
    author='Cerene Rúbio',
    author_email='your-email@example.com',
    description='Symbolic audit metrics for model divergence and integrity',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Cerene-Salt/Digamma-Prime-Framework',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'sympy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
