from decouple import Csv, config
from dj_database_url import parse as db_url

from .base import *  # noqa


DEBUG = False

SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    'default': config('DATABASE_URL', cast=db_url),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Add sentry to installed apps
INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]

SERVER_EMAIL = 'sohaibfarooqi@hotmail.com'

# Production email config
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = config('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = config('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_HTTPONLY = True

# django-log-request-id
MIDDLEWARE.insert(  # insert RequestIDMiddleware on the top
    0, 'log_request_id.middleware.RequestIDMiddleware')

# Sentry 404 middleware
MIDDLEWARE = (
    'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware'
) + MIDDLEWARE

# Sentry error handling middleware
MIDDLEWARE.insert(
    0, 'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware'
)
LOG_REQUEST_ID_HEADER = 'HTTP_X_REQUEST_ID'
LOG_REQUESTS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'request_id': {
            '()': 'log_request_id.filters.RequestIDFilter'
        },
    },
    'formatters': {
        'standard': {
            'format': '%(levelname)-8s [%(asctime)s] [%(request_id)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'filters': ['request_id'],
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO'
        },
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'log_request_id.middleware': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}
