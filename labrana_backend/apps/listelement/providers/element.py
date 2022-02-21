from typing import Optional, List, Union

from django.db.models.query import QuerySet
from labrana_backend.apps.listelement.models import Element


def get_element_by_pk(pk: int) -> Optional[Element]:
    """
    Method to obtain element by pk
    - Returns: Optional[Element]
    """
    try:
        element = Element.objects.get(pk=pk)
        return element
    except Element.DoesNotExist:
        return None


def get_all_elements() -> Union[QuerySet, List[Element]]:
    """
    Method to get a list all elements
    - Returns: List[Element]
    """
    elements = Element.objects.all()
    return elements
