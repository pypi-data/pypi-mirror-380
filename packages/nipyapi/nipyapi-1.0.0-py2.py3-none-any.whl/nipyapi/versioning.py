"""
For interactions with the NiFi Registry Service and related functions
"""

import logging

import nipyapi

# Due to line lengths, creating shortened names for these objects
from nipyapi.nifi import VersionControlInformationDTO as VciDTO
from nipyapi.registry import VersionedFlowSnapshotMetadata as VfsMd

__all__ = [
    "create_registry_client",
    "list_registry_clients",
    "delete_registry_client",
    "get_registry_client",
    "ensure_registry_client",
    "list_registry_buckets",
    "create_registry_bucket",
    "delete_registry_bucket",
    "get_registry_bucket",
    "ensure_registry_bucket",
    "save_flow_ver",
    "list_flows_in_bucket",
    "get_flow_in_bucket",
    "get_latest_flow_ver",
    "update_flow_ver",
    "get_version_info",
    "create_flow",
    "create_flow_version",
    "get_flow_version",
    "export_flow_version",
    "import_flow_version",
    "list_flow_versions",
    "deploy_flow_version",
]

log = logging.getLogger(__name__)


def create_registry_client(name, uri, description, reg_type=None, ssl_context_service=None):
    """
    Creates a Registry Client in the NiFi Controller Services

    Args:
        name (str): The name of the new Client
        uri (str): The URI for the connection
        description (str): A description for the Client
        reg_type (str): The type of registry client to create.
            Defaults to 'org.apache.nifi.registry.flow.NifiRegistryFlowRegistryClient'
        ssl_context_service (ControllerServiceEntity): Optional SSL Context Service

    Returns:
        :class:`~nipyapi.nifi.models.FlowRegistryClientEntity`: The new registry client object
    """
    assert isinstance(uri, str) and uri is not False
    assert isinstance(name, str) and name is not False
    assert isinstance(description, str)

    # NiFi 2.x registry client format
    component = {
        "name": name,
        "description": description,
        "type": reg_type or "org.apache.nifi.registry.flow.NifiRegistryFlowRegistryClient",
        "properties": {"url": uri},
    }

    with nipyapi.utils.rest_exceptions():
        controller = nipyapi.nifi.ControllerApi().create_flow_registry_client(
            body={"component": component, "revision": {"version": 0}}
        )

    # Update with SSL context if provided
    if ssl_context_service:
        update_component = dict(controller.component.to_dict())
        update_component["properties"] = {"url": uri, "ssl-context-service": ssl_context_service.id}

        with nipyapi.utils.rest_exceptions():
            controller = nipyapi.nifi.ControllerApi().update_flow_registry_client(
                id=controller.id,
                body={
                    "component": update_component,
                    "revision": {"version": controller.revision.version},
                },
            )

    return controller


def delete_registry_client(client, refresh=True):
    """
    Deletes a Registry Client from the list of NiFI Controller Services

    Args:
        client (FlowRegistryClientEntity): The client to delete
        refresh (bool): Whether to refresh the object before action

    Returns:
        (FlowRegistryClientEntity): The updated client object
    """
    assert isinstance(client, nipyapi.nifi.FlowRegistryClientEntity)
    with nipyapi.utils.rest_exceptions():
        if refresh:
            target = nipyapi.nifi.ControllerApi().get_flow_registry_client(client.id)
        else:
            target = client
        return nipyapi.nifi.ControllerApi().delete_flow_registry_client(
            id=target.id, version=target.revision.version
        )


def list_registry_clients():
    """
    Lists the available Registry Clients in the NiFi Controller Services

    Returns:
        list[:class:`~nipyapi.nifi.models.FlowRegistryClientEntity`]: objects
    """
    with nipyapi.utils.rest_exceptions():
        return nipyapi.nifi.ControllerApi().get_flow_registry_clients()


