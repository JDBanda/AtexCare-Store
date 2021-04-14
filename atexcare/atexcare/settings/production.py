from atexcare.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iz^!crn_wg4b3=ui2p+l4_&y3i2kp1(%2hz*-0*mum6d8571ic'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# Lo ideal es colocar unicamente el dominio o ip a la que apunta
'''
pythonanywhere: atexcare.pythonanywhere.com

'''

ALLOWED_HOSTS = ['atexcare.pythonanywhere.com']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# Esta ruta puede cambiar de acuerdo a las carpetas del proyecto
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Media, los archivos que se suben desde el cliente hacia el servidor
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
