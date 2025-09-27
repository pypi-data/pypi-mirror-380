from setuptools import setup, find_packages

setup(
    name="qmemcalc",
    version="0.1.0",
    author="Sachin",
    author_email="sachin18449kumar@gmail.com",
    description="GPU Memory Estimator for QLoRA / LoRA / Transformers",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sachin62025/qmemcalc",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0",
        "transformers>=4.40",
    ],
    extras_require={
        "dev": ["pytest"]
    },
    entry_points={
        "console_scripts": [
            "qmemcalc = qmemcalc.memory:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
