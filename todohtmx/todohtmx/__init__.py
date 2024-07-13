from django.conf import settings

some_settings = settings.SOME_SETTINGS

def initialize():
  # perform initialization tasks
  print(f"Initializing main project with settings: {some_settings}")

initialize()

