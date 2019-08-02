from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import Posts
from .forms import PostForm
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


def index(request):
    allPosts = Posts.objects.all()
    template = loader.get_template("index.html")
    return HttpResponse(template.render({'allPosts': allPosts}, request))


def newpost(request):
    template = loader.get_template("postForm.html")
    postForm = PostForm()
    if request.POST:
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            post = Posts(title=postForm.cleaned_data['title'], content=postForm.cleaned_data['content'], created_on=timezone.now())
            post.save()
            return HttpResponseRedirect('/')
    return HttpResponse(template.render({"buttonText": "Save", "postForm": postForm}, request))



def delete(request, id):
    post = get_object_or_404(Posts, pk=id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, id):
    post = get_object_or_404(Posts, pk=id)
    template = loader.get_template("postForm.html")
    if request.POST:
        post_data = PostForm(request.POST)
        if post_data.is_valid():
            post.title = post_data.cleaned_data['title']
            post.content = post_data.cleaned_data['content']
            post.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse(template.render({"buttonText": "Update", 'id': id, 'postForm': post_data}, request))
    else:
        postForm = PostForm(initial=model_to_dict(post))
        return HttpResponse(template.render({"buttonText": "Update", 'id': id, 'postForm': postForm}, request))
