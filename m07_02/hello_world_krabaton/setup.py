from setuptools import setup, find_namespace_packages

setup(
    name='hello_world_krabaton',
    version='0.1.0',
    description='Hello world for testing',
    author='Yurii Kuchma',
    author_email='krabatua@gmail.com',
    license='MIT',
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'greeting=hello_world_krabaton.main:greeting']}
)
