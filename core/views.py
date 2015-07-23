from django.views import generic


class ErrorView404(generic.TemplateView):
    template_name = '404.html'
