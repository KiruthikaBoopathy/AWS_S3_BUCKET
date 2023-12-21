import boto3
from botocore.exceptions import NoCredentialsError
from urllib.parse import quote
import os

ACCESS_KEY = 'AKIARRDRMAIAULU3EV64'
SECRET_KEY = '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'


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    try:
        # s3.upload_file(local_file, bucket, s3_file)
        # print("Upload Successful")
        # return True
        with open(local_file, 'rb') as data:
            s3.put_object(Bucket=bucket, Key=s3_file, Body=data)
        print(f"Successfully uploaded {local_file} to {bucket}/{s3_file}")
        print(data)
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = upload_to_aws(r"C:\Users\Vrdella\Downloads\123015036_JAYSHRI_PICKYOURTAIL.pdf", 's3buckett01',
                         'resume_file/Resume')


def download_from_aws(bucket, s3_file, local_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

    try:
        s3.download_file(bucket, s3_file, local_file)
        print("Download Successful")
        return True
    except FileNotFoundError:
        print("The file was not found on S3")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


# downloaded = download_from_aws('s3buckett01', 'resume_file/resume', 'local_resume.pdf')


def get_url(Bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    try:
        s3.get_object(Bucket, s3_file)
        s3_url = f"https://{Bucket}.s3.amazonaws.com/{quote(s3_file)}"
        print("S3 URL:", s3_url)
        return True
    except FileNotFoundError:
        print("The file was not found on S3")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

# url = get_url('s3buckett01','Resume_file/resume')
