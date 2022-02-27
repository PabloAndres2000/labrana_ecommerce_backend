from typing import Optional, List, Union

from django.db.models.query import QuerySet
from labrana_backend.apps.listelement.models import Type


def get_type_by_pk(pk: int) -> Optional[Type]:
    """
    Method to obtain type by pk
    - Returns: Optional[Type]
    """
    try:
        type = Type.objects.get(pk=pk)
        return type
    except Type.DoesNotExist:
        return None


def get_all_types() -> Union[QuerySet, List[Type]]:
    """
    Method to get a list all types
    - Returns: List[Type]
    """
    types = Type.objects.all()
    return types
