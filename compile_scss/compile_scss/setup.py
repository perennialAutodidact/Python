from setuptools import setup, find_packages

with open("README.md") as readme:
    long_description = readme.read()

setup(
    name="Compile SCSS",
    version="0.9.1",
    description="Compile multiple SCSS files into a single CSS file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Keegan Good",
    author_email="keegood8@gmail.com",
    py_modules=['compile_scss', 'utilities', 'observe_files', 'config'],
    packages=find_packages(exclude=[]),
    python_requires=">=3.6",
    install_requires=[
        "libsass>=0.19.4",
        "Click>=7.1.1",
        "watchdog"
    ],
    entry_points={
        "console_scripts":["compile_scss=src.compile_scss:compile_scss"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Utilities",
        "Operating System :: OS Independent",
    ],

)

