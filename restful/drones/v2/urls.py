"""
Book: Django RESTful Web Services
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.urls import re_path
from .. import views
from . import views as views2

urlpatterns = [
    re_path(r'^vehicle-categories/$',
            views.DroneCategoryList.as_view(),
            name=views.DroneCategoryList.name),
    re_path(r'^vehicle-categories/(?P<pk>[0-9]+)$',
            views.DroneCategoryDetail.as_view(),
            name=views.DroneCategoryDetail.name),
    re_path(r'^vehicles/$',
            views.DroneList.as_view(),
            name=views.DroneList.name),
    re_path(r'^vehicles/(?P<pk>[0-9]+)$',
            views.DroneDetail.as_view(),
            name=views.DroneDetail.name),
    re_path(r'^pilots/$',
            views.PilotList.as_view(),
            name=views.PilotList.name),
    re_path(r'^pilots/(?P<pk>[0-9]+)$',
            views.PilotDetail.as_view(),
            name=views.PilotDetail.name),
    re_path(r'^competitions/$',
            views.CompetitionList.as_view(),
            name=views.CompetitionList.name),
    re_path(r'^competitions/(?P<pk>[0-9]+)$',
            views.CompetitionDetail.as_view(),
            name=views.CompetitionDetail.name),
    re_path(r'^$',
            views2.ApiRootVersion2.as_view(),
            name=views2.ApiRootVersion2.name),
]
