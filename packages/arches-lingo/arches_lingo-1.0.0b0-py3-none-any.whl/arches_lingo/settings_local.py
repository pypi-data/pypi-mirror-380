# ES setting to connect to arches dev dependencies
ELASTICSEARCH_HTTP_PORT = 9202  # this should be in increments of 200, eg: 9400, 9600, 9800
ELASTICSEARCH_HOSTS = [{"scheme": "http", "host": "localhost", "port": ELASTICSEARCH_HTTP_PORT}]
CELERY_BROKER_URL = "amqp://localhost:5674/"
DEBUG = True

ALLOWED_HOSTS = ["*"]
PUBLIC_SERVER_ADDRESS = "http://127.0.0.1:8000/"

DATABASES = {
    "default": {
        "ATOMIC_REQUESTS": False,
        "AUTOCOMMIT": True,
        "CONN_MAX_AGE": 0,
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "HOST": "localhost",
        "NAME": "arches_lingo",
        "OPTIONS": {},
        "PASSWORD": "postgis",
        "PORT": "5432",
        "POSTGIS_TEMPLATE": "template_postgis",
        "TEST": {
            "CHARSET": None,
            "COLLATION": None,
            "MIRROR": None,
            "NAME": None
        },
        "TIME_ZONE": None,
        "USER": "postgres"
    }
}

OAUTH_CLIENT_ID = "YDi2UvOiHXnpwHo5RM5xxFqvqAHidM3bA3ukFqGs"


from django.utils.translation import gettext_lazy as _
# see https://docs.djangoproject.com/en/1.9/topics/i18n/translation/#how-django-discovers-language-preference
# to see how LocaleMiddleware tries to determine the user"s language preference
# (make sure to check your accept headers as they will override the LANGUAGE_CODE setting!)
# also see get_language_from_request in django.utils.translation.trans_real.py
# to see how the language code is derived in the actual code

####### TO GENERATE .PO FILES DO THE FOLLOWING ########
# run the following commands
# language codes used in the command should be in the form (which is slightly different
# form the form used in the LANGUAGE_CODE and LANGUAGES settings below):
# --local={countrycode}_{REGIONCODE} <-- countrycode is lowercase, regioncode is uppercase, also notice the underscore instead of hyphen
# commands to run (to generate files for "British English, German, and Spanish"):
# django-admin.py makemessages --ignore=env/* --local=de --local=en --local=en_GB --local=es  --extension=htm,py
# django-admin.py compilemessages


# default language of the application
# language code needs to be all lower case with the form:
# {langcode}-{regioncode} eg: en, en-gb ....
# a list of language codes can be found here http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en"

# list of languages to display in the language switcher,
# if left empty or with a single entry then the switch won"t be displayed
# language codes need to be all lower case with the form:
# {langcode}-{regioncode} eg: en, en-gb ....
# a list of language codes can be found here http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGES = [
    ("en", _("English")),
    # ("de", _("German")),
    # ("en-gb", _("British English")),
    # ("es", _("Spanish")),
]

# override this to permenantly display/hide the language switcher
SHOW_LANGUAGE_SWITCH = len(LANGUAGES) > 1


REFERENCES_INDEX_NAME = "references"
ELASTICSEARCH_CUSTOM_INDEXES = [
    {
        "module": "arches_controlled_lists.search_indexes.reference_index.ReferenceIndex",
        "name": REFERENCES_INDEX_NAME,
        "should_update_asynchronously": True,
    }
]

# BYPASS_REQUIRED_VALUE_TILE_VALIDATION = True