from setuptools import setup, find_packages

with open("README.md") as readme:
    long_description = readme.read()

setup(
    name="fruit_stand",
    version="1.0.0",
    description="Generate lists and dictionaries with fruit names and random pricing data for demonstrating fundamentals in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Keegan Good",
    author_email="keegood8@gmail.com",
    py_modules=['fruit_basket'],
    packages=find_packages(exclude=[]),
    python_requires=">=3.6",
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Utilities",
        "Operating System :: OS Independent",
    ],

)

