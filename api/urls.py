
from django.urls import path,include,re_path
from api import views
urlpatterns = [

    re_path(r'^RegisteredView/$', views.RegisteredView.as_view()),
]
