import os

environment = os.environ.get("ENVIRONMENT")

if environment == "dev":
    from .dev import *
else:
    from .prod import *
