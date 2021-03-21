from django.db import models
from pf_portfolio.model_choices import *
class ProjectCompany(models.Model):



    assignment_of_contracts_and_accounts = models.IntegerField(blank=True, null=True, choices=ASSIGNMENT_OF_CONTRACTS_AND_ACCOUNTS_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    cash_sweep = models.NullBooleanField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    control_over_cash_flow = models.IntegerField(blank=True, null=True, choices=CONTROL_OVER_CASH_FLOW_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    covenant_package = models.IntegerField(blank=True, null=True, choices=COVENANT_PACKAGE_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    covenants = models.TextField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    debt_service_coverage_ratio = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    debttoequity_ratio = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    dividend_restrictions = models.NullBooleanField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    financial_ratios = models.IntegerField(blank=True, null=True, choices=FINANCIAL_RATIOS_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    financial_strength = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    financial_structure = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    foreign_exchange_risk = models.IntegerField(blank=True, null=True, choices=FOREIGN_EXCHANGE_RISK_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    impact_category = models.IntegerField(blank=True, null=True, choices=IMPACT_CATEGORY_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    independent_escrow_account = models.NullBooleanField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    independent_monitoring_and_reporting = models.TextField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    independent_review = models.TextField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    interest_coverage_ratio = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    legal_type_of_project = models.IntegerField(blank=True, null=True, choices=LEGAL_TYPE_OF_PROJECT_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    loan_life_coverage_ratio = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    mandatory_prepayments = models.NullBooleanField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    name_of_project = models.TextField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    payment_cascade = models.NullBooleanField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    payment_deferrals = models.NullBooleanField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    pledge_of_assets = models.IntegerField(blank=True, null=True, choices=PLEDGE_OF_ASSETS_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    project_identifier = models.TextField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    project_lei = models.TextField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    project_life_coverage_ratio = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    refinancing_risk = models.IntegerField(blank=True, null=True, choices=REFINANCING_RISK_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    reporting_and_transparency = models.TextField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    reserve_funds = models.IntegerField(blank=True, null=True, choices=RESERVE_FUNDS_CHOICES, help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')


    security_package = models.FloatField(blank=True, null=True, 
help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

