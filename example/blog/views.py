# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post
from blog.forms import NoticiaForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def nueva_noticia(request):
    if request.method=='POST':
        formulario = NoticiaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect ('/Post')
    else:
        formulario = NoticiaForm()
    return render_to_response('NoticiaForm.html',{'formulario':formulario}, context_instance=RequestContext(request))
