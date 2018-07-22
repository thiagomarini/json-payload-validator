import setuptools


def readme():
    with open('README.rst') as f:
        return f.read()


setuptools.setup(
    name="json_payload_validator",
    version="0.0.3",
    author="Thiago Marini",
    description="JSON validator package based on jsonschema that returns nicer validation errors for end users",
    long_description=readme(),
    keywords='json schema payload validation',
    url="https://github.com/thiagomarini/json-payload-validator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    install_requires=[
        "jsonschema",
    ],
    test_suite="nose.collector",
    tests_require=["nose"],
)
