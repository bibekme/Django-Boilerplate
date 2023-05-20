import os

environment = os.environ.get("ENVIRONMENT")

if environment == "development":
    from .dev import *
else:
    from .prod import *
