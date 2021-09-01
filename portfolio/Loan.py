# Copyright (c) 2021 Open Risk (https://www.openriskmanagement.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from django.db import models
from portfolio.model_choices import *
from django.urls import reverse


class Loan(models.Model):
    """
    The Loan model holds data for each for each loan (or other credit facility / financial instrument) that provides financing to a project


    """

    accounting_stages_of_asset_quality = models.IntegerField(blank=True, null=True,
                                                             choices=ACCOUNTING_STAGES_OF_ASSET_QUALITY_CHOICES,
                                                             help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    amortisation_schedule = models.IntegerField(blank=True, null=True, choices=AMORTISATION_SCHEDULE_CHOICES,
                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    amortisation_type = models.IntegerField(blank=True, null=True, choices=AMORTISATION_TYPE_CHOICES,
                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    code_of_conduct = models.BooleanField(blank=True, null=True,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    comments_on_code_of_conduct = models.TextField(blank=True, null=True,
                                                   help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    comments_on_covenant_waiver = models.TextField(blank=True, null=True,
                                                   help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    contract_identifier = models.TextField(blank=True, null=True,
                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    country_of_origination = models.TextField(blank=True, null=True,
                                              help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    covenant_waiver = models.BooleanField(blank=True, null=True,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_covenant_levels = models.FloatField(blank=True, null=True,
                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_external_credit_rating = models.TextField(blank=True, null=True,
                                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_interest_base_rate = models.FloatField(blank=True, null=True,
                                                   help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_interest_margin = models.FloatField(blank=True, null=True,
                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_interest_rate = models.FloatField(blank=True, null=True,
                                              help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_interest_rate_reference = models.IntegerField(blank=True, null=True,
                                                          choices=CURRENT_INTEREST_RATE_REFERENCE_CHOICES,
                                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_interest_rate_type = models.IntegerField(blank=True, null=True, choices=CURRENT_INTEREST_RATE_TYPE_CHOICES,
                                                     help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_internal_credit_rating = models.TextField(blank=True, null=True,
                                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_maturity_date = models.DateField(blank=True, null=True,
                                             help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    current_reversion_interest_rate = models.FloatField(blank=True, null=True,
                                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    date_of_origination = models.DateField(blank=True, null=True,
                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    default_penalty_interest_margin = models.FloatField(blank=True, null=True,
                                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    description_of_bespoke_repayment = models.TextField(blank=True, null=True,
                                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    description_of_current_interest_rate_type = models.TextField(blank=True, null=True,
                                                                 help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    description_of_original_interest_rate_type = models.TextField(blank=True, null=True,
                                                                  help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    description_of_relevant_schemes = models.TextField(blank=True, null=True,
                                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    details_of_origination_channel = models.TextField(blank=True, null=True,
                                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    early_redemption_penalty = models.FloatField(blank=True, null=True,
                                                 help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    end_date_of_current_fixed_interest_period = models.DateField(blank=True, null=True,
                                                                 help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    end_date_of_interest_only_period = models.DateField(blank=True, null=True,
                                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    end_date_of_subsidy = models.DateField(blank=True, null=True,
                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    external_credit_rating_at_origination = models.TextField(blank=True, null=True,
                                                             help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    final_bullet_repayment = models.FloatField(blank=True, null=True,
                                               help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    governing_law_of_loan_agreement = models.TextField(blank=True, null=True,
                                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    ghg_attribution_factor = models.FloatField(blank=True, null=True,
                                               help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    ghg_data_quality = models.IntegerField(blank=True, null=True, choices=GHG_DATA_QUALITY_CHOICES,
                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    interest_cap_rate = models.FloatField(blank=True, null=True,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    interest_floor_rate = models.FloatField(blank=True, null=True,
                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    interest_payment_frequency = models.IntegerField(blank=True, null=True, choices=INTEREST_PAYMENT_FREQUENCY_CHOICES,
                                                     help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    interest_reset_interval = models.FloatField(blank=True, null=True,
                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    internal_credit_rating_at_origination = models.TextField(blank=True, null=True,
                                                             help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    last_covenant_test_date = models.DateField(blank=True, null=True,
                                               help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    last_interest_reset_date = models.DateField(blank=True, null=True,
                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    last_payment_amount = models.FloatField(blank=True, null=True,
                                            help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    last_payment_date = models.DateField(blank=True, null=True,
                                         help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    legal_balance = models.FloatField(blank=True, null=True,
                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    loan_commitment = models.FloatField(blank=True, null=True,
                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    loan_covenants = models.IntegerField(blank=True, null=True, choices=LOAN_COVENANTS_CHOICES,
                                         help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    loan_currency = models.TextField(blank=True, null=True,
                                     help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    next_interest_reset_date = models.DateField(blank=True, null=True,
                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    next_interest_scheduled_repayment_amount = models.FloatField(blank=True, null=True,
                                                                 help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    next_interest_scheduled_repayment_date = models.DateField(blank=True, null=True,
                                                              help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    next_principal_scheduled_repayment_amount = models.FloatField(blank=True, null=True,
                                                                  help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    next_principal_scheduled_repayment_date = models.DateField(blank=True, null=True,
                                                               help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    original_interest_base_rate = models.FloatField(blank=True, null=True,
                                                    help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    original_interest_margin = models.FloatField(blank=True, null=True,
                                                 help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    original_interest_rate = models.FloatField(blank=True, null=True,
                                               help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    original_interest_rate_reference = models.IntegerField(blank=True, null=True,
                                                           choices=ORIGINAL_INTEREST_RATE_REFERENCE_CHOICES,
                                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    original_interest_rate_type = models.IntegerField(blank=True, null=True,
                                                      choices=ORIGINAL_INTEREST_RATE_TYPE_CHOICES,
                                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    original_maturity_date = models.DateField(blank=True, null=True,
                                              help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    origination_amount = models.FloatField(blank=True, null=True,
                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    other_balances = models.FloatField(blank=True, null=True,
                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    other_syndicate_counterparties = models.TextField(blank=True, null=True,
                                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    pastdue_penalty_interest_margin = models.FloatField(blank=True, null=True,
                                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    principal_balance = models.FloatField(blank=True, null=True,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    principal_payment_frequency = models.IntegerField(blank=True, null=True,
                                                      choices=PRINCIPAL_PAYMENT_FREQUENCY_CHOICES,
                                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    product_type = models.IntegerField(blank=True, null=True, choices=PRODUCT_TYPE_CHOICES,
                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    recourse_to_other_assets = models.BooleanField(blank=True, null=True,
                                                   help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    relevant_schemes = models.BooleanField(blank=True, null=True,
                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    securitised = models.BooleanField(blank=True, null=True,
                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    source_of_current_external_credit_rating = models.TextField(blank=True, null=True,
                                                                help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    source_of_external_credit_rating_at_origination = models.TextField(blank=True, null=True,
                                                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    specialised_product = models.BooleanField(blank=True, null=True,
                                              help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    start_date_of_current_fixed_interest_period = models.DateField(blank=True, null=True,
                                                                   help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    start_date_of_interest_only_period = models.DateField(blank=True, null=True,
                                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    start_date_of_subsidy = models.DateField(blank=True, null=True,
                                             help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    subsidy = models.BooleanField(blank=True, null=True,
                                  help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    subsidy_amount = models.FloatField(blank=True, null=True,
                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    subsidy_provider = models.TextField(blank=True, null=True,
                                        help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    syndicated_loan = models.BooleanField(blank=True, null=True,
                                          help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    syndicated_portion = models.FloatField(blank=True, null=True,
                                           help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    total_balance = models.FloatField(blank=True, null=True,
                                      help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    trigger_levels_of_loan_covenants = models.FloatField(blank=True, null=True,
                                                         help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    type_of_reversion_interest_rate = models.TextField(blank=True, null=True,
                                                       help_text='Standard Description. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contract_identifier

    def get_absolute_url(self):
        return reverse('portfolio:Loan_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"