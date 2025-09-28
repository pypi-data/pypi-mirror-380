from setuptools import setup, find_packages

setup(
    name="aek-lregr-trainer",  # Paket adı (PyPI’de benzersiz olmalı)
    version="0.1.0",
    author="Alp Emre Karaahmet",
    author_email="alpemrekaraahmet@gmail.com",  # kendi mailini yaz
    description="Automatic ANN/DNN Linear Regression and Classification Trainer",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/alpemre8/aek-lregr-trainer",  # GitHub repo linki
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0",
        "numpy",
        "scikit-learn",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    include_package_data=True,
)
