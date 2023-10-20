"""The script will upload all of the PSD files to Backblaze, 
setting the content-type to image/vnd.adobe.photoshop."""

import os
import backblaze_b2

b2 = backblaze_b2.B2()

# Replace the following with your Backblaze credentials
# You can find your Backblaze credentials in the Backblaze console
account_id = ""
api_key = ""

# Replace the following with the name of the Backblaze bucket you want to upload the files to
bucket_name = "my-bucket"

# Get a list of all the PSD files in the current folder
psd_files = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".psd"):
            psd_files.append(os.path.join(root, file))

# Upload each PSD file to Backblaze
for psd_file in psd_files:
    with open(psd_file, "rb") as f:
        file_data = f.read()

    b2.upload_file(
        bucket_name,
        psd_file,
        file_data,
        content_type="image/vnd.adobe.photoshop",
    )

print("All PSD files have been uploaded to Backblaze.")

# open the terminal in the folder and run the following command: python backblaze_upload.py
