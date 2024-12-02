import re

from django.core.exceptions import FieldDoesNotExist
from django.db import models

def normalize_text(text):
    """
    Normalize text by removing extra spaces and converting to lowercase.
    """
    if not isinstance(text, str):
        return text

    # Remove excess spaces and convert to lowercase
    return re.sub(r'\s+', ' ', text.strip()).lower()





