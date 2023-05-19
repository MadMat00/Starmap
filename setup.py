from setuptools import setup, find_packages

setup(
    name="Starmap",
    version="0.0.1",
    url="https://github.com/MadMat00/Starmap",
    author="Mattia Rossini",
    author_email="mattlerox03@gmail.com",
    description="Application to facilitate navigation and commerce in Star Citizen",
    packages=find_packages(),
    install_requires=[
        'Flask==2.0.1',
        'beautifulsoup4==4.9.3',
        'requests==2.25.1',
        'networkx==2.5',
        'numpy==1.20.3',
        'pandas==1.2.4',
        'lxml==4.6.3',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
    ],
)
