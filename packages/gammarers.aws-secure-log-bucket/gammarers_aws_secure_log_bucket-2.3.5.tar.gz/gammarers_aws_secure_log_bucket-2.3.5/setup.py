import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "gammarers.aws-secure-log-bucket",
    "version": "2.3.5",
    "description": "secure multiple transition phases in a single lifecycle policy bucket.",
    "license": "Apache-2.0",
    "url": "https://github.com/gammarers/aws-secure-log-bucket.git",
    "long_description_content_type": "text/markdown",
    "author": "yicr<yicr@users.noreply.github.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/gammarers/aws-secure-log-bucket.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "gammarers.aws_secure_log_bucket",
        "gammarers.aws_secure_log_bucket._jsii"
    ],
    "package_data": {
        "gammarers.aws_secure_log_bucket._jsii": [
            "aws-secure-log-bucket@2.3.5.jsii.tgz"
        ],
        "gammarers.aws_secure_log_bucket": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.9",
    "install_requires": [
        "aws-cdk-lib>=2.189.1, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "gammarers.aws-secure-bucket>=2.4.1, <3.0.0",
        "jsii>=1.114.1, <2.0.0",
        "publication>=0.0.3",
        "typeguard>=2.13.3,<4.3.0"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
