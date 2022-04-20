##core/dbrouter.py 
##core는 장고 앱 이름 
## django-admin startapp djangotest라면, 앱이름은 djangotest이겠죠! 
from django.db import models
from django.db.models.base import Model


class MultiDBRouter(object): 
    
    def __init__(self):
          self.model_list = ['default', 'Jung']

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.model_list:
            return  model._meta.app_label
        
        return None

                  
                  
    def db_for_write(self, model, **hints): 
       
        return None
    
    def allow_relation(self, obj1, obj2, **hints):

        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):  
    
        return None

# class MultiDBRouter(object):
#     """
#     A router to control all database operations on models in the
#     auth application.
#     """
#     def db_for_read(self, model, **hints):
#         """
#         Attempts to read remote models go to remote database.
#         """
#         if model._meta.app_label == 'Jung':
#             return 'Jung'
#         return 'default'

#     def db_for_write(self, model, **hints):
#         """
#         Attempts to write remote models go to the remote database.
#         """
#         if model._meta.app_label == 'Jung':
#             return 'Jung'
#         return 'dafault'

#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Do not allow relations involving the remote database
#         """
#         if obj1._meta.app_label == 'Jung' or \
#            obj2._meta.app_label == 'Jung':
#            return False
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         Do not allow migrations on the remote database
#         """
#         if app_label== 'Jung':
#             return False
#         return True


