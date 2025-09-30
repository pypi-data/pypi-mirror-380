# from setuptools import setup, find_packages 

# setup(
#     name = 'aplicacion_ventas_cbracho',
#     version = '0.1.0',
#     author = 'Canchita Bracho',
#     author_email = 'canchita.bracho@gmail.com',
#     description = 'Paquete para gestionar ventas, precios, descuentos e impuestos',
#     long_description = open('README.md').read(),
#     long_description_content_type = 'text/markdown',
#     url = 'https://github.com/curso_python/aplicacion_ventas_cbracho',
#     packages = find_packages(),
#     install_requires = [],
#     classifiers = [
#         'Lenguaje de Programación::Python 3.12',
#         'License::MIT License',
#         'Sistema Operativo::Multiplataforma'
#     ],
#     python_requires='>=3.7'
#     )
from setuptools import setup, find_packages 

setup(
    name="aplicacion_ventas_cbracho",
    version="0.1.0",
    author="Canchita Bracho",
    author_email="canchita.bracho@gmail.com",
    description="Paquete para gestionar ventas, precios, descuentos e impuestos",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/curso_python/aplicacion_ventas_cbracho",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
