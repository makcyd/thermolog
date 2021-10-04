import setuptools

setuptools.setup(
    name="thermolog",
    version="0.0.1",
    author="Max Sudyin",
    author_email="msudyin@gmail.com",
    description="Thermolog - Small app to log temperature at my country house",
    url="https://github.com/makcyd/thermolog",
    packages=["thermolog"],
    install_requires=["weback-unofficial", "requests", "Django", "boto3"],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