def get_registry_client(identifier, identifier_type="name"):
    """
    Filters the Registry clients to a particular identifier

    Args:
        identifier (str): the filter string
        identifier_type (str): the parameter to filter on

    Returns:
        None for no matches, Single Object for unique match,
        list(Objects) for multiple matches
    """
    with nipyapi.utils.rest_exceptions():
        obj = list_registry_clients().registries
    return nipyapi.utils.filter_obj(obj, identifier, identifier_type)


def ensure_registry_client(name, uri, description, reg_type=None, ssl_context_service=None):
    """
    Ensures a Registry Client exists, creating it if necessary.

    This is a convenience function that implements the common pattern of:
    1. Try to get existing client by name
    2. If not found, create it
    3. Handle race conditions gracefully

    Args:
        name (str): The name of the Client
        uri (str): The URI for the connection
        description (str): A description for the Client
        reg_type (str): The type of registry client to create.
            Defaults to 'org.apache.nifi.registry.flow.NifiRegistryFlowRegistryClient'
        ssl_context_service (ControllerServiceEntity): Optional SSL Context Service

    Returns:
        (FlowRegistryClientEntity): The registry client object (existing or new)
    """
    # Try to get existing client first
    try:
        existing = get_registry_client(name)
        if existing:
            # Handle both single object and list of objects
            if isinstance(existing, list):
                # Multiple matches - use the first one
                log.warning(
                    "Multiple registry clients found with name '%s', using first match", name
                )
                existing = existing[0]

            # Check if existing client's URI matches the desired URI
            existing_uri = existing.component.properties.get("url", "")
            if existing_uri == uri:
                log.debug("Found existing registry client with matching URI: %s", name)
                return existing

            # URI mismatch - delete existing and create new one
            log.debug(
                "Registry client %s URI mismatch (existing: %s, desired: %s) - recreating",
                name,
                existing_uri,
                uri,
            )
            delete_registry_client(existing)
    except ValueError:
        # Client doesn't exist, we'll create it below
        pass

    # Try to create new client
    try:
        client = create_registry_client(name, uri, description, reg_type, ssl_context_service)
        log.debug("Created new registry client: %s", name)
        return client
    except Exception as e:
        # Handle race condition where client was created between check and creation
        error_msg = str(e).lower()
        if "already exists" in error_msg or "duplicate" in error_msg:
            try:
                existing = get_registry_client(name)
                if existing:
                    # Handle both single object and list of objects
                    if isinstance(existing, list):
                        log.warning(
                            "Multiple registry clients found with name '%s' "
                            "after race condition, using first match",
                            name,
                        )
                        existing = existing[0]
                    log.debug("Found existing registry client after race condition: %s", name)
                    return existing
            except ValueError:
                # If we still can't find it, something else is wrong
                pass
        # Re-raise the original exception if we can't handle it
        raise e


def list_registry_buckets():
    """
    Lists all available Buckets in the NiFi Registry

    Returns:
        list[:class:`~nipyapi.registry.models.Bucket`]: objects
    """
    with nipyapi.utils.rest_exceptions():
        return nipyapi.registry.BucketsApi().get_buckets()


def create_registry_bucket(name, description=None):
    """
    Creates a new Registry Bucket

    Args:
        name (str): name for the bucket, must be unique in the Registry
        description (str, optional): description for the bucket

    Returns:
        :class:`~nipyapi.registry.models.Bucket`: The new Bucket object
    """
    with nipyapi.utils.rest_exceptions():
        # Create a proper Bucket object with all supported fields
        bucket_obj = nipyapi.registry.models.Bucket(name=name, description=description)

        bucket = nipyapi.registry.BucketsApi().create_bucket(body=bucket_obj)
        log.debug(
            "Created bucket %s against registry connection at %s",
            bucket.identifier,
            nipyapi.config.registry_config.api_client.host,
        )
        return bucket


