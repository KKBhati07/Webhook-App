from .celery_config import app as celery_app

# to call the celery app on initialization of module
__all__ = ("celery_app")