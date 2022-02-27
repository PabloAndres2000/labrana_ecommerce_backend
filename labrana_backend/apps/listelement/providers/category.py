from typing import Optional, List, Union

from django.db.models.query import QuerySet
from labrana_backend.apps.listelement.models import Category


def get_category_by_pk(pk: int) -> Optional[Category]:
    """
    Method to obtain categories by pk
    - Returns: Optional[Category]
    """
    try:
        category = Category.objects.get(pk=pk)
        return category
    except Category.DoesNotExist:
        return None


def get_all_categories() -> Union[QuerySet, List[Category]]:
    """
    Method to get a list all categories
    - Returns: List[Category]
    """
    categories = Category.objects.all()
    return categories
