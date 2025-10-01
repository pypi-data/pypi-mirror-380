r'''
# GenAI IDP BdaProcessor

[![Compatible with GenAI IDP version: 0.3.16](https://img.shields.io/badge/Compatible%20with%20GenAI%20IDP-0.3.16-brightgreen)](https://github.com/aws-solutions-library-samples/accelerated-intelligent-document-processing-on-aws/releases/tag/v0.3.16)
![Stability: Experimental](https://img.shields.io/badge/Stability-Experimental-important.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

> This package is provided on an "as-is" basis, and may include bugs, errors, or other issues.
> All classes are under active development and subject to non-backward compatible changes or removal in any
> future version. These are not subject to the [Semantic Versioning](https://semver.org/) model.
> This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

---


## Overview

The GenAI IDP BdaProcessor implements intelligent document processing using Amazon Bedrock Data Automation. This package provides a complete AWS CDK implementation for extracting structured data from standard documents with well-defined formats using Amazon's managed document processing capabilities.

The BdaProcessor is ideal for processing common document types such as invoices, receipts, financial statements, and other standardized forms where the structure is consistent and well-understood.

For a detailed exploration of all constructs and their configuration options, we invite you to check out our [API documentation](./API.md). This comprehensive reference will help you make the most of Pattern 1's capabilities in your document processing workflows.

## Features

* **Amazon Bedrock Data Automation Integration**: Leverages Amazon's managed document processing capabilities
* **Serverless Architecture**: Built on AWS Lambda, Step Functions, and other serverless technologies
* **Automatic Document Classification**: Identifies document types and applies appropriate extraction schemas
* **Configurable Processing Rules**: Customize extraction behavior through configuration
* **Document Summarization**: Optional AI-powered document summarization capabilities
* **Evaluation Framework**: Built-in mechanisms for evaluating extraction quality
* **Comprehensive Metrics**: Detailed CloudWatch metrics for monitoring processing performance
* **Cost Optimization**: Efficient resource utilization to minimize processing costs

## Getting Started

### Installation

The package is available through npm for JavaScript/TypeScript projects and PyPI for Python projects.

#### JavaScript/TypeScript (npm)

```bash
# Using npm
npm install @cdklabs/genai-idp-bda-processor @cdklabs/genai-idp

# Using yarn
yarn add @cdklabs/genai-idp-bda-processor @cdklabs/genai-idp
```

#### Python (PyPI)

```bash
# Using pip
pip install cdklabs.genai-idp-bda-processor cdklabs.genai-idp

# Using poetry
poetry add cdklabs.genai-idp-bda-processor cdklabs.genai-idp
```

### Basic Usage

Here's how to integrate BdaProcessor into your IDP solution:

```python
import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as kms from 'aws-cdk-lib/aws-kms';
import { ProcessingEnvironment } from '@cdklabs/genai-idp';
import { BdaProcessor, BdaProcessorConfiguration, IDataAutomationProject } from '@cdklabs/genai-idp-bda-processor';

export class MyIdpStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create encryption key
    const key = new kms.Key(this, 'IdpKey', {
      enableKeyRotation: true,
    });

    // Create S3 buckets for input, output, and working data
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

    // Create processor configuration
    const configuration = BdaProcessorConfiguration.lendingPackageSample();

    // Reference your Bedrock Data Automation project
    const dataAutomationProject: IDataAutomationProject = /* Your data automation project */;

    // Create the processor
    const processor = new BdaProcessor(this, 'Processor', {
      environment,
      configuration,
      dataAutomationProject,
    });
  }
}
```

## Configuration

BdaProcessor supports extensive configuration options:

* **Data Automation Project**: Connect to your Amazon Bedrock Data Automation project
* **Invokable Models**: Specify which models to use for evaluation and summarization
* **Guardrails**: Apply content guardrails to model interactions
* **Concurrency**: Control processing throughput and resource utilization
* **VPC Configuration**: Deploy in a VPC for enhanced security and connectivity

For detailed configuration options, refer to the TypeScript type definitions and JSDoc comments in the source code.

## Contributing

We welcome contributions to the GenAI IDP BdaProcessor! Please follow these steps to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code adheres to our coding standards and includes appropriate tests.

## Related Projects

* [@cdklabs/genai-idp](../idp): Core IDP constructs and infrastructure
* [@cdklabs/genai-idp-bedrock-llm-processor](../idp-bedrock-llm-processor): BedrockLlmProcessor implementation for custom extraction using Amazon Bedrock models
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
import aws_cdk.aws_dynamodb as _aws_cdk_aws_dynamodb_ceddda9d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import aws_cdk.aws_kinesis as _aws_cdk_aws_kinesis_ceddda9d
import aws_cdk.aws_kms as _aws_cdk_aws_kms_ceddda9d
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_ceddda9d
import aws_cdk.aws_stepfunctions as _aws_cdk_aws_stepfunctions_ceddda9d
import cdklabs.genai_idp as _cdklabs_genai_idp_bf65f2c1
import cdklabs.generative_ai_cdk_constructs.bedrock as _cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec
import constructs as _constructs_77d1e7e8


@jsii.data_type(
    jsii_type="@cdklabs/genai-idp-bda-processor.BdaMetadataTableProps",
    jsii_struct_bases=[_cdklabs_genai_idp_bf65f2c1.FixedKeyTableProps],
    name_mapping={
        "billing_mode": "billingMode",
        "contributor_insights_enabled": "contributorInsightsEnabled",
        "contributor_insights_specification": "contributorInsightsSpecification",
        "deletion_protection": "deletionProtection",
        "encryption": "encryption",
        "encryption_key": "encryptionKey",
        "import_source": "importSource",
        "kinesis_precision_timestamp": "kinesisPrecisionTimestamp",
        "kinesis_stream": "kinesisStream",
        "max_read_request_units": "maxReadRequestUnits",
        "max_write_request_units": "maxWriteRequestUnits",
        "point_in_time_recovery": "pointInTimeRecovery",
        "point_in_time_recovery_specification": "pointInTimeRecoverySpecification",
        "read_capacity": "readCapacity",
        "removal_policy": "removalPolicy",
        "replica_removal_policy": "replicaRemovalPolicy",
        "replication_regions": "replicationRegions",
        "replication_timeout": "replicationTimeout",
        "resource_policy": "resourcePolicy",
        "stream": "stream",
        "table_class": "tableClass",
        "table_name": "tableName",
        "wait_for_replication_to_finish": "waitForReplicationToFinish",
        "warm_throughput": "warmThroughput",
        "write_capacity": "writeCapacity",
    },
)
class BdaMetadataTableProps(_cdklabs_genai_idp_bf65f2c1.FixedKeyTableProps):
    def __init__(
        self,
        *,
        billing_mode: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.BillingMode] = None,
        contributor_insights_enabled: typing.Optional[builtins.bool] = None,
        contributor_insights_specification: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.ContributorInsightsSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
        deletion_protection: typing.Optional[builtins.bool] = None,
        encryption: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableEncryption] = None,
        encryption_key: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
        import_source: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.ImportSourceSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_precision_timestamp: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.ApproximateCreationDateTimePrecision] = None,
        kinesis_stream: typing.Optional[_aws_cdk_aws_kinesis_ceddda9d.IStream] = None,
        max_read_request_units: typing.Optional[jsii.Number] = None,
        max_write_request_units: typing.Optional[jsii.Number] = None,
        point_in_time_recovery: typing.Optional[builtins.bool] = None,
        point_in_time_recovery_specification: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.PointInTimeRecoverySpecification, typing.Dict[builtins.str, typing.Any]]] = None,
        read_capacity: typing.Optional[jsii.Number] = None,
        removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        replica_removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        replication_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        replication_timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        resource_policy: typing.Optional[_aws_cdk_aws_iam_ceddda9d.PolicyDocument] = None,
        stream: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.StreamViewType] = None,
        table_class: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableClass] = None,
        table_name: typing.Optional[builtins.str] = None,
        wait_for_replication_to_finish: typing.Optional[builtins.bool] = None,
        warm_throughput: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.WarmThroughput, typing.Dict[builtins.str, typing.Any]]] = None,
        write_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Properties for the BDA Metadata Table.

        Uses the same FixedKeyTableProps pattern as other tables in the genai-idp package.

        :param billing_mode: Specify how you are charged for read and write throughput and how you manage capacity. Default: PROVISIONED if ``replicationRegions`` is not specified, PAY_PER_REQUEST otherwise
        :param contributor_insights_enabled: (deprecated) Whether CloudWatch contributor insights is enabled. Default: false
        :param contributor_insights_specification: Whether CloudWatch contributor insights is enabled and what mode is selected. Default: - contributor insights is not enabled
        :param deletion_protection: Enables deletion protection for the table. Default: false
        :param encryption: Whether server-side encryption with an AWS managed customer master key is enabled. This property cannot be set if ``serverSideEncryption`` is set. .. epigraph:: **NOTE**: if you set this to ``CUSTOMER_MANAGED`` and ``encryptionKey`` is not specified, the key that the Tablet generates for you will be created with default permissions. If you are using CDKv2, these permissions will be sufficient to enable the key for use with DynamoDB tables. If you are using CDKv1, make sure the feature flag ``@aws-cdk/aws-kms:defaultKeyPolicies`` is set to ``true`` in your ``cdk.json``. Default: - The table is encrypted with an encryption key managed by DynamoDB, and you are not charged any fee for using it.
        :param encryption_key: External KMS key to use for table encryption. This property can only be set if ``encryption`` is set to ``TableEncryption.CUSTOMER_MANAGED``. Default: - If ``encryption`` is set to ``TableEncryption.CUSTOMER_MANAGED`` and this property is undefined, a new KMS key will be created and associated with this table. If ``encryption`` and this property are both undefined, then the table is encrypted with an encryption key managed by DynamoDB, and you are not charged any fee for using it.
        :param import_source: The properties of data being imported from the S3 bucket source to the table. Default: - no data import from the S3 bucket
        :param kinesis_precision_timestamp: Kinesis Data Stream approximate creation timestamp precision. Default: ApproximateCreationDateTimePrecision.MICROSECOND
        :param kinesis_stream: Kinesis Data Stream to capture item-level changes for the table. Default: - no Kinesis Data Stream
        :param max_read_request_units: The maximum read request units for the table. Careful if you add Global Secondary Indexes, as those will share the table's maximum on-demand throughput. Can only be provided if billingMode is PAY_PER_REQUEST. Default: - on-demand throughput is disabled
        :param max_write_request_units: The write request units for the table. Careful if you add Global Secondary Indexes, as those will share the table's maximum on-demand throughput. Can only be provided if billingMode is PAY_PER_REQUEST. Default: - on-demand throughput is disabled
        :param point_in_time_recovery: (deprecated) Whether point-in-time recovery is enabled. Default: false - point in time recovery is not enabled.
        :param point_in_time_recovery_specification: Whether point-in-time recovery is enabled and recoveryPeriodInDays is set. Default: - point in time recovery is not enabled.
        :param read_capacity: The read capacity for the table. Careful if you add Global Secondary Indexes, as those will share the table's provisioned throughput. Can only be provided if billingMode is Provisioned. Default: 5
        :param removal_policy: The removal policy to apply to the DynamoDB Table. Default: RemovalPolicy.RETAIN
        :param replica_removal_policy: The removal policy to apply to the DynamoDB replica tables. Default: undefined - use DynamoDB Table's removal policy
        :param replication_regions: Regions where replica tables will be created. Default: - no replica tables are created
        :param replication_timeout: The timeout for a table replication operation in a single region. Default: Duration.minutes(30)
        :param resource_policy: Resource policy to assign to table. Default: - No resource policy statement
        :param stream: When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Default: - streams are disabled unless ``replicationRegions`` is specified
        :param table_class: Specify the table class. Default: STANDARD
        :param table_name: Enforces a particular physical table name. Default: 
        :param wait_for_replication_to_finish: [WARNING: Use this flag with caution, misusing this flag may cause deleting existing replicas, refer to the detailed documentation for more information] Indicates whether CloudFormation stack waits for replication to finish. If set to false, the CloudFormation resource will mark the resource as created and replication will be completed asynchronously. This property is ignored if replicationRegions property is not set. WARNING: DO NOT UNSET this property if adding/removing multiple replicationRegions in one deployment, as CloudFormation only supports one region replication at a time. CDK overcomes this limitation by waiting for replication to finish before starting new replicationRegion. If the custom resource which handles replication has a physical resource ID with the format ``region`` instead of ``tablename-region`` (this would happen if the custom resource hasn't received an event since v1.91.0), DO NOT SET this property to false without making a change to the table name. This will cause the existing replicas to be deleted. Default: true
        :param warm_throughput: Specify values to pre-warm you DynamoDB Table Warm Throughput feature is not available for Global Table replicas using the ``Table`` construct. To enable Warm Throughput, use the ``TableV2`` construct instead. Default: - warm throughput is not configured
        :param write_capacity: The write capacity for the table. Careful if you add Global Secondary Indexes, as those will share the table's provisioned throughput. Can only be provided if billingMode is Provisioned. Default: 5

        :stability: experimental
        '''
        if isinstance(contributor_insights_specification, dict):
            contributor_insights_specification = _aws_cdk_aws_dynamodb_ceddda9d.ContributorInsightsSpecification(**contributor_insights_specification)
        if isinstance(import_source, dict):
            import_source = _aws_cdk_aws_dynamodb_ceddda9d.ImportSourceSpecification(**import_source)
        if isinstance(point_in_time_recovery_specification, dict):
            point_in_time_recovery_specification = _aws_cdk_aws_dynamodb_ceddda9d.PointInTimeRecoverySpecification(**point_in_time_recovery_specification)
        if isinstance(warm_throughput, dict):
            warm_throughput = _aws_cdk_aws_dynamodb_ceddda9d.WarmThroughput(**warm_throughput)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4849acdd9a3ca6b19cf44efee7524ebdc7c212b205fefbcd2ed3c99a51e7b574)
            check_type(argname="argument billing_mode", value=billing_mode, expected_type=type_hints["billing_mode"])
            check_type(argname="argument contributor_insights_enabled", value=contributor_insights_enabled, expected_type=type_hints["contributor_insights_enabled"])
            check_type(argname="argument contributor_insights_specification", value=contributor_insights_specification, expected_type=type_hints["contributor_insights_specification"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument import_source", value=import_source, expected_type=type_hints["import_source"])
            check_type(argname="argument kinesis_precision_timestamp", value=kinesis_precision_timestamp, expected_type=type_hints["kinesis_precision_timestamp"])
            check_type(argname="argument kinesis_stream", value=kinesis_stream, expected_type=type_hints["kinesis_stream"])
            check_type(argname="argument max_read_request_units", value=max_read_request_units, expected_type=type_hints["max_read_request_units"])
            check_type(argname="argument max_write_request_units", value=max_write_request_units, expected_type=type_hints["max_write_request_units"])
            check_type(argname="argument point_in_time_recovery", value=point_in_time_recovery, expected_type=type_hints["point_in_time_recovery"])
            check_type(argname="argument point_in_time_recovery_specification", value=point_in_time_recovery_specification, expected_type=type_hints["point_in_time_recovery_specification"])
            check_type(argname="argument read_capacity", value=read_capacity, expected_type=type_hints["read_capacity"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument replica_removal_policy", value=replica_removal_policy, expected_type=type_hints["replica_removal_policy"])
            check_type(argname="argument replication_regions", value=replication_regions, expected_type=type_hints["replication_regions"])
            check_type(argname="argument replication_timeout", value=replication_timeout, expected_type=type_hints["replication_timeout"])
            check_type(argname="argument resource_policy", value=resource_policy, expected_type=type_hints["resource_policy"])
            check_type(argname="argument stream", value=stream, expected_type=type_hints["stream"])
            check_type(argname="argument table_class", value=table_class, expected_type=type_hints["table_class"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument wait_for_replication_to_finish", value=wait_for_replication_to_finish, expected_type=type_hints["wait_for_replication_to_finish"])
            check_type(argname="argument warm_throughput", value=warm_throughput, expected_type=type_hints["warm_throughput"])
            check_type(argname="argument write_capacity", value=write_capacity, expected_type=type_hints["write_capacity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if billing_mode is not None:
            self._values["billing_mode"] = billing_mode
        if contributor_insights_enabled is not None:
            self._values["contributor_insights_enabled"] = contributor_insights_enabled
        if contributor_insights_specification is not None:
            self._values["contributor_insights_specification"] = contributor_insights_specification
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if encryption is not None:
            self._values["encryption"] = encryption
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if import_source is not None:
            self._values["import_source"] = import_source
        if kinesis_precision_timestamp is not None:
            self._values["kinesis_precision_timestamp"] = kinesis_precision_timestamp
        if kinesis_stream is not None:
            self._values["kinesis_stream"] = kinesis_stream
        if max_read_request_units is not None:
            self._values["max_read_request_units"] = max_read_request_units
        if max_write_request_units is not None:
            self._values["max_write_request_units"] = max_write_request_units
        if point_in_time_recovery is not None:
            self._values["point_in_time_recovery"] = point_in_time_recovery
        if point_in_time_recovery_specification is not None:
            self._values["point_in_time_recovery_specification"] = point_in_time_recovery_specification
        if read_capacity is not None:
            self._values["read_capacity"] = read_capacity
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if replica_removal_policy is not None:
            self._values["replica_removal_policy"] = replica_removal_policy
        if replication_regions is not None:
            self._values["replication_regions"] = replication_regions
        if replication_timeout is not None:
            self._values["replication_timeout"] = replication_timeout
        if resource_policy is not None:
            self._values["resource_policy"] = resource_policy
        if stream is not None:
            self._values["stream"] = stream
        if table_class is not None:
            self._values["table_class"] = table_class
        if table_name is not None:
            self._values["table_name"] = table_name
        if wait_for_replication_to_finish is not None:
            self._values["wait_for_replication_to_finish"] = wait_for_replication_to_finish
        if warm_throughput is not None:
            self._values["warm_throughput"] = warm_throughput
        if write_capacity is not None:
            self._values["write_capacity"] = write_capacity

    @builtins.property
    def billing_mode(
        self,
    ) -> typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.BillingMode]:
        '''Specify how you are charged for read and write throughput and how you manage capacity.

        :default: PROVISIONED if ``replicationRegions`` is not specified, PAY_PER_REQUEST otherwise
        '''
        result = self._values.get("billing_mode")
        return typing.cast(typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.BillingMode], result)

    @builtins.property
    def contributor_insights_enabled(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Whether CloudWatch contributor insights is enabled.

        :default: false

        :deprecated: use `contributorInsightsSpecification instead

        :stability: deprecated
        '''
        result = self._values.get("contributor_insights_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def contributor_insights_specification(
        self,
    ) -> typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.ContributorInsightsSpecification]:
        '''Whether CloudWatch contributor insights is enabled and what mode is selected.

        :default: - contributor insights is not enabled
        '''
        result = self._values.get("contributor_insights_specification")
        return typing.cast(typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.ContributorInsightsSpecification], result)

    @builtins.property
    def deletion_protection(self) -> typing.Optional[builtins.bool]:
        '''Enables deletion protection for the table.

        :default: false
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption(
        self,
    ) -> typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableEncryption]:
        '''Whether server-side encryption with an AWS managed customer master key is enabled.

        This property cannot be set if ``serverSideEncryption`` is set.
        .. epigraph::

           **NOTE**: if you set this to ``CUSTOMER_MANAGED`` and ``encryptionKey`` is not
           specified, the key that the Tablet generates for you will be created with
           default permissions. If you are using CDKv2, these permissions will be
           sufficient to enable the key for use with DynamoDB tables.  If you are
           using CDKv1, make sure the feature flag
           ``@aws-cdk/aws-kms:defaultKeyPolicies`` is set to ``true`` in your ``cdk.json``.

        :default: - The table is encrypted with an encryption key managed by DynamoDB, and you are not charged any fee for using it.
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableEncryption], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey]:
        '''External KMS key to use for table encryption.

        This property can only be set if ``encryption`` is set to ``TableEncryption.CUSTOMER_MANAGED``.

        :default:

        - If ``encryption`` is set to ``TableEncryption.CUSTOMER_MANAGED`` and this
        property is undefined, a new KMS key will be created and associated with this table.
        If ``encryption`` and this property are both undefined, then the table is encrypted with
        an encryption key managed by DynamoDB, and you are not charged any fee for using it.
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey], result)

    @builtins.property
    def import_source(
        self,
    ) -> typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.ImportSourceSpecification]:
        '''The properties of data being imported from the S3 bucket source to the table.

        :default: - no data import from the S3 bucket
        '''
        result = self._values.get("import_source")
        return typing.cast(typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.ImportSourceSpecification], result)

    @builtins.property
    def kinesis_precision_timestamp(
        self,
    ) -> typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.ApproximateCreationDateTimePrecision]:
        '''Kinesis Data Stream approximate creation timestamp precision.

        :default: ApproximateCreationDateTimePrecision.MICROSECOND
        '''
        result = self._values.get("kinesis_precision_timestamp")
        return typing.cast(typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.ApproximateCreationDateTimePrecision], result)

    @builtins.property
    def kinesis_stream(self) -> typing.Optional[_aws_cdk_aws_kinesis_ceddda9d.IStream]:
        '''Kinesis Data Stream to capture item-level changes for the table.

        :default: - no Kinesis Data Stream
        '''
        result = self._values.get("kinesis_stream")
        return typing.cast(typing.Optional[_aws_cdk_aws_kinesis_ceddda9d.IStream], result)

    @builtins.property
    def max_read_request_units(self) -> typing.Optional[jsii.Number]:
        '''The maximum read request units for the table.

        Careful if you add Global Secondary Indexes, as
        those will share the table's maximum on-demand throughput.

        Can only be provided if billingMode is PAY_PER_REQUEST.

        :default: - on-demand throughput is disabled
        '''
        result = self._values.get("max_read_request_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_write_request_units(self) -> typing.Optional[jsii.Number]:
        '''The write request units for the table.

        Careful if you add Global Secondary Indexes, as
        those will share the table's maximum on-demand throughput.

        Can only be provided if billingMode is PAY_PER_REQUEST.

        :default: - on-demand throughput is disabled
        '''
        result = self._values.get("max_write_request_units")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def point_in_time_recovery(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Whether point-in-time recovery is enabled.

        :default: false - point in time recovery is not enabled.

        :deprecated: use ``pointInTimeRecoverySpecification`` instead

        :stability: deprecated
        '''
        result = self._values.get("point_in_time_recovery")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def point_in_time_recovery_specification(
        self,
    ) -> typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.PointInTimeRecoverySpecification]:
        '''Whether point-in-time recovery is enabled and recoveryPeriodInDays is set.

        :default: - point in time recovery is not enabled.
        '''
        result = self._values.get("point_in_time_recovery_specification")
        return typing.cast(typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.PointInTimeRecoverySpecification], result)

    @builtins.property
    def read_capacity(self) -> typing.Optional[jsii.Number]:
        '''The read capacity for the table. Careful if you add Global Secondary Indexes, as those will share the table's provisioned throughput.

        Can only be provided if billingMode is Provisioned.

        :default: 5
        '''
        result = self._values.get("read_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy]:
        '''The removal policy to apply to the DynamoDB Table.

        :default: RemovalPolicy.RETAIN
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy], result)

    @builtins.property
    def replica_removal_policy(
        self,
    ) -> typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy]:
        '''The removal policy to apply to the DynamoDB replica tables.

        :default: undefined - use DynamoDB Table's removal policy
        '''
        result = self._values.get("replica_removal_policy")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy], result)

    @builtins.property
    def replication_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Regions where replica tables will be created.

        :default: - no replica tables are created
        '''
        result = self._values.get("replication_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def replication_timeout(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''The timeout for a table replication operation in a single region.

        :default: Duration.minutes(30)
        '''
        result = self._values.get("replication_timeout")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    @builtins.property
    def resource_policy(
        self,
    ) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.PolicyDocument]:
        '''Resource policy to assign to table.

        :default: - No resource policy statement
        '''
        result = self._values.get("resource_policy")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.PolicyDocument], result)

    @builtins.property
    def stream(self) -> typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.StreamViewType]:
        '''When an item in the table is modified, StreamViewType determines what information is written to the stream for this table.

        :default: - streams are disabled unless ``replicationRegions`` is specified
        '''
        result = self._values.get("stream")
        return typing.cast(typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.StreamViewType], result)

    @builtins.property
    def table_class(self) -> typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableClass]:
        '''Specify the table class.

        :default: STANDARD
        '''
        result = self._values.get("table_class")
        return typing.cast(typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableClass], result)

    @builtins.property
    def table_name(self) -> typing.Optional[builtins.str]:
        '''Enforces a particular physical table name.

        :default:
        '''
        result = self._values.get("table_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_for_replication_to_finish(self) -> typing.Optional[builtins.bool]:
        '''[WARNING: Use this flag with caution, misusing this flag may cause deleting existing replicas, refer to the detailed documentation for more information] Indicates whether CloudFormation stack waits for replication to finish.

        If set to false, the CloudFormation resource will mark the resource as
        created and replication will be completed asynchronously. This property is
        ignored if replicationRegions property is not set.

        WARNING:
        DO NOT UNSET this property if adding/removing multiple replicationRegions
        in one deployment, as CloudFormation only supports one region replication
        at a time. CDK overcomes this limitation by waiting for replication to
        finish before starting new replicationRegion.

        If the custom resource which handles replication has a physical resource
        ID with the format ``region`` instead of ``tablename-region`` (this would happen
        if the custom resource hasn't received an event since v1.91.0), DO NOT SET
        this property to false without making a change to the table name.
        This will cause the existing replicas to be deleted.

        :default: true
        '''
        result = self._values.get("wait_for_replication_to_finish")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def warm_throughput(
        self,
    ) -> typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.WarmThroughput]:
        '''Specify values to pre-warm you DynamoDB Table Warm Throughput feature is not available for Global Table replicas using the ``Table`` construct.

        To enable Warm Throughput, use the ``TableV2`` construct instead.

        :default: - warm throughput is not configured
        '''
        result = self._values.get("warm_throughput")
        return typing.cast(typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.WarmThroughput], result)

    @builtins.property
    def write_capacity(self) -> typing.Optional[jsii.Number]:
        '''The write capacity for the table. Careful if you add Global Secondary Indexes, as those will share the table's provisioned throughput.

        Can only be provided if billingMode is Provisioned.

        :default: 5
        '''
        result = self._values.get("write_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BdaMetadataTableProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BdaProcessorConfigurationDefinition(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/genai-idp-bda-processor.BdaProcessorConfigurationDefinition",
):
    '''(experimental) Configuration definition for BDA document processing.

    Provides methods to create and customize configuration for Bedrock Data Automation processing.

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
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "IBdaProcessorConfigurationDefinition":
        '''(experimental) Creates a configuration definition from a YAML file.

        Allows users to provide custom configuration files for document processing.

        :param file_path: Path to the YAML configuration file.
        :param evaluation_model: (experimental) Optional configuration for the evaluation stage. Defines the model and parameters used for evaluating extraction accuracy.
        :param summarization_model: (experimental) Optional configuration for the summarization stage. Defines the model and parameters used for generating document summaries.

        :return: A configuration definition loaded from the file

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b266a1d8f515f3e63813ed64f8a75f7e7adc6fbc948d194821662513953d07e8)
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
        options = BdaProcessorConfigurationDefinitionOptions(
            evaluation_model=evaluation_model, summarization_model=summarization_model
        )

        return typing.cast("IBdaProcessorConfigurationDefinition", jsii.sinvoke(cls, "fromFile", [file_path, options]))

    @jsii.member(jsii_name="lendingPackageSample")
    @builtins.classmethod
    def lending_package_sample(
        cls,
        *,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "IBdaProcessorConfigurationDefinition":
        '''(experimental) Creates a default configuration definition for BDA processing.

        This configuration includes basic settings for evaluation and summarization
        when using Bedrock Data Automation projects.

        :param evaluation_model: (experimental) Optional configuration for the evaluation stage. Defines the model and parameters used for evaluating extraction accuracy.
        :param summarization_model: (experimental) Optional configuration for the summarization stage. Defines the model and parameters used for generating document summaries.

        :return: A configuration definition with default settings

        :stability: experimental
        '''
        options = BdaProcessorConfigurationDefinitionOptions(
            evaluation_model=evaluation_model, summarization_model=summarization_model
        )

        return typing.cast("IBdaProcessorConfigurationDefinition", jsii.sinvoke(cls, "lendingPackageSample", [options]))


@jsii.data_type(
    jsii_type="@cdklabs/genai-idp-bda-processor.BdaProcessorConfigurationDefinitionOptions",
    jsii_struct_bases=[],
    name_mapping={
        "evaluation_model": "evaluationModel",
        "summarization_model": "summarizationModel",
    },
)
class BdaProcessorConfigurationDefinitionOptions:
    def __init__(
        self,
        *,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> None:
        '''(experimental) Options for configuring the BDA processor configuration definition.

        Allows customization of evaluation and summarization models and parameters.

        :param evaluation_model: (experimental) Optional configuration for the evaluation stage. Defines the model and parameters used for evaluating extraction accuracy.
        :param summarization_model: (experimental) Optional configuration for the summarization stage. Defines the model and parameters used for generating document summaries.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39e0e7b75eb47733ba39f314b1ac307f07c54e7d174568d7fa2e85429c0547d6)
            check_type(argname="argument evaluation_model", value=evaluation_model, expected_type=type_hints["evaluation_model"])
            check_type(argname="argument summarization_model", value=summarization_model, expected_type=type_hints["summarization_model"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if evaluation_model is not None:
            self._values["evaluation_model"] = evaluation_model
        if summarization_model is not None:
            self._values["summarization_model"] = summarization_model

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
        return "BdaProcessorConfigurationDefinitionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdklabs/genai-idp-bda-processor.BdaProcessorProps",
    jsii_struct_bases=[_cdklabs_genai_idp_bf65f2c1.DocumentProcessorProps],
    name_mapping={
        "environment": "environment",
        "max_processing_concurrency": "maxProcessingConcurrency",
        "configuration": "configuration",
        "data_automation_project": "dataAutomationProject",
        "enable_hitl": "enableHITL",
        "evaluation_baseline_bucket": "evaluationBaselineBucket",
        "sage_maker_a2_i_review_portal_url": "sageMakerA2IReviewPortalURL",
        "summarization_guardrail": "summarizationGuardrail",
    },
)
class BdaProcessorProps(_cdklabs_genai_idp_bf65f2c1.DocumentProcessorProps):
    def __init__(
        self,
        *,
        environment: _cdklabs_genai_idp_bf65f2c1.IProcessingEnvironment,
        max_processing_concurrency: typing.Optional[jsii.Number] = None,
        configuration: "IBdaProcessorConfiguration",
        data_automation_project: "IDataAutomationProject",
        enable_hitl: typing.Optional[builtins.bool] = None,
        evaluation_baseline_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        sage_maker_a2_i_review_portal_url: typing.Optional[builtins.str] = None,
        summarization_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    ) -> None:
        '''(experimental) Configuration properties for the BDA document processor.

        BDA Processor uses Amazon Bedrock Data Automation for document processing,
        providing a managed solution for extracting structured data from documents
        with minimal custom code. This processor leverages Amazon Bedrock's pre-built
        document processing capabilities through Data Automation projects.

        BDA Processor is the simplest implementation path for common document types
        that are well-supported by Amazon Bedrock's extraction capabilities.

        :param environment: (experimental) The processing environment that provides shared infrastructure and services. Contains input/output buckets, tracking tables, API endpoints, and other resources needed for document processing operations.
        :param max_processing_concurrency: (experimental) The maximum number of documents that can be processed concurrently. Controls the throughput and resource utilization of the document processing system. Default: 100 concurrent workflows
        :param configuration: (experimental) Configuration for the BDA document processor. Provides customization options for the processing workflow, including schema definitions and evaluation settings.
        :param data_automation_project: (experimental) The Bedrock Data Automation Project used for document processing. This project defines the document processing workflow in Amazon Bedrock, including document types, extraction schemas, and processing rules.
        :param enable_hitl: (experimental) Enable Human In The Loop (HITL) review for documents with low confidence scores. When enabled, documents that fall below the confidence threshold will be sent for human review before proceeding with the workflow. Default: false
        :param evaluation_baseline_bucket: (experimental) Optional S3 bucket containing baseline evaluation data for model performance assessment. Used to store reference documents and expected outputs for evaluating the accuracy and quality of document processing results. Default: - No evaluation baseline bucket is configured
        :param sage_maker_a2_i_review_portal_url: (experimental) URL for the SageMaker A2I review portal used for HITL tasks. This URL is provided to human reviewers to access documents that require manual review and correction. Default: - No review portal URL is provided
        :param summarization_guardrail: (experimental) Optional Bedrock guardrail to apply to summarization model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78a29d496050d67a9dc0f9a561a352f655170e0379e2603e91a7b588f71d714a)
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument max_processing_concurrency", value=max_processing_concurrency, expected_type=type_hints["max_processing_concurrency"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument data_automation_project", value=data_automation_project, expected_type=type_hints["data_automation_project"])
            check_type(argname="argument enable_hitl", value=enable_hitl, expected_type=type_hints["enable_hitl"])
            check_type(argname="argument evaluation_baseline_bucket", value=evaluation_baseline_bucket, expected_type=type_hints["evaluation_baseline_bucket"])
            check_type(argname="argument sage_maker_a2_i_review_portal_url", value=sage_maker_a2_i_review_portal_url, expected_type=type_hints["sage_maker_a2_i_review_portal_url"])
            check_type(argname="argument summarization_guardrail", value=summarization_guardrail, expected_type=type_hints["summarization_guardrail"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "environment": environment,
            "configuration": configuration,
            "data_automation_project": data_automation_project,
        }
        if max_processing_concurrency is not None:
            self._values["max_processing_concurrency"] = max_processing_concurrency
        if enable_hitl is not None:
            self._values["enable_hitl"] = enable_hitl
        if evaluation_baseline_bucket is not None:
            self._values["evaluation_baseline_bucket"] = evaluation_baseline_bucket
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
    def configuration(self) -> "IBdaProcessorConfiguration":
        '''(experimental) Configuration for the BDA document processor.

        Provides customization options for the processing workflow,
        including schema definitions and evaluation settings.

        :stability: experimental
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast("IBdaProcessorConfiguration", result)

    @builtins.property
    def data_automation_project(self) -> "IDataAutomationProject":
        '''(experimental) The Bedrock Data Automation Project used for document processing.

        This project defines the document processing workflow in Amazon Bedrock,
        including document types, extraction schemas, and processing rules.

        :stability: experimental
        '''
        result = self._values.get("data_automation_project")
        assert result is not None, "Required property 'data_automation_project' is missing"
        return typing.cast("IDataAutomationProject", result)

    @builtins.property
    def enable_hitl(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Enable Human In The Loop (HITL) review for documents with low confidence scores.

        When enabled, documents that fall below the confidence threshold will be
        sent for human review before proceeding with the workflow.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("enable_hitl")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def evaluation_baseline_bucket(
        self,
    ) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket]:
        '''(experimental) Optional S3 bucket containing baseline evaluation data for model performance assessment.

        Used to store reference documents and expected outputs for evaluating
        the accuracy and quality of document processing results.

        :default: - No evaluation baseline bucket is configured

        :stability: experimental
        '''
        result = self._values.get("evaluation_baseline_bucket")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket], result)

    @builtins.property
    def sage_maker_a2_i_review_portal_url(self) -> typing.Optional[builtins.str]:
        '''(experimental) URL for the SageMaker A2I review portal used for HITL tasks.

        This URL is provided to human reviewers to access documents that require
        manual review and correction.

        :default: - No review portal URL is provided

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
        return "BdaProcessorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@cdklabs/genai-idp-bda-processor.IBdaMetadataTable")
class IBdaMetadataTable(
    _aws_cdk_aws_dynamodb_ceddda9d.ITable,
    typing_extensions.Protocol,
):
    '''(experimental) Interface for the BDA metadata table.

    This table stores metadata about BDA (Bedrock Data Automation) processing records,
    enabling tracking of individual document processing records within BDA jobs.

    :stability: experimental
    '''

    pass


class _IBdaMetadataTableProxy(
    jsii.proxy_for(_aws_cdk_aws_dynamodb_ceddda9d.ITable), # type: ignore[misc]
):
    '''(experimental) Interface for the BDA metadata table.

    This table stores metadata about BDA (Bedrock Data Automation) processing records,
    enabling tracking of individual document processing records within BDA jobs.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/genai-idp-bda-processor.IBdaMetadataTable"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBdaMetadataTable).__jsii_proxy_class__ = lambda : _IBdaMetadataTableProxy


@jsii.interface(jsii_type="@cdklabs/genai-idp-bda-processor.IBdaProcessor")
class IBdaProcessor(
    _cdklabs_genai_idp_bf65f2c1.IDocumentProcessor,
    typing_extensions.Protocol,
):
    '''(experimental) Interface for BDA document processor implementation.

    BDA Processor uses Amazon Bedrock Data Automation for document processing,
    leveraging pre-built extraction capabilities for common document types.
    This processor is ideal for standard documents with well-defined structures
    and requires minimal custom code to implement.

    Use BDA Processor when:

    - Processing standard document types like invoices, receipts, or forms
    - You need a managed solution with minimal custom code
    - You want to leverage Amazon Bedrock's pre-built extraction capabilities

    :stability: experimental
    '''

    pass


class _IBdaProcessorProxy(
    jsii.proxy_for(_cdklabs_genai_idp_bf65f2c1.IDocumentProcessor), # type: ignore[misc]
):
    '''(experimental) Interface for BDA document processor implementation.

    BDA Processor uses Amazon Bedrock Data Automation for document processing,
    leveraging pre-built extraction capabilities for common document types.
    This processor is ideal for standard documents with well-defined structures
    and requires minimal custom code to implement.

    Use BDA Processor when:

    - Processing standard document types like invoices, receipts, or forms
    - You need a managed solution with minimal custom code
    - You want to leverage Amazon Bedrock's pre-built extraction capabilities

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/genai-idp-bda-processor.IBdaProcessor"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBdaProcessor).__jsii_proxy_class__ = lambda : _IBdaProcessorProxy


@jsii.interface(
    jsii_type="@cdklabs/genai-idp-bda-processor.IBdaProcessorConfiguration"
)
class IBdaProcessorConfiguration(typing_extensions.Protocol):
    '''(experimental) Interface for BDA document processor configuration.

    Provides configuration management for Bedrock Data Automation processing.

    :stability: experimental
    '''

    @jsii.member(jsii_name="bind")
    def bind(self, processor: IBdaProcessor) -> "IBdaProcessorConfigurationDefinition":
        '''(experimental) Binds the configuration to a processor instance.

        This method applies the configuration to the processor.

        :param processor: The BDA document processor to apply to.

        :stability: experimental
        '''
        ...


class _IBdaProcessorConfigurationProxy:
    '''(experimental) Interface for BDA document processor configuration.

    Provides configuration management for Bedrock Data Automation processing.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/genai-idp-bda-processor.IBdaProcessorConfiguration"

    @jsii.member(jsii_name="bind")
    def bind(self, processor: IBdaProcessor) -> "IBdaProcessorConfigurationDefinition":
        '''(experimental) Binds the configuration to a processor instance.

        This method applies the configuration to the processor.

        :param processor: The BDA document processor to apply to.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87deafe5a6b77182983f6688ee03cbab8a39df5f116c97289a443886146fa02a)
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        return typing.cast("IBdaProcessorConfigurationDefinition", jsii.invoke(self, "bind", [processor]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBdaProcessorConfiguration).__jsii_proxy_class__ = lambda : _IBdaProcessorConfigurationProxy


@jsii.interface(
    jsii_type="@cdklabs/genai-idp-bda-processor.IBdaProcessorConfigurationDefinition"
)
class IBdaProcessorConfigurationDefinition(
    _cdklabs_genai_idp_bf65f2c1.IConfigurationDefinition,
    typing_extensions.Protocol,
):
    '''(experimental) Interface for BDA processor configuration definition.

    Defines the structure and capabilities of configuration for Bedrock Data Automation processing.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="evaluationModel")
    def evaluation_model(
        self,
    ) -> _cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable:
        '''(experimental) The invokable model used for evaluating extraction results.

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

        When provided, enables automatic generation of document summaries
        that capture key information from processed documents.

        :stability: experimental
        '''
        ...


class _IBdaProcessorConfigurationDefinitionProxy(
    jsii.proxy_for(_cdklabs_genai_idp_bf65f2c1.IConfigurationDefinition), # type: ignore[misc]
):
    '''(experimental) Interface for BDA processor configuration definition.

    Defines the structure and capabilities of configuration for Bedrock Data Automation processing.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/genai-idp-bda-processor.IBdaProcessorConfigurationDefinition"

    @builtins.property
    @jsii.member(jsii_name="evaluationModel")
    def evaluation_model(
        self,
    ) -> _cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable:
        '''(experimental) The invokable model used for evaluating extraction results.

        Used to assess the quality and accuracy of extracted information by
        comparing extraction results against expected values.

        :stability: experimental
        '''
        return typing.cast(_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable, jsii.get(self, "evaluationModel"))

    @builtins.property
    @jsii.member(jsii_name="summarizationModel")
    def summarization_model(
        self,
    ) -> typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable]:
        '''(experimental) Optional invokable model used for document summarization.

        When provided, enables automatic generation of document summaries
        that capture key information from processed documents.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable], jsii.get(self, "summarizationModel"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBdaProcessorConfigurationDefinition).__jsii_proxy_class__ = lambda : _IBdaProcessorConfigurationDefinitionProxy


@jsii.interface(
    jsii_type="@cdklabs/genai-idp-bda-processor.IBdaProcessorConfigurationSchema"
)
class IBdaProcessorConfigurationSchema(typing_extensions.Protocol):
    '''(experimental) Interface for BDA configuration schema.

    Defines the structure and validation rules for BDA processor configuration.

    :stability: experimental
    '''

    @jsii.member(jsii_name="bind")
    def bind(self, processor: IBdaProcessor) -> None:
        '''(experimental) Binds the configuration schema to a processor instance.

        This method applies the schema definition to the processor's configuration table.

        :param processor: The BDA document processor to apply the schema to.

        :stability: experimental
        '''
        ...


class _IBdaProcessorConfigurationSchemaProxy:
    '''(experimental) Interface for BDA configuration schema.

    Defines the structure and validation rules for BDA processor configuration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/genai-idp-bda-processor.IBdaProcessorConfigurationSchema"

    @jsii.member(jsii_name="bind")
    def bind(self, processor: IBdaProcessor) -> None:
        '''(experimental) Binds the configuration schema to a processor instance.

        This method applies the schema definition to the processor's configuration table.

        :param processor: The BDA document processor to apply the schema to.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2336f51d7f8c205432d79be7d5d4a47244b37fecdc8f64f110ddc111137e761e)
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        return typing.cast(None, jsii.invoke(self, "bind", [processor]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBdaProcessorConfigurationSchema).__jsii_proxy_class__ = lambda : _IBdaProcessorConfigurationSchemaProxy


@jsii.interface(jsii_type="@cdklabs/genai-idp-bda-processor.IDataAutomationProject")
class IDataAutomationProject(typing_extensions.Protocol):
    '''(experimental) Interface representing an Amazon Bedrock Data Automation Project.

    Data Automation Projects in Amazon Bedrock provide a managed way to extract
    structured data from documents using foundation models. This interface allows
    the IDP solution to work with existing Bedrock Data Automation Projects.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        '''(experimental) The Amazon Resource Name (ARN) of the Bedrock Data Automation Project.

        This ARN is used to invoke the project for document processing and is
        referenced in IAM policies to grant appropriate permissions.

        Format: arn:aws:bedrock:{region}:{account}:data-automation-project/{project-id}

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="grantInvokeAsync")
    def grant_invoke_async(
        self,
        grantee: _aws_cdk_aws_iam_ceddda9d.IGrantable,
    ) -> _aws_cdk_aws_iam_ceddda9d.Grant:
        '''
        :param grantee: -

        :stability: experimental
        '''
        ...


class _IDataAutomationProjectProxy:
    '''(experimental) Interface representing an Amazon Bedrock Data Automation Project.

    Data Automation Projects in Amazon Bedrock provide a managed way to extract
    structured data from documents using foundation models. This interface allows
    the IDP solution to work with existing Bedrock Data Automation Projects.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cdklabs/genai-idp-bda-processor.IDataAutomationProject"

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        '''(experimental) The Amazon Resource Name (ARN) of the Bedrock Data Automation Project.

        This ARN is used to invoke the project for document processing and is
        referenced in IAM policies to grant appropriate permissions.

        Format: arn:aws:bedrock:{region}:{account}:data-automation-project/{project-id}

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @jsii.member(jsii_name="grantInvokeAsync")
    def grant_invoke_async(
        self,
        grantee: _aws_cdk_aws_iam_ceddda9d.IGrantable,
    ) -> _aws_cdk_aws_iam_ceddda9d.Grant:
        '''
        :param grantee: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bc8453e383b35f333a47bf5bcab02b41734295d205fab59b5964ac26840c878)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.Grant, jsii.invoke(self, "grantInvokeAsync", [grantee]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataAutomationProject).__jsii_proxy_class__ = lambda : _IDataAutomationProjectProxy


@jsii.implements(IBdaMetadataTable)
class BdaMetadataTable(
    _aws_cdk_aws_dynamodb_ceddda9d.Table,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/genai-idp-bda-processor.BdaMetadataTable",
):
    '''(experimental) A DynamoDB table for storing BDA processing metadata.

    This table uses a composite key (execution_id, record_number) to efficiently store
    and query metadata about individual records processed by Bedrock Data Automation.
    The table design supports tracking the processing status and results of each
    document record within a BDA execution.

    Key features:

    - Partition key: execution_id (String) - identifies the BDA execution
    - Sort key: record_number (Number) - identifies individual records within the execution
    - TTL enabled with ExpiresAfter attribute for automatic cleanup
    - Point-in-time recovery enabled for data protection
    - KMS encryption for data security

    :stability: experimental
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        billing_mode: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.BillingMode] = None,
        contributor_insights_enabled: typing.Optional[builtins.bool] = None,
        contributor_insights_specification: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.ContributorInsightsSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
        deletion_protection: typing.Optional[builtins.bool] = None,
        encryption: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableEncryption] = None,
        encryption_key: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
        import_source: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.ImportSourceSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_precision_timestamp: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.ApproximateCreationDateTimePrecision] = None,
        kinesis_stream: typing.Optional[_aws_cdk_aws_kinesis_ceddda9d.IStream] = None,
        max_read_request_units: typing.Optional[jsii.Number] = None,
        max_write_request_units: typing.Optional[jsii.Number] = None,
        point_in_time_recovery: typing.Optional[builtins.bool] = None,
        point_in_time_recovery_specification: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.PointInTimeRecoverySpecification, typing.Dict[builtins.str, typing.Any]]] = None,
        read_capacity: typing.Optional[jsii.Number] = None,
        removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        replica_removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
        replication_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        replication_timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        resource_policy: typing.Optional[_aws_cdk_aws_iam_ceddda9d.PolicyDocument] = None,
        stream: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.StreamViewType] = None,
        table_class: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableClass] = None,
        table_name: typing.Optional[builtins.str] = None,
        wait_for_replication_to_finish: typing.Optional[builtins.bool] = None,
        warm_throughput: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.WarmThroughput, typing.Dict[builtins.str, typing.Any]]] = None,
        write_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Creates a new BdaMetadataTable.

        :param scope: The construct scope.
        :param id: The construct ID.
        :param billing_mode: Specify how you are charged for read and write throughput and how you manage capacity. Default: PROVISIONED if ``replicationRegions`` is not specified, PAY_PER_REQUEST otherwise
        :param contributor_insights_enabled: (deprecated) Whether CloudWatch contributor insights is enabled. Default: false
        :param contributor_insights_specification: Whether CloudWatch contributor insights is enabled and what mode is selected. Default: - contributor insights is not enabled
        :param deletion_protection: Enables deletion protection for the table. Default: false
        :param encryption: Whether server-side encryption with an AWS managed customer master key is enabled. This property cannot be set if ``serverSideEncryption`` is set. .. epigraph:: **NOTE**: if you set this to ``CUSTOMER_MANAGED`` and ``encryptionKey`` is not specified, the key that the Tablet generates for you will be created with default permissions. If you are using CDKv2, these permissions will be sufficient to enable the key for use with DynamoDB tables. If you are using CDKv1, make sure the feature flag ``@aws-cdk/aws-kms:defaultKeyPolicies`` is set to ``true`` in your ``cdk.json``. Default: - The table is encrypted with an encryption key managed by DynamoDB, and you are not charged any fee for using it.
        :param encryption_key: External KMS key to use for table encryption. This property can only be set if ``encryption`` is set to ``TableEncryption.CUSTOMER_MANAGED``. Default: - If ``encryption`` is set to ``TableEncryption.CUSTOMER_MANAGED`` and this property is undefined, a new KMS key will be created and associated with this table. If ``encryption`` and this property are both undefined, then the table is encrypted with an encryption key managed by DynamoDB, and you are not charged any fee for using it.
        :param import_source: The properties of data being imported from the S3 bucket source to the table. Default: - no data import from the S3 bucket
        :param kinesis_precision_timestamp: Kinesis Data Stream approximate creation timestamp precision. Default: ApproximateCreationDateTimePrecision.MICROSECOND
        :param kinesis_stream: Kinesis Data Stream to capture item-level changes for the table. Default: - no Kinesis Data Stream
        :param max_read_request_units: The maximum read request units for the table. Careful if you add Global Secondary Indexes, as those will share the table's maximum on-demand throughput. Can only be provided if billingMode is PAY_PER_REQUEST. Default: - on-demand throughput is disabled
        :param max_write_request_units: The write request units for the table. Careful if you add Global Secondary Indexes, as those will share the table's maximum on-demand throughput. Can only be provided if billingMode is PAY_PER_REQUEST. Default: - on-demand throughput is disabled
        :param point_in_time_recovery: (deprecated) Whether point-in-time recovery is enabled. Default: false - point in time recovery is not enabled.
        :param point_in_time_recovery_specification: Whether point-in-time recovery is enabled and recoveryPeriodInDays is set. Default: - point in time recovery is not enabled.
        :param read_capacity: The read capacity for the table. Careful if you add Global Secondary Indexes, as those will share the table's provisioned throughput. Can only be provided if billingMode is Provisioned. Default: 5
        :param removal_policy: The removal policy to apply to the DynamoDB Table. Default: RemovalPolicy.RETAIN
        :param replica_removal_policy: The removal policy to apply to the DynamoDB replica tables. Default: undefined - use DynamoDB Table's removal policy
        :param replication_regions: Regions where replica tables will be created. Default: - no replica tables are created
        :param replication_timeout: The timeout for a table replication operation in a single region. Default: Duration.minutes(30)
        :param resource_policy: Resource policy to assign to table. Default: - No resource policy statement
        :param stream: When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Default: - streams are disabled unless ``replicationRegions`` is specified
        :param table_class: Specify the table class. Default: STANDARD
        :param table_name: Enforces a particular physical table name. Default: 
        :param wait_for_replication_to_finish: [WARNING: Use this flag with caution, misusing this flag may cause deleting existing replicas, refer to the detailed documentation for more information] Indicates whether CloudFormation stack waits for replication to finish. If set to false, the CloudFormation resource will mark the resource as created and replication will be completed asynchronously. This property is ignored if replicationRegions property is not set. WARNING: DO NOT UNSET this property if adding/removing multiple replicationRegions in one deployment, as CloudFormation only supports one region replication at a time. CDK overcomes this limitation by waiting for replication to finish before starting new replicationRegion. If the custom resource which handles replication has a physical resource ID with the format ``region`` instead of ``tablename-region`` (this would happen if the custom resource hasn't received an event since v1.91.0), DO NOT SET this property to false without making a change to the table name. This will cause the existing replicas to be deleted. Default: true
        :param warm_throughput: Specify values to pre-warm you DynamoDB Table Warm Throughput feature is not available for Global Table replicas using the ``Table`` construct. To enable Warm Throughput, use the ``TableV2`` construct instead. Default: - warm throughput is not configured
        :param write_capacity: The write capacity for the table. Careful if you add Global Secondary Indexes, as those will share the table's provisioned throughput. Can only be provided if billingMode is Provisioned. Default: 5

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4473b17875dd9ebd39f8f1cd72be862ad72e1803004162cc63bdc02e0395825a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BdaMetadataTableProps(
            billing_mode=billing_mode,
            contributor_insights_enabled=contributor_insights_enabled,
            contributor_insights_specification=contributor_insights_specification,
            deletion_protection=deletion_protection,
            encryption=encryption,
            encryption_key=encryption_key,
            import_source=import_source,
            kinesis_precision_timestamp=kinesis_precision_timestamp,
            kinesis_stream=kinesis_stream,
            max_read_request_units=max_read_request_units,
            max_write_request_units=max_write_request_units,
            point_in_time_recovery=point_in_time_recovery,
            point_in_time_recovery_specification=point_in_time_recovery_specification,
            read_capacity=read_capacity,
            removal_policy=removal_policy,
            replica_removal_policy=replica_removal_policy,
            replication_regions=replication_regions,
            replication_timeout=replication_timeout,
            resource_policy=resource_policy,
            stream=stream,
            table_class=table_class,
            table_name=table_name,
            wait_for_replication_to_finish=wait_for_replication_to_finish,
            warm_throughput=warm_throughput,
            write_capacity=write_capacity,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.implements(IBdaProcessor)
class BdaProcessor(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/genai-idp-bda-processor.BdaProcessor",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        configuration: IBdaProcessorConfiguration,
        data_automation_project: IDataAutomationProject,
        enable_hitl: typing.Optional[builtins.bool] = None,
        evaluation_baseline_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        sage_maker_a2_i_review_portal_url: typing.Optional[builtins.str] = None,
        summarization_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
        environment: _cdklabs_genai_idp_bf65f2c1.IProcessingEnvironment,
        max_processing_concurrency: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param configuration: (experimental) Configuration for the BDA document processor. Provides customization options for the processing workflow, including schema definitions and evaluation settings.
        :param data_automation_project: (experimental) The Bedrock Data Automation Project used for document processing. This project defines the document processing workflow in Amazon Bedrock, including document types, extraction schemas, and processing rules.
        :param enable_hitl: (experimental) Enable Human In The Loop (HITL) review for documents with low confidence scores. When enabled, documents that fall below the confidence threshold will be sent for human review before proceeding with the workflow. Default: false
        :param evaluation_baseline_bucket: (experimental) Optional S3 bucket containing baseline evaluation data for model performance assessment. Used to store reference documents and expected outputs for evaluating the accuracy and quality of document processing results. Default: - No evaluation baseline bucket is configured
        :param sage_maker_a2_i_review_portal_url: (experimental) URL for the SageMaker A2I review portal used for HITL tasks. This URL is provided to human reviewers to access documents that require manual review and correction. Default: - No review portal URL is provided
        :param summarization_guardrail: (experimental) Optional Bedrock guardrail to apply to summarization model interactions. Helps ensure model outputs adhere to content policies and guidelines by filtering inappropriate content and enforcing usage policies. Default: - No guardrail is applied
        :param environment: (experimental) The processing environment that provides shared infrastructure and services. Contains input/output buckets, tracking tables, API endpoints, and other resources needed for document processing operations.
        :param max_processing_concurrency: (experimental) The maximum number of documents that can be processed concurrently. Controls the throughput and resource utilization of the document processing system. Default: 100 concurrent workflows

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d69ba8dcc5cc944af50f625bf20f0946cbb3ff06c2c77d085c8ca086ef18b91a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BdaProcessorProps(
            configuration=configuration,
            data_automation_project=data_automation_project,
            enable_hitl=enable_hitl,
            evaluation_baseline_bucket=evaluation_baseline_bucket,
            sage_maker_a2_i_review_portal_url=sage_maker_a2_i_review_portal_url,
            summarization_guardrail=summarization_guardrail,
            environment=environment,
            max_processing_concurrency=max_processing_concurrency,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="metricBdaJobsFailed")
    def metric_bda_jobs_failed(
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
        '''(experimental) Creates a CloudWatch metric for failed BDA jobs.

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

        :return: CloudWatch Metric for failed BDA jobs

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBdaJobsFailed", [props]))

    @jsii.member(jsii_name="metricBdaJobsSucceeded")
    def metric_bda_jobs_succeeded(
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
        '''(experimental) Creates a CloudWatch metric for successful BDA jobs.

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

        :return: CloudWatch Metric for successful BDA jobs

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBdaJobsSucceeded", [props]))

    @jsii.member(jsii_name="metricBdaJobsTotal")
    def metric_bda_jobs_total(
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
        '''(experimental) Creates a CloudWatch metric for total BDA jobs.

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

        :return: CloudWatch Metric for total BDA jobs

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBdaJobsTotal", [props]))

    @jsii.member(jsii_name="metricBdaRequestLatency")
    def metric_bda_request_latency(
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
        '''(experimental) Creates a CloudWatch metric for BDA request latency.

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

        :return: CloudWatch Metric for BDA request latency in milliseconds

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBdaRequestLatency", [props]))

    @jsii.member(jsii_name="metricBdaRequestsFailed")
    def metric_bda_requests_failed(
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
        '''(experimental) Creates a CloudWatch metric for failed BDA requests.

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

        :return: CloudWatch Metric for failed BDA requests

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBdaRequestsFailed", [props]))

    @jsii.member(jsii_name="metricBdaRequestsMaxRetriesExceeded")
    def metric_bda_requests_max_retries_exceeded(
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
        '''(experimental) Creates a CloudWatch metric for BDA requests that exceeded max retries.

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

        :return: CloudWatch Metric for BDA requests that exceeded max retries

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBdaRequestsMaxRetriesExceeded", [props]))

    @jsii.member(jsii_name="metricBdaRequestsNonRetryableErrors")
    def metric_bda_requests_non_retryable_errors(
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
        '''(experimental) Creates a CloudWatch metric for BDA non-retryable errors.

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

        :return: CloudWatch Metric for BDA non-retryable errors

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBdaRequestsNonRetryableErrors", [props]))

    @jsii.member(jsii_name="metricBdaRequestsRetrySuccess")
    def metric_bda_requests_retry_success(
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
        '''(experimental) Creates a CloudWatch metric for successful BDA request retries.

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

        :return: CloudWatch Metric for successful BDA request retries

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBdaRequestsRetrySuccess", [props]))

    @jsii.member(jsii_name="metricBdaRequestsSucceeded")
    def metric_bda_requests_succeeded(
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
        '''(experimental) Creates a CloudWatch metric for successful BDA requests.

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

        :return: CloudWatch Metric for successful BDA requests

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBdaRequestsSucceeded", [props]))

    @jsii.member(jsii_name="metricBdaRequestsThrottles")
    def metric_bda_requests_throttles(
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
        '''(experimental) Creates a CloudWatch metric for BDA request throttles.

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

        :return: CloudWatch Metric for BDA request throttles

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBdaRequestsThrottles", [props]))

    @jsii.member(jsii_name="metricBdaRequestsTotal")
    def metric_bda_requests_total(
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
        '''(experimental) Creates a CloudWatch metric for total BDA requests.

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

        :return: CloudWatch Metric for total BDA requests

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBdaRequestsTotal", [props]))

    @jsii.member(jsii_name="metricBdaRequestsTotalLatency")
    def metric_bda_requests_total_latency(
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
        '''(experimental) Creates a CloudWatch metric for total BDA request latency.

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

        :return: CloudWatch Metric for total BDA request latency in milliseconds

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBdaRequestsTotalLatency", [props]))

    @jsii.member(jsii_name="metricBdaRequestsUnexpectedErrors")
    def metric_bda_requests_unexpected_errors(
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
        '''(experimental) Creates a CloudWatch metric for BDA unexpected errors.

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

        :return: CloudWatch Metric for BDA unexpected errors

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricBdaRequestsUnexpectedErrors", [props]))

    @jsii.member(jsii_name="metricProcessedCustomPages")
    def metric_processed_custom_pages(
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
        '''(experimental) Creates a CloudWatch metric for processed custom pages.

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

        :return: CloudWatch Metric for processed custom pages

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricProcessedCustomPages", [props]))

    @jsii.member(jsii_name="metricProcessedDocuments")
    def metric_processed_documents(
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
        '''(experimental) Creates a CloudWatch metric for processed documents.

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

        :return: CloudWatch Metric for processed documents

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricProcessedDocuments", [props]))

    @jsii.member(jsii_name="metricProcessedPages")
    def metric_processed_pages(
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
        '''(experimental) Creates a CloudWatch metric for processed pages.

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

        :return: CloudWatch Metric for processed pages

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricProcessedPages", [props]))

    @jsii.member(jsii_name="metricProcessedStandardPages")
    def metric_processed_standard_pages(
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
        '''(experimental) Creates a CloudWatch metric for processed standard pages.

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

        :return: CloudWatch Metric for processed standard pages

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

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricProcessedStandardPages", [props]))

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


@jsii.implements(IBdaProcessorConfiguration)
class BdaProcessorConfiguration(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/genai-idp-bda-processor.BdaProcessorConfiguration",
):
    '''(experimental) Configuration management for BDA document processing using Bedrock Data Automation.

    This construct creates and manages the configuration for BDA document processing,
    including schema definitions and configuration values. It provides a centralized
    way to manage extraction schemas, evaluation settings, and summarization parameters.

    :stability: experimental
    '''

    def __init__(self, definition: IBdaProcessorConfigurationDefinition) -> None:
        '''(experimental) Protected constructor to enforce factory method usage.

        :param definition: The configuration definition instance.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__664a6aaafecf743d592e8a4f622b618ee2c0bd00056e93bc991c24c0ea51473f)
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
        jsii.create(self.__class__, self, [definition])

    @jsii.member(jsii_name="fromFile")
    @builtins.classmethod
    def from_file(
        cls,
        file_path: builtins.str,
        *,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "BdaProcessorConfiguration":
        '''(experimental) Creates a configuration from a YAML file.

        :param file_path: Path to the YAML configuration file.
        :param evaluation_model: (experimental) Optional configuration for the evaluation stage. Defines the model and parameters used for evaluating extraction accuracy.
        :param summarization_model: (experimental) Optional configuration for the summarization stage. Defines the model and parameters used for generating document summaries.

        :return: A new BdaProcessorConfiguration instance

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b05238a52cca03738c6fde6a065399200e61ac361bfa5e4478bf14cc390e7913)
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
        options = BdaProcessorConfigurationDefinitionOptions(
            evaluation_model=evaluation_model, summarization_model=summarization_model
        )

        return typing.cast("BdaProcessorConfiguration", jsii.sinvoke(cls, "fromFile", [file_path, options]))

    @jsii.member(jsii_name="lendingPackageSample")
    @builtins.classmethod
    def lending_package_sample(
        cls,
        *,
        evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
        summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    ) -> "BdaProcessorConfiguration":
        '''(experimental) Creates a configuration for lending package processing.

        :param evaluation_model: (experimental) Optional configuration for the evaluation stage. Defines the model and parameters used for evaluating extraction accuracy.
        :param summarization_model: (experimental) Optional configuration for the summarization stage. Defines the model and parameters used for generating document summaries.

        :return: A configuration definition with default settings

        :stability: experimental
        '''
        options = BdaProcessorConfigurationDefinitionOptions(
            evaluation_model=evaluation_model, summarization_model=summarization_model
        )

        return typing.cast("BdaProcessorConfiguration", jsii.sinvoke(cls, "lendingPackageSample", [options]))

    @jsii.member(jsii_name="bind")
    def bind(self, processor: IBdaProcessor) -> IBdaProcessorConfigurationDefinition:
        '''(experimental) Binds the configuration to a processor instance.

        This method applies the configuration to the processor.

        :param processor: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d8e52fb5a7ccbb836a0a82b7b5541144fb1c9d8504e11789c2ceb6fc0be7b33)
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        return typing.cast(IBdaProcessorConfigurationDefinition, jsii.invoke(self, "bind", [processor]))


@jsii.implements(IBdaProcessorConfigurationSchema)
class BdaProcessorConfigurationSchema(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdklabs/genai-idp-bda-processor.BdaProcessorConfigurationSchema",
):
    '''(experimental) Schema definition for BDA processor configuration. Provides JSON Schema validation rules for the configuration UI and API.

    This class defines the structure, validation rules, and UI presentation
    for the BDA processor configuration, including document classes, attributes,
    evaluation settings, and summarization parameters.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''(experimental) Creates a new BdaProcessorConfigurationSchema.

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="bind")
    def bind(self, processor: IBdaProcessor) -> None:
        '''(experimental) Binds the configuration schema to a processor instance.

        Creates a custom resource that updates the schema in the configuration table.

        :param processor: The BDA document processor to apply the schema to.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ffc45bd765ced55547a605ea37ff9735c386a6820cfe1edf63ffdd47338b76c)
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
        return typing.cast(None, jsii.invoke(self, "bind", [processor]))


__all__ = [
    "BdaMetadataTable",
    "BdaMetadataTableProps",
    "BdaProcessor",
    "BdaProcessorConfiguration",
    "BdaProcessorConfigurationDefinition",
    "BdaProcessorConfigurationDefinitionOptions",
    "BdaProcessorConfigurationSchema",
    "BdaProcessorProps",
    "IBdaMetadataTable",
    "IBdaProcessor",
    "IBdaProcessorConfiguration",
    "IBdaProcessorConfigurationDefinition",
    "IBdaProcessorConfigurationSchema",
    "IDataAutomationProject",
]

publication.publish()

def _typecheckingstub__4849acdd9a3ca6b19cf44efee7524ebdc7c212b205fefbcd2ed3c99a51e7b574(
    *,
    billing_mode: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.BillingMode] = None,
    contributor_insights_enabled: typing.Optional[builtins.bool] = None,
    contributor_insights_specification: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.ContributorInsightsSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    deletion_protection: typing.Optional[builtins.bool] = None,
    encryption: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableEncryption] = None,
    encryption_key: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
    import_source: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.ImportSourceSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis_precision_timestamp: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.ApproximateCreationDateTimePrecision] = None,
    kinesis_stream: typing.Optional[_aws_cdk_aws_kinesis_ceddda9d.IStream] = None,
    max_read_request_units: typing.Optional[jsii.Number] = None,
    max_write_request_units: typing.Optional[jsii.Number] = None,
    point_in_time_recovery: typing.Optional[builtins.bool] = None,
    point_in_time_recovery_specification: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.PointInTimeRecoverySpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    read_capacity: typing.Optional[jsii.Number] = None,
    removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    replica_removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    replication_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    replication_timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    resource_policy: typing.Optional[_aws_cdk_aws_iam_ceddda9d.PolicyDocument] = None,
    stream: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.StreamViewType] = None,
    table_class: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableClass] = None,
    table_name: typing.Optional[builtins.str] = None,
    wait_for_replication_to_finish: typing.Optional[builtins.bool] = None,
    warm_throughput: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.WarmThroughput, typing.Dict[builtins.str, typing.Any]]] = None,
    write_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b266a1d8f515f3e63813ed64f8a75f7e7adc6fbc948d194821662513953d07e8(
    file_path: builtins.str,
    *,
    evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39e0e7b75eb47733ba39f314b1ac307f07c54e7d174568d7fa2e85429c0547d6(
    *,
    evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78a29d496050d67a9dc0f9a561a352f655170e0379e2603e91a7b588f71d714a(
    *,
    environment: _cdklabs_genai_idp_bf65f2c1.IProcessingEnvironment,
    max_processing_concurrency: typing.Optional[jsii.Number] = None,
    configuration: IBdaProcessorConfiguration,
    data_automation_project: IDataAutomationProject,
    enable_hitl: typing.Optional[builtins.bool] = None,
    evaluation_baseline_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    sage_maker_a2_i_review_portal_url: typing.Optional[builtins.str] = None,
    summarization_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87deafe5a6b77182983f6688ee03cbab8a39df5f116c97289a443886146fa02a(
    processor: IBdaProcessor,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2336f51d7f8c205432d79be7d5d4a47244b37fecdc8f64f110ddc111137e761e(
    processor: IBdaProcessor,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bc8453e383b35f333a47bf5bcab02b41734295d205fab59b5964ac26840c878(
    grantee: _aws_cdk_aws_iam_ceddda9d.IGrantable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4473b17875dd9ebd39f8f1cd72be862ad72e1803004162cc63bdc02e0395825a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    billing_mode: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.BillingMode] = None,
    contributor_insights_enabled: typing.Optional[builtins.bool] = None,
    contributor_insights_specification: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.ContributorInsightsSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    deletion_protection: typing.Optional[builtins.bool] = None,
    encryption: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableEncryption] = None,
    encryption_key: typing.Optional[_aws_cdk_aws_kms_ceddda9d.IKey] = None,
    import_source: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.ImportSourceSpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis_precision_timestamp: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.ApproximateCreationDateTimePrecision] = None,
    kinesis_stream: typing.Optional[_aws_cdk_aws_kinesis_ceddda9d.IStream] = None,
    max_read_request_units: typing.Optional[jsii.Number] = None,
    max_write_request_units: typing.Optional[jsii.Number] = None,
    point_in_time_recovery: typing.Optional[builtins.bool] = None,
    point_in_time_recovery_specification: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.PointInTimeRecoverySpecification, typing.Dict[builtins.str, typing.Any]]] = None,
    read_capacity: typing.Optional[jsii.Number] = None,
    removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    replica_removal_policy: typing.Optional[_aws_cdk_ceddda9d.RemovalPolicy] = None,
    replication_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    replication_timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    resource_policy: typing.Optional[_aws_cdk_aws_iam_ceddda9d.PolicyDocument] = None,
    stream: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.StreamViewType] = None,
    table_class: typing.Optional[_aws_cdk_aws_dynamodb_ceddda9d.TableClass] = None,
    table_name: typing.Optional[builtins.str] = None,
    wait_for_replication_to_finish: typing.Optional[builtins.bool] = None,
    warm_throughput: typing.Optional[typing.Union[_aws_cdk_aws_dynamodb_ceddda9d.WarmThroughput, typing.Dict[builtins.str, typing.Any]]] = None,
    write_capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d69ba8dcc5cc944af50f625bf20f0946cbb3ff06c2c77d085c8ca086ef18b91a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration: IBdaProcessorConfiguration,
    data_automation_project: IDataAutomationProject,
    enable_hitl: typing.Optional[builtins.bool] = None,
    evaluation_baseline_bucket: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    sage_maker_a2_i_review_portal_url: typing.Optional[builtins.str] = None,
    summarization_guardrail: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IGuardrail] = None,
    environment: _cdklabs_genai_idp_bf65f2c1.IProcessingEnvironment,
    max_processing_concurrency: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__664a6aaafecf743d592e8a4f622b618ee2c0bd00056e93bc991c24c0ea51473f(
    definition: IBdaProcessorConfigurationDefinition,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b05238a52cca03738c6fde6a065399200e61ac361bfa5e4478bf14cc390e7913(
    file_path: builtins.str,
    *,
    evaluation_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
    summarization_model: typing.Optional[_cdklabs_generative_ai_cdk_constructs_bedrock_8b4f33ec.IInvokable] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d8e52fb5a7ccbb836a0a82b7b5541144fb1c9d8504e11789c2ceb6fc0be7b33(
    processor: IBdaProcessor,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ffc45bd765ced55547a605ea37ff9735c386a6820cfe1edf63ffdd47338b76c(
    processor: IBdaProcessor,
) -> None:
    """Type checking stubs"""
    pass
