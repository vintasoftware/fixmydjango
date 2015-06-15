import django_filters


class AllValuesFilterWithEmpty(django_filters.AllValuesFilter):

    def __init__(self, *args, **kwargs):
        self.empty_label = kwargs.pop('empty_label', u'---------')
        super(AllValuesFilterWithEmpty, self).__init__(*args, **kwargs)

    @property
    def field(self):
        field = super(AllValuesFilterWithEmpty, self).field
        field.choices.insert(0, ('', self.empty_label))
        return field
