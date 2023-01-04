import random
import string
import datetime
from django.utils import timezone

from .models import Url_Mapping

def url_shortener(url):
    random_hash = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
    mapping = Url_Mapping(original_url=url, hash=random_hash, validity=timezone.now() + datetime.timedelta(minutes=30))
    mapping.save()
    return random_hash

def load_url(url_hash):
    return Url_Mapping.objects.get(hash=url_hash)

def validity_check(validity:datetime) -> bool:
    if validity <= timezone.now():
        return False
    else:
        return True
