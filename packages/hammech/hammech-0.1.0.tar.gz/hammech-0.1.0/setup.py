from setuptools import setup, find_packages

setup(
    name="hammech", 
    version="0.1.0",
    description="Hamiltonian-inspired phase space calculator for entropy-information flows",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="rsx",
    author_email="rsxcoding@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["numpy"],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
