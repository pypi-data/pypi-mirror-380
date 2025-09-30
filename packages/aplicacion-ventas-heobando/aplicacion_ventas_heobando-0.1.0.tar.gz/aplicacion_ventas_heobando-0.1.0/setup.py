from setuptools import setup, find_packages

setup(
    name="aplicacion_ventas_heobando",
    version="0.1.0",
    author="Hector Obando",
    description="Paquete para gestionar ventas, precios, impuestos y descuentos",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/heobando/aplicacion_ventas_heobando",
    packages=find_packages(),
    install_requires=[
        "setuptools",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)