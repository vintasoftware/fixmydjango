from storages.backends.s3boto import S3BotoStorage


class StaticS3BotoStorage(S3BotoStorage):
    location = 'static'
    querystring_auth = False


class MediaS3BotoStorage(S3BotoStorage):
    location = 'media'
    querystring_auth = False
