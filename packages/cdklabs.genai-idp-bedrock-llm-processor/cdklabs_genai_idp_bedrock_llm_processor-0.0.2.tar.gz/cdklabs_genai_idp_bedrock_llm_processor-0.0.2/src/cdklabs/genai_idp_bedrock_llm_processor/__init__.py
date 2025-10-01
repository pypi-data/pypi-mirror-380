r'''
# GenAI IDP BedrockLlmProcessor

[![Compatible with GenAI IDP version: 0.3.16](https://img.shields.io/badge/Compatible%20with%20GenAI%20IDP-0.3.16-brightgreen)](https://github.com/aws-solutions-library-samples/accelerated-intelligent-document-processing-on-aws/releases/tag/v0.3.16)
![Stability: Experimental](https://img.shields.io/badge/Stability-Experimental-important.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

> This package is provided on an "as-is" basis, and may include bugs, errors, or other issues.
> All classes are under active development and subject to non-backward compatible changes or removal in any
> future version. These are not subject to the [Semantic Versioning](https://semver.org/) model.
> This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

---


## Overview

The GenAI IDP BedrockLlmProcessor implements intelligent document processing using custom extraction with Amazon Bedrock foundation models. This package provides a flexible AWS CDK implementation for extracting structured data from a wide range of document types, offering greater control over the extraction process compared to the BdaProcessor.

The BedrockLlmProcessor is ideal for processing complex or custom document types where you need fine-grained control over the extraction process, or when dealing with documents that don't fit standard templates.

Ready to dive deeper? Explore our comprehensive [API documentation](./API.md) to discover all available constructs and configuration options that will help you build powerful custom document processing solutions.

## Features

* **Custom Extraction Logic**: Fine-grained control over how information is extracted from documents
* **Multiple Classification Methods**: Support for page-level and document-level classification
* **Multimodal Processing**: Analyze both text and visual elements for improved accuracy
* **Flexible Schema Definition**: Define custom extraction schemas for your specific document types
* **Document Summarization**: Optional AI-powered document summarization capabilities
* **Evaluation Framework**: Built-in mechanisms for evaluating extraction quality
* **Comprehensive Metrics**: Detailed CloudWatch metrics for monitoring processing performance
* **Configurable Concurrency**: Control processing throughput and resource utilization

## Getting Started

### Installation

The package is available through npm for JavaScript/TypeScript projects and PyPI for Python projects.

#### JavaScript/TypeScript (npm)

```bash
# Using npm
npm install @cdklabs/genai-idp-bedrock-llm-processor @cdklabs/genai-idp

# Using yarn
yarn add @cdklabs/genai-idp-bedrock-llm-processor @cdklabs/genai-idp
```

#### Python (PyPI)

```bash
# Using pip
pip install cdklabs.genai-idp-bedrock-llm-processor cdklabs.genai-idp

# Using poetry
poetry add cdklabs.genai-idp-bedrock-llm-processor cdklabs.genai-idp
```

### Basic Usage

Here's how to integrate BedrockLlmProcessor into your IDP solution:

```python
import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as kms from 'aws-cdk-lib/aws-kms';
import * as bedrock from '@cdklabs/generative-ai-cdk-constructs/lib/cdk-lib/bedrock';
import { ProcessingEnvironment } from '@cdklabs/genai-idp';
import { BedrockLlmProcessor, ClassificationMethod } from '@cdklabs/genai-idp-bedrock-llm-processor';

export class MyIdpStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create encryption key
    const key = new kms.Key(this, 'IdpKey', {
      enableKeyRotation: true,
    });

    // Create S3 buckets for input and output
    const inputBucket = new s3.Bucket(this, 'InputBucket', {
      encryption: s3.BucketEncryption.KMS,
      encryptionKey: key,
      eventBridgeEnabled: true,
    });

    const outputBucket = new s3.Bucket(this, 'OutputBucket', {
      encryption: s3.BucketEncryption.KMS,
      encryptionKey: key,
    });

    const workingBucket = new s3.Bucket(this, 'WorkingBucket', {
      encryption: s3.BucketEncryption.KMS,
      encryptionKey: key,
    });

    // Create processing environment
    const environment = new ProcessingEnvironment(this, 'Environment', {
      key,
      inputBucket,
      outputBucket,
      workingBucket,
      metricNamespace: 'MyIdpSolution',
    });

    // Create the processor
    const processor = new BedrockLlmProcessor(this, 'Processor', {
      environment,
      configuration: /* Your BedrockLlmProcessorConfiguration */,
      classificationMaxWorkers: 10,
      ocrMaxWorkers: 20,
    });
  }
}
```

## Classification Methods

BedrockLlmProcessor supports two classification methods to accommodate different document types:

* **MULTIMODAL_PAGE_LEVEL_CLASSIFICATION**: Uses multimodal models to classify documents at the page level. Analyzes both text and visual elements on each page for classification. This method is effective for documents where each page may belong to a different document type or category.
* **TEXTBASED_HOLISTIC_CLASSIFICATION**: Uses text-based analysis to classify the entire document holistically. Considers the full document text content for classification decisions. This method is more efficient and cost-effective as it only processes the extracted text.

Choose the classification method that best suits your document types and processing requirements.

## Configuration

BedrockLlmProcessor supports extensive configuration options:

* **Classification Method**: Choose how documents are classified and categorized
* **Invokable Models**: Specify which models to use for classification, extraction, evaluation, and summarization
* **Guardrails**: Apply content guardrails to model interactions
* **Concurrency**: Control processing throughput and resource utilization
* **VPC Configuration**: Deploy in a VPC for enhanced security and connectivity

For detailed configuration options, refer to the TypeScript type definitions and JSDoc comments in the source code.

## Contributing

We welcome contributions to the GenAI IDP BedrockLlmProcessor! Please follow these steps to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code adheres to our coding standards and includes appropriate tests.

## Related Projects

* [@cdklabs/genai-idp](../idp): Core IDP constructs and infrastructure
* [@cdklabs/genai-idp-bda-processor](../idp-bda-processor): BdaProcessor implementation using Amazon Bedrock Data Automation
* [@cdklabs/genai-idp-sagemaker-udop-processor](../idp-sagemaker-udop-processor): SagemakerUdopProcessor implementation for specialized document processing using SageMaker endpoints

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---


Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import aws_cdk.aws_cloudwatch as _aws_cdk_aws_cloudwatch_ceddda9d
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_ceddda9d
import aws_cdk.aws_stepfunctions as _aws_cdk_aws_stepfunctions_ceddda9d
import cdklabs.genai_idp as _cdklabs_genai_idp_bf65f2c1
import cdklabs.generative_ai_cdk_constructs.bedrock as _cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec
import constructs as _constructs_77d1e7e8


class BedrockLlmProcessorConfigurationDefinition(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/genai-idp-bedrock-llm-processor.BedrockLlmProcessorConfigurationDefinition",
):
    '''(experimental) Configuration definition for Pattern 2 document processing.

    Provides methods to create and customize configuration for Bedrock LLM processing.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="bankStatementSample")
    @builtins.classmethod
    def bank_statement_sample(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional["ClassificationMethod"] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "IBedrockLlmProcessorConfigurationDefinition":
        '''(experimental) Creates a configuration definition for bank statement sample processing.

        This configuration includes settings for classification, extraction,
        evaluation, and summarization optimized for bank statement documents.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition for bank statement processing

        :stability: experimental
        '''
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("IBedrockLlmProcessorConfigurationDefinition", jsii.sinvoke(cls, "bankStatementSample", [options]))

    @jsii.member(jsii_name="checkboxedAttributesExtraction")
    @builtins.classmethod
    def checkboxed_attributes_extraction(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional["ClassificationMethod"] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "IBedrockLlmProcessorConfigurationDefinition":
        '''(experimental) Creates a configuration definition optimized for checkbox attribute extraction.

        This configuration includes specialized prompts and settings for detecting
        and extracting checkbox states from documents.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition for checkbox extraction

        :stability: experimental
        '''
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("IBedrockLlmProcessorConfigurationDefinition", jsii.sinvoke(cls, "checkboxedAttributesExtraction", [options]))

    @jsii.member(jsii_name="criteriaValidation")
    @builtins.classmethod
    def criteria_validation(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional["ClassificationMethod"] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "IBedrockLlmProcessorConfigurationDefinition":
        '''(experimental) Creates a configuration definition for criteria validation processing.

        This configuration includes settings for validating documents against
        specific criteria and requirements.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition for criteria validation

        :stability: experimental
        '''
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("IBedrockLlmProcessorConfigurationDefinition", jsii.sinvoke(cls, "criteriaValidation", [options]))

    @jsii.member(jsii_name="fewShotExampleWithMultimodalPageClassification")
    @builtins.classmethod
    def few_shot_example_with_multimodal_page_classification(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional["ClassificationMethod"] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "IBedrockLlmProcessorConfigurationDefinition":
        '''(experimental) Creates a configuration definition with few-shot examples for multimodal page classification.

        This configuration includes example prompts that demonstrate how to classify
        document pages using both visual and textual information.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition with few-shot examples

        :stability: experimental
        '''
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("IBedrockLlmProcessorConfigurationDefinition", jsii.sinvoke(cls, "fewShotExampleWithMultimodalPageClassification", [options]))

    @jsii.member(jsii_name="fromFile")
    @builtins.classmethod
    def from_file(
        cls,
        file_path: builtins.str,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional["ClassificationMethod"] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "IBedrockLlmProcessorConfigurationDefinition":
        '''(experimental) Creates a configuration definition from a YAML file.

        Allows users to provide custom configuration files for document processing.

        :param file_path: Path to the YAML configuration file.
        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition loaded from the file

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ecbbbd313e533065c033957cfea1b0345a89cc5b2e70264b066674315b00e3f)
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("IBedrockLlmProcessorConfigurationDefinition", jsii.sinvoke(cls, "fromFile", [file_path, options]))

    @jsii.member(jsii_name="lendingPackageSample")
    @builtins.classmethod
    def lending_package_sample(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional["ClassificationMethod"] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "IBedrockLlmProcessorConfigurationDefinition":
        '''(experimental) Creates a configuration definition for lending package sample processing.

        This configuration includes settings for classification, extraction,
        evaluation, and summarization optimized for lending documents.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition for lending package processing

        :stability: experimental
        '''
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("IBedrockLlmProcessorConfigurationDefinition", jsii.sinvoke(cls, "lendingPackageSample", [options]))

    @jsii.member(jsii_name="medicalRecordsSummarization")
    @builtins.classmethod
    def medical_records_summarization(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional["ClassificationMethod"] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "IBedrockLlmProcessorConfigurationDefinition":
        '''(experimental) Creates a configuration definition optimized for medical records summarization.

        This configuration includes specialized prompts and settings for extracting
        and summarizing key information from medical documents.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition for medical records summarization

        :stability: experimental
        '''
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("IBedrockLlmProcessorConfigurationDefinition", jsii.sinvoke(cls, "medicalRecordsSummarization", [options]))

    @jsii.member(jsii_name="rvlCdipPackageSample")
    @builtins.classmethod
    def rvl_cdip_package_sample(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional["ClassificationMethod"] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "IBedrockLlmProcessorConfigurationDefinition":
        '''(experimental) Creates a configuration definition for RVL-CDIP package sample processing.

        This configuration includes settings for classification, extraction,
        evaluation, and summarization optimized for RVL-CDIP documents.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition for RVL-CDIP package processing

        :stability: experimental
        '''
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("IBedrockLlmProcessorConfigurationDefinition", jsii.sinvoke(cls, "rvlCdipPackageSample", [options]))

    @jsii.member(jsii_name="rvlCdipPackageSampleWithFewShotExamples")
    @builtins.classmethod
    def rvl_cdip_package_sample_with_few_shot_examples(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional["ClassificationMethod"] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "IBedrockLlmProcessorConfigurationDefinition":
        '''(experimental) Creates a configuration definition for RVL-CDIP package sample with few-shot examples.

        This configuration includes few-shot examples to improve classification and extraction
        accuracy for RVL-CDIP documents.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition for RVL-CDIP package processing with few-shot examples

        :stability: experimental
        '''
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("IBedrockLlmProcessorConfigurationDefinition", jsii.sinvoke(cls, "rvlCdipPackageSampleWithFewShotExamples", [options]))


@jsii.data_type(
    jsii_type="@cdklabs/genai-idp-bedrock-llm-processor.BedrockLlmProcessorConfigurationDefinitionOptions",
    jsii_struct_bases=[],
    name_mapping={
        "assessment_model": "assessmentModel",
        "classification_method": "classificationMethod",
        "classification_model": "classificationModel",
        "evaluation_model": "evaluationModel",
        "extraction_model": "extractionModel",
        "ocr_model": "ocrModel",
        "summarization_model": "summarizationModel",
    },
)
class BedrockLlmProcessorConfigurationDefinitionOptions:
    def __init__(
        self,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional["ClassificationMethod"] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> None:
        '''(experimental) Options for configuring the Bedrock LLM processor configuration definition.

        Allows customization of classification, extraction, evaluation, summarization, and OCR stages.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38bf2cc189f96acbec7d1624475f43abb0ca3ce6b614a3fe0b0e552a9f7a7ea1)
            check_type(argname="argument assessment_model", value=assessment_model, expected_type=type_hints["assessment_model"])
            check_type(argname="argument classification_method", value=classification_method, expected_type=type_hints["classification_method"])
            check_type(argname="argument classification_model", value=classification_model, expected_type=type_hints["classification_model"])
            check_type(argname="argument evaluation_model", value=evaluation_model, expected_type=type_hints["evaluation_model"])
            check_type(argname="argument extraction_model", value=extraction_model, expected_type=type_hints["extraction_model"])
            check_type(argname="argument ocr_model", value=ocr_model, expected_type=type_hints["ocr_model"])
            check_type(argname="argument summarization_model", value=summarization_model, expected_type=type_hints["summarization_model"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if assessment_model is not None:
            self._values["assessment_model"] = assessment_model
        if classification_method is not None:
            self._values["classification_method"] = classification_method
        if classification_model is not None:
            self._values["classification_model"] = classification_model
        if evaluation_model is not None:
            self._values["evaluation_model"] = evaluation_model
        if extraction_model is not None:
            self._values["extraction_model"] = extraction_model
        if ocr_model is not None:
            self._values["ocr_model"] = ocr_model
        if summarization_model is not None:
            self._values["summarization_model"] = summarization_model

    @builtins.property
    def assessment_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional model for the assessment stage.

        :stability: experimental
        '''
        result = self._values.get("assessment_model")
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], result)

    @builtins.property
    def classification_method(self) -> typing.Optional["ClassificationMethod"]:
        '''(experimental) Optional classification method to use for document categorization.

        Determines how documents are analyzed and categorized before extraction.

        :stability: experimental
        '''
        result = self._values.get("classification_method")
        return typing.cast(typing.Optional["ClassificationMethod"], result)

    @builtins.property
    def classification_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional model for the classification stage.

        :stability: experimental
        '''
        result = self._values.get("classification_model")
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], result)

    @builtins.property
    def evaluation_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional model for the evaluation stage.

        :stability: experimental
        '''
        result = self._values.get("evaluation_model")
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], result)

    @builtins.property
    def extraction_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional model for the extraction stage.

        :stability: experimental
        '''
        result = self._values.get("extraction_model")
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], result)

    @builtins.property
    def ocr_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional model for the OCR stage when using Bedrock-based OCR.

        Only used when the OCR backend is set to 'bedrock' in the configuration.

        :stability: experimental
        '''
        result = self._values.get("ocr_model")
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], result)

    @builtins.property
    def summarization_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional model for the summarization stage.

        :stability: experimental
        '''
        result = self._values.get("summarization_model")
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BedrockLlmProcessorConfigurationDefinitionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/genai-idp-bedrock-llm-processor.BedrockLlmProcessorProps",
    jsii_struct_bases=[_cdklabs_genai_idp_bf65f2c1.DocumentProcessorProps],
    name_mapping={
        "environment": "environment",
        "max_processing_concurrency": "maxProcessingConcurrency",
        "configuration": "configuration",
        "assessment_guardrail": "assessmentGuardrail",
        "classification_guardrail": "classificationGuardrail",
        "classification_max_workers": "classificationMaxWorkers",
        "custom_prompt_generator": "customPromptGenerator",
        "enable_hitl": "enableHitl",
        "evaluation_baseline_bucket": "evaluationBaselineBucket",
        "extraction_guardrail": "extractionGuardrail",
        "ocr_guardrail": "ocrGuardrail",
        "ocr_max_workers": "ocrMaxWorkers",
        "sage_maker_a2_i_review_portal_url": "sageMakerA2IReviewPortalUrl",
        "summarization_guardrail": "summarizationGuardrail",
    },
)
class BedrockLlmProcessorProps(_cdklabs_genai_idp_bf65f2c1.DocumentProcessorProps):
    def __init__(
        self,
        *,
        environment: _cdklabs_genai_idp_bf65f2c1.IProcessingEnvironment,
        max_processing_concurrency: typing.Optional[jsii.Number] = None,
        configuration: "IBedrockLlmProcessorConfiguration",
        assessment_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        classification_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        classification_max_workers: typing.Optional[jsii.Number] = None,
        custom_prompt_generator: typing.Optional[_cdklabs_genai_idp_bf65f2c1.ICustomPromptGenerator] = None,
        enable_hitl: typing.Optional[builtins.bool] = None,
        evaluation_baseline_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        extraction_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        ocr_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        ocr_max_workers: typing.Optional[jsii.Number] = None,
        sage_maker_a2_i_review_portal_url: typing.Optional[builtins.str] = None,
        summarization_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    ) -> None:
        '''(experimental) Configuration properties for the Bedrock LLM document processor.

        Bedrock LLM Processor uses custom extraction with Amazon Bedrock models, providing
        flexible document processing capabilities for a wide range of document types.
        This processor is ideal when you need more control over the extraction process
        and want to implement custom classification and extraction logic using
        foundation models directly.

        Bedrock LLM Processor offers a balance between customization and implementation complexity,
        allowing you to define custom extraction schemas and prompts while leveraging
        the power of Amazon Bedrock foundation models.

        :param environment: (experimental) The processing environment that provides shared infrastructure and services. Contains input/output buckets, tracking tables, API endpoints, and other resources needed for document processing operations.
        :param max_processing_concurrency: (experimental) The maximum number of documents that can be processed concurrently. Controls the throughput and resource utilization of the document processing system. Default: 100 concurrent workflows
        :param configuration: (experimental) Configuration for the Bedrock LLM document processor. Provides customization options for the processing workflow, including schema definitions, prompts, and evaluation settings.
        :param assessment_guardrail: (experimental) Optional Bedrock guardrail to apply to assessment model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param classification_guardrail: (experimental) Optional Bedrock guardrail to apply to classification model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param classification_max_workers: (experimental) The maximum number of concurrent workers for document classification. Controls parallelism during the classification phase to optimize throughput while managing resource utilization. Default: 20
        :param custom_prompt_generator: (experimental) Optional custom prompt generator for injecting business logic into extraction processing. When provided, this Lambda function will be called to customize prompts based on document content, business rules, or external system integrations. Default: - No custom prompt generator is used
        :param enable_hitl: (experimental) Enable Human In The Loop (A2I) for document review. Default: false
        :param evaluation_baseline_bucket: (experimental) Optional S3 bucket containing baseline documents for evaluation. Used as ground truth when evaluating extraction accuracy by comparing extraction results against known correct values. Default: - No evaluation baseline bucket is configured
        :param extraction_guardrail: (experimental) Optional Bedrock guardrail to apply to extraction model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param ocr_guardrail: (experimental) Optional Bedrock guardrail to apply to OCR model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param ocr_max_workers: (experimental) The maximum number of concurrent workers for OCR processing. Controls parallelism during the text extraction phase to optimize throughput while managing resource utilization. Default: 20
        :param sage_maker_a2_i_review_portal_url: (experimental) Optional SageMaker A2I Review Portal URL for HITL workflows. Used to provide human reviewers with access to the A2I review interface for document validation and correction workflows. Default: - No A2I review portal URL is configured
        :param summarization_guardrail: (experimental) Optional Bedrock guardrail to apply to summarization model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8644cca7bc5dc380c9174019dfc3937fe8b5a9c175901bbbb59c07ee2a628f51)
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument max_processing_concurrency", value=max_processing_concurrency, expected_type=type_hints["max_processing_concurrency"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument assessment_guardrail", value=assessment_guardrail, expected_type=type_hints["assessment_guardrail"])
            check_type(argname="argument classification_guardrail", value=classification_guardrail, expected_type=type_hints["classification_guardrail"])
            check_type(argname="argument classification_max_workers", value=classification_max_workers, expected_type=type_hints["classification_max_workers"])
            check_type(argname="argument custom_prompt_generator", value=custom_prompt_generator, expected_type=type_hints["custom_prompt_generator"])
            check_type(argname="argument enable_hitl", value=enable_hitl, expected_type=type_hints["enable_hitl"])
            check_type(argname="argument evaluation_baseline_bucket", value=evaluation_baseline_bucket, expected_type=type_hints["evaluation_baseline_bucket"])
            check_type(argname="argument extraction_guardrail", value=extraction_guardrail, expected_type=type_hints["extraction_guardrail"])
            check_type(argname="argument ocr_guardrail", value=ocr_guardrail, expected_type=type_hints["ocr_guardrail"])
            check_type(argname="argument ocr_max_workers", value=ocr_max_workers, expected_type=type_hints["ocr_max_workers"])
            check_type(argname="argument sage_maker_a2_i_review_portal_url", value=sage_maker_a2_i_review_portal_url, expected_type=type_hints["sage_maker_a2_i_review_portal_url"])
            check_type(argname="argument summarization_guardrail", value=summarization_guardrail, expected_type=type_hints["summarization_guardrail"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "environment": environment,
            "configuration": configuration,
        }
        if max_processing_concurrency is not None:
            self._values["max_processing_concurrency"] = max_processing_concurrency
        if assessment_guardrail is not None:
            self._values["assessment_guardrail"] = assessment_guardrail
        if classification_guardrail is not None:
            self._values["classification_guardrail"] = classification_guardrail
        if classification_max_workers is not None:
            self._values["classification_max_workers"] = classification_max_workers
        if custom_prompt_generator is not None:
            self._values["custom_prompt_generator"] = custom_prompt_generator
        if enable_hitl is not None:
            self._values["enable_hitl"] = enable_hitl
        if evaluation_baseline_bucket is not None:
            self._values["evaluation_baseline_bucket"] = evaluation_baseline_bucket
        if extraction_guardrail is not None:
            self._values["extraction_guardrail"] = extraction_guardrail
        if ocr_guardrail is not None:
            self._values["ocr_guardrail"] = ocr_guardrail
        if ocr_max_workers is not None:
            self._values["ocr_max_workers"] = ocr_max_workers
        if sage_maker_a2_i_review_portal_url is not None:
            self._values["sage_maker_a2_i_review_portal_url"] = sage_maker_a2_i_review_portal_url
        if summarization_guardrail is not None:
            self._values["summarization_guardrail"] = summarization_guardrail

    @builtins.property
    def environment(self) -> _cdklabs_genai_idp_bf65f2c1.IProcessingEnvironment:
        '''(experimental) The processing environment that provides shared infrastructure and services.

        Contains input/output buckets, tracking tables, API endpoints, and other
        resources needed for document processing operations.

        :stability: experimental
        '''
        result = self._values.get("environment")
        assert result is not None, "Required property 'environment' is missing"
        return typing.cast(_cdklabs_genai_idp_bf65f2c1.IProcessingEnvironment, result)

    @builtins.property
    def max_processing_concurrency(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The maximum number of documents that can be processed concurrently.

        Controls the throughput and resource utilization of the document processing system.

        :default: 100 concurrent workflows

        :stability: experimental
        '''
        result = self._values.get("max_processing_concurrency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def configuration(self) -> "IBedrockLlmProcessorConfiguration":
        '''(experimental) Configuration for the Bedrock LLM document processor.

        Provides customization options for the processing workflow,
        including schema definitions, prompts, and evaluation settings.

        :stability: experimental
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast("IBedrockLlmProcessorConfiguration", result)

    @builtins.property
    def assessment_guardrail(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail]:
        '''(experimental) Optional Bedrock guardrail to apply to assessment model interactions.

        Helps ensure model outputs adhere to content policies and guidelines
        by filtering inappropriate content and enforcing usage policies.

        :default: - No guardrail is applied

        :stability: experimental
        '''
        result = self._values.get("assessment_guardrail")
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail], result)

    @builtins.property
    def classification_guardrail(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail]:
        '''(experimental) Optional Bedrock guardrail to apply to classification model interactions.

        Helps ensure model outputs adhere to content policies and guidelines
        by filtering inappropriate content and enforcing usage policies.

        :default: - No guardrail is applied

        :stability: experimental
        '''
        result = self._values.get("classification_guardrail")
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail], result)

    @builtins.property
    def classification_max_workers(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The maximum number of concurrent workers for document classification.

        Controls parallelism during the classification phase to optimize
        throughput while managing resource utilization.

        :default: 20

        :stability: experimental
        '''
        result = self._values.get("classification_max_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def custom_prompt_generator(
        self,
    ) -> typing.Optional[_cdklabs_genai_idp_bf65f2c1.ICustomPromptGenerator]:
        '''(experimental) Optional custom prompt generator for injecting business logic into extraction processing.

        When provided, this Lambda function will be called to customize prompts based on
        document content, business rules, or external system integrations.

        :default: - No custom prompt generator is used

        :stability: experimental
        '''
        result = self._values.get("custom_prompt_generator")
        return typing.cast(typing.Optional[_cdklabs_genai_idp_bf65f2c1.ICustomPromptGenerator], result)

    @builtins.property
    def enable_hitl(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Enable Human In The Loop (A2I) for document review.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("enable_hitl")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def evaluation_baseline_bucket(
        self,
    ) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket]:
        '''(experimental) Optional S3 bucket containing baseline documents for evaluation.

        Used as ground truth when evaluating extraction accuracy by
        comparing extraction results against known correct values.

        :default: - No evaluation baseline bucket is configured

        :stability: experimental
        '''
        result = self._values.get("evaluation_baseline_bucket")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket], result)

    @builtins.property
    def extraction_guardrail(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail]:
        '''(experimental) Optional Bedrock guardrail to apply to extraction model interactions.

        Helps ensure model outputs adhere to content policies and guidelines
        by filtering inappropriate content and enforcing usage policies.

        :default: - No guardrail is applied

        :stability: experimental
        '''
        result = self._values.get("extraction_guardrail")
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail], result)

    @builtins.property
    def ocr_guardrail(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail]:
        '''(experimental) Optional Bedrock guardrail to apply to OCR model interactions.

        Helps ensure model outputs adhere to content policies and guidelines
        by filtering inappropriate content and enforcing usage policies.

        :default: - No guardrail is applied

        :stability: experimental
        '''
        result = self._values.get("ocr_guardrail")
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail], result)

    @builtins.property
    def ocr_max_workers(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The maximum number of concurrent workers for OCR processing.

        Controls parallelism during the text extraction phase to optimize
        throughput while managing resource utilization.

        :default: 20

        :stability: experimental
        '''
        result = self._values.get("ocr_max_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sage_maker_a2_i_review_portal_url(self) -> typing.Optional[builtins.str]:
        '''(experimental) Optional SageMaker A2I Review Portal URL for HITL workflows.

        Used to provide human reviewers with access to the A2I review interface
        for document validation and correction workflows.

        :default: - No A2I review portal URL is configured

        :stability: experimental
        '''
        result = self._values.get("sage_maker_a2_i_review_portal_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summarization_guardrail(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail]:
        '''(experimental) Optional Bedrock guardrail to apply to summarization model interactions.

        Helps ensure model outputs adhere to content policies and guidelines
        by filtering inappropriate content and enforcing usage policies.

        :default: - No guardrail is applied

        :stability: experimental
        '''
        result = self._values.get("summarization_guardrail")
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BedrockLlmProcessorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cdklabs/genai-idp-bedrock-llm-processor.ClassificationMethod")
class ClassificationMethod(enum.Enum):
    '''(experimental) Defines the methods available for document classification in Pattern 2 processing.

    Document classification is a critical step in the IDP workflow that determines
    how documents are categorized and processed. Different classification methods
    offer varying levels of accuracy, performance, and capabilities.

    :stability: experimental
    '''

    MULTIMODAL_PAGE_LEVEL_CLASSIFICATION = "MULTIMODAL_PAGE_LEVEL_CLASSIFICATION"
    '''(experimental) Uses multimodal models to classify documents at the page level.

    Analyzes both text and visual elements on each page for classification.

    This method is effective for documents where each page may belong to a different
    document type or category. It provides high accuracy for complex layouts by
    considering both textual content and visual structure of each page individually.

    :stability: experimental
    '''
    TEXTBASED_HOLISTIC_CLASSIFICATION = "TEXTBASED_HOLISTIC_CLASSIFICATION"
    '''(experimental) Uses text-based analysis to classify the entire document holistically. Considers the full document text content for classification decisions.

    This method is more efficient and cost-effective as it only processes the
    extracted text. It works well for text-heavy documents where the document type
    is consistent across all pages and visual elements are less important for classification.

    :stability: experimental
    '''


@jsii.interface(
    jsii_type="@cdklabs/genai-idp-bedrock-llm-processor.IBedrockLlmProcessor"
)
class IBedrockLlmProcessor(
    _cdklabs_genai_idp_bf65f2c1.IDocumentProcessor,
    typing_extensions.Protocol,
):
    '''(experimental) Interface for Bedrock LLM document processor implementation.

    Bedrock LLM Processor uses custom extraction with Amazon Bedrock models for flexible
    document processing. This processor provides more control over the extraction
    process and is ideal for custom document types or complex extraction needs
    that require fine-grained control over the processing workflow.

    Use Bedrock LLM Processor when:

    - Processing custom or complex document types not well-handled by BDA Processor
    - You need more control over the extraction process and prompting
    - You want to leverage foundation models directly with custom prompts
    - You need to implement custom classification logic

    :stability: experimental
    '''

    pass


class _IBedrockLlmProcessorProxy(
    jsii.proxy_for(_cdklabs_genai_idp_bf65f2c1.IDocumentProcessor), # type: ignore[misc]
):
    '''(experimental) Interface for Bedrock LLM document processor implementation.

    Bedrock LLM Processor uses custom extraction with Amazon Bedrock models for flexible
    document processing. This processor provides more control over the extraction
    process and is ideal for custom document types or complex extraction needs
    that require fine-grained control over the processing workflow.

    Use Bedrock LLM Processor when:

    - Processing custom or complex document types not well-handled by BDA Processor
    - You need more control over the extraction process and prompting
    - You want to leverage foundation models directly with custom prompts
    - You need to implement custom classification logic

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/genai-idp-bedrock-llm-processor.IBedrockLlmProcessor"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBedrockLlmProcessor).__jsii_proxy_class__ = lambda : _IBedrockLlmProcessorProxy


@jsii.interface(
    jsii_type="@cdklabs/genai-idp-bedrock-llm-processor.IBedrockLlmProcessorConfiguration"
)
class IBedrockLlmProcessorConfiguration(typing_extensions.Protocol):
    '''(experimental) Interface for Bedrock LLM document processor configuration.

    Provides configuration management for custom extraction with Bedrock models.

    :stability: experimental
    '''

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        processor: IBedrockLlmProcessor,
    ) -> "IBedrockLlmProcessorConfigurationDefinition":
        '''(experimental) Binds the configuration to a processor instance.

        This method applies the configuration to the processor.

        :param processor: The Bedrock LLM document processor to apply to.

        :stability: experimental
        '''
        ...


