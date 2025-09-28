from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-yasmim",  # Nome do pacote alterado
    version="0.0.4",               # Versão aumentada
    author="Yasmim",
    description="Image Processing Package using skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YasmimFreitas13/image-processing-yasmim.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.5",
)
