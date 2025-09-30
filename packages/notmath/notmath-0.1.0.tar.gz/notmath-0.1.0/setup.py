from setuptools import setup, find_packages

setup(
    name="notmath",              # Your library name (pip install my_library)
    version="0.1.0",                # Version number
    author="Beka Kopadze",
    author_email="beka.kopadze@iliauni.edu.ge", # Your email (optional)
    description="it is not for math",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_library",  # GitHub or project link
    packages=find_packages(),
    classifiers=[                   # Metadata for PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",        # Minimum Python version
)