from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="marketflow",
    version="1.1.86",
    author="ODJO OLABIYI AUREL GEOFFROY",
    author_email="xgeosoft@gmail.com",
    description="Access to African, American, European and Asian market data for financial analysis, scientific study and to provide a decision-making basis to investors.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xgeosoft/marketflow",
    packages=find_packages(where="marketflow"),
    package_dir={"": "marketflow"},
    package_data={"marketflow": ["__data__/*.db"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    install_requires=[
        "bs4>=0.0.2",
        "requests>=2.31.0",
        "numpy>=1.9.0",
        "pandas>=2.3.0",
        "tabulate>=0.9.0",
        "certifi>=2025.8.3"
    ],
    keywords=["finance", "analysis", "raw data", "market", "evaluation"],
)
