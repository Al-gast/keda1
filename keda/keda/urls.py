"""
URL configuration for keda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from website.views import *
from django.urls import path, include, re_path
from django.conf.urls import (handler400, handler403, handler404, handler500)
import website

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('solution/', solution, name='solution'),
    path('consultation/', consultation, name='consultation'),

    path('process-overview/', processOverview, name='process-overview'),
    path('process-brief/', processBrief, name='process-brief'),
    path('process-scope/', processScope, name='process-scope'),
    path('process-estimation/', processEstimation, name='process-estimation'),
    path('process-development/', processDevelopment, name='process-development'),
    path('process-support/', processSupport, name='process-support'),
    path('process-next-steps/', processNextSteps, name='process-next-steps'),
    path('about-career/', aboutCareer, name='about-career'),

    # path('fourzerofour/', fourzerofour, name='fourzerofour'),
    path('about-technologies/', aboutTechnologies, name='about-technologies'),
    path('detail-technologies/', detailTechnologies, name='detail-technologies'),
    path('detail-mysql/', detailMysql, name='detail-mysql'),
    path('detail-python/', detailPython, name='detail-python/'),
    path('detail-blog/(?P<slug_blog>[-a-zA-Z0-9_]+)\\Z', detailBlog, name='detail-blog'),
    path('project/', project, name='project'),

    path('detail-project/', detailProject, name='detail-project'),
    path('about-story/', aboutStory, name='about-story'),
    path('about-team/', aboutTeam, name='about-team'),
    path('detail-career/<slug:slug_career>', detailCareer, name='detail-career'),
    path('process-overview/', process, name='process-overview'),

    path('blog/', blog, name="blog"),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path("__reload__/", include("django_browser_reload.urls")),

]

handler404 = 'website.views.not_found'
handler500 = 'website.views.error'
handler403 = 'website.views.permission_denied'
handler400 = 'website.views.bad_request'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
