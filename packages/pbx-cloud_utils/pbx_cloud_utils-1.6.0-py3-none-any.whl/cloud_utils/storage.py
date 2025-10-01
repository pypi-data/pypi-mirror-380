from __future__ import annotations

import os
from abc import ABC, abstractmethod
from typing import IO, Any, Callable, Iterable

import boto3
from azure.core.exceptions import AzureError
from azure.storage.blob import BlobClient, ContainerClient, ContentSettings
from botocore.exceptions import BotoCoreError, ClientError
from google.cloud import storage as gcs_storage

from cloud_utils import exceptions
from cloud_utils.const import GOOGLE_BUCKET_API_URL
from cloud_utils.types import (
    azure_storage_class_map,
    gcs_storage_class_map,
    s3_storage_class_map,
)

BotoError = (BotoCoreError, ClientError)


class StorageObject(ABC):
    provider_storage_class_map: dict[str, str]
    pbx_storage_class_map: dict[str, str]

    def __new__(cls, *args):
        new = super().__new__(cls)
        new.pbx_storage_class_map = {v: k for k, v in cls.provider_storage_class_map.items()}
        return new

    def __init__(self, client) -> None:
        super().__init__()
        self.client = client

    @property
    @abstractmethod
    def path(self):
        pass

    @property
    @abstractmethod
    def bucket_name(self) -> str:
        pass

    @property
    @abstractmethod
    def content_length(self) -> int:
        pass

    @property
    @abstractmethod
    def checksum(self) -> str:
        pass

    @abstractmethod
    def exists(self) -> bool:
        pass

    @abstractmethod
    def download(self, stream: IO) -> None:
        pass

    @abstractmethod
    def upload(self, content: Iterable | IO, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def read(self) -> bytes | str:
        pass

    @abstractmethod
    def set_storage_class(self, storage_class: str) -> None:
        pass

    @property
    def storage_class(self) -> str:
        return self.pbx_storage_class_map[self._provider_storage_class]

    @property
    @abstractmethod
    def _provider_storage_class(self) -> str:
        pass

    @property
    @abstractmethod
    def content_type(self) -> str:
        pass


class AmazonS3Object(StorageObject):
    provider_storage_class_map: dict[str, str] = s3_storage_class_map

    @property
    def path(self):
        return self.client.key

    @property
    def bucket_name(self) -> str:
        return self.client.bucket_name

    @property
    def content_length(self) -> int:
        return self.client.content_length

    @property
    def checksum(self) -> str:
        return self.client.e_tag.strip('"')

    @property
    def content_type(self) -> str:
        return self.client.content_type

    def exists(self) -> bool:
        try:
            self.client.load()
        except ClientError:
            return False
        else:
            return True

    def download(self, stream: IO) -> None:
        try:
            self.client.download_fileobj(stream)
        except BotoError as e:
            raise exceptions.StorageError(e)

    def read(self) -> bytes | str:
        try:
            obj = self.client.get()
            return obj["Body"].read()
        except BotoError as e:
            raise exceptions.StorageError(e) from e

    def upload(self, content: Iterable | IO, **kwargs: Any) -> None:
        client_kwargs = {"Body": content}
        if content_type := kwargs.get("content_type"):
            client_kwargs["ContentType"] = content_type
        if acl := kwargs.get("acl"):
            client_kwargs["ACL"] = acl
        if storage_class := kwargs.get("storage_class"):
            client_kwargs["StorageClass"] = self.provider_storage_class_map[storage_class]

        try:
            self.client.put(**client_kwargs)
        except BotoError as e:
            raise exceptions.StorageError() from e

    def set_storage_class(self, storage_class: str) -> None:
        self.client.copy(
            {"Bucket": self.bucket_name, "Key": self.path},
            ExtraArgs={
                "StorageClass": self.provider_storage_class_map[storage_class],
                "MetadataDirective": "COPY",
                "ACL": "bucket-owner-full-control",
            },
        )

    @property
    def _provider_storage_class(self) -> str:
        return self.client.storage_class or "STANDARD"


class AzureBlobObject(StorageObject):
    provider_storage_class_map: dict[str, str] = azure_storage_class_map

    @property
    def path(self):
        return self.client.blob_name

    @property
    def bucket_name(self) -> str:
        return self.client.container_name

    @property
    def content_length(self) -> int:
        return self.client.get_blob_properties()["size"]

    @property
    def checksum(self) -> str:
        return self.client.get_blob_properties().content_settings.content_md5.hex()

    @property
    def content_type(self) -> str:
        return self.client.get_blob_properties().content_settings.content_type

    def exists(self) -> bool:
        return self.client.exists()

    def download(self, stream: IO) -> None:
        try:
            self.client.download_blob().readinto(stream)
        except AzureError as e:
            raise exceptions.StorageError(e) from e

    def read(self) -> bytes | str:
        try:
            return self.client.download_blob().readall()
        except AzureError as e:
            raise exceptions.StorageError(e) from e

    def upload(self, content: Iterable | IO, **kwargs: Any) -> None:
        content_type = kwargs.get("content_type")
        content_settings = ContentSettings(content_type=content_type)
        try:
            self.client.upload_blob(
                content,
                overwrite=True,
                content_settings=content_settings,
            )
        except AzureError as e:
            raise exceptions.StorageError(e)

    def set_storage_class(self, storage_class: str) -> None:
        self.client.set_standard_blob_tier(self.provider_storage_class_map[storage_class])

    @property
    def _provider_storage_class(self) -> str:
        return self.client.get_blob_properties()["blob_tier"]


class HybridGoogleCloudStorageObject(AmazonS3Object):
    provider_storage_class_map: dict[str, str] = gcs_storage_class_map

    def __init__(self, client, gcs_client: gcs_storage.Bucket) -> None:
        super().__init__(client)
        self.gcs_client = gcs_client
        self.blob = self.gcs_client.get_blob(self.path)

    @property
    def _provider_storage_class(self) -> str:
        return self.blob.storage_class

    def set_storage_class(self, storage_class: str) -> None:
        destination_storage_class = self.provider_storage_class_map[storage_class]
        self.blob.update_storage_class(destination_storage_class)


class Storage(ABC):
    object_class: type[StorageObject]

    def get_object(self, path: str) -> StorageObject:
        object_client = self.object_client_class(path)
        return self.object_class(object_client)

    def upload_object(self, path: str, content: Iterable | IO, **kwargs: Any) -> StorageObject:
        object_client = self.object_client_class(path)
        created_object = self.object_class(object_client)
        created_object.upload(content, **kwargs)
        return created_object

    @abstractmethod
    def find_object_names(self, prefix: str) -> Iterable[str]:
        pass

    @property
    @abstractmethod
    def object_client_class(self):
        pass


class AmazonS3Storage(Storage):
    object_class: type[StorageObject] = AmazonS3Object

    def __init__(self, bucket_name: str, region_name: str, **kwargs: Any) -> None:
        self.bucket_name: str = bucket_name
        self.region_name: str = region_name
        self.bucket = self._get_bucket(**kwargs)

    @property
    def object_client_class(self):
        return self.bucket.Object

    def find_object_names(self, prefix: str) -> Iterable[str]:
        return (item.key for item in self.bucket.objects.filter(Prefix=prefix))

    def _get_bucket(self, **kwargs: Any):
        aws_access_key_id = kwargs.get(
            "aws_access_key_id",
            os.environ.get("AWS_ACCESS_KEY_ID"),
        )
        aws_secret_access_key = kwargs.get(
            "aws_secret_access_key",
            os.environ.get("AWS_SECRET_ACCESS_KEY"),
        )

        s3_kwargs = {"region_name": self.region_name}

        if aws_access_key_id and aws_secret_access_key:
            s3_kwargs["aws_access_key_id"] = aws_access_key_id
            s3_kwargs["aws_secret_access_key"] = aws_secret_access_key

        s3 = boto3.resource("s3", **kwargs)
        return s3.Bucket(self.bucket_name)


class AzureBlobStorage(Storage):
    object_class: type[StorageObject] = AzureBlobObject

    def __init__(self, container_name: str, **kwargs: Any) -> None:
        connection_string = kwargs.get(
            "conn_str",
            os.environ.get("AZURE_STORAGE_CONNECTION_STRING", ""),
        )
        self.client: ContainerClient = ContainerClient.from_connection_string(
            conn_str=connection_string, container_name=container_name
        )

    @property
    def object_client_class(
        self,
    ) -> Callable[..., BlobClient]:
        return self.client.get_blob_client

    def find_object_names(self, prefix: str) -> Iterable[str]:
        return (item.name for item in self.client.list_blobs(name_starts_with=prefix))


class HybridGoogleCloudStorage(AmazonS3Storage):
    object_class = HybridGoogleCloudStorageObject

    def __init__(
        self, bucket_name: str, region_name: str, gcs_project: str = "", **kwargs: Any
    ) -> None:
        kwargs["endpoint_url"] = kwargs.get("endpoint_url", GOOGLE_BUCKET_API_URL)
        super().__init__(bucket_name, region_name, **kwargs)
        self.gcs_project = gcs_project or os.environ.get("GCS_PROJECT_ID")
        gcs_storage_client_kwargs = {
            key.removeprefix("gcs_"): value
            for key, value in kwargs.items()
            if key.startswith("gcs_")
        }
        self.gcs_client = self.get_gcs_bucket_client(**gcs_storage_client_kwargs)

    def get_gcs_bucket_client(self, **kwargs: Any) -> gcs_storage.Bucket:
        gcs_storage_client = gcs_storage.Client(project=self.gcs_project, **kwargs)
        return gcs_storage_client.bucket(self.bucket_name)

    def get_object(self, path: str) -> HybridGoogleCloudStorageObject:
        object_client = self.object_client_class(path)
        return self.object_class(object_client, self.gcs_client)
