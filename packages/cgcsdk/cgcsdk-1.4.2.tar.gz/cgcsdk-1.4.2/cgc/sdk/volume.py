import json as _json
import cgc.sdk.exceptions as _exceptions
import cgc.utils.prepare_headers as _prepare_headers
import cgc.utils.requests_helper as _requests_helper
import cgc.utils.response_utils as _response_utils
from cgc.commands.volume.volume_models import StorageClassList as _StorageClassList
from cgc.commands.volume.data_model import (
    volume_create_payload_validator as _volume_create_payload_validator,
    volume_delete_payload_validator as _volume_delete_payload_validator,
    volume_mount_payload_validator as _volume_mount_payload_validator,
    volume_umount_payload_validator as _volume_umount_payload_validator,
)


def volume_list():
    """
    List all volumes for user namespace.

    Returns:
        dict: Response with code and details containing volumes information

    Raises:
        SDKException: If the API call fails

    Example:
        >>> import cgc.sdk.volume as volume
        >>> response = volume.volume_list()
        >>> if response['code'] == 200:
        ...     print("Volumes:", response['details'])
    """
    api_url, headers = _prepare_headers.get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/storage/volume/list"
    metric = "volume.list"

    __res = _requests_helper.call_api(
        request=_requests_helper.EndpointTypes.get,
        url=url,
        headers=headers,
    )

    return _response_utils.retrieve_and_validate_response_send_metric_for_sdk(
        __res, metric
    )


def volume_storage_class_details(storage_class: str):
    """
    Get details of a storage class.

    Args:
        storage_class (str): Type of disk/storage class

    Returns:
        dict: Response with code and details about the storage class

    Raises:
        SDKException: If the API call fails or storage class is invalid

    Example:
        >>> import cgc.sdk.volume as volume
        >>> response = volume.volume_storage_class_details("standard")
        >>> if response['code'] == 200:
        ...     print("Storage details:", response['details'])
    """
    if not storage_class:
        raise _exceptions.SDKException(-1, "Storage class is required")

    api_url, headers = _prepare_headers.get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/storage/volume/details/{storage_class}"
    metric = "volume.details"

    __res = _requests_helper.call_api(
        request=_requests_helper.EndpointTypes.get,
        url=url,
        headers=headers,
    )

    return _response_utils.retrieve_and_validate_response_send_metric_for_sdk(
        __res, metric
    )


def volume_create(name: str, size: int, storage_class: str = None):
    """
    Create a volume in user namespace.

    Args:
        name (str): Name of the volume
        size (int): Size of volume in GiB (minimum: 1)
        storage_class (str, optional): Type of disk. If not provided, uses default

    Returns:
        dict: Response with code and message about volume creation

    Raises:
        SDKException: If parameters are invalid or API call fails

    Example:
        >>> import cgc.sdk.volume as volume
        >>> response = volume.volume_create("my-volume", 10, "standard")
        >>> if response['code'] == 200:
        ...     print("Volume created successfully")
    """
    if not name:
        raise _exceptions.SDKException(-1, "Volume name is required")
    if not isinstance(size, int) or size < 1:
        raise _exceptions.SDKException(-2, "Volume size must be an integer >= 1")

    if storage_class is None:
        storage_class = _StorageClassList.load_default_storage_class()

    # Validate storage class
    available_classes = _StorageClassList.load_data()
    if storage_class not in available_classes:
        raise _exceptions.SDKException(
            -3, f"Invalid storage class: {storage_class}. Available: {available_classes}"
        )

    api_url, headers = _prepare_headers.get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/storage/volume/create"
    metric = "volume.create"

    __payload = _volume_create_payload_validator(
        name=name, size=size, storage_class=storage_class
    )

    __res = _requests_helper.call_api(
        request=_requests_helper.EndpointTypes.post,
        url=url,
        data=_json.dumps(__payload).encode("utf-8"),
        headers=headers,
    )

    return _response_utils.retrieve_and_validate_response_send_metric_for_sdk(
        __res, metric
    )


def volume_delete(name: str, force: bool = False):
    """
    Delete a specific volume from user namespace.

    Args:
        name (str): Name of the volume to delete
        force (bool, optional): Delete volume even if it is still mounted

    Returns:
        dict: Response with code and message about volume deletion

    Raises:
        SDKException: If volume name is invalid or API call fails

    Example:
        >>> import cgc.sdk.volume as volume
        >>> response = volume.volume_delete("my-volume", force=True)
        >>> if response['code'] == 200:
        ...     print("Volume deleted successfully")
    """
    if not name:
        raise _exceptions.SDKException(-1, "Volume name is required")

    api_url, headers = _prepare_headers.get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/storage/volume/delete"
    metric = "volume.delete"

    __payload = _volume_delete_payload_validator(
        name=name, force_delete=force
    )

    __res = _requests_helper.call_api(
        request=_requests_helper.EndpointTypes.delete,
        url=url,
        data=_json.dumps(__payload).encode("utf-8"),
        headers=headers,
    )

    return _response_utils.retrieve_and_validate_response_send_metric_for_sdk(
        __res, metric
    )


