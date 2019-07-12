from rbac.models import *

def init_role(uid):
    rid=User.objects.filter(id=uid).values('roles__id')[0]
    print(rid)
    url=Role.objects.filter(id=rid).values('model__model_url')
#    print(url)
    return rid
    
