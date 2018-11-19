from django.conf.urls import include, url
from django.contrib import admin
from formula import views

admin.site.site_header = "Formula Admin"
admin.site.site_title = "Formula Portal"
admin.site.index_title = "Welcome Formula Calculator"

urlpatterns = [
    # Examples:
    # url(r'^$', 'calculator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'calculate/', views.calculate),
    url(r'^', views.test),
]