def ensure_registry_bucket(name, description=None):
    """
    Ensures a Registry Bucket exists, creating it if necessary.

    This is a convenience function that implements the common pattern of:
    1. Try to get existing bucket by name
    2. If not found, create it
    3. Handle race conditions gracefully

    Args:
        name (str): name for the bucket, must be unique in the Registry
        description (str, optional): description for the bucket (only used if creating new)

    Returns:
        (Bucket): The bucket object (existing or new)
    """
    # Try to get existing bucket first
    try:
        existing = get_registry_bucket(name)
        if existing:
            log.debug("Found existing registry bucket: %s", name)
            return existing
    except ValueError:
        # Bucket doesn't exist, we'll create it below
        pass

    # Try to create new bucket
    try:
        bucket = create_registry_bucket(name, description)
        log.debug("Created new registry bucket: %s", name)
        return bucket
    except Exception as e:
        # Handle race condition where bucket was created between check and creation
        error_msg = str(e).lower()
        if "already exists" in error_msg or "duplicate" in error_msg:
            try:
                existing = get_registry_bucket(name)
                log.debug("Found existing registry bucket after race condition: %s", name)
                return existing
            except ValueError:
                # If we still can't find it, something else is wrong
                pass
        # Re-raise the original exception if we can't handle it
        raise e


def delete_registry_bucket(bucket):
    """
    Removes a bucket from the NiFi Registry

    Args:
        bucket (Bucket): the Bucket object to remove

    Returns:
        (Bucket): The updated Bucket object
    """
    try:
        return nipyapi.registry.BucketsApi().delete_bucket(
            version=bucket.revision.version if bucket.revision is not None else 0,
            bucket_id=bucket.identifier,
        )
    except (nipyapi.registry.rest.ApiException, AttributeError) as e:
        raise ValueError(e) from e


def get_registry_bucket(identifier, identifier_type="name", greedy=True):
    """
    Filters the Bucket list to a particular identifier

    Args:
        identifier (str): the filter string
        identifier_type (str): the param to filter on
        greedy (bool): False for exact match, True for greedy match

    Returns:
        None for no matches, Single Object for unique match,
        list(Objects) for multiple matches
    """
    with nipyapi.utils.rest_exceptions():
        obj = list_registry_buckets()
    return nipyapi.utils.filter_obj(obj, identifier, identifier_type, greedy=greedy)


def list_flows_in_bucket(bucket_id):
    """
    List of all Flows in a given NiFi Registry Bucket

    Args:
        bucket_id (str): The UUID of the Bucket to fetch from

    Returns:
        (list[VersionedFlow]) objects
    """
    with nipyapi.utils.rest_exceptions():
        return nipyapi.registry.BucketFlowsApi().get_flows(bucket_id)


def get_flow_in_bucket(bucket_id, identifier, identifier_type="name", greedy=True):
    """
    Filters the Flows in a Bucket against a particular identifier

    Args:
        bucket_id (str): UUID of the Bucket to filter against
        identifier (str): The string to filter on
        identifier_type (str): The param to check
        greedy (bool): False for exact match, True for greedy match

    Returns:
        None for no matches, Single Object for unique match,
        list(Objects) for multiple matches
    """
    with nipyapi.utils.rest_exceptions():
        obj = list_flows_in_bucket(bucket_id)
    return nipyapi.utils.filter_obj(obj, identifier, identifier_type, greedy=greedy)


