from meta.views import MetadataMixin


class CustomMetadataMixin(MetadataMixin):
    site_name = 'Fix My Django'
    image = 'https://s3.amazonaws.com/fixmydjango/fixmydjango-ogimage.png'
    twitter_card = 'summary'
    twitter_site = '@vintasoftware'
    twitter_creator = '@vintasoftware'
