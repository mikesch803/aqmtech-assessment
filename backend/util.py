import boto3
import os
from uuid import uuid4

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

print("BUCKET:", os.getenv("AWS_S3_BUCKET"))
print("REGION:", os.getenv("AWS_REGION"))


BUCKET_NAME = os.getenv("AWS_S3_BUCKET")


def upload_image_to_s3(file):
    file_ext = file.filename.split(".")[-1]
    s3_key = f"images/{uuid4()}.{file_ext}"

    s3.upload_fileobj(
        file.file,
        BUCKET_NAME,
        s3_key,
        ExtraArgs={
            "ContentType": file.content_type
        },
    )

    return f"https://{BUCKET_NAME}.s3.{os.getenv('AWS_REGION')}.amazonaws.com/{s3_key}"

