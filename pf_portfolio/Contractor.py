from django.db import models
from pf_portfolio.model_choices import *
class Contractor(models.Model):



    completion_guarantees = models.NullBooleanField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    completion_guarantees_and_liquidated_damages = models.IntegerField(blank=True, null=True, choices=COMPLETION_GUARANTEES_AND_LIQUIDATED_DAMAGES_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    completion_risk = models.IntegerField(blank=True, null=True, choices=COMPLETION_RISK_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    construction_risk = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    contractor_identifier = models.TextField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    contractor_legal_entity_identifier = models.TextField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    contractor_track_record = models.IntegerField(blank=True, null=True, choices=CONTRACTOR_TRACK_RECORD_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    liquidated_damages = models.NullBooleanField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    name_of_contractor = models.TextField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    permitting_and_siting = models.IntegerField(blank=True, null=True, choices=PERMITTING_AND_SITING_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    type_of_construction_contract = models.IntegerField(blank=True, null=True, choices=TYPE_OF_CONSTRUCTION_CONTRACT_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