# pylint: disable=R0913,R0917
def save_flow_ver(
    process_group,
    registry_client,
    bucket,
    flow_name=None,
    flow_id=None,
    comment="",
    desc="",
    refresh=True,
    force=False,
):
    """
    Adds a Process Group into NiFi Registry Version Control, or saves a new
    version to an existing VersionedFlow with a new version

    Args:
        process_group (ProcessGroupEntity): the ProcessGroup object to save
            as a new Flow Version
        registry_client (RegistryClient): The Client linked to the Registry
            which contains the Bucket to save to
        bucket (Bucket): the Bucket on the NiFi Registry to save to
        flow_name (str): A name for the VersionedFlow in the Bucket
            Note you need either a name for a new VersionedFlow, or the ID of
            an existing one to save a new version
        flow_id (Optional [str]): Identifier of an existing VersionedFlow in
            the bucket, if saving a new version to an existing flow
        comment (str): A comment for the version commit
        desc (str): A description of the VersionedFlow
        refresh (bool): Whether to refresh the object revisions before action
        force (bool): Whether to Force Commit, or just regular Commit

    Returns:
        :class:`~nipyapi.nifi.models.VersionControlInformationEntity`
    """
    # Validate parameter types
    assert isinstance(
        registry_client, nipyapi.nifi.FlowRegistryClientEntity
    ), "registry_client must be a FlowRegistryClientEntity, got: {}".format(type(registry_client))
    assert isinstance(
        bucket, nipyapi.registry.Bucket
    ), "bucket must be a Registry Bucket, got: {}".format(type(bucket))
    assert isinstance(
        process_group, nipyapi.nifi.ProcessGroupEntity
    ), "process_group must be a ProcessGroupEntity, got: {}".format(type(process_group))

    if refresh:
        target_pg = nipyapi.canvas.get_process_group(process_group.id, "id")
    else:
        target_pg = process_group
    flow_dto = nipyapi.nifi.VersionedFlowDTO(
        bucket_id=bucket.identifier,
        comments=comment,
        description=desc,
        flow_name=flow_name,
        flow_id=flow_id,
        registry_id=registry_client.id,
    )
    if nipyapi.utils.check_version("1.10.0") <= 0:
        # no 'action' property in versions < 1.10
        flow_dto.action = "FORCE_COMMIT" if force else "COMMIT"
    with nipyapi.utils.rest_exceptions():
        nipyapi.utils.validate_parameters_versioning_support()
        return nipyapi.nifi.VersionsApi().save_to_flow_registry(
            id=target_pg.id,
            body=nipyapi.nifi.StartVersionControlRequestEntity(
                process_group_revision=target_pg.revision, versioned_flow=flow_dto
            ),
        )


def stop_flow_ver(process_group, refresh=True):
    """
    Removes a Process Group from Version Control

    Args:
        process_group (ProcessGroupEntity): the ProcessGroup to work with
        refresh (bool): Whether to refresh the object status before actioning

    Returns:
        :class:`~nipyapi.nifi.models.VersionControlInformationEntity`
    """
    with nipyapi.utils.rest_exceptions():
        if refresh:
            target_pg = nipyapi.canvas.get_process_group(process_group.id, "id")
        else:
            target_pg = process_group
        return nipyapi.nifi.VersionsApi().stop_version_control(
            id=target_pg.id, version=target_pg.revision.version
        )


def revert_flow_ver(process_group):
    """
    Attempts to roll back uncommitted changes to a Process Group to the last
    committed version

    Args:
        process_group (ProcessGroupEntity): the ProcessGroup to work with

    Returns:
        (VersionedFlowUpdateRequestEntity)
    """
    assert isinstance(process_group, nipyapi.nifi.ProcessGroupEntity)
    with nipyapi.utils.rest_exceptions():
        return nipyapi.nifi.VersionsApi().initiate_revert_flow_version(
            id=process_group.id,
            body=nipyapi.nifi.VersionsApi().get_version_information(process_group.id),
        )


