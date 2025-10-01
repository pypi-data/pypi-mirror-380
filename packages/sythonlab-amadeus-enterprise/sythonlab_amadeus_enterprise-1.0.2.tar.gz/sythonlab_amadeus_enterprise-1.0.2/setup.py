from setuptools import setup, find_packages

setup(
    name='sythonlab_amadeus_enterprise',
    version='1.0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
        'zeep',
        'setuptools',
    ],
    url='https://github.com/sythonlab/SythonLab-Amadeus-Enterprise',
    author='José Angel Alvarez Abraira',
    author_email='sythonlab@gmail.com',
    description='A Python library for integration with Amadeus Enterprise Service.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires=">=3.8",
)
