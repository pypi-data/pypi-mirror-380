<a id="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://fbn-prd.lusid.com/horizon*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*InstrumentApi* | [**create_instrument**](docs/InstrumentApi.md#create_instrument) | **POST** /api/instrument/onboarding/create | [EARLY ACCESS] CreateInstrument: Creates and masters instruments with third party vendors.
*InstrumentApi* | [**enrich_instrument**](docs/InstrumentApi.md#enrich_instrument) | **POST** /api/instrument/onboarding/enrich | [EARLY ACCESS] EnrichInstrument: Enriches an existing LUSID instrument using vendor data. Enrichment included identifiers, properties and market data.
*InstrumentApi* | [**get_open_figi_parameter_option**](docs/InstrumentApi.md#get_open_figi_parameter_option) | **GET** /api/instrument/onboarding/search/openfigi/parameterOptions | [EARLY ACCESS] GetOpenFigiParameterOption: Get all supported market sector values for OpenFigi search
*InstrumentApi* | [**retrieve_perm_id_result**](docs/InstrumentApi.md#retrieve_perm_id_result) | **GET** /api/instrument/onboarding/search/permid/{id} | [EARLY ACCESS] RetrievePermIdResult: Retrieve PermId results from a previous query.
*InstrumentApi* | [**search_open_figi**](docs/InstrumentApi.md#search_open_figi) | **GET** /api/instrument/onboarding/search/openfigi | [EARLY ACCESS] SearchOpenFigi: Search OpenFigi for instruments that match the specified terms.
*InstrumentApi* | [**vendors**](docs/InstrumentApi.md#vendors) | **GET** /api/instrument/onboarding/vendors | [EARLY ACCESS] Vendors: Gets the VendorProducts of any supported and licenced integrations for a given market sector and security type.
*IntegrationsApi* | [**create_instance**](docs/IntegrationsApi.md#create_instance) | **POST** /api/integrations/instances | [EXPERIMENTAL] CreateInstance: Create a single integration instance.
*IntegrationsApi* | [**delete_instance**](docs/IntegrationsApi.md#delete_instance) | **DELETE** /api/integrations/instances/{instanceId} | [EXPERIMENTAL] DeleteInstance: Delete a single integration instance.
*IntegrationsApi* | [**execute_instance**](docs/IntegrationsApi.md#execute_instance) | **POST** /api/integrations/instances/{instanceId}/execute | [EXPERIMENTAL] ExecuteInstance: Execute an integration instance.
*IntegrationsApi* | [**execute_instance_with_params**](docs/IntegrationsApi.md#execute_instance_with_params) | **POST** /api/integrations/instances/{instanceId}/executewithparams | [EXPERIMENTAL] ExecuteInstanceWithParams: Execute an integration instance with runtime parameters
*IntegrationsApi* | [**get_execution_ids_for_instance**](docs/IntegrationsApi.md#get_execution_ids_for_instance) | **GET** /api/integrations/instances/{instanceId}/executions | [EXPERIMENTAL] GetExecutionIdsForInstance: Get integration instance execution ids.
*IntegrationsApi* | [**get_instance_optional_property_mapping**](docs/IntegrationsApi.md#get_instance_optional_property_mapping) | **GET** /api/integrations/instances/configuration/{integration}/{instanceId} | [EXPERIMENTAL] GetInstanceOptionalPropertyMapping: Get the Optional Property Mapping for an Integration Instance
*IntegrationsApi* | [**get_integration_configuration**](docs/IntegrationsApi.md#get_integration_configuration) | **GET** /api/integrations/configuration/{integration} | [EXPERIMENTAL] GetIntegrationConfiguration: Get the Field and Property Mapping configuration for a given integration
*IntegrationsApi* | [**get_schema**](docs/IntegrationsApi.md#get_schema) | **GET** /api/integrations/schema/{integration} | [EXPERIMENTAL] GetSchema: Get the JSON schema for the details section of an integration instance.
*IntegrationsApi* | [**list_instances**](docs/IntegrationsApi.md#list_instances) | **GET** /api/integrations/instances | [EXPERIMENTAL] ListInstances: List instances across all integrations.
*IntegrationsApi* | [**list_integrations**](docs/IntegrationsApi.md#list_integrations) | **GET** /api/integrations | [EXPERIMENTAL] ListIntegrations: List available integrations.
*IntegrationsApi* | [**set_instance_optional_property_mapping**](docs/IntegrationsApi.md#set_instance_optional_property_mapping) | **PUT** /api/integrations/instances/configuration/{integration}/{instanceId} | [EXPERIMENTAL] SetInstanceOptionalPropertyMapping: Set the Optional Property Mapping for an Integration Instance
*IntegrationsApi* | [**update_instance**](docs/IntegrationsApi.md#update_instance) | **PUT** /api/integrations/instances/{instanceId} | [EXPERIMENTAL] UpdateInstance: Update a single integration instance.
*LogsApi* | [**get_integration_log_results**](docs/LogsApi.md#get_integration_log_results) | **GET** /api/logs | [EXPERIMENTAL] GetIntegrationLogResults: Get integration log results
*LogsApi* | [**insert_external_logs**](docs/LogsApi.md#insert_external_logs) | **POST** /api/logs/{instanceid}/{runid} | [EXPERIMENTAL] InsertExternalLogs: Inserts external logs into the specified ExternalApp Integration instance execution
*ProcessHistoryApi* | [**create_complete_event**](docs/ProcessHistoryApi.md#create_complete_event) | **POST** /api/process-history/event/complete | [EARLY ACCESS] CreateCompleteEvent: Write a completed event to the Horizon Dashboard
*ProcessHistoryApi* | [**create_update_event**](docs/ProcessHistoryApi.md#create_update_event) | **POST** /api/process-history/event/update | [EARLY ACCESS] CreateUpdateEvent: Write an update event to the Horizon Dashboard
*ProcessHistoryApi* | [**get_latest_runs**](docs/ProcessHistoryApi.md#get_latest_runs) | **GET** /api/process-history/$latestRuns | [EARLY ACCESS] GetLatestRuns: Get latest run for each process
*ProcessHistoryApi* | [**process_entry_updates**](docs/ProcessHistoryApi.md#process_entry_updates) | **POST** /api/process-history/entries/$query | [EARLY ACCESS] ProcessEntryUpdates: Get process entry updates for a query
*ProcessHistoryApi* | [**process_history_entries**](docs/ProcessHistoryApi.md#process_history_entries) | **POST** /api/process-history/$query | [EARLY ACCESS] ProcessHistoryEntries: Get process history entries
*RunsApi* | [**cancel_instance**](docs/RunsApi.md#cancel_instance) | **PUT** /api/runs/{runId}/cancel | [EXPERIMENTAL] CancelInstance: Cancels a single instance execution.
*RunsApi* | [**get_run_results**](docs/RunsApi.md#get_run_results) | **GET** /api/runs | [EXPERIMENTAL] GetRunResults: Get run results
*RunsApi* | [**rerun_instance**](docs/RunsApi.md#rerun_instance) | **PUT** /api/runs/{runId}/rerun | [EXPERIMENTAL] RerunInstance: Reruns a single instance execution.
*RunsApi* | [**stop_instance_execution**](docs/RunsApi.md#stop_instance_execution) | **PUT** /api/runs/{instanceId}/{runId}/stop | [EXPERIMENTAL] StopInstanceExecution: Stops a single instance execution.
*VendorApi* | [**get_core_field_mappings_for_product_entity**](docs/VendorApi.md#get_core_field_mappings_for_product_entity) | **GET** /api/vendor/mappings/fields | [EARLY ACCESS] GetCoreFieldMappingsForProductEntity: Get core field mappings for a given vendor product's entity.
*VendorApi* | [**get_optional_mappings_for_product_entity**](docs/VendorApi.md#get_optional_mappings_for_product_entity) | **GET** /api/vendor/mappings/optional | [EARLY ACCESS] GetOptionalMappingsForProductEntity: Get a user defined LUSID property mappings for the specified vendor / LUSID entity.
*VendorApi* | [**get_property_mappings_for_product_entity**](docs/VendorApi.md#get_property_mappings_for_product_entity) | **GET** /api/vendor/mappings/properties | [EARLY ACCESS] GetPropertyMappingsForProductEntity: Gets the property mappings for a given vendor product's entity
*VendorApi* | [**query_vendors**](docs/VendorApi.md#query_vendors) | **POST** /api/vendor/$query | [EARLY ACCESS] QueryVendors: Query for vendors and their packages with entities and sub-entities.
*VendorApi* | [**set_optional_mappings_for_product_entity**](docs/VendorApi.md#set_optional_mappings_for_product_entity) | **POST** /api/vendor/mappings/optional | [EARLY ACCESS] SetOptionalMappingsForProductEntity: Create a user defined LUSID property mappings for the specified vendor / LUSID entity.


<a id="documentation-for-models"></a>
## Documentation for Models

 - [AllowedParameterValue](docs/AllowedParameterValue.md)
 - [AuditCompleteRequest](docs/AuditCompleteRequest.md)
 - [AuditCompleteResponse](docs/AuditCompleteResponse.md)
 - [AuditCompleteStatus](docs/AuditCompleteStatus.md)
 - [AuditFileDetails](docs/AuditFileDetails.md)
 - [AuditFileType](docs/AuditFileType.md)
 - [AuditUpdateRequest](docs/AuditUpdateRequest.md)
 - [AuditUpdateResponse](docs/AuditUpdateResponse.md)
 - [CreateInstanceRequest](docs/CreateInstanceRequest.md)
 - [EnrichmentResponse](docs/EnrichmentResponse.md)
 - [ExecuteInstanceResponse](docs/ExecuteInstanceResponse.md)
 - [ExternalLogInsertionRequest](docs/ExternalLogInsertionRequest.md)
 - [ExternalLogRecord](docs/ExternalLogRecord.md)
 - [FieldMapping](docs/FieldMapping.md)
 - [FileDetails](docs/FileDetails.md)
 - [IIntegrationLogResponse](docs/IIntegrationLogResponse.md)
 - [Identifiers](docs/Identifiers.md)
 - [InstanceExecutionReferenceId](docs/InstanceExecutionReferenceId.md)
 - [InstanceIdentifier](docs/InstanceIdentifier.md)
 - [IntegrationDescription](docs/IntegrationDescription.md)
 - [IntegrationInstance](docs/IntegrationInstance.md)
 - [IntegrationLogActivity](docs/IntegrationLogActivity.md)
 - [IntegrationLogRecord](docs/IntegrationLogRecord.md)
 - [IntegrationLogTargetRecord](docs/IntegrationLogTargetRecord.md)
 - [IntegrationPropertyConfiguration](docs/IntegrationPropertyConfiguration.md)
 - [IntegrationRerunResponse](docs/IntegrationRerunResponse.md)
 - [IntegrationRunIntegration](docs/IntegrationRunIntegration.md)
 - [IntegrationRunLog](docs/IntegrationRunLog.md)
 - [IntegrationRunLogLink](docs/IntegrationRunLogLink.md)
 - [IntegrationRunResponse](docs/IntegrationRunResponse.md)
 - [IntegrationRunVersion](docs/IntegrationRunVersion.md)
 - [JSchema](docs/JSchema.md)
 - [JSchemaType](docs/JSchemaType.md)
 - [Link](docs/Link.md)
 - [LusidEntity](docs/LusidEntity.md)
 - [LusidField](docs/LusidField.md)
 - [LusidProblemDetails](docs/LusidProblemDetails.md)
 - [LusidPropertyDefinition](docs/LusidPropertyDefinition.md)
 - [LusidPropertyDefinitionOverrides](docs/LusidPropertyDefinitionOverrides.md)
 - [LusidPropertyDefinitionOverridesByType](docs/LusidPropertyDefinitionOverridesByType.md)
 - [LusidPropertyDefinitionOverridesResponse](docs/LusidPropertyDefinitionOverridesResponse.md)
 - [LusidPropertyToVendorFieldMapping](docs/LusidPropertyToVendorFieldMapping.md)
 - [LusidValidationProblemDetails](docs/LusidValidationProblemDetails.md)
 - [OnboardInstrumentRequest](docs/OnboardInstrumentRequest.md)
 - [OnboardInstrumentResponse](docs/OnboardInstrumentResponse.md)
 - [OpenFigiData](docs/OpenFigiData.md)
 - [OpenFigiParameterOptionName](docs/OpenFigiParameterOptionName.md)
 - [OpenFigiPermIdResult](docs/OpenFigiPermIdResult.md)
 - [OpenFigiSearchResult](docs/OpenFigiSearchResult.md)
 - [Optionality](docs/Optionality.md)
 - [PagedResourceListOfIIntegrationLogResponse](docs/PagedResourceListOfIIntegrationLogResponse.md)
 - [PagedResourceListOfIntegrationRunResponse](docs/PagedResourceListOfIntegrationRunResponse.md)
 - [PagedResourceListOfProcessInformation](docs/PagedResourceListOfProcessInformation.md)
 - [PagedResourceListOfProcessUpdateResult](docs/PagedResourceListOfProcessUpdateResult.md)
 - [PagedResourceListOfVendorProduct](docs/PagedResourceListOfVendorProduct.md)
 - [PermIdData](docs/PermIdData.md)
 - [ProcessInformation](docs/ProcessInformation.md)
 - [ProcessSummary](docs/ProcessSummary.md)
 - [ProcessUpdateResult](docs/ProcessUpdateResult.md)
 - [PropertyMapping](docs/PropertyMapping.md)
 - [QueryRequest](docs/QueryRequest.md)
 - [QuerySpecification](docs/QuerySpecification.md)
 - [ResourceId](docs/ResourceId.md)
 - [RowDetails](docs/RowDetails.md)
 - [Trigger](docs/Trigger.md)
 - [UpdateInstanceRequest](docs/UpdateInstanceRequest.md)
 - [VendorField](docs/VendorField.md)
 - [VendorProduct](docs/VendorProduct.md)

