import os
import logging
from typing import Optional, Union
import uuid
import aioboto3
import aiofiles
from .base import BlobStorageClient
from botocore.exceptions import ClientError

class AWSBlobStorageClient(BlobStorageClient):
    def __init__(self, container_name: Optional[str] = None):
        super().__init__(container_name=container_name)        
        self.region = os.getenv("AWS_REGION", "eu-west-1")
        self.endpoint_url = os.getenv("BLOB_STORAGE_ENDPOINT_URL")
        self.session = aioboto3.Session()

    def the_container_name(self, container_name: Optional[str] = None) -> str:
        if container_name:
            return container_name
        return self.container_name
    
    async def download_blob(self, remote_path: str, local_dir: str, make_unique=False, container_name: Optional[str] = None) -> str:
        filename = os.path.basename(remote_path)
        if make_unique:
            filename = f"{uuid.uuid4()}_{filename}"
        local_path = os.path.join(local_dir, filename)

        async with self.session.client("s3", region_name=self.region, endpoint_url=self.endpoint_url) as s3:
            try:
                response = await s3.get_object(Bucket=self.the_container_name(container_name), Key=remote_path)
                content = await response["Body"].read()
                async with aiofiles.open(local_path, "wb") as f:
                    await f.write(content)
                logging.info(f"Downloaded {remote_path} to {local_path}")
                return local_path
            except Exception as e:
                logging.error(f"Error downloading {remote_path}: {e}")
                raise

    async def upload_blob(self, remote_path: str, content: Union[str, bytes], container_name: Optional[str] = None) -> str:
        if isinstance(content, str):
            content = content.encode("utf-8")

        async with self.session.client("s3", region_name=self.region, endpoint_url=self.endpoint_url) as s3:
            try:
                await s3.put_object(Bucket=self.the_container_name(container_name), Key=remote_path, Body=content)
                logging.info(f"Uploaded {remote_path}")
                return remote_path
            except Exception as e:
                logging.error(f"Error uploading {remote_path}: {e}")
                raise
    
    async def blob_exists(self, remote_path: str, container_name: Optional[str] = None) -> bool:
        async with self.session.client(
            "s3",
            region_name=self.region,
            endpoint_url=self.endpoint_url           
        ) as client:
            try:
                await client.head_object(Bucket=self.the_container_name(container_name), Key=remote_path)
                return True
            except ClientError as e:
                if e.response["Error"]["Code"] in ("404", "NoSuchKey"):
                    return False
                logging.error(f"Error checking object exists: {e}")
                return False

    async def fetch_blob_content(self, remote_path: str, container_name: Optional[str] = None) -> str:
        async with self.session.client(
            "s3",
            region_name=self.region,
            endpoint_url=self.endpoint_url            
        ) as client:
            try:
                resp = await client.get_object(Bucket=self.the_container_name(container_name), Key=remote_path)
                data = await resp["Body"].read()
                return data.decode("utf-8")
            except ClientError as e:
                logging.error(f"Error fetching object content: {e}")
                raise

    async def close(self):
        # aioboto3 Sessions don’t need explicit close,
        # but if you stored any client references, you can close them here.
        pass