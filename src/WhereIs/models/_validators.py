import logging
from django.core.exceptions import ValidationError
import re

logger = logging.getLogger('debug')


def validate_ip(value) -> None:
    match = re.search(
        r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b',
        value,
    )
    logger.debug('Match: %s', match)
    if not match:
        raise ValidationError('%s não é um valor de ip válido.' % value)
