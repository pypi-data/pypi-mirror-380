r'''
# GenAI IDP SagemakerUdopProcessor

[![Compatible with GenAI IDP version: 0.3.16](https://img.shields.io/badge/Compatible%20with%20GenAI%20IDP-0.3.16-brightgreen)](https://github.com/aws-solutions-library-samples/accelerated-intelligent-document-processing-on-aws/releases/tag/v0.3.16)
![Stability: Experimental](https://img.shields.io/badge/Stability-Experimental-important.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

> This package is provided on an "as-is" basis, and may include bugs, errors, or other issues.
> All classes are under active development and subject to non-backward compatible changes or removal in any
> future version. These are not subject to the [Semantic Versioning](https://semver.org/) model.
> This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

---


## Overview

The GenAI IDP SagemakerUdopProcessor implements intelligent document processing using specialized document processing with SageMaker endpoints for classification, combined with foundation models for extraction. This package provides an advanced AWS CDK implementation for processing specialized document types that require custom classification models.

The SagemakerUdopProcessor is ideal for domain-specific documents, complex forms, or technical documents that require specialized classification models beyond what's possible with foundation models alone.

To master the full potential of this advanced pattern, we encourage you to browse our detailed [API documentation](./API.md). This resource provides in-depth information about all constructs, their properties, and how to configure them for your specialized document processing needs.

## Features

* **SageMaker-Based Classification**: Deploy specialized document classification models on SageMaker
* **Custom Model Support**: Integrate models like RVL-CDIP or UDOP for specialized document classification
* **Auto-Scaling Endpoints**: Automatically scale SageMaker endpoints based on processing demand
* **Foundation Model Extraction**: Use Amazon Bedrock foundation models for information extraction
* **Document Summarization**: Optional AI-powered document summarization capabilities
* **Evaluation Framework**: Built-in mechanisms for evaluating extraction quality
* **Comprehensive Metrics**: Detailed CloudWatch metrics for monitoring processing performance
* **GPU Acceleration**: Support for GPU-accelerated inference for improved performance

## Getting Started

### Installation

The package is available through npm for JavaScript/TypeScript projects and PyPI for Python projects.

#### JavaScript/TypeScript (npm)

```bash
# Using npm
npm install @cdklabs/genai-idp-sagemaker-udop-processor @cdklabs/genai-idp @aws-cdk/aws-sagemaker-alpha

# Using yarn
yarn add @cdklabs/genai-idp-sagemaker-udop-processor @cdklabs/genai-idp @aws-cdk/aws-sagemaker-alpha
```

#### Python (PyPI)

```bash
# Using pip
pip install cdklabs.genai-idp-sagemaker-udop-processor cdklabs.genai-idp aws-cdk.aws-sagemaker-alpha

# Using poetry
poetry add cdklabs.genai-idp-sagemaker-udop-processor cdklabs.genai-idp aws-cdk.aws-sagemaker-alpha
```

### Basic Usage

Here's how to integrate SagemakerUdopProcessor into your IDP solution:

```python
import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as kms from 'aws-cdk-lib/aws-kms';
import * as sagemaker from '@aws-cdk/aws-sagemaker-alpha';
import * as bedrock from '@cdklabs/generative-ai-cdk-constructs/lib/cdk-lib/bedrock';
import { ProcessingEnvironment } from '@cdklabs/genai-idp';
import { SagemakerUdopProcessor, BasicSagemakerClassifier } from '@cdklabs/genai-idp-sagemaker-udop-processor';

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

    // Create SageMaker classifier
    const classifier = new BasicSagemakerClassifier(this, 'Classifier', {
      outputBucket: environment.outputBucket,
      modelData: sagemaker.ModelData.fromAsset('./model'),
      instanceType: sagemaker.InstanceType.of(
        sagemaker.InstanceClass.G4DN,
        sagemaker.InstanceSize.XLARGE2
      ),
      minInstanceCount: 1,
      maxInstanceCount: 4,
    });

    // Create the processor
    const processor = new SagemakerUdopProcessor(this, 'Processor', {
      environment,
      configuration: /* Your SagemakerUdopProcessorConfiguration */,
      classifierEndpoint: classifier.endpoint,
      ocrMaxWorkers: 20,
    });
  }
}
```

## SageMaker Classifier

The SagemakerUdopProcessor accepts a SageMaker endpoint for document classification, providing flexibility in how you create and manage your classification models.

### Option 1: Using the BasicSagemakerClassifier Convenience Construct

For quick setup, use the provided `BasicSagemakerClassifier` construct:

```python
// Create SageMaker classifier using the basic convenience construct
const classifier = new BasicSagemakerClassifier(this, 'Classifier', {
  outputBucket: environment.outputBucket,
  modelData: sagemaker.ModelData.fromAsset('./model'),
  instanceType: sagemaker.InstanceType.ML_G4DN_XLARGE,
  minInstanceCount: 1,
  maxInstanceCount: 4,
});

const processor = new SagemakerUdopProcessor(this, 'Processor', {
  environment,
  classifierEndpoint: classifier.endpoint, // Pass the endpoint directly
  // ... other configuration
});
```

### Option 2: Using Your Own SageMaker Endpoint

For maximum flexibility, create your own SageMaker endpoint and pass it directly:

```python
// Create your own SageMaker endpoint
const model = new sagemaker.Model(this, 'MyCustomModel', {
  containers: [{
    image: sagemaker.ContainerImage.fromDlc('pytorch-inference', '2.1.0-gpu-py310'),
    modelData: sagemaker.ModelData.fromAsset('./my-custom-model'),
    // ... custom configuration
  }],
});

const endpointConfig = new sagemaker.EndpointConfig(this, 'MyEndpointConfig', {
  instanceProductionVariants: [{
    variantName: 'AllTraffic',
    initialInstanceCount: 1,
    instanceType: sagemaker.InstanceType.ML_G4DN_XLARGE,
    model: model,
    initialVariantWeight: 1.0,
  }],
});

const endpoint = new sagemaker.Endpoint(this, 'MyEndpoint', {
  endpointConfig: endpointConfig,
});

const processor = new SagemakerUdopProcessor(this, 'Processor', {
  environment,
  classifierEndpoint: endpoint, // Pass your custom endpoint directly
  // ... other configuration
});
```

### Option 3: Using an Existing Endpoint

You can also reference an existing SageMaker endpoint:

```python
// Reference an existing endpoint
const existingEndpoint = sagemaker.Endpoint.fromEndpointName(
  this,
  'ExistingEndpoint',
  'my-existing-endpoint-name'
);

const processor = new SagemakerUdopProcessor(this, 'Processor', {
  environment,
  classifierEndpoint: existingEndpoint,
  // ... other configuration
});
```

### Key Benefits of This Approach

* **Flexibility**: Use any SageMaker endpoint creation method
* **Reusability**: Share endpoints across multiple processors
* **Cost Optimization**: Better control over endpoint lifecycle and scaling
* **Custom Models**: Deploy any classification model (RVL-CDIP, UDOP, custom models)
* **GPU Acceleration**: Use GPU instances for improved inference performance
* **Auto-Scaling**: Configure scaling based on your specific needs

## Configuration

SagemakerUdopProcessor supports extensive configuration options:

* **SageMaker Endpoint**: Provide any SageMaker endpoint for document classification (using convenience construct, custom endpoint, or existing endpoint)
* **Invokable Models**: Specify which models to use for extraction, evaluation, and summarization
* **Guardrails**: Apply content guardrails to model interactions
* **Concurrency**: Control processing throughput and resource utilization
* **VPC Configuration**: Deploy in a VPC for enhanced security and connectivity

For detailed configuration options, refer to the TypeScript type definitions and JSDoc comments in the source code.

## Contributing

We welcome contributions to the GenAI IDP SagemakerUdopProcessor! Please follow these steps to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code adheres to our coding standards and includes appropriate tests.

## Related Projects

* [@cdklabs/genai-idp](../idp): Core IDP constructs and infrastructure
* [@cdklabs/genai-idp-bda-processor](../idp-bda-processor): BdaProcessor implementation using Amazon Bedrock Data Automation
* [@cdklabs/genai-idp-bedrock-llm-processor](../idp-bedrock-llm-processor): BedrockLlmProcessor implementation for custom extraction using Amazon Bedrock models

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
import aws_cdk.aws_kms as _aws_cdk_aws_kms_ceddda9d
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_ceddda9d
import aws_cdk.aws_sagemaker_alpha as _aws_cdk_aws_sagemaker_alpha_90d55fd8
import aws_cdk.aws_stepfunctions as _aws_cdk_aws_stepfunctions_ceddda9d
import cdklabs.genai_idp as _cdklabs_genai_idp_bf65f2c1
import cdklabs.generative_ai_cdk_constructs.bedrock as _cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec
import constructs as _constructs_77d1e7e8


class BasicSagemakerClassifier(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/genai-idp-sagemaker-udop-processor.BasicSagemakerClassifier",
):
    '''(experimental) A basic SageMaker-based document classifier for the Pattern 3 document processor.

    This construct provides a simple way to deploy a SageMaker endpoint with a document
    classification model that can categorize documents based on their content and structure.
    It supports models like RVL-CDIP or UDOP for specialized document classification tasks.

    The basic classifier includes standard auto-scaling capabilities and sensible defaults
    for common use cases. For more advanced configurations, consider creating your own
    SageMaker endpoint and passing it directly to the SagemakerUdopProcessor.

    :stability: experimental

    Example::

        const classifier = new BasicSagemakerClassifier(this, 'Classifier', {
          outputBucket: bucket,
          modelData: ModelData.fromAsset('./model'),
          instanceType: InstanceType.ML_G4DN_XLARGE,
        });
        
        const processor = new SagemakerUdopProcessor(this, 'Processor', {
          environment,
          classifierEndpoint: classifier.endpoint,
          // ... other configuration
        });
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_type: _aws_cdk_aws_sagemaker_alpha_90d55fd8.InstanceType,
        model_data: _aws_cdk_aws_sagemaker_alpha_90d55fd8.ModelData,
        output_bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
        key: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
        max_instance_count: typing.Optional[jsii.Number] = None,
        min_instance_count: typing.Optional[jsii.Number] = None,
        scale_in_cooldown: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        scale_out_cooldown: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        target_invocations_per_instance_per_minute: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param instance_type: (experimental) The instance type to use for the SageMaker endpoint. Determines the computational resources available for document classification. For deep learning models, GPU instances are typically recommended.
        :param model_data: (experimental) The model data for the SageMaker endpoint. Contains the trained model artifacts that will be deployed to the endpoint. This can be a pre-trained document classification model like RVL-CDIP or UDOP.
        :param output_bucket: (experimental) The S3 bucket where classification outputs will be stored. Contains intermediate results from the document classification process.
        :param key: (experimental) Optional KMS key for encrypting classifier resources. When provided, ensures data security for the SageMaker endpoint and associated resources.
        :param max_instance_count: (experimental) The maximum number of instances for the SageMaker endpoint. Controls the maximum capacity for document classification during high load. Default: 4
        :param min_instance_count: (experimental) The minimum number of instances for the SageMaker endpoint. Controls the baseline capacity for document classification. Default: 1
        :param scale_in_cooldown: (experimental) The cooldown period after scaling in before another scale-in action can occur. Prevents rapid fluctuations in endpoint capacity. Default: cdk.Duration.minutes(5)
        :param scale_out_cooldown: (experimental) The cooldown period after scaling out before another scale-out action can occur. Prevents rapid fluctuations in endpoint capacity. Default: cdk.Duration.minutes(1)
        :param target_invocations_per_instance_per_minute: (experimental) The target number of invocations per instance per minute. Used to determine when to scale the endpoint in or out. Default: 20

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33bd9b9c171b640e2b3d84d0c978fb23584ac94d5973bcce4a919879ab1f7783)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BasicSagemakerClassifierProps(
            instance_type=instance_type,
            model_data=model_data,
            output_bucket=output_bucket,
            key=key,
            max_instance_count=max_instance_count,
            min_instance_count=min_instance_count,
            scale_in_cooldown=scale_in_cooldown,
            scale_out_cooldown=scale_out_cooldown,
            target_invocations_per_instance_per_minute=target_invocations_per_instance_per_minute,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> _aws_cdk_aws_sagemaker_alpha_90d55fd8.IEndpoint:
        '''(experimental) The SageMaker endpoint that hosts the document classification model.

        This endpoint is invoked during document processing to determine
        document types and categories.

        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_sagemaker_alpha_90d55fd8.IEndpoint, jsii.get(self, "endpoint"))


@jsii.data_type(
    jsii_type="@cdklabs/genai-idp-sagemaker-udop-processor.BasicSagemakerClassifierProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "model_data": "modelData",
        "output_bucket": "outputBucket",
        "key": "key",
        "max_instance_count": "maxInstanceCount",
        "min_instance_count": "minInstanceCount",
        "scale_in_cooldown": "scaleInCooldown",
        "scale_out_cooldown": "scaleOutCooldown",
        "target_invocations_per_instance_per_minute": "targetInvocationsPerInstancePerMinute",
    },
)
class BasicSagemakerClassifierProps:
    def __init__(
        self,
        *,
        instance_type: _aws_cdk_aws_sagemaker_alpha_90d55fd8.InstanceType,
        model_data: _aws_cdk_aws_sagemaker_alpha_90d55fd8.ModelData,
        output_bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
        key: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
        max_instance_count: typing.Optional[jsii.Number] = None,
        min_instance_count: typing.Optional[jsii.Number] = None,
        scale_in_cooldown: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        scale_out_cooldown: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        target_invocations_per_instance_per_minute: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Configuration properties for the basic SageMaker-based document classifier.

        This classifier uses a SageMaker endpoint to categorize documents based on
        their content and structure, enabling targeted extraction strategies.

        :param instance_type: (experimental) The instance type to use for the SageMaker endpoint. Determines the computational resources available for document classification. For deep learning models, GPU instances are typically recommended.
        :param model_data: (experimental) The model data for the SageMaker endpoint. Contains the trained model artifacts that will be deployed to the endpoint. This can be a pre-trained document classification model like RVL-CDIP or UDOP.
        :param output_bucket: (experimental) The S3 bucket where classification outputs will be stored. Contains intermediate results from the document classification process.
        :param key: (experimental) Optional KMS key for encrypting classifier resources. When provided, ensures data security for the SageMaker endpoint and associated resources.
        :param max_instance_count: (experimental) The maximum number of instances for the SageMaker endpoint. Controls the maximum capacity for document classification during high load. Default: 4
        :param min_instance_count: (experimental) The minimum number of instances for the SageMaker endpoint. Controls the baseline capacity for document classification. Default: 1
        :param scale_in_cooldown: (experimental) The cooldown period after scaling in before another scale-in action can occur. Prevents rapid fluctuations in endpoint capacity. Default: cdk.Duration.minutes(5)
        :param scale_out_cooldown: (experimental) The cooldown period after scaling out before another scale-out action can occur. Prevents rapid fluctuations in endpoint capacity. Default: cdk.Duration.minutes(1)
        :param target_invocations_per_instance_per_minute: (experimental) The target number of invocations per instance per minute. Used to determine when to scale the endpoint in or out. Default: 20

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44a3f7949dd90007393520eaa0a1a7508158ec20cb9323cd16604f7c376d365f)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument model_data", value=model_data, expected_type=type_hints["model_data"])
            check_type(argname="argument output_bucket", value=output_bucket, expected_type=type_hints["output_bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument max_instance_count", value=max_instance_count, expected_type=type_hints["max_instance_count"])
            check_type(argname="argument min_instance_count", value=min_instance_count, expected_type=type_hints["min_instance_count"])
            check_type(argname="argument scale_in_cooldown", value=scale_in_cooldown, expected_type=type_hints["scale_in_cooldown"])
            check_type(argname="argument scale_out_cooldown", value=scale_out_cooldown, expected_type=type_hints["scale_out_cooldown"])
            check_type(argname="argument target_invocations_per_instance_per_minute", value=target_invocations_per_instance_per_minute, expected_type=type_hints["target_invocations_per_instance_per_minute"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_type": instance_type,
            "model_data": model_data,
            "output_bucket": output_bucket,
        }
        if key is not None:
            self._values["key"] = key
        if max_instance_count is not None:
            self._values["max_instance_count"] = max_instance_count
        if min_instance_count is not None:
            self._values["min_instance_count"] = min_instance_count
        if scale_in_cooldown is not None:
            self._values["scale_in_cooldown"] = scale_in_cooldown
        if scale_out_cooldown is not None:
            self._values["scale_out_cooldown"] = scale_out_cooldown
        if target_invocations_per_instance_per_minute is not None:
            self._values["target_invocations_per_instance_per_minute"] = target_invocations_per_instance_per_minute

    @builtins.property
    def instance_type(self) -> _aws_cdk_aws_sagemaker_alpha_90d55fd8.InstanceType:
        '''(experimental) The instance type to use for the SageMaker endpoint.

        Determines the computational resources available for document classification.
        For deep learning models, GPU instances are typically recommended.

        :stability: experimental
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(_aws_cdk_aws_sagemaker_alpha_90d55fd8.InstanceType, result)

    @builtins.property
    def model_data(self) -> _aws_cdk_aws_sagemaker_alpha_90d55fd8.ModelData:
        '''(experimental) The model data for the SageMaker endpoint.

        Contains the trained model artifacts that will be deployed to the endpoint.
        This can be a pre-trained document classification model like RVL-CDIP or UDOP.

        :stability: experimental
        '''
        result = self._values.get("model_data")
        assert result is not None, "Required property 'model_data' is missing"
        return typing.cast(_aws_cdk_aws_sagemaker_alpha_90d55fd8.ModelData, result)

    @builtins.property
    def output_bucket(self) -> _aws_cdk_aws_s3_ceddda9d.IBucket:
        '''(experimental) The S3 bucket where classification outputs will be stored.

        Contains intermediate results from the document classification process.

        :stability: experimental
        '''
        result = self._values.get("output_bucket")
        assert result is not None, "Required property 'output_bucket' is missing"
        return typing.cast(_aws_cdk_aws_s3_ceddda9d.IBucket, result)

    @builtins.property
    def key(self) -> typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey]:
        '''(experimental) Optional KMS key for encrypting classifier resources.

        When provided, ensures data security for the SageMaker endpoint
        and associated resources.

        :stability: experimental
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey], result)

    @builtins.property
    def max_instance_count(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The maximum number of instances for the SageMaker endpoint.

        Controls the maximum capacity for document classification during high load.

        :default: 4

        :stability: experimental
        :min: 1
        '''
        result = self._values.get("max_instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_instance_count(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The minimum number of instances for the SageMaker endpoint.

        Controls the baseline capacity for document classification.

        :default: 1

        :stability: experimental
        :min: 1
        '''
        result = self._values.get("min_instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scale_in_cooldown(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''(experimental) The cooldown period after scaling in before another scale-in action can occur.

        Prevents rapid fluctuations in endpoint capacity.

        :default: cdk.Duration.minutes(5)

        :stability: experimental
        '''
        result = self._values.get("scale_in_cooldown")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    @builtins.property
    def scale_out_cooldown(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''(experimental) The cooldown period after scaling out before another scale-out action can occur.

        Prevents rapid fluctuations in endpoint capacity.

        :default: cdk.Duration.minutes(1)

        :stability: experimental
        '''
        result = self._values.get("scale_out_cooldown")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    @builtins.property
    def target_invocations_per_instance_per_minute(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''(experimental) The target number of invocations per instance per minute.

        Used to determine when to scale the endpoint in or out.

        :default: 20

        :stability: experimental
        :min: 1
        '''
        result = self._values.get("target_invocations_per_instance_per_minute")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BasicSagemakerClassifierProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="@cdklabs/genai-idp-sagemaker-udop-processor.ISagemakerUdopProcessor"
)
class ISagemakerUdopProcessor(
    _cdklabs_genai_idp_bf65f2c1.IDocumentProcessor,
    typing_extensions.Protocol,
):
    '''(experimental) Interface for SageMaker UDOP document processor implementation.

    SageMaker UDOP Processor uses specialized document processing with SageMaker endpoints
    for document classification, combined with foundation models for extraction.
    This processor is ideal for specialized document types that require custom
    classification models like RVL-CDIP or UDOP for accurate document categorization
    before extraction.

    Use SageMaker UDOP Processor when:

    - Processing highly specialized or complex document types
    - You need custom classification models beyond what foundation models can provide
    - You have domain-specific document types requiring specialized handling
    - You want to leverage fine-tuned models for specific document domains

    :stability: experimental
    '''

    pass


class _ISagemakerUdopProcessorProxy(
    jsii.proxy_for(_cdklabs_genai_idp_bf65f2c1.IDocumentProcessor), # type: ignore[misc]
):
    '''(experimental) Interface for SageMaker UDOP document processor implementation.

    SageMaker UDOP Processor uses specialized document processing with SageMaker endpoints
    for document classification, combined with foundation models for extraction.
    This processor is ideal for specialized document types that require custom
    classification models like RVL-CDIP or UDOP for accurate document categorization
    before extraction.

    Use SageMaker UDOP Processor when:

    - Processing highly specialized or complex document types
    - You need custom classification models beyond what foundation models can provide
    - You have domain-specific document types requiring specialized handling
    - You want to leverage fine-tuned models for specific document domains

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/genai-idp-sagemaker-udop-processor.ISagemakerUdopProcessor"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISagemakerUdopProcessor).__jsii_proxy_class__ = lambda : _ISagemakerUdopProcessorProxy


@jsii.interface(
    jsii_type="@cdklabs/genai-idp-sagemaker-udop-processor.ISagemakerUdopProcessorConfiguration"
)
class ISagemakerUdopProcessorConfiguration(typing_extensions.Protocol):
    '''(experimental) Interface for SageMaker UDOP document processor configuration.

    Provides configuration management for specialized document processing with SageMaker.

    :stability: experimental
    '''

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        processor: ISagemakerUdopProcessor,
    ) -> "ISagemakerUdopProcessorConfigurationDefinition":
        '''(experimental) Binds the configuration to a processor instance.

        This method applies the configuration to the processor.

        :param processor: The SageMaker UDOP document processor to apply to.

        :stability: experimental
        '''
        ...


class _ISagemakerUdopProcessorConfigurationProxy:
    '''(experimental) Interface for SageMaker UDOP document processor configuration.

    Provides configuration management for specialized document processing with SageMaker.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/genai-idp-sagemaker-udop-processor.ISagemakerUdopProcessorConfiguration"

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        processor: ISagemakerUdopProcessor,
    ) -> "ISagemakerUdopProcessorConfigurationDefinition":
        '''(experimental) Binds the configuration to a processor instance.

        This method applies the configuration to the processor.

        :param processor: The SageMaker UDOP document processor to apply to.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c182eb97dfcf80a64d49011e7a60d62f22f9c506a1ac0b8aa92877743280c92e)
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        return typing.cast("ISagemakerUdopProcessorConfigurationDefinition", jsii.invoke(self, "bind", [processor]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISagemakerUdopProcessorConfiguration).__jsii_proxy_class__ = lambda : _ISagemakerUdopProcessorConfigurationProxy


@jsii.interface(
    jsii_type="@cdklabs/genai-idp-sagemaker-udop-processor.ISagemakerUdopProcessorConfigurationDefinition"
)
class ISagemakerUdopProcessorConfigurationDefinition(
    _cdklabs_genai_idp_bf65f2c1.IConfigurationDefinition,
    typing_extensions.Protocol,
):
    '''(experimental) Interface for SageMaker UDOP processor configuration definition.

    Defines the structure and capabilities of configuration for SageMaker UDOP processing.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="extractionModel")
    def extraction_model(
        self,
    ) -> _cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable:
        '''(experimental) The invokable model used for information extraction.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.
        Extracts structured data from documents based on defined schemas,
        transforming unstructured content into structured information.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="assessmentModel")
    def assessment_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional invokable model used for document assessment.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.

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

        :stability: experimental
        '''
        ...


