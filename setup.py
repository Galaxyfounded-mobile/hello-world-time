# setup.py

from setuptools import setup, find_packages

setup(
    name="hello_world_time",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hello-world-time = hello_world_time.hello:print_time_and_message',
        ],
    },
    author="galaxyfounded",
    author_email="host@literun.rf.gd",
    description="A simple package that prints OS time and 'Hello, World!'",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Galaxyfounded-mobile/hello-world-time/tree/main",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
