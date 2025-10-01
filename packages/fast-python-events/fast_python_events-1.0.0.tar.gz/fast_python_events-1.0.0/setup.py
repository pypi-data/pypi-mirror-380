from setuptools import find_packages, setup

setup(
    name="fast-python-events",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "celery>=5.0.0",
    ],
    extras_require={
        "django": ["django>=3.2"],
        "fastapi": ["fastapi>=0.68.0"],
        "dev": ["pytest>=6.0", "black", "isort", "mypy"],
    },
    python_requires=">=3.8",
)
