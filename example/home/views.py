# Create your views here.
from django.shortcuts import render, redirect
from home.forms import NoticiaForm
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



@login_required
def index(request):
	list_post = Post.objects.filter(author = request.user)
	return render(request, 'index.html', {
		'user' : request.user,
		'list_post' : list_post,
	})


def nueva_noticia(request):
    if request.method=='POST':
        formulario = NoticiaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save(commit=False)
            formulario.author = request.user
            formulario.save()
            return HttpResponseRedirect ('/login')
    else:
        formulario = NoticiaForm()
    return render_to_response('NoticiaForm.html',{'formulario':formulario}, context_instance=RequestContext(request))
	
def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))
