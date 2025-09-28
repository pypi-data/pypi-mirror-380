from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-yasmim",  # Nome do pacote alterado
    version="0.0.2",               # Versão aumentada
    author="Karina",
    description="Image Processing Package using skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tiemi/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.5",
)
