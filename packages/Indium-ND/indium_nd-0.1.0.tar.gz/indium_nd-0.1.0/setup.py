from setuptools import setup, find_packages

setup(
    name="Indium-ND",                 # ⚠ must be unique on PyPI
    version="0.1.0",
    author="Sayon",
    author_email="codewithsayon@gmail.com",
    description="Utility package with file operations and ASCII headings",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "pyfiglet",
        "colorama",
        "pyautogui",
        "yaspin",
        "alive-progress",
        "rich",
        "InquirerPy"
    ],
    python_requires=">=3.7",
)
