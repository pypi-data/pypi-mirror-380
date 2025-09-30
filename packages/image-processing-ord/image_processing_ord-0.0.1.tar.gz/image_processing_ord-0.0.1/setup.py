from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_ord",
    version="0.0.1",
    author="ORD",
    author_email="ord@gmail.com",
    description="Pacote de Processamento de Imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    utl="https://github.com/osmarrdias/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)