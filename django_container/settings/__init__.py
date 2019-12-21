import os

from configurations import Configuration

from django_container.settings.apps import AppsMixin
from django_container.settings.database import DatabaseMixin
from django_container.settings.path import PathMixin


class Common(AppsMixin, DatabaseMixin, PathMixin, Configuration):
    @classmethod
    def pre_setup(cls):
        cls.DOTENV = os.path.join(cls.BASE_DIR, '.env')
        super(Common, cls).pre_setup()


class Dev(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = True
