# coding: utf-8

from django.core.files.storage import get_storage_class

from storages.backends.s3boto import S3BotoStorage


# based in: http://django-compressor.readthedocs.org/en/1.3/remote-storages/
class CachedS3BotoStorage(S3BotoStorage):

    def __init__(self, *args, **kwargs):
        super(CachedS3BotoStorage, self).__init__(*args, **kwargs)
        # self.local_storage = get_storage_class(
        #     "compressor.storage.CompressorFileStorage")()

    def _save(self, name, content):
        name = super(CachedS3BotoStorage, self)._save(name, content)
        # self.local_storage._save(name, content)
        return name


class StaticCachedS3BotoStorage(CachedS3BotoStorage):

    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'static'
        kwargs['querystring_auth'] = False

        super(StaticCachedS3BotoStorage, self).__init__(*args, **kwargs)


class MediaS3BotoStorage(S3BotoStorage):

    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'media'
        kwargs['querystring_auth'] = True
        kwargs['acl'] = 'private'

        super(MediaS3BotoStorage, self).__init__(*args, **kwargs)
