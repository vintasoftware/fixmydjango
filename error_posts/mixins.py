from core.mixins import CustomMetadataMixin


class ErrorPostListMetadataMixin(CustomMetadataMixin):
    object_type = 'website'

    def get_meta_description(self, context):
        return ("Fix my Django shows information about "
                "common Django exceptions and how to fix them")


class ErrorPostMetadataMixin(CustomMetadataMixin):
    object_type = 'article'

    def get_meta_description(self, context):
        error_post = context['errorpost']
        return 'Solution to the exception {}: {}'.format(
            error_post.exception_type,
            error_post.error_message)
