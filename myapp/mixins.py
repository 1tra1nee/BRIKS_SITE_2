
class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['title'] = 'Регистрация'
        return context