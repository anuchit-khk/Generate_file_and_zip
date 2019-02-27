import os
import json
import zipfile
import logging
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials


def oat(pathed, version):
    print(pathed)
    if not os.path.exists(pathed):
        os.makedirs(pathed)
        print("version is "+version)
        file = open("C:/Users/Anuchit/Desktop/kowoatkowoatz/oat.txt", "w")
        file.write(version)
        file.close()
        print ("Generated !!")
    else:
        print("Directory already exists")

def zipdir(path, zipf):
    for folder, subfolders, files in os.walk(path):
        for file in files:
            if file.endswith('.txt'):
                zipf.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), path ), compress_type = zipfile.ZIP_DEFLATED)
                zipf.printdir()
    zipf.close()

def get_storage_client():
    google_api_secret = json.load(open('TRUE-DMP-8b90a0152082.json'))
    credentials_dict = {
        'type': 'service_account',
        'client_id': google_api_secret['client_id'],
        'client_email': google_api_secret['client_email'],
        'private_key': google_api_secret['private_key'],
        'private_key_id': google_api_secret['private_key_id']
    }
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        credentials_dict
    )
    storage_client = storage.Client(credentials=credentials, project='true-dmp')
    return storage_client

def gcs_dowload_file(gcs_bucket, target, destination):
    client = get_storage_client()
    bucket = client.get_bucket(gcs_bucket)
    blob = bucket.get_blob(target)
    print(blob)
    blob.download_to_filename(destination)
    log.info("Downloaded")

def gcs_upload_file(gcs_bucket, filename, bucket_filename):
    client2 = get_storage_client()
    bucket2 = client2.get_bucket(gcs_bucket)
    blob2 = bucket2.blob(bucket_filename)
    blob2.upload_from_filename(filename)
    log.info("Uploaded")