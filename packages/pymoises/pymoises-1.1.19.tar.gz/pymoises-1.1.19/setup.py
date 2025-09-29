from setuptools import setup

setup(
    name="pymoises",
    version="1.1.19",
    description="Callings from old moises endpoints...",
    author="Activatalk",
    packages=[
        "pymoises", 
        "pymoises.dto", 
        "pymoises.dto.input", 
        "pymoises.dto.input.customer",
        "pymoises.dto.input.transaction",
        "pymoises.dto.output",
        "pymoises.dto.output.customer",
        "pymoises.dto.output.transaction",
        "pymoises.dto.output.psps"
        ],
    install_requires=['requests', 'marshmallow'],
)