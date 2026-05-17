import string
from random import SystemRandom
from django.utils.text import slugify

def random_letter(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits, k=k
    ))

def slugfy_new(text, k=5):
    return slugify(text) + '-' + random_letter(k)
