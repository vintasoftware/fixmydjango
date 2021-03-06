# coding: utf-8

from model_utils import Choices

DJANGO_VERSIONS = Choices(
    ('1.2', '1.2'),
    ('1.3', '1.3'),
    ('1.4', '1.4'),
    ('1.5', '1.5'),
    ('1.6', '1.6'),
    ('1.7', '1.7'),
    ('1.8', '1.8'),
    ('1.9', '1.9'),
    ('1.10', '1.10'),
    ('1.11', '1.11'),
)


ERROR_POST_DATA_CAME_FROM = Choices(
    ('lib', 'Lib'),
    ('site', 'Site'),
)
