from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="PSI_GLAD",
    version="0.1",
    author="Nguyen Thang Loi",
    author_email="23520872@gm.uit.edu.vn",
    url="https://github.com/DAIR-Group/PSI-GLAD",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "cvxpy",
        "mpmath",
        "numpy",
        "POT",
        "scikit-learn",
        "scipy"
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)