import boto3

from decouple import config


class S3Service:
    def __init__(self):
        self.s3 = boto3.resource(
            "s3",
            aws_access_key_id=config("AWS_KEY"),
            aws_secret_access_key=config("AWS_SECRET"),
        )

    def upload_file(self, file_path, file_name, bucket=None, region=None):
        if not bucket:
            bucket = config("BUCKET_NAME")

        if not region:
            region = config("BUCKET_REGION")

        self.s3.meta.client.upload_file(file_path, bucket, file_name)

        return (
            f"https://{bucket}.s3.{region}.amazonaws.com/{file_name}"
        )
