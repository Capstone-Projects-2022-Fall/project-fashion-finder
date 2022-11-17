from django.apps import AppConfig


class FashionfinderappConfig(AppConfig):
    """
    Configure settings for app. 
    
    default_auto_field: An IntegerField that automatically increments according to available IDs.

    :param AppConfig: Class representing a Django application and its configuration.
    :type kind: None
    :return: None
    :rtype: None
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fashionfinderapp'
