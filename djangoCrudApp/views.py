from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import Posts
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

def index(request):
    allPosts = Posts.objects.all()
    template = loader.get_template("index.html")
    return HttpResponse(template.render({'allPosts':allPosts},request))

def newpost(request):
    template = loader.get_template("newpost.html")
    return HttpResponse(template.render({},request))

def post(request):
    id = request.POST['id']
    title = request.POST['title']
    content = request.POST['content']
    if(id=="0"):
        post = Posts(title=title, content=content, created_on=timezone.now())
    else:
        post = get_object_or_404(Posts,pk=id)
        post.title = title
        post.content = content
    post.save()
    return HttpResponseRedirect('/')

def delete(request,id):
    post = get_object_or_404(Posts,pk=id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request,id):
    post = get_object_or_404(Posts,pk=id)
    template = loader.get_template("newpost.html")
    return HttpResponse(template.render({'post':post},request))