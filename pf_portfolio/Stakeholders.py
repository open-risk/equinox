from django.db import models
from pf_portfolio.model_choices import *
class Stakeholders(models.Model):



    compliance_with_standards = models.TextField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    environmental_and_social_assessment = models.TextField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    environmental_and_social_management_system = models.TextField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    force_majeure_risk = models.IntegerField(blank=True, null=True, choices=FORCE_MAJEURE_RISK_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    government_support = models.IntegerField(blank=True, null=True, choices=GOVERNMENT_SUPPORT_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    grievance_mechanisms = models.TextField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    legal_and_regulatory_risk = models.IntegerField(blank=True, null=True, choices=LEGAL_AND_REGULATORY_RISK_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    political_and_legal_environment = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    political_risk = models.IntegerField(blank=True, null=True, choices=POLITICAL_RISK_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    project_approval_risk = models.IntegerField(blank=True, null=True, choices=PROJECT_APPROVAL_RISK_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    stakeholder_engagement = models.TextField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    stakeholders_group = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

