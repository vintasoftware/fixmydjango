from compressor.filters.css_default import CssAbsoluteFilter
from compressor.utils import staticfiles
from django_libsass import SassCompiler


# based on: http://stackoverflow.com/a/17033883/145349
class CustomCssAbsoluteFilter(CssAbsoluteFilter):

    def find(self, basename):
        if basename and staticfiles.finders:
            return staticfiles.finders.find(basename)


# fix issue in localhost: https://github.com/django-compressor/django-compressor/issues/226
class PatchedSCSSCompiler(SassCompiler):

    def input(self, **kwargs):
        content = super(PatchedSCSSCompiler, self).input(**kwargs)
        return CustomCssAbsoluteFilter(content).input(**kwargs)
