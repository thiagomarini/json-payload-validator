import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json_payload_validator",
    version="0.0.1",
    author="Thiago Marini",
    description="JSON validator package based on jsonschema that returns nicer validation errors for end users",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='json schema payload validation',
    url="https://github.com/thiagomarini/json-payload-validator",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: JSON :: Validation',
    ),
    license='MIT',
    install_requires=[
        'jsonschema',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
