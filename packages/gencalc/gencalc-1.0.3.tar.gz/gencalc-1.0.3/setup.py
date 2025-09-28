from setuptools import setup, find_packages

setup(
    name='gencalc',
    version='1.0.3',
    packages=find_packages(),
    install_requires=[],  # No external dependencies
    description='A Python library to calculate the start and end of any new or old generation.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Niral Bhatt',
    author_email='niralbhatt@hotmail.com',  
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)