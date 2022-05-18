from django.contrib import admin
from django.urls import path, include

import address
import homepage
import event
import institution
import incubation
import quiz
import catalyst
import thinktank

from homepage import views
from address import views
from champion import views
from event import views
from institution import views
from quiz import views
from catalyst import views
from thinktank import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('champ/', include('champion.urls')),
    path('home/', include('homepage.urls')),
    path('address/', include('address.urls')),
    path('event/', include('event.urls')),
    path('users/', include('users.urls')),
    path('institution/', include('institution.urls')),
    path('incubation/', include('incubation.urls')),
    path('quiz/', include('quiz.urls')),
    path('catalyst', include('catalyst.urls')),
    path('thinktank', include('thinktank.urls')),
]


# path('sentry-debug/', trigger_error),
#+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
