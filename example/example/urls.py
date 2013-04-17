

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	
	url(r'^login$', auth_views.login, {
		'template_name' : 'log.html',
	}),
	
	url(r'^$', 'home.views.index'),
	url(r'^noticias/nuevo$','home.views.nueva_noticia'),
	url(r'^usuario/nuevo$','home.views.nuevo_usuario'),
)
