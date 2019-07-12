from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from rbac import utils
from django.template import RequestContext

def index(req):
    context_instance=utils.renders(req)
    return render_to_response('backend/index.html',locals())


