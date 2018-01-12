try:
    from .local_settings import *
except ImportError:
    from .development import *