def list_flow_versions(bucket_id, flow_id, registry_id=None, service="registry"):
    """
    EXPERIMENTAL
    List all the versions of a given Flow in a given Bucket

    Args:
        bucket_id (str): UUID of the bucket holding the flow to be enumerated
        flow_id (str): UUID of the flow in the bucket to be enumerated
        registry_id (str): UUID of the registry client linking the bucket, only
            required if requesting flows via NiFi instead of directly Registry
        service (str): Accepts 'nifi' or 'registry', indicating which service
            to query

    Returns:
        list(VersionedFlowSnapshotMetadata) or
            (VersionedFlowSnapshotMetadataSetEntity)
    """
    assert service in ["nifi", "registry"]
    if service == "nifi":
        with nipyapi.utils.rest_exceptions():
            return nipyapi.nifi.FlowApi().get_versions(
                registry_id=registry_id, bucket_id=bucket_id, flow_id=flow_id
            )
    else:
        with nipyapi.utils.rest_exceptions():
            return nipyapi.registry.BucketFlowsApi().get_flow_versions(
                bucket_id=bucket_id, flow_id=flow_id
            )


def update_flow_ver(process_group, target_version=None):
    """
    Changes a versioned flow to the specified version, or the latest version

    Args:
        process_group (ProcessGroupEntity): ProcessGroupEntity under version
            control to change
        target_version (Optional [None, Int]): Either None to move to the
        latest available version, or Int of the version number to move to

    Returns:
        (bool): True if successful, False if not
    """

    def _running_update_flow_version():
        """
        Tests for completion of the operation

        Returns:
            (bool) Boolean of operation success
        """
        status = nipyapi.nifi.VersionsApi().get_update_request(u_init.request.request_id)
        if not status.request.complete:
            return False
        if status.request.failure_reason is None:
            return True
        raise ValueError(
            "Flow Version Update did not complete successfully. "
            "Error text {0}".format(status.request.failure_reason)
        )

    with nipyapi.utils.rest_exceptions():
        vci = get_version_info(process_group)
        assert isinstance(vci, nipyapi.nifi.VersionControlInformationEntity)
        flow_vers = list_flow_versions(
            vci.version_control_information.bucket_id, vci.version_control_information.flow_id
        )
        if target_version is None:
            # the first version is always the latest available
            ver = flow_vers[0].version
        else:
            # otherwise the version must be an int
            if not isinstance(target_version, int):
                raise ValueError(
                    "target_version must be a positive Integer to"
                    " pick a specific available version, or None"
                    " for the latest version to be fetched"
                )
            ver = target_version
        u_init = nipyapi.nifi.VersionsApi().initiate_version_control_update(
            id=process_group.id,
            body=nipyapi.nifi.VersionControlInformationEntity(
                process_group_revision=vci.process_group_revision,
                version_control_information=VciDTO(
                    bucket_id=vci.version_control_information.bucket_id,
                    flow_id=vci.version_control_information.flow_id,
                    group_id=vci.version_control_information.group_id,
                    registry_id=vci.version_control_information.registry_id,
                    version=ver,
                ),
            ),
        )
        nipyapi.utils.wait_to_complete(_running_update_flow_version)
        return nipyapi.nifi.VersionsApi().get_update_request(u_init.request.request_id)


def get_latest_flow_ver(bucket_id, flow_id):
    """
    Gets the most recent version of a VersionedFlowSnapshot from a bucket

    Args:
        bucket_id (str): the UUID of the Bucket containing the flow
        flow_id (str): the UUID of the VersionedFlow to be retrieved

    Returns:
        (VersionedFlowSnapshot)
    """
    with nipyapi.utils.rest_exceptions():
        return get_flow_version(bucket_id, flow_id, version=None)


def get_version_info(process_group):
    """
    Gets the Version Control information for a particular Process Group

    Args:
        process_group (ProcessGroupEntity): the ProcessGroup to work with

    Returns:
        :class:`~nipyapi.nifi.models.VersionControlInformationEntity`
    """
    assert isinstance(process_group, nipyapi.nifi.ProcessGroupEntity)
    with nipyapi.utils.rest_exceptions():
        return nipyapi.nifi.VersionsApi().get_version_information(process_group.id)


