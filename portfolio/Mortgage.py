# Copyright (c) 2020 - 2023 Open Risk (https://www.openriskmanagement.com)
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
from django.urls import reverse

from portfolio.mortgage_choices import *
from portfolio.Borrower import Borrower


class Mortgage(models.Model):
    """
    The Mortgage model holds Mortgage Loan Portfolio data conforming to the EBA NPL Template specification
    `EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Loan_Table>`_

    .. note:: The EBA Templates make a distinction between instrument and contract. At present this is not fully implemented

    """

    #
    # IDENTIFICATION FIELDS
    #

    contract_identifier = models.TextField(blank=True, null=True)

    instrument_identifier = models.TextField(blank=True, null=True,
                                             help_text='Institution internal identifier for the Loan part. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Instrument_Identifier">Documentation</a>')

    #
    # FOREIGN KEYS
    #

    counterparty_identifier = models.ForeignKey(Borrower, on_delete=models.CASCADE, null=True, blank=True)

    #
    # DATA PROPERTIES
    #

    accounting_stages_of_asset_quality = models.IntegerField(blank=True, null=True,
                                                             choices=ACCOUNTING_STAGES_OF_ASSET_QUALITY_CHOICES,
                                                             help_text='Accounting stages of asset quality, i.e. IFRS Stage 1, IFRS Stage 2, IFRS Stage 3 (impaired), Fair Value Through P&L, Other Accounting Standard - impaired asset, Other Accounting Standard - Not impaired. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Accounting_stages_of_Asset_Quality">Documentation</a>')

    accrued_interest_balance_off_book = models.BigIntegerField(blank=True, null=True,
                                                               help_text='Amount of interest that has been accrued but not capitalised to the Loan,  as not recognised on the balance sheet. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Accrued_Interest_Balance_Off_book">Documentation</a>')

    accrued_interest_balance_on_book = models.BigIntegerField(blank=True, null=True,
                                                              help_text='Current amount of outstanding interest as recognised on the balance sheet at the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Accrued_Interest_Balance_On_book">Documentation</a>')

    amortisation_type = models.IntegerField(blank=True, null=True, choices=AMORTISATION_TYPE_CHOICES,
                                            help_text='Description of the Amortisation type of the loan as per the latest Loan Agreement e.g. Full amortisation, part amortisation, final bullet, bespoke repayment. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Amortisation_Type">Documentation</a>')

    asset_class = models.IntegerField(blank=True, null=True, choices=ASSET_CLASS_CHOICES,
                                      help_text='Asset class of the Loan, i.e. Residential, CRE, SME/Corp, etc.. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Asset_Class">Documentation</a>')

    balance_at_default = models.BigIntegerField(blank=True, null=True,
                                                help_text='Balance of the Loan when the Loan has defaulted (CRR Art.178). <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Balance_at_default">Documentation</a>')

    capitalised_pastdue_amount = models.BigIntegerField(blank=True, null=True,
                                                        help_text='Total capitalised past-due balance as recognised on balance sheet at NPL Portfolio Cut-Off Date i.e. Interest and Legal Fees. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Capitalised_PastDue_Amount">Documentation</a>')

    channel_of_origination = models.IntegerField(blank=True, null=True, choices=CHANNEL_OF_ORIGINATION_CHOICES,
                                                 help_text='Channel through which the Loan was originated, i.e. Branch, Internet and Broker. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Channel_of_Origination">Documentation</a>')

    chargeoff_date = models.DateField(blank=True, null=True,
                                      help_text='Date when the Loan went into charge-off. A charge-off is the declaration by the Institution commonly on Unsecured Retail when the Borrower is severely delinquent, and the Institution starts the recovery process officially.. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Chargeoff_Date">Documentation</a>')

    code_of_conduct = models.TextField(blank=True, null=True,
                                       help_text='Indicator as to whether the Loan is subject to certain Code of Conduct. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Code_of_Conduct">Documentation</a>')

    comments_on_code_of_conduct = models.TextField(blank=True, null=True,
                                                   help_text='Further comments / details on Code of Conduct. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Comments_on_Code_of_Conduct">Documentation</a>')

    comments_on_covenant_waiver = models.TextField(blank=True, null=True,
                                                   help_text='Further comments / details on the covenant waiver if "Yes" is selected in field "Covenant Waiver". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Comments_on_Covenant_Waiver">Documentation</a>')

    country_of_origination = models.TextField(blank=True, null=True,
                                              help_text='Country where the Loan was originated. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Country_of_Origination">Documentation</a>')

    covenant_waiver = models.TextField(blank=True, null=True,
                                       help_text='Indicator as to whether there has been a covenant waiver sent out for any breaches of the Loan Agreement. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Covenant_Waiver">Documentation</a>')

    current_covenant_levels = models.BigIntegerField(blank=True, null=True,
                                                     help_text='Current levels of covenants as at NPL Portfolio Cut-Off date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Current_Covenant_Levels">Documentation</a>')

    current_interest_base_rate = models.FloatField(blank=True, null=True,
                                                   help_text='Current base rate of the Loan as at NPL Portfolio Cut-Off Date when "Variable" is selected in field "Current Interest Rate Type". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Current_Interest_Base_Rate">Documentation</a>')

    current_interest_margin = models.FloatField(blank=True, null=True,
                                                help_text='is the current margin above the base rate as stated in the Loan Agreement and applicable at the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Current_Interest_Margin">Documentation</a>')

    current_interest_rate = models.FloatField(blank=True, null=True,
                                              help_text='is the current total interest rate of the loan as stated in the Loan Agreement on and applicable at the NPL Portfolio Cut-Off Date.. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Current_Interest_Rate">Documentation</a>')

    current_interest_rate_reference = models.IntegerField(blank=True, null=True,
                                                          choices=CURRENT_INTEREST_RATE_REFERENCE_CHOICES,
                                                          help_text='Current interest rate base or reference of the loan as stated in the Loan Agreement and applicable at the NPL Portfolio Cut-Off Date when Variable is selected in field Current Interest Rate Type. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Current_Interest_Rate_Reference">Documentation</a>')

    current_interest_rate_type = models.IntegerField(blank=True, null=True, choices=CURRENT_INTEREST_RATE_TYPE_CHOICES,
                                                     help_text='is the current interest rate type as per Loan Agreement and applicable at the NPL Portfolio Cut-Off Date, i.e. Fixed / Variable / Mixed. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Current_Interest_Rate_Type">Documentation</a>')

    current_maturity_date = models.DateField(blank=True, null=True,
                                             help_text='Contractual maturity date of the Loan as at NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Current_Maturity_Date">Documentation</a>')

    current_reversion_interest_rate = models.FloatField(blank=True, null=True,
                                                        help_text='Current level of reversion interest rate according to the Loan Agreement and applicable as at NPL Portfolio Cut-Off Date, reversion means that after the interest fixed period the Institution would revert the rate to a different type, e.g. the Institutions Standard Variable Rate. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Current_Reversion_Interest_Rate">Documentation</a>')

    date_of_default = models.DateField(blank=True, null=True,
                                       help_text='Date that the Loan defaulted. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Date_of_Default">Documentation</a>')

    date_of_origination = models.DateField(blank=True, null=True,
                                           help_text='Date that the Loan originated as per the Loan Agreement. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Date_of_Origination">Documentation</a>')

    days_in_pastdue = models.BigIntegerField(blank=True, null=True,
                                             help_text='Number of days that the Loan is currently past-due as at the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Days_in_PastDue">Documentation</a>')

    default_penalty_interest_margin = models.FloatField(blank=True, null=True,
                                                        help_text='Additional margin charged on the balance of the Loan in default according to the Loan Agreement and applicable as of the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Default_Penalty_Interest_Margin">Documentation</a>')

    description_of_bespoke_repayment = models.TextField(blank=True, null=True,
                                                        help_text='Description of the bespoke repayment profile when "Bespoke Repayment" is selected in field "Amortisation Type". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Description_of_Bespoke_Repayment">Documentation</a>')

    description_of_current_interest_rate_type = models.TextField(blank=True, null=True,
                                                                 help_text='Description of current interest rate type when "Mixed" is selected in field "Current Interest Rate Type". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Description_of_Current_Interest_Rate_Type">Documentation</a>')

    description_of_original_interest_rate_type = models.TextField(blank=True, null=True,
                                                                  help_text='Description of original interest rate type when "Mixed" is selected in field "Original Interest Rate Type". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Description_of_Original_Interest_Rate_Type">Documentation</a>')

    description_of_relevant_schemes = models.TextField(blank=True, null=True,
                                                       help_text='Description of the relevant scheme if YES is selected in the field Relevant Schemes. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Description_of_Relevant_Schemes">Documentation</a>')

    details_of_origination_channel = models.TextField(blank=True, null=True,
                                                      help_text='Description of the origination channel when "Broker" or "Other" is selected in field "Channel of Origination". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Details_of_Origination_Channel">Documentation</a>')

    early_redemption_penalty = models.FloatField(blank=True, null=True,
                                                 help_text='Additional charge on the early redemption made by the Counterparty according to the Loan Agreement and applicable as of the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Early_Redemption_Penalty">Documentation</a>')

    end_date_of_current_fixed_interest_period = models.DateField(blank=True, null=True,
                                                                 help_text='Date that the current fixed interest period ends according to the Loan Agreement and applicable as at the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.End_Date_of_Current_Fixed_Interest_Period">Documentation</a>')

    end_date_of_interest_grace_period = models.DateField(blank=True, null=True,
                                                         help_text='Date that the interest payment ends postponement according to the Loan Agreement and applicable as of the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.End_Date_of_Interest_Grace_Period">Documentation</a>')

    end_date_of_interest_only_period = models.DateField(blank=True, null=True,
                                                        help_text='Date that the interest repayment only period ends according to the current Loan Agreement and applicable as at the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.End_Date_of_Interest_Only_Period">Documentation</a>')

    end_date_of_principal_grace_period = models.DateField(blank=True, null=True,
                                                          help_text='Date that the principal payment ends postponement according to the Loan Agreement and applicable as of the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.End_Date_of_Principal_Grace_Period">Documentation</a>')

    end_date_of_subsidy = models.DateField(blank=True, null=True,
                                           help_text='Date that the current subsidy ends. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.End_Date_of_Subsidy">Documentation</a>')

    external_credit_rating_at_origination = models.TextField(blank=True, null=True,
                                                             help_text='External credit rating issued to the Loan applicable at the point of time when the counterparty became a customer. In case several ratings are assigned, the approach described in Art. 138 of the CRR applies.. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.External_Credit_Rating_at_Origination">Documentation</a>')

    final_bullet_repayment = models.BigIntegerField(blank=True, null=True,
                                                    help_text='Total amount of principal repayment to be paid at the maturity date of the loan. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Final_Bullet_Repayment">Documentation</a>')

    governing_law_of_loan_agreement = models.TextField(blank=True, null=True,
                                                       help_text='Governing law is the law of the country in which the Loan Agreement was entered into. This does not necessarily correspond to the country where the loan was originated. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Governing_Law_of_Loan_Agreement">Documentation</a>')

    interest_cap_rate = models.FloatField(blank=True, null=True,
                                          help_text='Maximum interest rate which can be charged on the Loan as specified in the current Loan Agreement (if applicable). <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Interest_Cap_Rate">Documentation</a>')

    interest_floor_rate = models.FloatField(blank=True, null=True,
                                            help_text='Minimum interest rate of a loan which can be charged on the Loan as specified in the current Loan Agreement (if applicable). <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Interest_Floor_Rate">Documentation</a>')

    interest_payment_frequency = models.IntegerField(blank=True, null=True, choices=INTEREST_PAYMENT_FREQUENCY_CHOICES,
                                                     help_text='Frequency of interest payments based on the current Loan Agreement as at the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Interest_Payment_Frequency">Documentation</a>')

    interest_reset_interval = models.BigIntegerField(blank=True, null=True,
                                                     help_text='Number of months between two interest reset dates according to the Loan Agreement and applicable as of the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Interest_Reset_Interval">Documentation</a>')

    last_covenant_test_date = models.DateField(blank=True, null=True,
                                               help_text='Date that the covenant levels were tested last time by the institution. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Last_Covenant_Test_Date">Documentation</a>')

    last_interest_reset_date = models.DateField(blank=True, null=True,
                                                help_text='Date that the last interest reset event happened. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Last_Interest_Reset_Date">Documentation</a>')

    last_payment_amount = models.BigIntegerField(blank=True, null=True,
                                                 help_text='Amount of last payment. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Last_Payment_Amount">Documentation</a>')

    last_payment_date = models.DateField(blank=True, null=True,
                                         help_text='Date that the last payment was made. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Last_Payment_Date">Documentation</a>')

    legal_balance = models.BigIntegerField(blank=True, null=True,
                                           help_text='Total claim amount, i.e. Total Balance + Accrued Interest Balance (Off book). <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Legal_Balance">Documentation</a>')

    legal_balance_at_chargeoff_date = models.BigIntegerField(blank=True, null=True,
                                                             help_text='Total claim amount when the Loan went into charge-off. A charge-off is the declaration by the Institution commonly on Unsecured Retail when the Borrower is severely delinquent, and the Institution starts the recovery process officially.. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Legal_Balance_at_Chargeoff_Date">Documentation</a>')

    loan_commitment = models.BigIntegerField(blank=True, null=True,
                                             help_text='Total available credit extended as at the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Loan_Commitment">Documentation</a>')

    loan_covenants = models.IntegerField(blank=True, null=True, choices=LOAN_COVENANTS_CHOICES,
                                         help_text='List of the covenants as agreed in the current Loan Agreement as at the NPL Portfolio Cut-Off Date (LTV, ICR, DSCR etc.), each in a separate column. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Loan_Covenants">Documentation</a>')

    loan_currency = models.TextField(blank=True, null=True,
                                     help_text='Currency which the Loan is expressed in as per latest Loan Agreement. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Loan_Currency">Documentation</a>')

    loan_purpose = models.IntegerField(blank=True, null=True, choices=LOAN_PURPOSE_CHOICES,
                                       help_text='ultimate financing purpose of the Loan, e.g. Residential real estate purchase for own use, Residential real estate purchase for investment, Commercial real estate purchase, Margin lending, Debt financing, Imports/Exports, Construction investment, and Working capital facility.. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Loan_Purpose">Documentation</a>')

    loan_status = models.IntegerField(blank=True, null=True, choices=LOAN_STATUS_CHOICES,
                                      help_text='Loan status, e.g. performing and non-performing. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Loan_Status">Documentation</a>')

    marp_applicable = models.BooleanField(blank=True, null=True,
                                          help_text='Indicator as to whether the Institution operates a Mortgage Arrears Resolution Process when dealing with Corporates or Private Individual Counterparties in Mortgage Arrears. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.MARP_Applicable">Documentation</a>')

    marp_entry = models.DateField(blank=True, null=True,
                                  help_text='Date loan entered current MARP status. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.MARP_Entry">Documentation</a>')

    marp_status = models.IntegerField(blank=True, null=True, choices=MARP_STATUS_CHOICES,
                                      help_text='The status of the current Mortgage Arrears Resolution Process; Not in MARP, Exited MARP, Provision 23,24,28,29,42,45,47,Self Cure, Alternative Repayment Arrangement (ARA). <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.MARP_Status">Documentation</a>')

    next_interest_reset_date = models.DateField(blank=True, null=True,
                                                help_text='Date that the next interest reset event happened. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Next_Interest_Reset_Date">Documentation</a>')

    next_interest_scheduled_repayment_amount = models.BigIntegerField(blank=True, null=True,
                                                                      help_text='Amount of next scheduled interest repayment as at the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Next_Interest_Scheduled_Repayment_Amount">Documentation</a>')

    next_interest_scheduled_repayment_date = models.DateField(blank=True, null=True,
                                                              help_text='Date that the next interest repayment is made as at the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Next_Interest_Scheduled_Repayment_Date">Documentation</a>')

    next_principal_scheduled_repayment_amount = models.BigIntegerField(blank=True, null=True,
                                                                       help_text='Amount of next scheduled principal repayment as at the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Next_Principal_Scheduled_Repayment_Amount">Documentation</a>')

    next_principal_scheduled_repayment_date = models.DateField(blank=True, null=True,
                                                               help_text='Date that the next principal repayment is made as at the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Next_Principal_Scheduled_Repayment_Date">Documentation</a>')

    nonperforming_reason = models.IntegerField(blank=True, null=True, choices=NONPERFORMING_REASON_CHOICES,
                                               help_text='Main reason why the non-performing status was provided, i.e. impaired (according to the applicable accounting standard), defaulted (CRR Art. 178), more than 90 ,DPD, unlikely to pay. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.NonPerforming_Reason">Documentation</a>')

    number_of_pastdue_events = models.BigIntegerField(blank=True, null=True,
                                                      help_text='Number of times that the Loan was previously categorised as past-due. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Number_of_PastDue_Events">Documentation</a>')

    original_interest_base_rate = models.FloatField(blank=True, null=True,
                                                    help_text='Original base rate of the Loan when "Variable" is selected in field "Original Interest Rate Type". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Original_Interest_Base_Rate">Documentation</a>')

    original_interest_margin = models.FloatField(blank=True, null=True,
                                                 help_text='Original margin above the base rate at loan origination. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Original_Interest_Margin">Documentation</a>')

    original_interest_rate = models.FloatField(blank=True, null=True,
                                               help_text='Original total interest rate of the Loan as states in the Loan Agreement and as applicable as of Loan Origination. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Original_Interest_Rate">Documentation</a>')

    original_interest_rate_reference = models.IntegerField(blank=True, null=True,
                                                           choices=ORIGINAL_INTEREST_RATE_REFERENCE_CHOICES,
                                                           help_text='Original interest rate base / reference of the Loan when "Variable" is selected in field "Original Interest Rate Type". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Original_Interest_Rate_Reference">Documentation</a>')

    original_interest_rate_type = models.IntegerField(blank=True, null=True,
                                                      choices=ORIGINAL_INTEREST_RATE_TYPE_CHOICES,
                                                      help_text='Original interest rate type as states in the Loan Agreement and as applicable as of Loan origination i.e. Fixed / Variable / Mixed. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Original_Interest_Rate_Type">Documentation</a>')

    original_maturity_date = models.DateField(blank=True, null=True,
                                              help_text='Original contractual maturity date of the Loan. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Original_Maturity_Date">Documentation</a>')

    origination_amount = models.BigIntegerField(blank=True, null=True,
                                                help_text='Loan amount advanced to the Borrower / drawn down by the Borrower at the origination date on the loan. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Origination_Amount">Documentation</a>')

    other_balances = models.BigIntegerField(blank=True, null=True,
                                            help_text='Current amount of other outstanding amounts, e.g. other charges, commissions, fees etc., as recognised on the balance sheet. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Other_Balances">Documentation</a>')

    other_pastdue_amounts = models.BigIntegerField(blank=True, null=True,
                                                   help_text='Accumulated amount of other past-due amounts, e.g. fees, as recognised on balance sheet at NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Other_PastDue_Amounts">Documentation</a>')

    other_syndicate_counterparties = models.TextField(blank=True, null=True,
                                                      help_text='Who the other syndicate Counterparties are when "Yes" is selected in field "Syndicated Loan". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Other_Syndicate_Counterparties">Documentation</a>')

    pastdue_interest_amount = models.BigIntegerField(blank=True, null=True,
                                                     help_text='Accumulated amount of past-due interest as recognised on balance sheet as at NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.PastDue_Interest_Amount">Documentation</a>')

    pastdue_penalty_interest_margin = models.FloatField(blank=True, null=True,
                                                        help_text='Additional margin charged on the past-due portion of the Loan according to the Loan Agreement and applicable as of the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.PastDue_Penalty_Interest_Margin">Documentation</a>')

    pastdue_principal_amount = models.BigIntegerField(blank=True, null=True,
                                                      help_text='Accumulated amount of past-due principal as recognised on balance sheet at NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.PastDue_Principal_Amount">Documentation</a>')

    principal_balance = models.BigIntegerField(blank=True, null=True,
                                               help_text='Current amount of outstanding principal as recognised on the balance sheet at Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Principal_Balance">Documentation</a>')

    principal_payment_frequency = models.IntegerField(blank=True, null=True,
                                                      choices=PRINCIPAL_PAYMENT_FREQUENCY_CHOICES,
                                                      help_text='Frequency that the principal payment is currently made based on the current Loan Agreement as at the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Principal_Payment_Frequency">Documentation</a>')

    relevant_schemes = models.TextField(blank=True, null=True,
                                        help_text='Indicator as to whether the Loan is involved with any relevant schemes, e.g. Right to Buy Scheme in UK. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Relevant_Schemes">Documentation</a>')

    recourse_to_other_assets = models.BooleanField(blank=True, null=True,
                                                   help_text='Indicator as to whether the Institution has the legal right to access other assets of the Borrower. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Recourse_to_Other_Assets">Documentation</a>')

    securitised = models.TextField(blank=True, null=True,
                                   help_text='Indicator as to whether the Loan has been securitised or within covered bond pool. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Securitised">Documentation</a>')

    specialised_product = models.TextField(blank=True, null=True,
                                           help_text='Indicator as to whether the Loan is a specialised product, e.g. Fractioned Loans in Italy. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Specialised_Product">Documentation</a>')

    start_date_of_current_fixed_interest_period = models.DateField(blank=True, null=True,
                                                                   help_text='Date that the current fixed interest period started according to the Loan Agreement and applicable as at the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Start_Date_of_Current_Fixed_Interest_Period">Documentation</a>')

    start_date_of_interest_grace_period = models.DateField(blank=True, null=True,
                                                           help_text='Date that the interest payment starts being postponed according to the Loan Agreement and applicable as of the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Start_Date_of_Interest_Grace_Period">Documentation</a>')

    start_date_of_interest_only_period = models.DateField(blank=True, null=True,
                                                          help_text='Date that the interest repayment only period starts according to the most recent Loan Agreement and applicable as  the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Start_Date_of_Interest_Only_Period">Documentation</a>')

    start_date_of_principal_grace_period = models.DateField(blank=True, null=True,
                                                            help_text='Date that the principal payment starts being postponed according to the Loan Agreement and applicable as of the NPL Portfolio Cut-Off Date. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Start_Date_of_Principal_Grace_Period">Documentation</a>')

    start_date_of_subsidy = models.DateField(blank=True, null=True,
                                             help_text='Date that the current subsidy starts. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Start_Date_of_Subsidy">Documentation</a>')

    subsidy = models.TextField(blank=True, null=True,
                               help_text='Indicator where contractual payments are subsidised by an external party. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Subsidy">Documentation</a>')

    subsidy_amount = models.BigIntegerField(blank=True, null=True,
                                            help_text='Amount of the subsidy received. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Subsidy_Amount">Documentation</a>')

    subsidy_provider = models.TextField(blank=True, null=True,
                                        help_text='Name of the external party who provided the subsidy. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Subsidy_Provider">Documentation</a>')

    syndicated_loan = models.TextField(blank=True, null=True,
                                       help_text='Indicator as to whether the Loan is provided by a syndicate or consortium of two or more institutions. This means that in the case of a syndicated loan the Institution holds less than 100% of the total loan. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Syndicated_Loan">Documentation</a>')

    syndicated_portion = models.FloatField(blank=True, null=True,
                                           help_text='Percentage of the portion held by the Institution when "Yes" is selected in field "Syndicated Loan". <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Syndicated_Portion">Documentation</a>')

    time_in_pastdue = models.BigIntegerField(blank=True, null=True,
                                             help_text='Total number of months that the Loan has been in past-due in the past 12 months. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Time_in_PastDue">Documentation</a>')

    total_balance = models.BigIntegerField(blank=True, null=True,
                                           help_text='Total unpaid balance, i.e. Principal Balance + Accrued Interest Balance (On book) + Other Balances. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Total_Balance">Documentation</a>')

    total_pastdue_amount = models.BigIntegerField(blank=True, null=True,
                                                  help_text='Total past-due amount, i.e. Past-Due Principal Amount + Past-Due Interest Amount + Other Past-Due Amount. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Total_PastDue_Amount">Documentation</a>')

    trigger_levels_of_loan_covenants = models.BigIntegerField(blank=True, null=True,
                                                              help_text='Corresponding trigger levels as agreed in the Loan Agreement, as at the NPL Portfolio Cut-Off Date, each in a separate column. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Trigger_Levels_of_Loan_Covenants">Documentation</a>')

    type_of_reversion_interest_rate = models.TextField(blank=True, null=True,
                                                       help_text='Type of reversion interest rate after the fixed interest period according to the Loan Agreement and applicable as of the NPL Portfolio Cur-Off Date, reversion means that after the interest fixed period the Institution would revert the rate to a different type, e.g. the Institutions Standard Variable Rate. <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki/EBA_NPL.Loan.Type_of_Reversion_Interest_Rate">Documentation</a>')

    #
    # BOOKKEEPING FIELDS
    #

    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contract_identifier

    def get_absolute_url(self):
        return reverse('portfolio:Mortgage_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Mortgage"
        verbose_name_plural = "Mortgages"