class _ISagemakerUdopProcessorConfigurationDefinitionProxy(
    jsii.proxy_for(_cdklabs_genai_idp_bf65f2c1.IConfigurationDefinition), # type: ignore[misc]
):
    '''(experimental) Interface for SageMaker UDOP processor configuration definition.

    Defines the structure and capabilities of configuration for SageMaker UDOP processing.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/genai-idp-sagemaker-udop-processor.ISagemakerUdopProcessorConfigurationDefinition"

    @builtins.property
    @jsii.member(jsii_name="extractionModel")
    def extraction_model(
        self,
    ) -> _cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable:
        '''(experimental) The invokable model used for information extraction.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.
        Extracts structured data from documents based on defined schemas,
        transforming unstructured content into structured information.

        :stability: experimental
        '''
        return typing.cast(_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable, jsii.get(self, "extractionModel"))

    @builtins.property
    @jsii.member(jsii_name="assessmentModel")
    def assessment_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional invokable model used for document assessment.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.

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

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], jsii.get(self, "evaluationModel"))

    @builtins.property
    @jsii.member(jsii_name="summarizationModel")
    def summarization_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional invokable model used for document summarization.

        Can be a Bedrock foundation model, Bedrock inference profile, or custom model.
        When provided, enables automatic generation of document summaries
        that capture key information from processed documents.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], jsii.get(self, "summarizationModel"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISagemakerUdopProcessorConfigurationDefinition).__jsii_proxy_class__ = lambda : _ISagemakerUdopProcessorConfigurationDefinitionProxy


@jsii.interface(
    jsii_type="@cdklabs/genai-idp-sagemaker-udop-processor.ISagemakerUdopProcessorConfigurationSchema"
)
class ISagemakerUdopProcessorConfigurationSchema(typing_extensions.Protocol):
    '''(experimental) Interface for SageMaker UDOP configuration schema.

    Defines the structure and validation rules for SageMaker UDOP processor configuration.

    :stability: experimental
    '''

    @jsii.member(jsii_name="bind")
    def bind(self, processor: "SagemakerUdopProcessor") -> None:
        '''(experimental) Binds the configuration schema to a processor instance.

        This method applies the schema definition to the processor's configuration table.

        :param processor: The SageMaker UDOP document processor to apply the schema to.

        :stability: experimental
        '''
        ...


class _ISagemakerUdopProcessorConfigurationSchemaProxy:
    '''(experimental) Interface for SageMaker UDOP configuration schema.

    Defines the structure and validation rules for SageMaker UDOP processor configuration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/genai-idp-sagemaker-udop-processor.ISagemakerUdopProcessorConfigurationSchema"

    @jsii.member(jsii_name="bind")
    def bind(self, processor: "SagemakerUdopProcessor") -> None:
        '''(experimental) Binds the configuration schema to a processor instance.

        This method applies the schema definition to the processor's configuration table.

        :param processor: The SageMaker UDOP document processor to apply the schema to.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8c38817d25f32866ebc9acbcd9112c5de9e977e12d16f648770f7b82c0954d9)
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        return typing.cast(None, jsii.invoke(self, "bind", [processor]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISagemakerUdopProcessorConfigurationSchema).__jsii_proxy_class__ = lambda : _ISagemakerUdopProcessorConfigurationSchemaProxy


@jsii.implements(ISagemakerUdopProcessor)
class SagemakerUdopProcessor(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/genai-idp-sagemaker-udop-processor.SagemakerUdopProcessor",
):
    '''(experimental) SageMaker UDOP document processor implementation that uses specialized models for document processing.

    This processor implements an intelligent document processing workflow that uses specialized
    models like UDOP (Unified Document Processing) or RVL-CDIP deployed on SageMaker for document classification,
    followed by foundation models for information extraction.

    SageMaker UDOP Processor is ideal for specialized document types that require custom classification models
    beyond what's possible with foundation models alone, such as complex forms, technical documents,
    or domain-specific content. It provides the highest level of customization for document
    classification while maintaining the flexibility of foundation models for extraction.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        classifier_endpoint: _aws_cdk_aws_sagemaker_alpha_90d55fd8.IEndpoint,
        configuration: ISagemakerUdopProcessorConfiguration,
        assessment_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        classification_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        custom_prompt_generator: typing.Optional[_cdklabs_genai_idp_bf65f2c1.ICustomPromptGenerator] = None,
        evaluation_baseline_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        evaluation_enabled: typing.Optional[builtins.bool] = None,
        extraction_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        ocr_max_workers: typing.Optional[jsii.Number] = None,
        summarization_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        environment: _cdklabs_genai_idp_bf65f2c1.IProcessingEnvironment,
        max_processing_concurrency: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param classifier_endpoint: (experimental) The SageMaker endpoint used for document classification. Determines document types based on content and structure analysis using specialized models like RVL-CDIP or UDOP deployed on SageMaker. This is a key component of Pattern 3, enabling specialized document classification beyond what's possible with foundation models alone. Users can create their own SageMaker endpoint using any method (CDK constructs, existing endpoints, etc.) and pass it directly to the processor.
        :param configuration: (experimental) Configuration for the SageMaker UDOP document processor. Provides customization options for the processing workflow, including schema definitions, prompts, and evaluation settings.
        :param assessment_guardrail: (experimental) Optional Bedrock guardrail to apply to assessment model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param classification_guardrail: (experimental) Optional Bedrock guardrail to apply to classification model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param custom_prompt_generator: (experimental) Optional custom prompt generator for injecting business logic into extraction processing. When provided, this Lambda function will be called to customize prompts based on document content, business rules, or external system integrations. Default: - No custom prompt generator is used
        :param evaluation_baseline_bucket: (experimental) Optional S3 bucket containing baseline documents for evaluation. Used as ground truth when evaluating extraction accuracy by comparing extraction results against known correct values. Required when evaluationEnabled is true. Default: - No evaluation baseline bucket is configured
        :param evaluation_enabled: (experimental) Controls whether extraction results are evaluated for accuracy. When enabled, compares extraction results against expected values to measure extraction quality and identify improvement areas. Default: false
        :param extraction_guardrail: (experimental) Optional Bedrock guardrail to apply to extraction model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param ocr_max_workers: (experimental) The maximum number of concurrent workers for OCR processing. Controls parallelism during the text extraction phase to optimize throughput while managing resource utilization. Default: 20
        :param summarization_guardrail: (experimental) Optional Bedrock guardrail to apply to summarization model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param environment: (experimental) The processing environment that provides shared infrastructure and services. Contains input/output buckets, tracking tables, API endpoints, and other resources needed for document processing operations.
        :param max_processing_concurrency: (experimental) The maximum number of documents that can be processed concurrently. Controls the throughput and resource utilization of the document processing system. Default: 100 concurrent workflows

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2a519fc1300ad0f2c0724a7dbbb44fb59a0de9afbea0a2055985669ad8707da)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SagemakerUdopProcessorProps(
            classifier_endpoint=classifier_endpoint,
            configuration=configuration,
            assessment_guardrail=assessment_guardrail,
            classification_guardrail=classification_guardrail,
            custom_prompt_generator=custom_prompt_generator,
            evaluation_baseline_bucket=evaluation_baseline_bucket,
            evaluation_enabled=evaluation_enabled,
            extraction_guardrail=extraction_guardrail,
            ocr_max_workers=ocr_max_workers,
            summarization_guardrail=summarization_guardrail,
            environment=environment,
            max_processing_concurrency=max_processing_concurrency,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="metricClassificationRequestsTotal")
    def metric_classification_requests_total(
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
        '''(experimental) Creates a CloudWatch metric for total classification requests.

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

        :return: CloudWatch Metric for total classification requests

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricClassificationRequestsTotal", [props]))

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


@jsii.implements(ISagemakerUdopProcessorConfiguration)
class SagemakerUdopProcessorConfiguration(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/genai-idp-sagemaker-udop-processor.SagemakerUdopProcessorConfiguration",
):
    '''(experimental) Configuration management for SageMaker UDOP document processing using SageMaker for classification.

    This construct creates and manages the configuration for SageMaker UDOP document processing,
    including schema definitions, extraction prompts, and configuration values.
    It provides a centralized way to manage document classes, extraction schemas, and
    model parameters for specialized document processing with SageMaker.

    :stability: experimental
    '''

    def __init__(
        self,
        definition: ISagemakerUdopProcessorConfigurationDefinition,
    ) -> None:
        '''(experimental) Protected constructor to enforce factory method usage.

        :param definition: The configuration definition instance.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f2160cf87128b97ab0eb8048ed483bcf8c90ce5678f108d9dd093ad4d2ba903)
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
        jsii.create(self.__class__, self, [definition])

    @jsii.member(jsii_name="fromFile")
    @builtins.classmethod
    def from_file(
        cls,
        file_path: builtins.str,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "SagemakerUdopProcessorConfiguration":
        '''(experimental) Creates a configuration from a YAML file.

        :param file_path: Path to the YAML configuration file.
        :param assessment_model: (experimental) Optional invokable model used for evaluating assessment results. Can be a Bedrock foundation model, Bedrock inference profile, or custom model. Used to assess the quality and accuracy of extracted information by comparing assessment results against expected values. Default: - as defined in the definition file
        :param evaluation_model: (experimental) Optional configuration for the evaluation stage. Defines the model and parameters used for evaluating extraction accuracy.
        :param extraction_model: (experimental) Optional configuration for the extraction stage. Defines the model and parameters used for information extraction.
        :param summarization_model: (experimental) Optional configuration for the summarization stage. Defines the model and parameters used for generating document summaries.

        :return: A new SagemakerUdopProcessorConfiguration instance

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03ca4a1f711553731e5b03ec631852aca2fdeab0c10ac6f85efff83bff549029)
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
        options = SagemakerUdopProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            summarization_model=summarization_model,
        )

        return typing.cast("SagemakerUdopProcessorConfiguration", jsii.sinvoke(cls, "fromFile", [file_path, options]))

    @jsii.member(jsii_name="rvlCdipPackageSample")
    @builtins.classmethod
    def rvl_cdip_package_sample(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "SagemakerUdopProcessorConfiguration":
        '''(experimental) Creates a default configuration with standard settings.

        :param assessment_model: (experimental) Optional invokable model used for evaluating assessment results. Can be a Bedrock foundation model, Bedrock inference profile, or custom model. Used to assess the quality and accuracy of extracted information by comparing assessment results against expected values. Default: - as defined in the definition file
        :param evaluation_model: (experimental) Optional configuration for the evaluation stage. Defines the model and parameters used for evaluating extraction accuracy.
        :param extraction_model: (experimental) Optional configuration for the extraction stage. Defines the model and parameters used for information extraction.
        :param summarization_model: (experimental) Optional configuration for the summarization stage. Defines the model and parameters used for generating document summaries.

        :return: A configuration definition with default settings

        :stability: experimental
        '''
        options = SagemakerUdopProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            summarization_model=summarization_model,
        )

        return typing.cast("SagemakerUdopProcessorConfiguration", jsii.sinvoke(cls, "rvlCdipPackageSample", [options]))

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        processor: ISagemakerUdopProcessor,
    ) -> ISagemakerUdopProcessorConfigurationDefinition:
        '''(experimental) Binds the configuration to a processor instance.

        This method applies the configuration to the processor.

        :param processor: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44243da7299b0e182e99e2c69ec563a2ea4df5eb908b00ddc06552b492c37486)
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        return typing.cast(ISagemakerUdopProcessorConfigurationDefinition, jsii.invoke(self, "bind", [processor]))


