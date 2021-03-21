from django.db import models
from pf_portfolio.model_choices import *
class Operator(models.Model):



    o_and_m_contract = models.IntegerField(blank=True, null=True, choices=O_AND_M_CONTRACT_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    operating_risk = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    operator_identifier = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    operator_lei = models.TextField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    operator_track_record = models.IntegerField(blank=True, null=True, choices=OPERATOR_TRACK_RECORD_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

