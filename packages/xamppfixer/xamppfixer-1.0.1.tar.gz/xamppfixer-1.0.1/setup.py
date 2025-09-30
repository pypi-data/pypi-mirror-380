from setuptools import setup, find_packages

setup(
    name='xamppfixer',
    version='1.0.1',
    author='Sumit Poudel',
    author_email='sumitpoudel79@gmail.com',
    description='Automatic XAMPP fixer tool for Windows',
    url="https://github.com/sumitpoudelxyz/xamppfixer",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'xfix = xamppfixer.fixer:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ],
    python_requires='>=3.6',
)