def volume_mount(
    name: str,
    target: str,
    start_mount_path: str = None,
    full_mount_path: str = None
):
    """
    Mount a volume to a specific template.

    Args:
        name (str): Name of the volume to mount
        target (str): Name of the template to mount volume to
        start_mount_path (str, optional): Path to mount volume under (not default)
        full_mount_path (str, optional): Specifies full mount path (can lead to errors)

    Returns:
        dict: Response with code and message about volume mounting

    Raises:
        SDKException: If required parameters are missing or API call fails

    Example:
        >>> import cgc.sdk.volume as volume
        >>> response = volume.volume_mount("my-volume", "my-compute")
        >>> if response['code'] == 200:
        ...     print("Volume mounted successfully")
    """
    if not name:
        raise _exceptions.SDKException(-1, "Volume name is required")
    if not target:
        raise _exceptions.SDKException(-2, "Target template name is required")

    api_url, headers = _prepare_headers.get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/storage/volume/mount"
    metric = "volume.mount"

    __payload = _volume_mount_payload_validator(
        name=name,
        target=target,
        start_mount_path=start_mount_path,
        full_mount_path=full_mount_path,
    )

    __res = _requests_helper.call_api(
        request=_requests_helper.EndpointTypes.post,
        url=url,
        data=_json.dumps(__payload).encode("utf-8"),
        headers=headers,
    )

    return _response_utils.retrieve_and_validate_response_send_metric_for_sdk(
        __res, metric
    )


def volume_umount(name: str, target_template_names: list = None):
    """
    Unmount a volume from compute resources.

    Args:
        name (str): Name of the volume to unmount
        target_template_names (list, optional): List of template names to unmount from.
                                              If None or empty, unmounts from all resources.
        force (bool, optional): Force unmount even if resources are not responding

    Returns:
        dict: Response with code and message about volume unmounting

    Raises:
        SDKException: If volume name is missing or API call fails

    Example:
        >>> import cgc.sdk.volume as volume
        >>> # Unmount from all resources
        >>> response = volume.volume_umount("my-volume")
        >>> # Unmount from specific resources
        >>> response = volume.volume_umount("my-volume", ["compute1", "compute2"])
        >>> # Force unmount
        >>> response = volume.volume_umount("my-volume", force=True)
        >>> if response['code'] == 200:
        ...     print("Volume unmounted successfully")
    """
    if not name:
        raise _exceptions.SDKException(-1, "Volume name is required")

    if target_template_names is None:
        target_template_names = []

    api_url, headers = _prepare_headers.get_api_url_and_prepare_headers()
    url = f"{api_url}/v1/api/storage/volume/umount"
    metric = "volume.umount"

    __payload = _volume_umount_payload_validator(
        name=name, target_template_names=target_template_names
    )

    __res = _requests_helper.call_api(
        request=_requests_helper.EndpointTypes.post,
        url=url,
        data=_json.dumps(__payload).encode("utf-8"),
        headers=headers,
    )

    return _response_utils.retrieve_and_validate_response_send_metric_for_sdk(
        __res, metric
    )


def volume_ready(name: str) -> bool:
    """
    Check if a volume is ready (bound and available).

    Args:
        name (str): Name of the volume to check

    Returns:
        bool: True if volume is ready, False otherwise

    Raises:
        SDKException: If volume name is missing or API call fails

    Example:
        >>> import cgc.sdk.volume as volume
        >>> if volume.volume_ready("my-volume"):
        ...     print("Volume is ready for use")
        ... else:
        ...     print("Volume is not ready yet")
    """
    if not name:
        raise _exceptions.SDKException(-1, "Volume name is required")

    try:
        response = volume_list()
        if response['code'] != 200:
            return False

        volumes = response.get('details', {}).get('volume_list', [])
        for vol in volumes:
            if vol.get('name') == name:
                status = vol.get('status', '').lower()
                return status == 'bound'

        return False

    except Exception:
        return False


def get_available_storage_classes() -> list:
    """
    Get list of available storage classes.

    Returns:
        list: List of available storage class names

    Example:
        >>> import cgc.sdk.volume as volume
        >>> storage_classes = volume.get_available_storage_classes()
        >>> print("Available storage classes:", storage_classes)
    """
    try:
        return _StorageClassList.load_data()
    except Exception:
        return []


def get_default_storage_class() -> str:
    """
    Get the default storage class.

    Returns:
        str: Default storage class name

    Example:
        >>> import cgc.sdk.volume as volume
        >>> default_class = volume.get_default_storage_class()
        >>> print("Default storage class:", default_class)
    """
    try:
        return _StorageClassList.load_default_storage_class()
    except Exception:
        return ""