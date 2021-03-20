from django.conf.urls.static import static
from django.conf import settings

"""excel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django .conf.urls import include
from django.conf.urls import url
from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap
from django_xmlrpc.views import handle_xmlrpc
from django_comments.models import Comment
# from zinnia import views as zinnia_views
# from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import zinnia
from django_xmlrpc.views import handle_xmlrpc

from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps.views import index

sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,
            }


urlpatterns = [
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django_comments.urls')),
    # url(r'^sitemap.xml$', 'index',{'sitemaps': sitemaps}),
    # url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',{'sitemaps': sitemaps}),
    path('admin/', admin.site.urls),
    url(r'^xmlrpc/$', handle_xmlrpc, name='xmlrpc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


    # url(r'^$', RedirectView.as_view(url='/blog/', permanent=True)),
    # url(r'^blog/', include('zinnia.urls')),
    # url(r'^comments/', include('django_comments.urls')),
    # url(r'^xmlrpc/$', handle_xmlrpc),
    # url(r'^i18n/', include('django.conf.urls.i18n')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', admin.site.urls),