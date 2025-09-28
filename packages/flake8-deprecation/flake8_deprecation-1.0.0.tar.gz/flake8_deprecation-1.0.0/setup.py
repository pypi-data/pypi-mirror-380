import setuptools

requires = [
    "flake8 > 3.0.0",
    "astroid > 3.0.0",


]

setuptools.setup(
    name="flake8_deprecation",
    license="MIT",
    version="1.0.0",
    description="flake8 extension to warning when you call a function that calls warning.warn",
    author="Campbell Starky",
    install_requires=requires,
    entry_points={
        "flake8.extension": [
            "WNG311 = flake8_deprecation:Flake8Deprecation",
        ],
    },
    py_modules=["flake8_deprecation"],
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
