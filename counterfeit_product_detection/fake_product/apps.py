from django.apps import AppConfig


class FakeProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fake_product'