def create_flow(bucket_id, flow_name, flow_desc="", flow_type="Flow"):
    """
    Creates a new VersionedFlow stub in NiFi Registry.
    Can be used to write VersionedFlow information to without using a NiFi
    Process Group directly

    Args:
        bucket_id (str): UUID of the Bucket to write to
        flow_name (str): Name for the new VersionedFlow object
        flow_desc (Optional [str]): Description for the new VersionedFlow
            object
        flow_type (Optional [str]): Type of the VersionedFlow, should be 'Flow'

    Returns:
        (VersionedFlow)
    """
    with nipyapi.utils.rest_exceptions():
        return nipyapi.registry.BucketFlowsApi().create_flow(
            bucket_id=bucket_id,
            body=nipyapi.registry.VersionedFlow(
                name=flow_name,
                description=flow_desc,
                bucket_identifier=bucket_id,
                type=flow_type,
                version_count=0,
            ),
        )


def create_flow_version(flow, flow_snapshot, refresh=True):
    """
    EXPERIMENTAL

    Writes a FlowSnapshot into a VersionedFlow as a new version update

    Note that this differs from save_flow_ver which creates a new Flow Version
    containing the snapshot. This function writes a snapshot to an existing
    Flow Version. Useful in migrating Flow Versions between environments.

    Args:
        flow (VersionedFlowObject): the VersionedFlow object to write to
        flow_snapshot (VersionedFlowSnapshot): the Snapshot to write into the
            VersionedFlow
        refresh (bool): Whether to refresh the object status before actioning

    Returns:
        The new (VersionedFlowSnapshot)
    """
    if not isinstance(flow_snapshot, nipyapi.registry.VersionedFlowSnapshot):
        raise ValueError(
            "flow_snapshot must be an instance of a "
            "registry.VersionedFlowSnapshot object, not an {0}".format(type(flow_snapshot))
        )
    with nipyapi.utils.rest_exceptions():
        if refresh:
            target_flow = get_flow_in_bucket(
                bucket_id=flow.bucket_identifier, identifier=flow.identifier, identifier_type="id"
            )
        else:
            target_flow = flow
        target_bucket = get_registry_bucket(target_flow.bucket_identifier, "id")
        # The current version of NiFi doesn't ignore link objects passed to it
        bad_params = ["link"]
        for obj in [target_bucket, target_flow]:
            for p in bad_params:
                setattr(obj, p, None)
        nipyapi.utils.validate_parameters_versioning_support(verify_nifi=False)
        ecs = flow_snapshot.external_controller_services
        return nipyapi.registry.BucketFlowsApi().create_flow_version(
            bucket_id=target_bucket.identifier,
            flow_id=target_flow.identifier,
            body=nipyapi.registry.VersionedFlowSnapshot(
                flow=target_flow,
                bucket=target_bucket,
                flow_contents=flow_snapshot.flow_contents,
                parameter_contexts=flow_snapshot.parameter_contexts,
                external_controller_services=ecs,
                snapshot_metadata=VfsMd(
                    version=target_flow.version_count + 1,
                    comments=flow_snapshot.snapshot_metadata.comments,
                    bucket_identifier=target_flow.bucket_identifier,
                    flow_identifier=target_flow.identifier,
                ),
            ),
        )


