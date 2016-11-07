from model_mommy.recipe import Recipe, seq


django_traceback = '''Traceback (most recent call last):
  File "python2.7/site-packages/django/core/handlers/base.py", line 139, in get_response
    response = response.render()
  File "python2.7/site-packages/django/template/response.py", line 105, in render
    self.content = self.rendered_content
  File "python2.7/site-packages/django/template/response.py", line 80, in rendered_content
    template = self.resolve_template(self.template_name)
  File "python2.7/site-packages/django/template/response.py", line 56, in resolve_template
    return loader.select_template(template)
  File "python2.7/site-packages/django/template/loader.py", line 186, in select_template
    raise TemplateDoesNotExist(', '.join(not_found))
TemplateDoesNotExist: none.html'''

published_recipe = Recipe(
    'error_posts.ErrorPost',
    is_published=True,
    slug=seq('slug'),
    parsed_traceback={},
    traceback=django_traceback,
)

non_published_recipe = Recipe(
    'error_posts.ErrorPost',
    is_published=False,
    slug=seq('slug'),
    parsed_traceback={},
    traceback=django_traceback,
)
