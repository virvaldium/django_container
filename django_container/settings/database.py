from django_container.common.configurations import StringValue


class DatabaseMixin(object):
    DATABASE_HOST = StringValue()
    DATABASE_NAME = StringValue()
    DATABASE_USER = StringValue()
    DATABASE_PASSWORD = StringValue()

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': DATABASE_NAME,
            'USER': DATABASE_USER,
            'PASSWORD': DATABASE_PASSWORD,
            'HOST': DATABASE_HOST,
            'PORT': '5432',
        }
    }
