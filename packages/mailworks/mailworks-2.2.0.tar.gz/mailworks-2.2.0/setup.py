"""
Setup script for the email-sender package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Read version from the package
def get_version():
    version_file = this_directory / "mailworks" / "__init__.py"
    for line in version_file.read_text().splitlines():
        if line.startswith("__version__"):
            return line.split('"')[1]
    return "0.1.0"

setup(
    name="mailworks",
    version=get_version(),
    author="Antonio Costa",
    author_email="antoniocostabr@gmail.com",
    description="A Python package for sending emails using any SMTP server with STARTTLS support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/antoniocostabr/mailworks",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Email",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies - uses only Python standard library
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/antoniocostabr/mailworks/issues",
        "Source": "https://github.com/antoniocostabr/mailworks",
        "Documentation": "https://github.com/antoniocostabr/mailworks#readme",
    },
)