def get_flow_version(bucket_id, flow_id, version=None, export=False):
    """
    Retrieves the latest, or a specific, version of a Flow

    Args:
        bucket_id (str): the UUID of the bucket containing the Flow
        flow_id (str): the UUID of the Flow to be retrieved from the Bucket
        version (Optional [None, str]): 'None' to retrieve the latest version,
            or a version number as a string to get that version
        export (bool): True to get the raw json object from the server for
            export, False to get the native DataType

    Returns:
        (VersionedFlowSnapshot): If export=False, or the raw json otherwise

    WARNING: This call is impacted by
    https://issues.apache.org/jira/browse/NIFIREG-135
    Which means you sometimes can't trust the version count
    """
    assert isinstance(bucket_id, str)
    assert isinstance(flow_id, str)
    # Version needs to be coerced to str pass API client regex test
    # Even though the client specifies it as Int
    assert version is None or isinstance(version, (str, int))
    assert isinstance(export, bool)
    if version:
        with nipyapi.utils.rest_exceptions():
            out = nipyapi.registry.BucketFlowsApi().get_flow_version(
                bucket_id=bucket_id,
                flow_id=flow_id,
                version_number=str(version),  # This str coercion is intended
                _preload_content=not export,
            )
    else:
        with nipyapi.utils.rest_exceptions():
            out = nipyapi.registry.BucketFlowsApi().get_latest_flow_version(
                bucket_id, flow_id, _preload_content=not export
            )
    if export:
        return out.data
    return out


def export_flow_version(bucket_id, flow_id, version=None, file_path=None, mode="json"):
    """
    Convenience method to export the identified VersionedFlowSnapshot in the
    provided format mode.

    Args:
        bucket_id (str): the UUID of the bucket containing the Flow
        flow_id (str): the UUID of the Flow to be retrieved from the Bucket
        version (Optional [None, Str]): 'None' to retrieve the latest version,
            or a version number as a string to get that version
        file_path (str): The path and filename to write to. Defaults to None
            which returns the serialised obj
        mode (str): 'json' or 'yaml' to specific the encoding format

    Returns:
        (str) of the encoded Snapshot
    """
    assert isinstance(bucket_id, str)
    assert isinstance(flow_id, str)
    assert file_path is None or isinstance(file_path, str)
    assert version is None or isinstance(version, str)
    assert mode in ["yaml", "json"]
    raw_obj = get_flow_version(bucket_id, flow_id, version, export=True)
    export_obj = nipyapi.utils.dump(nipyapi.utils.load(raw_obj), mode)
    if file_path:
        return nipyapi.utils.fs_write(
            obj=export_obj,
            file_path=file_path,
        )
    return export_obj


def import_flow_version(bucket_id, encoded_flow=None, file_path=None, flow_name=None, flow_id=None):
    """
    Imports a given encoded_flow version into the bucket and flow described,
    may optionally be passed a file to read the encoded flow_contents from.

    Note that only one of encoded_flow or file_path, and only one of flow_name
    or flow_id should be specified.

    Args:
        bucket_id (str): UUID of the bucket to write the encoded_flow version
        encoded_flow (Optional [str]): The encoded flow to import; if not
            specified file_path is read from.
        file_path (Optional [str]): The file path to read the encoded flow from
            , if not specified encoded_flow is read from.
        flow_name (Optional [str]): If this is to be the first version in a new
            flow object, then this is the String name for the flow object.
        flow_id (Optional [str]): If this is a new version for an existing flow
            object, then this is the ID of that object.

    Returns:
        The new (VersionedFlowSnapshot)
    """
    # First, decode the flow snapshot contents
    dto = ("registry", "VersionedFlowSnapshot")
    if file_path is None and encoded_flow is not None:
        with nipyapi.utils.rest_exceptions():
            imported_flow = nipyapi.utils.load(encoded_flow, dto=dto)
    elif file_path is not None and encoded_flow is None:
        with nipyapi.utils.rest_exceptions():
            file_in = nipyapi.utils.fs_read(file_path=file_path)
            assert isinstance(file_in, (str, bytes))
            imported_flow = nipyapi.utils.load(obj=file_in, dto=dto)
            assert isinstance(imported_flow, nipyapi.registry.VersionedFlowSnapshot)
    else:
        raise ValueError(
            "Either file_path must point to a file for import, or"
            " flow_snapshot must be an importable object, but"
            "not both"
        )
    # Now handle determining which Versioned Item to write to
    if flow_id is None and flow_name is not None:
        # Case: New flow
        # create the Bucket item
        ver_flow = create_flow(bucket_id=bucket_id, flow_name=flow_name)
    elif flow_name is None and flow_id is not None:
        # Case: New version in existing flow
        ver_flow = get_flow_in_bucket(bucket_id=bucket_id, identifier=flow_id, identifier_type="id")
    else:
        raise ValueError(
            "Either flow_id must be the identifier of a flow to"
            " add this version to, or flow_name must be a unique "
            "name for a flow in this bucket, but not both"
        )
    # Now write the new version
    nipyapi.utils.validate_parameters_versioning_support(verify_nifi=False)
    return create_flow_version(
        flow=ver_flow,
        flow_snapshot=imported_flow,
    )


