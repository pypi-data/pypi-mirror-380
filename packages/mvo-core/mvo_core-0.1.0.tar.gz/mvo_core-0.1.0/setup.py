from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mvo_core",
    version="0.1.0",
    author="real853",
    author_email="2511063@zju.edu.cn",
    description="MVO algorithm for mortality vector optimization and evaluation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",  # 暂时留空
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    python_requires='>=3.8',
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
        "scikit-learn",
        "lifelines"
    ],
)
