from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView 
from registration.backends.simple.views import RegistrationView
from .settings import MEDIA_ROOT, DEBUG 

from extuser.forms import UserForm


urlpatterns = [
    
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^conf/', include('conference.urls', namespace='conf')),
    url(r'^chat/', include('chat.urls', namespace='chat')),
    url(r'^user/', include('extuser.urls', namespace='user')),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=UserForm), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls', namespace='auth')),
    url(r'^admin/', admin.site.urls),
]


if DEBUG:

    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    ]