class _IBedrockLlmProcessorConfigurationProxy:
    '''(experimental) Interface for Bedrock LLM document processor configuration.

    Provides configuration management for custom extraction with Bedrock models.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/genai-idp-bedrock-llm-processor.IBedrockLlmProcessorConfiguration"

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        processor: IBedrockLlmProcessor,
    ) -> "IBedrockLlmProcessorConfigurationDefinition":
        '''(experimental) Binds the configuration to a processor instance.

        This method applies the configuration to the processor.

        :param processor: The Bedrock LLM document processor to apply to.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86ddfd2ba0632bff2d76cad6b515de1975c87fc4896505961c68983c344d185d)
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        return typing.cast("IBedrockLlmProcessorConfigurationDefinition", jsii.invoke(self, "bind", [processor]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBedrockLlmProcessorConfiguration).__jsii_proxy_class__ = lambda : _IBedrockLlmProcessorConfigurationProxy


@jsii.interface(
    jsii_type="@cdklabs/genai-idp-bedrock-llm-processor.IBedrockLlmProcessorConfigurationDefinition"
)
class IBedrockLlmProcessorConfigurationDefinition(
    _cdklabs_genai_idp_bf65f2c1.IConfigurationDefinition,
    typing_extensions.Protocol,
):
    '''
    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="classificationMethod")
    def classification_method(self) -> ClassificationMethod:
        '''(experimental) The method used for document classification.

        Determines how documents are analyzed and categorized before extraction.
        Different methods offer varying levels of accuracy and performance.

        :default: - as defined in the definition file

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="classificationModel")
    def classification_model(
        self,
    ) -> _cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable:
        '''(experimental) The invokable model used for document classification.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.
        Determines document types and categories based on content analysis,
        enabling targeted extraction strategies for different document types.

        :default: - as defined in the definition file

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="extractionModel")
    def extraction_model(
        self,
    ) -> _cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable:
        '''(experimental) The invokable model used for information extraction.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.
        Extracts structured data from documents based on defined schemas,
        transforming unstructured content into structured information.

        :default: - as defined in the definition file

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="ocrBackend")
    def ocr_backend(self) -> builtins.str:
        '''(experimental) OCR backend to use for text extraction.

        Determines whether to use Amazon Textract or Bedrock for OCR processing.

        :default: "textract"

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="assessmentModel")
    def assessment_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional invokable model used for evaluating assessment results.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.
        Used to assess the quality and accuracy of extracted information by
        comparing assessment results against expected values.

        :default: - as defined in the definition file

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="evaluationModel")
    def evaluation_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional invokable model used for evaluating extraction results.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.
        Used to assess the quality and accuracy of extracted information by
        comparing extraction results against expected values.

        :default: - as defined in the definition file

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="ocrModel")
    def ocr_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional invokable model used for OCR when using Bedrock-based OCR.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.
        Only used when the OCR backend is set to 'bedrock' in the configuration.
        Provides vision-based text extraction capabilities for document processing.

        :default: - as defined in the definition file

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="summarizationModel")
    def summarization_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional invokable model used for document summarization.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.
        When provided, enables automatic generation of document summaries
        that capture key information from processed documents.

        :default: - as defined in the definition file

        :stability: experimental
        '''
        ...


