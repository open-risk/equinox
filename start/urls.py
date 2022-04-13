from django.urls import path
from django.urls import re_path
from . import views

app_name = 'start'

""" Custom URL's in addition to the admin url's

"""

urlpatterns = [
    path('', views.Front.as_view(), name='Front'),
    re_path(r'^documentation/(?P<slug>[-\w]+)$', views.documentation, name='Documentation'),
    re_path(r'^doclist$', views.DocList.as_view(), name='DocList'),
    re_path(r'^concepts$', views.Concepts.as_view(), name='Concepts'),
]

# url(r'^generic$', views.Generic.as_view(), name='Generic'),
# url(r'^not_implemented$', views.Not_Implemented.as_view(), name='Not Implemented'),
# url(r'^about$', views.About.as_view(), name='About'),
# url(r'^get_started$', views.GetStarted.as_view(), name='Get Started'),
# url(r'^overview$', views.Overview.as_view(), name='Overview'),
# url(r'^latest$', views.Latest.as_view(), name='Latest Releases'),
# url(r'^help$', views.Help.as_view(), name='Help'),

# url(r'^user_profile$', views.user_profile, name='User Profile'),
