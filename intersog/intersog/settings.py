import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1vb=t8=_lk7kqjrzm3=z@2t39i5!*setfko9ueqb@_hs8af*n)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'chat',
    'conference',
    'extuser',
    'swampdragon',
    'cuser'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'cuser.middleware.CuserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'intersog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR, 'common/templates'), 
                os.path.join(BASE_DIR, 'blog/templates'), 
                os.path.join(BASE_DIR, 'chat/templates'),
                os.path.join(BASE_DIR, 'conference/templates'),
                os.path.join(BASE_DIR, 'extuser/templates')
                ],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'intersog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'intersog',
        'USER': 'networkcom',
        'PASSWORD': 'AcidBurn',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]  


AUTH_USER_MODEL = 'extuser.User' 

LOGIN_URL = '/accounts/login/'

LOGOUT_URL = '/accounts/logout/'

LOGIN_REDIRECT_URL = '/conf/list'

# The number of days a password reset link is valid for
PASSWORD_RESET_TIMEOUT_DAYS = 3  

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  

#SWAMP_DRAGON_CONNECTION = ('swampdragon.connections.sockjs_connection.DjangoSubscriberConnection', '/data')
#SWAMP_DRAGON_CONNECTION = ('chat.sockserver.DataConnection', '/data')
SWAMP_DRAGON_CONNECTION = ('swampdragon_auth.socketconnection.HttpDataConnection', '/data')
SWAMP_DRAGON_SESSION_STORE = 'intersog.chat.sessions.UserOnlyCustomSession'

DRAGON_URL = 'http://localhost:9999/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)