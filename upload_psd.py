"""
The script will upload all of the PSD files to AWS s3, 
"""
import os
import boto3
import botocore
from dotenv import load_dotenv

load_dotenv()

# Importa las variables de entorno
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")


# Creación de la configuración de AWS
config = botocore.client.Config()

# Creación del cliente de S3
client = boto3.client("s3", config=config)

# Create a container
container_name = "uploadingpsd"
response = client.create_bucket(Bucket=container_name)

# Upload all PSD files from a folder.
for file in os.listdir("../Blackblaze_upload"):
    if file.endswith(".psd"):
        file_name = os.path.join("../Blackblaze_upload", file)
        try:
            with open(file_name, "rb") as f:
                response = client.upload_fileobj(f, container_name, file_name)
        except botocore.exceptions.ClientError as e:
            print(e)

# Check the status of the uploads
for file in os.listdir("../Blackblaze_upload"):
    if file.endswith(".psd"):
        file_name = os.path.join("../Blackblaze_upload", file)
        response = client.get_object(Bucket=container_name, Key=file_name)
        print(response)

# open the terminal in the folder and run the following command: python upload_psd.py to upload the files.
