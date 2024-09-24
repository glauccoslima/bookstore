"""
Django settings for bookstore project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os  # Importa o módulo os para manipulação de caminhos e variáveis de ambiente

# Define o diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta usada em produção - deve ser mantida segredo!
SECRET_KEY = "django-insecure-toi%#a!sl+7#^g&vk8&m1_!$co#zzpf-#=)xhvm+fuf$d^g()q"

# Define o modo de depuração - deve ser False em produção
# skipcq: PY-S0900
DEBUG = False  # Altere para False em produção

# Define os hosts permitidos para a aplicação
ALLOWED_HOSTS = ['ebac-bookstore-api-glaucco-f29e1a0a5c0b.herokuapp.com']
CSRF_TRUSTED_ORIGINS = ['https://ebac-bookstore-api-glaucco-f29e1a0a5c0b.herokuapp.com']

# Definição das aplicações instaladas
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",  # Extensões úteis para desenvolvimento
    "order",  # Aplicação de pedidos
    "product",  # Aplicação de produtos
    "rest_framework",  # Django REST framework para criação de APIs
    "debug_toolbar",  # Ferramenta de depuração
    "rest_framework.authtoken",  # Autenticação por token para APIs
]

# Definição dos middlewares
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Middleware para servir arquivos estáticos
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # Middleware para a barra de ferramentas de depuração
]

# Definição do arquivo de configuração de URLs
ROOT_URLCONF = "bookstore.urls"

# Configuração dos templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "bookstore", "templates")],  # Diretório de templates
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Definição da aplicação WSGI
WSGI_APPLICATION = "bookstore.wsgi.application"

# Diretório para arquivos estáticos
STATIC_URL = "static/"

# Diretório para onde os arquivos estáticos serão coletados
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configuração do armazenamento de arquivos estáticos com WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configuração do banco de dados
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),  # Engine do banco de dados
        "NAME": str(os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3")),  # Nome do banco de dados convertido em string
        "USER": os.environ.get("SQL_USER", "user"),  # Usuário do banco de dados
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),  # Senha do banco de dados
        "HOST": os.environ.get("SQL_HOST", "localhost"),  # Host do banco de dados
        "PORT": os.environ.get("SQL_PORT", "5432"),  # Porta do banco de dados
    }
}

# Validação de senhas de usuários
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Configuração de internacionalização
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Tipo de campo de chave primária padrão
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Configuração do Django REST framework
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}

# IPs internos permitidos para Debug Toolbar (desativar em produção)
if DEBUG:
    INTERNAL_IPS = [
        "127.0.0.1",
    ]
