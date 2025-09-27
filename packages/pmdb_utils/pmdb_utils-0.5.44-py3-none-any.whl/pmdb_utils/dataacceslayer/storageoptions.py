import os


class StorageOptions:
    """
    Configuration class for AWS/MinIO storage credentials and endpoints.
    Allows initialization from arguments or environment variables.
    """

    def __init__(
        self,
        access_key_id=None,
        secret_access_key=None,
        endpoint_url=None,
        allow_http="true",
    ):
        """
        Initialize DeltaStorageOptions.
        Args:
            aws_access_key_id (str, optional): AWS access key ID. Defaults to None.
            aws_secret_access_key (str, optional): AWS secret access key. Defaults to None.
            aws_endpoint_url (str, optional): AWS/MinIO endpoint URL. Defaults to None.
            region (str, optional): AWS region. Defaults to None.
            allow_http (str, optional): Allow HTTP connections. Defaults to "true".
        """
        self.access_key_id = access_key_id or os.getenv("MINIO_ROOT_USER")
        self.secret_access_key = secret_access_key or os.getenv("MINIO_ROOT_PASSWORD")
        self.endpoint_url = endpoint_url or os.getenv("MINIO_ENDPOINT_URL")
        self.allow_http = allow_http

    @property
    def minio(self) -> dict:
        """
        Return a dictionary of credentials and endpoint for MinIO/AWS SDKs.
        Returns:
            dict: Dictionary with keys 'aws_access_key_id', 'aws_secret_access_key', 'endpoint_url', 'allow_http'.
        """
        if (
            not self.access_key_id
            or not self.secret_access_key
            or not self.endpoint_url
        ):
            raise ValueError("AWS credentials and endpoint URL must be provided.")
        return {
            "aws_access_key_id": self.access_key_id,
            "aws_secret_access_key": self.secret_access_key,
            "endpoint_url": self.endpoint_url,
            "allow_http": self.allow_http,
        }
