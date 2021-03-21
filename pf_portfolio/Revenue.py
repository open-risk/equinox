from django.db import models
from pf_portfolio.model_choices import *
class Revenue(models.Model):



    market_conditions = models.IntegerField(blank=True, null=True, choices=MARKET_CONDITIONS_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    no_offtake_contract_case = models.IntegerField(blank=True, null=True, choices=NO_OFFTAKE_CONTRACT_CASE_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    offtake_contract_case = models.IntegerField(blank=True, null=True, choices=OFFTAKE_CONTRACT_CASE_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    price_risk = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    reserve_risk = models.IntegerField(blank=True, null=True, choices=RESERVE_RISK_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    revenue_assessment = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    revenue_contract_robustness = models.IntegerField(blank=True, null=True, choices=REVENUE_CONTRACT_ROBUSTNESS_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    revenue_group_identifier = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    stress_analysis = models.IntegerField(blank=True, null=True, choices=STRESS_ANALYSIS_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    supplier_track_record = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    supply_cost_risks = models.IntegerField(blank=True, null=True, choices=SUPPLY_COST_RISKS_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    supply_risk = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    transportation_risk = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    volume_risk = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

