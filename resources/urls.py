from django.conf.urls import url

from . import views
from .templateviews.useControlView import UseControlView

urlpatterns = [
    url(r'^teste/', views.index, name='resources'),
    url(r'^list/',  UseControlView.as_view(), name='usecontrol/list'),
    url(r'^add/', views.usecontrol_add, name='usecontrol/add'),
]
