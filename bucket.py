import os
import s3fs
from dotenv import load_dotenv

load_dotenv()

# Create a Backblaze B2 client
b2 = s3fs.S3FileSystem(
    config={
        "key": os.getenv("APPLICATION_ACCESS_KEY"),
        "secret": os.getenv("APPLICATION_SECRET_KEY"),
    }
)

# Get the bucket
bucket = b2.get("my-bucket")

# Upload all PSD files in the `/Blackblaze_upload` directory
for file in os.listdir("../Blackblaze_upload"):
    if file.endswith(".psd"):
        file_name = os.path.join("../Blackblaze_upload", file)
        with open(file_name, "rb") as f:
            b2.put(f, bucket, file_name)
