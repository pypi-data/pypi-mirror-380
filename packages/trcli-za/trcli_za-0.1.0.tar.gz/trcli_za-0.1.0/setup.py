from setuptools import setup

setup(
    name="trcli_za",  # PyPI'de görünecek isim
    version="0.1.0",
    py_modules=["translate"],
    install_requires=[
        "click",
        "googletrans==4.0.0-rc1",
    ],
    entry_points={
        "console_scripts": [
            "translate=translate:main",
        ],
    },
    author="Senin Adın",
    author_email="seninmailin@example.com",
    description="Terminal üzerinden metin çeviri yapan CLI aracı",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seninhesabin/cli-translator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