class _IBedrockLlmProcessorConfigurationDefinitionProxy(
    jsii.proxy_for(_cdklabs_genai_idp_bf65f2c1.IConfigurationDefinition), # type: ignore[misc]
):
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/genai-idp-bedrock-llm-processor.IBedrockLlmProcessorConfigurationDefinition"

    @builtins.property
    @jsii.member(jsii_name="classificationMethod")
    def classification_method(self) -> ClassificationMethod:
        '''(experimental) The method used for document classification.

        Determines how documents are analyzed and categorized before extraction.
        Different methods offer varying levels of accuracy and performance.

        :default: - as defined in the definition file

        :stability: experimental
        '''
        return typing.cast(ClassificationMethod, jsii.get(self, "classificationMethod"))

    @builtins.property
    @jsii.member(jsii_name="classificationModel")
    def classification_model(
        self,
    ) -> _cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable:
        '''(experimental) The invokable model used for document classification.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.
        Determines document types and categories based on content analysis,
        enabling targeted extraction strategies for different document types.

        :default: - as defined in the definition file

        :stability: experimental
        '''
        return typing.cast(_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable, jsii.get(self, "classificationModel"))

    @builtins.property
    @jsii.member(jsii_name="extractionModel")
    def extraction_model(
        self,
    ) -> _cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable:
        '''(experimental) The invokable model used for information extraction.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.
        Extracts structured data from documents based on defined schemas,
        transforming unstructured content into structured information.

        :default: - as defined in the definition file

        :stability: experimental
        '''
        return typing.cast(_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable, jsii.get(self, "extractionModel"))

    @builtins.property
    @jsii.member(jsii_name="ocrBackend")
    def ocr_backend(self) -> builtins.str:
        '''(experimental) OCR backend to use for text extraction.

        Determines whether to use Amazon Textract or Bedrock for OCR processing.

        :default: "textract"

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "ocrBackend"))

    @builtins.property
    @jsii.member(jsii_name="assessmentModel")
    def assessment_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional invokable model used for evaluating assessment results.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.
        Used to assess the quality and accuracy of extracted information by
        comparing assessment results against expected values.

        :default: - as defined in the definition file

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], jsii.get(self, "assessmentModel"))

    @builtins.property
    @jsii.member(jsii_name="evaluationModel")
    def evaluation_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional invokable model used for evaluating extraction results.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.
        Used to assess the quality and accuracy of extracted information by
        comparing extraction results against expected values.

        :default: - as defined in the definition file

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], jsii.get(self, "evaluationModel"))

    @builtins.property
    @jsii.member(jsii_name="ocrModel")
    def ocr_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional invokable model used for OCR when using Bedrock-based OCR.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.
        Only used when the OCR backend is set to 'bedrock' in the configuration.
        Provides vision-based text extraction capabilities for document processing.

        :default: - as defined in the definition file

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], jsii.get(self, "ocrModel"))

    @builtins.property
    @jsii.member(jsii_name="summarizationModel")
    def summarization_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional invokable model used for document summarization.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.
        When provided, enables automatic generation of document summaries
        that capture key information from processed documents.

        :default: - as defined in the definition file

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], jsii.get(self, "summarizationModel"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBedrockLlmProcessorConfigurationDefinition).__jsii_proxy_class__ = lambda : _IBedrockLlmProcessorConfigurationDefinitionProxy


@jsii.interface(
    jsii_type="@cdklabs/genai-idp-bedrock-llm-processor.IBedrockLlmProcessorConfigurationSchema"
)
class IBedrockLlmProcessorConfigurationSchema(typing_extensions.Protocol):
    '''(experimental) Interface for Bedrock LLM configuration schema.

    Defines the structure and validation rules for Bedrock LLM processor configuration.

    :stability: experimental
    '''

    @jsii.member(jsii_name="bind")
    def bind(self, processor: IBedrockLlmProcessor) -> None:
        '''(experimental) Binds the configuration schema to a processor instance.

        This method applies the schema definition to the processor's configuration table.

        :param processor: The Bedrock LLM document processor to apply the schema to.

        :stability: experimental
        '''
        ...


class _IBedrockLlmProcessorConfigurationSchemaProxy:
    '''(experimental) Interface for Bedrock LLM configuration schema.

    Defines the structure and validation rules for Bedrock LLM processor configuration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/genai-idp-bedrock-llm-processor.IBedrockLlmProcessorConfigurationSchema"

    @jsii.member(jsii_name="bind")
    def bind(self, processor: IBedrockLlmProcessor) -> None:
        '''(experimental) Binds the configuration schema to a processor instance.

        This method applies the schema definition to the processor's configuration table.

        :param processor: The Bedrock LLM document processor to apply the schema to.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41fbec2ee612f5718839556204137eac96e55b9b0d53152cd03b222e0c66424b)
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        return typing.cast(None, jsii.invoke(self, "bind", [processor]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBedrockLlmProcessorConfigurationSchema).__jsii_proxy_class__ = lambda : _IBedrockLlmProcessorConfigurationSchemaProxy


@jsii.implements(IBedrockLlmProcessor)
class BedrockLlmProcessor(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/genai-idp-bedrock-llm-processor.BedrockLlmProcessor",
):
    '''(experimental) This processor implements an intelligent document processing workflow that uses Amazon Bedrock with Nova or Claude models for both page classification/grouping and information extraction.

    The workflow consists of three main processing steps:

    - OCR processing using Amazon Textract
    - Page classification and grouping using Claude via Amazon Bedrock
    - Field extraction using Claude via Amazon Bedrock

    :stability: experimental
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        configuration: IBedrockLlmProcessorConfiguration,
        assessment_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        classification_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        classification_max_workers: typing.Optional[jsii.Number] = None,
        custom_prompt_generator: typing.Optional[_cdklabs_genai_idp_bf65f2c1.ICustomPromptGenerator] = None,
        enable_hitl: typing.Optional[builtins.bool] = None,
        evaluation_baseline_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        extraction_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        ocr_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        ocr_max_workers: typing.Optional[jsii.Number] = None,
        sage_maker_a2_i_review_portal_url: typing.Optional[builtins.str] = None,
        summarization_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        environment: _cdklabs_genai_idp_bf65f2c1.IProcessingEnvironment,
        max_processing_concurrency: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param configuration: (experimental) Configuration for the Bedrock LLM document processor. Provides customization options for the processing workflow, including schema definitions, prompts, and evaluation settings.
        :param assessment_guardrail: (experimental) Optional Bedrock guardrail to apply to assessment model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param classification_guardrail: (experimental) Optional Bedrock guardrail to apply to classification model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param classification_max_workers: (experimental) The maximum number of concurrent workers for document classification. Controls parallelism during the classification phase to optimize throughput while managing resource utilization. Default: 20
        :param custom_prompt_generator: (experimental) Optional custom prompt generator for injecting business logic into extraction processing. When provided, this Lambda function will be called to customize prompts based on document content, business rules, or external system integrations. Default: - No custom prompt generator is used
        :param enable_hitl: (experimental) Enable Human In The Loop (A2I) for document review. Default: false
        :param evaluation_baseline_bucket: (experimental) Optional S3 bucket containing baseline documents for evaluation. Used as ground truth when evaluating extraction accuracy by comparing extraction results against known correct values. Default: - No evaluation baseline bucket is configured
        :param extraction_guardrail: (experimental) Optional Bedrock guardrail to apply to extraction model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param ocr_guardrail: (experimental) Optional Bedrock guardrail to apply to OCR model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param ocr_max_workers: (experimental) The maximum number of concurrent workers for OCR processing. Controls parallelism during the text extraction phase to optimize throughput while managing resource utilization. Default: 20
        :param sage_maker_a2_i_review_portal_url: (experimental) Optional SageMaker A2I Review Portal URL for HITL workflows. Used to provide human reviewers with access to the A2I review interface for document validation and correction workflows. Default: - No A2I review portal URL is configured
        :param summarization_guardrail: (experimental) Optional Bedrock guardrail to apply to summarization model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param environment: (experimental) The processing environment that provides shared infrastructure and services. Contains input/output buckets, tracking tables, API endpoints, and other resources needed for document processing operations.
        :param max_processing_concurrency: (experimental) The maximum number of documents that can be processed concurrently. Controls the throughput and resource utilization of the document processing system. Default: 100 concurrent workflows

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c33945804a9c92aa98911d16b029701afa4bd79586d4573531a09b7c9636b74)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BedrockLlmProcessorProps(
            configuration=configuration,
            assessment_guardrail=assessment_guardrail,
            classification_guardrail=classification_guardrail,
            classification_max_workers=classification_max_workers,
            custom_prompt_generator=custom_prompt_generator,
            enable_hitl=enable_hitl,
            evaluation_baseline_bucket=evaluation_baseline_bucket,
            extraction_guardrail=extraction_guardrail,
            ocr_guardrail=ocr_guardrail,
            ocr_max_workers=ocr_max_workers,
            sage_maker_a2_i_review_portal_url=sage_maker_a2_i_review_portal_url,
            summarization_guardrail=summarization_guardrail,
            environment=environment,
            max_processing_concurrency=max_processing_concurrency,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="metricBedrockEmbeddingMaxRetriesExceeded")
    def metric_bedrock_embedding_max_retries_exceeded(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for Bedrock embedding requests that exceeded max retries.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for Bedrock embedding requests that exceeded max retries

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockEmbeddingMaxRetriesExceeded", [props]))

    @jsii.member(jsii_name="metricBedrockEmbeddingNonRetryableErrors")
    def metric_bedrock_embedding_non_retryable_errors(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for Bedrock embedding non-retryable errors.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for Bedrock embedding non-retryable errors

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockEmbeddingNonRetryableErrors", [props]))

    @jsii.member(jsii_name="metricBedrockEmbeddingRequestLatency")
    def metric_bedrock_embedding_request_latency(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for Bedrock embedding request latency.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for Bedrock embedding request latency in milliseconds

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockEmbeddingRequestLatency", [props]))

    @jsii.member(jsii_name="metricBedrockEmbeddingRequestsFailed")
    def metric_bedrock_embedding_requests_failed(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for failed Bedrock embedding requests.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for failed Bedrock embedding requests

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockEmbeddingRequestsFailed", [props]))

    @jsii.member(jsii_name="metricBedrockEmbeddingRequestsSucceeded")
    def metric_bedrock_embedding_requests_succeeded(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for successful Bedrock embedding requests.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for successful Bedrock embedding requests

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockEmbeddingRequestsSucceeded", [props]))

    @jsii.member(jsii_name="metricBedrockEmbeddingRequestsTotal")
    def metric_bedrock_embedding_requests_total(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for total Bedrock embedding requests.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for total Bedrock embedding requests

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockEmbeddingRequestsTotal", [props]))

    @jsii.member(jsii_name="metricBedrockEmbeddingThrottles")
    def metric_bedrock_embedding_throttles(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for Bedrock embedding request throttles.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for Bedrock embedding request throttles

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockEmbeddingThrottles", [props]))

    @jsii.member(jsii_name="metricBedrockEmbeddingUnexpectedErrors")
    def metric_bedrock_embedding_unexpected_errors(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for Bedrock embedding unexpected errors.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for Bedrock embedding unexpected errors

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockEmbeddingUnexpectedErrors", [props]))

    @jsii.member(jsii_name="metricBedrockMaxRetriesExceeded")
    def metric_bedrock_max_retries_exceeded(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for Bedrock requests that exceeded max retries.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for Bedrock requests that exceeded max retries

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockMaxRetriesExceeded", [props]))

    @jsii.member(jsii_name="metricBedrockNonRetryableErrors")
    def metric_bedrock_non_retryable_errors(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for Bedrock non-retryable errors.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for Bedrock non-retryable errors

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockNonRetryableErrors", [props]))

    @jsii.member(jsii_name="metricBedrockRequestLatency")
    def metric_bedrock_request_latency(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for Bedrock request latency.

        Measures individual request processing time.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for Bedrock request latency in milliseconds

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockRequestLatency", [props]))

    @jsii.member(jsii_name="metricBedrockRequestsFailed")
    def metric_bedrock_requests_failed(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for failed Bedrock requests.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for failed Bedrock requests

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockRequestsFailed", [props]))

    @jsii.member(jsii_name="metricBedrockRequestsSucceeded")
    def metric_bedrock_requests_succeeded(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for successful Bedrock requests.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for successful Bedrock requests

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockRequestsSucceeded", [props]))

    @jsii.member(jsii_name="metricBedrockRequestsTotal")
    def metric_bedrock_requests_total(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for total Bedrock requests.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for total Bedrock requests

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockRequestsTotal", [props]))

    @jsii.member(jsii_name="metricBedrockRetrySuccess")
    def metric_bedrock_retry_success(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for successful Bedrock request retries.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for successful Bedrock request retries

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockRetrySuccess", [props]))

    @jsii.member(jsii_name="metricBedrockThrottles")
    def metric_bedrock_throttles(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for Bedrock request throttles.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for Bedrock request throttles

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockThrottles", [props]))

    @jsii.member(jsii_name="metricBedrockTotalLatency")
    def metric_bedrock_total_latency(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for total Bedrock request latency.

        Measures total request processing time including retries.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for total Bedrock request latency in milliseconds

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockTotalLatency", [props]))

    @jsii.member(jsii_name="metricBedrockUnexpectedErrors")
    def metric_bedrock_unexpected_errors(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for Bedrock unexpected errors.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for Bedrock unexpected errors

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBedrockUnexpectedErrors", [props]))

    @jsii.member(jsii_name="metricCacheReadInputTokens")
    def metric_cache_read_input_tokens(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for cache read input tokens.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for cache read input tokens

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricCacheReadInputTokens", [props]))

    @jsii.member(jsii_name="metricCacheWriteInputTokens")
    def metric_cache_write_input_tokens(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for cache write input tokens.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for cache write input tokens

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricCacheWriteInputTokens", [props]))

    @jsii.member(jsii_name="metricInputDocumentPages")
    def metric_input_document_pages(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for input document pages processed.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for input document pages

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricInputDocumentPages", [props]))

    @jsii.member(jsii_name="metricInputDocuments")
    def metric_input_documents(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for input documents processed.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for input documents

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricInputDocuments", [props]))

    @jsii.member(jsii_name="metricInputTokens")
    def metric_input_tokens(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for input tokens consumed.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for input tokens

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricInputTokens", [props]))

    @jsii.member(jsii_name="metricOutputTokens")
    def metric_output_tokens(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for output tokens generated.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for output tokens

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricOutputTokens", [props]))

    @jsii.member(jsii_name="metricTotalTokens")
    def metric_total_tokens(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(experimental) Creates a CloudWatch metric for total tokens used.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true

        :return: CloudWatch Metric for total tokens

        :stability: experimental
        '''
        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricTotalTokens", [props]))

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> _cdklabs_genai_idp_bf65f2c1.IProcessingEnvironment:
        '''(experimental) The processing environment that provides shared infrastructure and services.

        Contains input/output buckets, tracking tables, API endpoints, and other
        resources needed for document processing operations.

        :stability: experimental
        '''
        return typing.cast(_cdklabs_genai_idp_bf65f2c1.IProcessingEnvironment, jsii.get(self, "environment"))

    @builtins.property
    @jsii.member(jsii_name="maxProcessingConcurrency")
    def max_processing_concurrency(self) -> jsii.Number:
        '''(experimental) The maximum number of documents that can be processed concurrently.

        Controls the throughput and resource utilization of the document processing system.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "maxProcessingConcurrency"))

    @builtins.property
    @jsii.member(jsii_name="stateMachine")
    def state_machine(self) -> _aws_cdk_aws_stepfunctions_ceddda9d.IStateMachine:
        '''(experimental) The Step Functions state machine that orchestrates the document processing workflow.

        Manages the sequence of processing steps and handles error conditions.
        This state machine is triggered for each document that needs processing
        and coordinates the entire extraction pipeline.

        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_stepfunctions_ceddda9d.IStateMachine, jsii.get(self, "stateMachine"))


@jsii.implements(IBedrockLlmProcessorConfiguration)
class BedrockLlmProcessorConfiguration(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/genai-idp-bedrock-llm-processor.BedrockLlmProcessorConfiguration",
):
    '''(experimental) Configuration management for Bedrock LLM document processing using custom extraction with Bedrock models.

    This construct creates and manages the configuration for Bedrock LLM document processing,
    including schema definitions, classification prompts, extraction prompts, and configuration
    values. It provides a centralized way to manage document classes, extraction schemas, and model parameters.

    :stability: experimental
    '''

    def __init__(self, definition: IBedrockLlmProcessorConfigurationDefinition) -> None:
        '''(experimental) Protected constructor to enforce factory method usage.

        :param definition: The configuration definition instance.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dab8e1e8d9318bb3c0e39153a3bb7d7a565a684b34c091f10821a6e897c56f2)
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
        jsii.create(self.__class__, self, [definition])

    @jsii.member(jsii_name="bankStatementSample")
    @builtins.classmethod
    def bank_statement_sample(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional[ClassificationMethod] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "BedrockLlmProcessorConfiguration":
        '''(experimental) Creates a configuration for bank statement processing.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition for bank statement processing

        :stability: experimental
        '''
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("BedrockLlmProcessorConfiguration", jsii.sinvoke(cls, "bankStatementSample", [options]))

    @jsii.member(jsii_name="checkboxedAttributesExtraction")
    @builtins.classmethod
    def checkboxed_attributes_extraction(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional[ClassificationMethod] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "BedrockLlmProcessorConfiguration":
        '''(experimental) Creates a configuration for checkbox extraction.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition for checkbox extraction

        :stability: experimental
        '''
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("BedrockLlmProcessorConfiguration", jsii.sinvoke(cls, "checkboxedAttributesExtraction", [options]))

    @jsii.member(jsii_name="criteriaValidation")
    @builtins.classmethod
    def criteria_validation(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional[ClassificationMethod] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "BedrockLlmProcessorConfiguration":
        '''(experimental) Creates a configuration for criteria validation.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition for criteria validation

        :stability: experimental
        '''
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("BedrockLlmProcessorConfiguration", jsii.sinvoke(cls, "criteriaValidation", [options]))

    @jsii.member(jsii_name="fewShotExampleWithMultimodalPageClassification")
    @builtins.classmethod
    def few_shot_example_with_multimodal_page_classification(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional[ClassificationMethod] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "BedrockLlmProcessorConfiguration":
        '''(experimental) Creates a configuration with few-shot examples and multimodal page classification.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition with few-shot examples

        :stability: experimental
        '''
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("BedrockLlmProcessorConfiguration", jsii.sinvoke(cls, "fewShotExampleWithMultimodalPageClassification", [options]))

    @jsii.member(jsii_name="fromFile")
    @builtins.classmethod
    def from_file(
        cls,
        file_path: builtins.str,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional[ClassificationMethod] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "BedrockLlmProcessorConfiguration":
        '''(experimental) Creates a configuration from a YAML file.

        :param file_path: Path to the YAML configuration file.
        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A new BedrockLlmProcessorConfiguration instance

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbc44bb7ca79530f2d7e8cc954c0a8d79fd49c57d9cbfad271e2e59c74cd840d)
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("BedrockLlmProcessorConfiguration", jsii.sinvoke(cls, "fromFile", [file_path, options]))

    @jsii.member(jsii_name="lendingPackageSample")
    @builtins.classmethod
    def lending_package_sample(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional[ClassificationMethod] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "BedrockLlmProcessorConfiguration":
        '''(experimental) Creates a configuration for lending package processing.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition for lending package processing

        :stability: experimental
        '''
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("BedrockLlmProcessorConfiguration", jsii.sinvoke(cls, "lendingPackageSample", [options]))

    @jsii.member(jsii_name="medicalRecordsSummarization")
    @builtins.classmethod
    def medical_records_summarization(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional[ClassificationMethod] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "BedrockLlmProcessorConfiguration":
        '''(experimental) Creates a configuration for medical records summarization.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition for medical records summarization

        :stability: experimental
        '''
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("BedrockLlmProcessorConfiguration", jsii.sinvoke(cls, "medicalRecordsSummarization", [options]))

    @jsii.member(jsii_name="rvlCdipPackageSample")
    @builtins.classmethod
    def rvl_cdip_package_sample(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional[ClassificationMethod] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "BedrockLlmProcessorConfiguration":
        '''(experimental) Creates a configuration for RVL-CDIP package processing.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition for RVL-CDIP package processing

        :stability: experimental
        '''
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("BedrockLlmProcessorConfiguration", jsii.sinvoke(cls, "rvlCdipPackageSample", [options]))

    @jsii.member(jsii_name="rvlCdipPackageSampleWithFewShotExamples")
    @builtins.classmethod
    def rvl_cdip_package_sample_with_few_shot_examples(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        classification_method: typing.Optional[ClassificationMethod] = None,
        classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "BedrockLlmProcessorConfiguration":
        '''(experimental) Creates a configuration for RVL-CDIP package processing with few-shot examples.

        :param assessment_model: (experimental) Optional model for the assessment stage.
        :param classification_method: (experimental) Optional classification method to use for document categorization. Determines how documents are analyzed and categorized before extraction.
        :param classification_model: (experimental) Optional model for the classification stage.
        :param evaluation_model: (experimental) Optional model for the evaluation stage.
        :param extraction_model: (experimental) Optional model for the extraction stage.
        :param ocr_model: (experimental) Optional model for the OCR stage when using Bedrock-based OCR. Only used when the OCR backend is set to 'bedrock' in the configuration.
        :param summarization_model: (experimental) Optional model for the summarization stage.

        :return: A configuration definition for RVL-CDIP package processing with few-shot examples

        :stability: experimental
        '''
        options = BedrockLlmProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            classification_method=classification_method,
            classification_model=classification_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            ocr_model=ocr_model,
            summarization_model=summarization_model,
        )

        return typing.cast("BedrockLlmProcessorConfiguration", jsii.sinvoke(cls, "rvlCdipPackageSampleWithFewShotExamples", [options]))

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        processor: IBedrockLlmProcessor,
    ) -> IBedrockLlmProcessorConfigurationDefinition:
        '''(experimental) Binds the configuration to a processor instance.

        This method applies the configuration to the processor.

        :param processor: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5daa463aa2c952add70ff581c486cafd5003375a4e969a673c59ba3ce391b042)
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        return typing.cast(IBedrockLlmProcessorConfigurationDefinition, jsii.invoke(self, "bind", [processor]))


@jsii.implements(IBedrockLlmProcessorConfigurationSchema)
class BedrockLlmProcessorConfigurationSchema(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/genai-idp-bedrock-llm-processor.BedrockLlmProcessorConfigurationSchema",
):
    '''(experimental) Schema definition for Bedrock LLM processor configuration. Provides JSON Schema validation rules for the configuration UI and API.

    This class defines the structure, validation rules, and UI presentation
    for the Bedrock LLM processor configuration, including document classes,
    attributes, classification settings, extraction parameters, evaluation
    criteria, and summarization options.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="bind")
    def bind(self, processor: IBedrockLlmProcessor) -> None:
        '''(experimental) Binds the configuration schema to a processor instance.

        Creates a custom resource that updates the schema in the configuration table.

        :param processor: The Bedrock LLM document processor to apply the schema to.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__208411703c79014af621a55ecbeb313be4d06631d9b3528b3f765c8d17062699)
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        return typing.cast(None, jsii.invoke(self, "bind", [processor]))


__all__ = [
    "BedrockLlmProcessor",
    "BedrockLlmProcessorConfiguration",
    "BedrockLlmProcessorConfigurationDefinition",
    "BedrockLlmProcessorConfigurationDefinitionOptions",
    "BedrockLlmProcessorConfigurationSchema",
    "BedrockLlmProcessorProps",
    "ClassificationMethod",
    "IBedrockLlmProcessor",
    "IBedrockLlmProcessorConfiguration",
    "IBedrockLlmProcessorConfigurationDefinition",
    "IBedrockLlmProcessorConfigurationSchema",
]

publication.publish()

def _typecheckingstub__2ecbbbd313e533065c033957cfea1b0345a89cc5b2e70264b066674315b00e3f(
    file_path: builtins.str,
    *,
    assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    classification_method: typing.Optional[ClassificationMethod] = None,
    classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38bf2cc189f96acbec7d1624475f43abb0ca3ce6b614a3fe0b0e552a9f7a7ea1(
    *,
    assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    classification_method: typing.Optional[ClassificationMethod] = None,
    classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8644cca7bc5dc380c9174019dfc3937fe8b5a9c175901bbbb59c07ee2a628f51(
    *,
    environment: _cdklabs_genai_idp_bf65f2c1.IProcessingEnvironment,
    max_processing_concurrency: typing.Optional[jsii.Number] = None,
    configuration: IBedrockLlmProcessorConfiguration,
    assessment_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    classification_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    classification_max_workers: typing.Optional[jsii.Number] = None,
    custom_prompt_generator: typing.Optional[_cdklabs_genai_idp_bf65f2c1.ICustomPromptGenerator] = None,
    enable_hitl: typing.Optional[builtins.bool] = None,
    evaluation_baseline_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    extraction_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    ocr_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    ocr_max_workers: typing.Optional[jsii.Number] = None,
    sage_maker_a2_i_review_portal_url: typing.Optional[builtins.str] = None,
    summarization_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86ddfd2ba0632bff2d76cad6b515de1975c87fc4896505961c68983c344d185d(
    processor: IBedrockLlmProcessor,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41fbec2ee612f5718839556204137eac96e55b9b0d53152cd03b222e0c66424b(
    processor: IBedrockLlmProcessor,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c33945804a9c92aa98911d16b029701afa4bd79586d4573531a09b7c9636b74(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration: IBedrockLlmProcessorConfiguration,
    assessment_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    classification_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    classification_max_workers: typing.Optional[jsii.Number] = None,
    custom_prompt_generator: typing.Optional[_cdklabs_genai_idp_bf65f2c1.ICustomPromptGenerator] = None,
    enable_hitl: typing.Optional[builtins.bool] = None,
    evaluation_baseline_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    extraction_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    ocr_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    ocr_max_workers: typing.Optional[jsii.Number] = None,
    sage_maker_a2_i_review_portal_url: typing.Optional[builtins.str] = None,
    summarization_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    environment: _cdklabs_genai_idp_bf65f2c1.IProcessingEnvironment,
    max_processing_concurrency: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dab8e1e8d9318bb3c0e39153a3bb7d7a565a684b34c091f10821a6e897c56f2(
    definition: IBedrockLlmProcessorConfigurationDefinition,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbc44bb7ca79530f2d7e8cc954c0a8d79fd49c57d9cbfad271e2e59c74cd840d(
    file_path: builtins.str,
    *,
    assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    classification_method: typing.Optional[ClassificationMethod] = None,
    classification_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ocr_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5daa463aa2c952add70ff581c486cafd5003375a4e969a673c59ba3ce391b042(
    processor: IBedrockLlmProcessor,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__208411703c79014af621a55ecbeb313be4d06631d9b3528b3f765c8d17062699(
    processor: IBedrockLlmProcessor,
) -> None:
    """Type checking stubs"""
    pass