# pylint: disable=R0913, R0917
def deploy_flow_version(parent_id, location, bucket_id, flow_id, reg_client_id, version=None):
    """
    Deploys a versioned flow as a new process group inside the given parent
    process group. If version is not provided, the latest version will be
    deployed.

    Args:
        parent_id (str): The ID of the parent Process Group to create the
            new process group in.
        location (tuple[x, y]): the x,y coordinates to place the new Process
            Group under the parent
        bucket_id (str): ID of the bucket containing the versioned flow to
            deploy.
        reg_client_id (str): ID of the registry client connection to use.
        flow_id (str): ID of the versioned flow to deploy.
        version (Optional [int,str]): version to deploy, if not provided latest
            version will be deployed.

    Returns:
        (ProcessGroupEntity) of the newly deployed Process Group
    """
    # Default location to (0, 0) if not provided per Issue #342
    location = location or (0, 0)
    assert isinstance(location, tuple)
    # check reg client is valid
    target_reg_client = get_registry_client(reg_client_id, "id")
    # Being pedantic about checking this as API failure errors are terse
    # Using NiFi here to keep all calls within the same API client
    flow_versions = list_flow_versions(
        bucket_id=bucket_id, flow_id=flow_id, registry_id=reg_client_id, service="nifi"
    )
    if not flow_versions:
        raise ValueError(
            "Could not find Flows matching Bucket ID [{0}] and "
            "Flow ID [{1}] on Registry Client [{2}]".format(bucket_id, flow_id, reg_client_id)
        )
    if version is None:
        target_flow = flow_versions.versioned_flow_snapshot_metadata_set
    else:
        target_flow = [
            x
            for x in flow_versions.versioned_flow_snapshot_metadata_set
            if str(x.versioned_flow_snapshot_metadata.version) == str(version)
        ]
    if not target_flow:
        available_versions = [
            str(x.versioned_flow_snapshot_metadata.version)
            for x in flow_versions.versioned_flow_snapshot_metadata_set
        ]
        raise ValueError(
            "Could not find Version [{0}] for Flow [{1}] in Bucket [{2}] on "
            "Registry Client [{3}]. Available versions are: {4}".format(
                str(version), flow_id, bucket_id, reg_client_id, ", ".join(available_versions)
            )
        )
    target_flow = sorted(
        target_flow, key=lambda x: x.versioned_flow_snapshot_metadata.version, reverse=True
    )[0].versioned_flow_snapshot_metadata
    # Issue deploy statement
    with nipyapi.utils.rest_exceptions():
        return nipyapi.nifi.ProcessGroupsApi().create_process_group(
            id=parent_id,
            body=nipyapi.nifi.ProcessGroupEntity(
                revision=nipyapi.nifi.RevisionDTO(version=0),
                component=nipyapi.nifi.ProcessGroupDTO(
                    position=nipyapi.nifi.PositionDTO(x=float(location[0]), y=float(location[1])),
                    version_control_information=VciDTO(
                        bucket_id=target_flow.bucket_identifier,
                        flow_id=target_flow.flow_identifier,
                        registry_id=target_reg_client.id,
                        version=target_flow.version,
                    ),
                ),
            ),
        )