class SagemakerUdopProcessorConfigurationDefinition(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/genai-idp-sagemaker-udop-processor.SagemakerUdopProcessorConfigurationDefinition",
):
    '''(experimental) Configuration definition for SageMaker UDOP document processing.

    Provides methods to create and customize configuration for SageMaker UDOP processing.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromFile")
    @builtins.classmethod
    def from_file(
        cls,
        file_path: builtins.str,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> ISagemakerUdopProcessorConfigurationDefinition:
        '''(experimental) Creates a configuration definition from a YAML file.

        Allows users to provide custom configuration files for document processing.

        :param file_path: Path to the YAML configuration file.
        :param assessment_model: (experimental) Optional invokable model used for evaluating assessment results. Can be a Bedrock foundation model, Bedrock inference profile, or custom model. Used to assess the quality and accuracy of extracted information by comparing assessment results against expected values. Default: - as defined in the definition file
        :param evaluation_model: (experimental) Optional configuration for the evaluation stage. Defines the model and parameters used for evaluating extraction accuracy.
        :param extraction_model: (experimental) Optional configuration for the extraction stage. Defines the model and parameters used for information extraction.
        :param summarization_model: (experimental) Optional configuration for the summarization stage. Defines the model and parameters used for generating document summaries.

        :return: A configuration definition loaded from the file

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a886bbbdf17171948c394ccc770b293d33aaf83cb94b6355160e70200154db48)
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
        options = SagemakerUdopProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            summarization_model=summarization_model,
        )

        return typing.cast(ISagemakerUdopProcessorConfigurationDefinition, jsii.sinvoke(cls, "fromFile", [file_path, options]))

    @jsii.member(jsii_name="rvlCdipPackageSample")
    @builtins.classmethod
    def rvl_cdip_package_sample(
        cls,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> ISagemakerUdopProcessorConfigurationDefinition:
        '''(experimental) Creates a default configuration definition for SageMaker UDOP processing.

        This configuration includes basic settings for extraction, evaluation, and summarization
        when using SageMaker for document classification.

        :param assessment_model: (experimental) Optional invokable model used for evaluating assessment results. Can be a Bedrock foundation model, Bedrock inference profile, or custom model. Used to assess the quality and accuracy of extracted information by comparing assessment results against expected values. Default: - as defined in the definition file
        :param evaluation_model: (experimental) Optional configuration for the evaluation stage. Defines the model and parameters used for evaluating extraction accuracy.
        :param extraction_model: (experimental) Optional configuration for the extraction stage. Defines the model and parameters used for information extraction.
        :param summarization_model: (experimental) Optional configuration for the summarization stage. Defines the model and parameters used for generating document summaries.

        :return: A configuration definition with default settings

        :stability: experimental
        '''
        options = SagemakerUdopProcessorConfigurationDefinitionOptions(
            assessment_model=assessment_model,
            evaluation_model=evaluation_model,
            extraction_model=extraction_model,
            summarization_model=summarization_model,
        )

        return typing.cast(ISagemakerUdopProcessorConfigurationDefinition, jsii.sinvoke(cls, "rvlCdipPackageSample", [options]))


@jsii.data_type(
    jsii_type="@cdklabs/genai-idp-sagemaker-udop-processor.SagemakerUdopProcessorConfigurationDefinitionOptions",
    jsii_struct_bases=[],
    name_mapping={
        "assessment_model": "assessmentModel",
        "evaluation_model": "evaluationModel",
        "extraction_model": "extractionModel",
        "summarization_model": "summarizationModel",
    },
)
class SagemakerUdopProcessorConfigurationDefinitionOptions:
    def __init__(
        self,
        *,
        assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> None:
        '''(experimental) Options for configuring the SageMaker UDOP processor configuration definition.

        Allows customization of extraction, evaluation, and summarization stages.

        :param assessment_model: (experimental) Optional invokable model used for evaluating assessment results. Can be a Bedrock foundation model, Bedrock inference profile, or custom model. Used to assess the quality and accuracy of extracted information by comparing assessment results against expected values. Default: - as defined in the definition file
        :param evaluation_model: (experimental) Optional configuration for the evaluation stage. Defines the model and parameters used for evaluating extraction accuracy.
        :param extraction_model: (experimental) Optional configuration for the extraction stage. Defines the model and parameters used for information extraction.
        :param summarization_model: (experimental) Optional configuration for the summarization stage. Defines the model and parameters used for generating document summaries.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__335d46eca9893646e0aead0bd52826b00f744494fca10cecc3efc3bfdfeb3045)
            check_type(argname="argument assessment_model", value=assessment_model, expected_type=type_hints["assessment_model"])
            check_type(argname="argument evaluation_model", value=evaluation_model, expected_type=type_hints["evaluation_model"])
            check_type(argname="argument extraction_model", value=extraction_model, expected_type=type_hints["extraction_model"])
            check_type(argname="argument summarization_model", value=summarization_model, expected_type=type_hints["summarization_model"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if assessment_model is not None:
            self._values["assessment_model"] = assessment_model
        if evaluation_model is not None:
            self._values["evaluation_model"] = evaluation_model
        if extraction_model is not None:
            self._values["extraction_model"] = extraction_model
        if summarization_model is not None:
            self._values["summarization_model"] = summarization_model

    @builtins.property
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
        result = self._values.get("assessment_model")
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], result)

    @builtins.property
    def evaluation_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional configuration for the evaluation stage.

        Defines the model and parameters used for evaluating extraction accuracy.

        :stability: experimental
        '''
        result = self._values.get("evaluation_model")
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], result)

    @builtins.property
    def extraction_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional configuration for the extraction stage.

        Defines the model and parameters used for information extraction.

        :stability: experimental
        '''
        result = self._values.get("extraction_model")
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], result)

    @builtins.property
    def summarization_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional configuration for the summarization stage.

        Defines the model and parameters used for generating document summaries.

        :stability: experimental
        '''
        result = self._values.get("summarization_model")
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerUdopProcessorConfigurationDefinitionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ISagemakerUdopProcessorConfigurationSchema)
class SagemakerUdopProcessorConfigurationSchema(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/genai-idp-sagemaker-udop-processor.SagemakerUdopProcessorConfigurationSchema",
):
    '''(experimental) Schema definition for SageMaker UDOP processor configuration. Provides JSON Schema validation rules for the configuration UI and API.

    This class defines the structure, validation rules, and UI presentation
    for the SageMaker UDOP processor configuration, including document classes,
    attributes, extraction parameters, evaluation criteria, and summarization options.
    It's specialized for use with SageMaker endpoints for document classification.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="bind")
    def bind(self, processor: SagemakerUdopProcessor) -> None:
        '''(experimental) Binds the configuration schema to a processor instance.

        Creates a custom resource that updates the schema in the configuration table.

        :param processor: The SageMaker UDOP document processor to apply the schema to.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25798e79d77258bd5932f3e39becdf5ad114eadcac672b8e9f0d53c441789c88)
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        return typing.cast(None, jsii.invoke(self, "bind", [processor]))


