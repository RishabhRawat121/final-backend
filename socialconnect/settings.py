import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# ---------------- Base ----------------
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dummy_secret")
DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",")

# ---------------- Installed Apps ----------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "users",
    "posts",
    "profiles",
    "profile",
    "followers",
    "engagement",
    "feed",
    "notifications",
    "admin_api",
]

AUTH_USER_MODEL = "users.CustomUser"

# ---------------- Middleware ----------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "socialconnect.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "socialconnect.wsgi.application"

# ---------------- Database ----------------
fallback_url = (
    f"postgresql://{os.getenv('PGUSER', 'postgres')}:"
    f"{os.getenv('PGPASSWORD', 'Deanambrose%4012345')}@"
    f"{os.getenv('PGHOST', 'db.rwocivhozcmfswyilrwy.supabase.co')}:"
    f"{os.getenv('PGPORT', '5432')}/"
    f"{os.getenv('PGDATABASE', 'postgres')}?sslmode=require"
)

DATABASES = {
    "default": dj_database_url.parse(os.getenv("DATABASE_URL"), conn_max_age=600, ssl_require=True)
}

# Ensure SSL options
DATABASES["default"]["OPTIONS"] = {"sslmode": "require"}

# ---------------- Internationalization ----------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ---------------- Static Files ----------------
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Whitenoise for static files in production
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# ---------------- Supabase ----------------
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# ---------------- REST Framework ----------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
}

# ---------------- CORS ----------------
CORS_ALLOW_ALL_ORIGINS = True
