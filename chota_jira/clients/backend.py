from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self,request,username=None,password=None):
        try:
            user=User.objects.get(email=username)
        except User.MultipleObjectsReturned:
            user=User.objects.filter(email=username).oredr_by('id').first()
        except User.DoesNotExist:
        	return None


        if getattr(user,'is_active') and user.check_password(password):
        	return username
        return None
    def get_user(self,user_id):
    	try:
    		return User.objects.get(pk=user_id)
    	except User.DoesNotExist:
    		return None