@jsii.data_type(
    jsii_type="@cdklabs/genai-idp-sagemaker-udop-processor.SagemakerUdopProcessorProps",
    jsii_struct_bases=[_cdklabs_genai_idp_bf65f2c1.DocumentProcessorProps],
    name_mapping={
        "environment": "environment",
        "max_processing_concurrency": "maxProcessingConcurrency",
        "classifier_endpoint": "classifierEndpoint",
        "configuration": "configuration",
        "assessment_guardrail": "assessmentGuardrail",
        "classification_guardrail": "classificationGuardrail",
        "custom_prompt_generator": "customPromptGenerator",
        "evaluation_baseline_bucket": "evaluationBaselineBucket",
        "evaluation_enabled": "evaluationEnabled",
        "extraction_guardrail": "extractionGuardrail",
        "ocr_max_workers": "ocrMaxWorkers",
        "summarization_guardrail": "summarizationGuardrail",
    },
)
class SagemakerUdopProcessorProps(_cdklabs_genai_idp_bf65f2c1.DocumentProcessorProps):
    def __init__(
        self,
        *,
        environment: _cdklabs_genai_idp_bf65f2c1.IProcessingEnvironment,
        max_processing_concurrency: typing.Optional[jsii.Number] = None,
        classifier_endpoint: _aws_cdk_aws_sagemaker_alpha_90d55fd8.IEndpoint,
        configuration: ISagemakerUdopProcessorConfiguration,
        assessment_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        classification_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        custom_prompt_generator: typing.Optional[_cdklabs_genai_idp_bf65f2c1.ICustomPromptGenerator] = None,
        evaluation_baseline_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        evaluation_enabled: typing.Optional[builtins.bool] = None,
        extraction_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        ocr_max_workers: typing.Optional[jsii.Number] = None,
        summarization_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    ) -> None:
        '''(experimental) Configuration properties for the SageMaker UDOP document processor.

        SageMaker UDOP Processor uses specialized document processing with SageMaker endpoints
        for document classification, combined with foundation models for extraction.
        This processor is ideal for specialized document types that require custom
        classification models for accurate document categorization before extraction.

        SageMaker UDOP Processor offers the highest level of customization for document processing,
        allowing you to deploy and use specialized models for document classification
        while still leveraging foundation models for extraction tasks. This processor
        is particularly useful for domain-specific document processing needs.

        :param environment: (experimental) The processing environment that provides shared infrastructure and services. Contains input/output buckets, tracking tables, API endpoints, and other resources needed for document processing operations.
        :param max_processing_concurrency: (experimental) The maximum number of documents that can be processed concurrently. Controls the throughput and resource utilization of the document processing system. Default: 100 concurrent workflows
        :param classifier_endpoint: (experimental) The SageMaker endpoint used for document classification. Determines document types based on content and structure analysis using specialized models like RVL-CDIP or UDOP deployed on SageMaker. This is a key component of Pattern 3, enabling specialized document classification beyond what's possible with foundation models alone. Users can create their own SageMaker endpoint using any method (CDK constructs, existing endpoints, etc.) and pass it directly to the processor.
        :param configuration: (experimental) Configuration for the SageMaker UDOP document processor. Provides customization options for the processing workflow, including schema definitions, prompts, and evaluation settings.
        :param assessment_guardrail: (experimental) Optional Bedrock guardrail to apply to assessment model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param classification_guardrail: (experimental) Optional Bedrock guardrail to apply to classification model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param custom_prompt_generator: (experimental) Optional custom prompt generator for injecting business logic into extraction processing. When provided, this Lambda function will be called to customize prompts based on document content, business rules, or external system integrations. Default: - No custom prompt generator is used
        :param evaluation_baseline_bucket: (experimental) Optional S3 bucket containing baseline documents for evaluation. Used as ground truth when evaluating extraction accuracy by comparing extraction results against known correct values. Required when evaluationEnabled is true. Default: - No evaluation baseline bucket is configured
        :param evaluation_enabled: (experimental) Controls whether extraction results are evaluated for accuracy. When enabled, compares extraction results against expected values to measure extraction quality and identify improvement areas. Default: false
        :param extraction_guardrail: (experimental) Optional Bedrock guardrail to apply to extraction model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param ocr_max_workers: (experimental) The maximum number of concurrent workers for OCR processing. Controls parallelism during the text extraction phase to optimize throughput while managing resource utilization. Default: 20
        :param summarization_guardrail: (experimental) Optional Bedrock guardrail to apply to summarization model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abcf98cadfb4cb958ff48f796fd58118dfdc700bcbd181eb9bc2a90f654baf03)
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument max_processing_concurrency", value=max_processing_concurrency, expected_type=type_hints["max_processing_concurrency"])
            check_type(argname="argument classifier_endpoint", value=classifier_endpoint, expected_type=type_hints["classifier_endpoint"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument assessment_guardrail", value=assessment_guardrail, expected_type=type_hints["assessment_guardrail"])
            check_type(argname="argument classification_guardrail", value=classification_guardrail, expected_type=type_hints["classification_guardrail"])
            check_type(argname="argument custom_prompt_generator", value=custom_prompt_generator, expected_type=type_hints["custom_prompt_generator"])
            check_type(argname="argument evaluation_baseline_bucket", value=evaluation_baseline_bucket, expected_type=type_hints["evaluation_baseline_bucket"])
            check_type(argname="argument evaluation_enabled", value=evaluation_enabled, expected_type=type_hints["evaluation_enabled"])
            check_type(argname="argument extraction_guardrail", value=extraction_guardrail, expected_type=type_hints["extraction_guardrail"])
            check_type(argname="argument ocr_max_workers", value=ocr_max_workers, expected_type=type_hints["ocr_max_workers"])
            check_type(argname="argument summarization_guardrail", value=summarization_guardrail, expected_type=type_hints["summarization_guardrail"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "environment": environment,
            "classifier_endpoint": classifier_endpoint,
            "configuration": configuration,
        }
        if max_processing_concurrency is not None:
            self._values["max_processing_concurrency"] = max_processing_concurrency
        if assessment_guardrail is not None:
            self._values["assessment_guardrail"] = assessment_guardrail
        if classification_guardrail is not None:
            self._values["classification_guardrail"] = classification_guardrail
        if custom_prompt_generator is not None:
            self._values["custom_prompt_generator"] = custom_prompt_generator
        if evaluation_baseline_bucket is not None:
            self._values["evaluation_baseline_bucket"] = evaluation_baseline_bucket
        if evaluation_enabled is not None:
            self._values["evaluation_enabled"] = evaluation_enabled
        if extraction_guardrail is not None:
            self._values["extraction_guardrail"] = extraction_guardrail
        if ocr_max_workers is not None:
            self._values["ocr_max_workers"] = ocr_max_workers
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
    def classifier_endpoint(self) -> _aws_cdk_aws_sagemaker_alpha_90d55fd8.IEndpoint:
        '''(experimental) The SageMaker endpoint used for document classification.

        Determines document types based on content and structure analysis using
        specialized models like RVL-CDIP or UDOP deployed on SageMaker.

        This is a key component of Pattern 3, enabling specialized document classification
        beyond what's possible with foundation models alone. Users can create their own
        SageMaker endpoint using any method (CDK constructs, existing endpoints, etc.)
        and pass it directly to the processor.

        :stability: experimental
        '''
        result = self._values.get("classifier_endpoint")
        assert result is not None, "Required property 'classifier_endpoint' is missing"
        return typing.cast(_aws_cdk_aws_sagemaker_alpha_90d55fd8.IEndpoint, result)

    @builtins.property
    def configuration(self) -> ISagemakerUdopProcessorConfiguration:
        '''(experimental) Configuration for the SageMaker UDOP document processor.

        Provides customization options for the processing workflow,
        including schema definitions, prompts, and evaluation settings.

        :stability: experimental
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(ISagemakerUdopProcessorConfiguration, result)

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
    def evaluation_baseline_bucket(
        self,
    ) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket]:
        '''(experimental) Optional S3 bucket containing baseline documents for evaluation.

        Used as ground truth when evaluating extraction accuracy by
        comparing extraction results against known correct values.

        Required when evaluationEnabled is true.

        :default: - No evaluation baseline bucket is configured

        :stability: experimental
        '''
        result = self._values.get("evaluation_baseline_bucket")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket], result)

    @builtins.property
    def evaluation_enabled(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Controls whether extraction results are evaluated for accuracy.

        When enabled, compares extraction results against expected values
        to measure extraction quality and identify improvement areas.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("evaluation_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

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
        return "SagemakerUdopProcessorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BasicSagemakerClassifier",
    "BasicSagemakerClassifierProps",
    "ISagemakerUdopProcessor",
    "ISagemakerUdopProcessorConfiguration",
    "ISagemakerUdopProcessorConfigurationDefinition",
    "ISagemakerUdopProcessorConfigurationSchema",
    "SagemakerUdopProcessor",
    "SagemakerUdopProcessorConfiguration",
    "SagemakerUdopProcessorConfigurationDefinition",
    "SagemakerUdopProcessorConfigurationDefinitionOptions",
    "SagemakerUdopProcessorConfigurationSchema",
    "SagemakerUdopProcessorProps",
]

publication.publish()

def _typecheckingstub__33bd9b9c171b640e2b3d84d0c978fb23584ac94d5973bcce4a919879ab1f7783(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_type: _aws_cdk_aws_sagemaker_alpha_90d55fd8.InstanceType,
    model_data: _aws_cdk_aws_sagemaker_alpha_90d55fd8.ModelData,
    output_bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
    key: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
    max_instance_count: typing.Optional[jsii.Number] = None,
    min_instance_count: typing.Optional[jsii.Number] = None,
    scale_in_cooldown: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    scale_out_cooldown: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    target_invocations_per_instance_per_minute: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44a3f7949dd90007393520eaa0a1a7508158ec20cb9323cd16604f7c376d365f(
    *,
    instance_type: _aws_cdk_aws_sagemaker_alpha_90d55fd8.InstanceType,
    model_data: _aws_cdk_aws_sagemaker_alpha_90d55fd8.ModelData,
    output_bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
    key: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
    max_instance_count: typing.Optional[jsii.Number] = None,
    min_instance_count: typing.Optional[jsii.Number] = None,
    scale_in_cooldown: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    scale_out_cooldown: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    target_invocations_per_instance_per_minute: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c182eb97dfcf80a64d49011e7a60d62f22f9c506a1ac0b8aa92877743280c92e(
    processor: ISagemakerUdopProcessor,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8c38817d25f32866ebc9acbcd9112c5de9e977e12d16f648770f7b82c0954d9(
    processor: SagemakerUdopProcessor,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2a519fc1300ad0f2c0724a7dbbb44fb59a0de9afbea0a2055985669ad8707da(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    classifier_endpoint: _aws_cdk_aws_sagemaker_alpha_90d55fd8.IEndpoint,
    configuration: ISagemakerUdopProcessorConfiguration,
    assessment_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    classification_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    custom_prompt_generator: typing.Optional[_cdklabs_genai_idp_bf65f2c1.ICustomPromptGenerator] = None,
    evaluation_baseline_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    evaluation_enabled: typing.Optional[builtins.bool] = None,
    extraction_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    ocr_max_workers: typing.Optional[jsii.Number] = None,
    summarization_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    environment: _cdklabs_genai_idp_bf65f2c1.IProcessingEnvironment,
    max_processing_concurrency: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f2160cf87128b97ab0eb8048ed483bcf8c90ce5678f108d9dd093ad4d2ba903(
    definition: ISagemakerUdopProcessorConfigurationDefinition,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03ca4a1f711553731e5b03ec631852aca2fdeab0c10ac6f85efff83bff549029(
    file_path: builtins.str,
    *,
    assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44243da7299b0e182e99e2c69ec563a2ea4df5eb908b00ddc06552b492c37486(
    processor: ISagemakerUdopProcessor,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a886bbbdf17171948c394ccc770b293d33aaf83cb94b6355160e70200154db48(
    file_path: builtins.str,
    *,
    assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__335d46eca9893646e0aead0bd52826b00f744494fca10cecc3efc3bfdfeb3045(
    *,
    assessment_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    extraction_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25798e79d77258bd5932f3e39becdf5ad114eadcac672b8e9f0d53c441789c88(
    processor: SagemakerUdopProcessor,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abcf98cadfb4cb958ff48f796fd58118dfdc700bcbd181eb9bc2a90f654baf03(
    *,
    environment: _cdklabs_genai_idp_bf65f2c1.IProcessingEnvironment,
    max_processing_concurrency: typing.Optional[jsii.Number] = None,
    classifier_endpoint: _aws_cdk_aws_sagemaker_alpha_90d55fd8.IEndpoint,
    configuration: ISagemakerUdopProcessorConfiguration,
    assessment_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    classification_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    custom_prompt_generator: typing.Optional[_cdklabs_genai_idp_bf65f2c1.ICustomPromptGenerator] = None,
    evaluation_baseline_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    evaluation_enabled: typing.Optional[builtins.bool] = None,
    extraction_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    ocr_max_workers: typing.Optional[jsii.Number] = None,
    summarization_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
) -> None:
    """Type checking stubs"""
    pass
