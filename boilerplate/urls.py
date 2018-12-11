from django.conf import settings
from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import include, path
from service.views import ServiceList
from service.views import ServiceDetail
from django.utils import translation
from service.views import IndexView
from service.provider.views import ProviderDetail



import django_js_reverse.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jsreverse/$', django_js_reverse.views.urls_js, name='js_reverse'),
    url(r'^$', IndexView.as_view()),
    #path('service/', include('service.urls'))
    path('<slug>/', ServiceDetail.as_view(), name='service-detail'),
    path('<service>/<provider>/', ProviderDetail.as_view(), name='provider-detail'),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
