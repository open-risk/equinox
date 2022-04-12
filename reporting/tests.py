from django.test import TestCase
from django.test import Client

"""
    re_path(r'^ghg_reduction$', views.ghg_reduction, name='ghg_reduction'),
    re_path(r'^gpc_report$', views.gpc_report, name='gpc_report'),
    re_path(r'^gpp_report$', views.gpp_report, name='gpp_report'),
    re_path(r'^portfolio_map$', views.portfolio_map, name='portfolio_map'),
    re_path(r'^pcaf_mortgage_report$', views.pcaf_mortgage_report, name='pcaf_mortgage_report'),
"""

class SimpleTest(TestCase):

    def test_ghg_reduction(self):
        client = Client()
        client.login(username='admin', password='admin')
        response = client.get('/reporting/ghg_reduction', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_gpc_report(self):
        client = Client()
        client.login(username='admin', password='admin')
        response = client.get('/reporting/gpc_report')
        self.assertEqual(response.status_code, 200)