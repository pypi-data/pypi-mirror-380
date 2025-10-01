import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdklabs.genai-idp-bedrock-llm-processor",
    "version": "0.0.2",
    "description": "@cdklabs/genai-idp-bedrock-llm-processor",
    "license": "Apache-2.0",
    "url": "https://github.com/cdklabs/genai-idp",
    "long_description_content_type": "text/markdown",
    "author": "AWS<aws-cdk-dev@amazon.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdklabs/genai-idp"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdklabs.genai_idp_bedrock_llm_processor",
        "cdklabs.genai_idp_bedrock_llm_processor._jsii"
    ],
    "package_data": {
        "cdklabs.genai_idp_bedrock_llm_processor._jsii": [
            "genai-idp-bedrock-llm-processor@0.0.2.jsii.tgz"
        ],
        "cdklabs.genai_idp_bedrock_llm_processor": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.9",
    "install_requires": [
        "aws-cdk-lib>=2.214.0, <3.0.0",
        "aws-cdk.aws-glue-alpha>=2.214.0.a0, <3.0.0",
        "aws-cdk.aws-lambda-python-alpha>=2.214.0.a0, <3.0.0",
        "aws-cdk.aws-sagemaker-alpha>=2.214.0.a0, <3.0.0",
        "cdklabs.genai-idp>=0.0.1, <0.0.2",
        "cdklabs.generative-ai-cdk-constructs>=0.1.309, <0.2.0",
        "constructs>=10.4.2, <11.0.0",
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
        "Development Status :: 4 - Beta",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
