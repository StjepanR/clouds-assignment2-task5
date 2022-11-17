# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import os
import logging
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import azure.identity
import azure.storage.blob

connect_str = "DefaultEndpointsProtocol=https;AccountName=task5function;AccountKey=2PZSbN9M0WuKEPIdtAY8WWGUS2PRuYyicO/3xLxBjuhcoVqQLubuWaeP4hfidYZl5cAkn/yOFViR+AStsiOeZQ==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

container_client = blob_service_client.get_container_client(container="input") 

def main(name: str) -> list[dict[int, str]]:

    output = []

    for blob in container_client.list_blobs():
        file = {}

        data = container_client.download_blob(blob.name).readall().decode("utf-8")

        for i, line in enumerate(data.split("\r\n")):
            file[i] = line
        
        output.append(file)


    return output

