MARKET_CONDITIONS_CHOICES = [(0, '(a) Few competing suppliers or substantial and durable advantage in locatio'),
                             (1, 'cos'), (2, 'or technology. Demand is strong and growing'),
                             (3, "'(b) Few competing suppliers or better than average locatio"), (4, 'cos'),
                             (5, 'or technology but this situation may not last. Demand is strong and stable'),
                             (6, "'(c) Project has no advantage in locatio"), (7, 'cos'),
                             (8, 'or technology. Demand is adequate and stable'),
                             (9, "'(d) Project has worse than average locatio"), (10, 'cos'),
                             (11, 'or technology. Demand is weak and declining')]

FINANCIAL_RATIOS_CHOICES = [
    (0, '(a) Strong financial ratios considering the level of project risk; very robust economic assumptions'), (1,
                                                                                                                 "'(b) Strong to acceptable financial ratios considering the level of project risk; robust project economic assumptions"),
    (2, "'(c) Standard financial ratios considering the level of project risk"),
    (3, "'(d) Aggressive financial ratios considering the level of project risk")]

STRESS_ANALYSIS_CHOICES = [(0, '(a) The project can meet its financial obligations under sustaine'),
                           (1, 'severely stressed economic or sectoral conditions'), (2,
                                                                                      "'(b) The project can meet its financial obligations under normal stressed economic or sectoral conditions. The project is only likely to default under severe economic conditions"),
                           (3,
                            "'(c) The project is vulnerable to stresses that are not uncommon through an economic cycl"),
                           (4, 'and may default in a normal downturn'),
                           (5, "'(d) The project is likely to default unless conditions improve soon")]

REFINANCING_RISK_CHOICES = [(0,
                             '(a) There is no or very limited exposure to market or cycle risk since the expected cashflows cover all future loan repayments during the tenor of the loan and there are no significant delays between the cashflows and the loan repayments.  \\n\\nThere is no or very low refinancing risk. \\n'),
                            (1,
                             "'(b) The exposure to market or cycle risk is limited since the expected cashflows cover the majority of future loan repayments during the tenor of the loan and there are no significant delays between the cashflows and the loan repayments. There is low refinancing risk.  \\n"),
                            (2,
                             "'(c) There is moderate exposure to market or cycle risk since the expected cashflows cover only a part of future loan repayments during the tenor of the loan or there are some significant delays between the cashflows and the loan repayments.  \\n\\nAverage refinancing risk.  \\n"),
                            (3,
                             "'(d) There is significant exposure to market or cycle risk since the expected cashflows cover only a small part of future loan repayments during the tenor of the loan or there are some significant delays between the cashflows and the loan repayments. \\n\\nHigh refinancing risk. \\n")]

AMORTISATION_SCHEDULE_CHOICES = [(0, '(a) Amortising debt without bullet repayment'),
                                 (1, "'(b) Amortising debt wth ot or insignificant bullet repayment"),
                                 (2, "'(c) Amortising debt repayments with limited bullet payment"),
                                 (3, "'(d) Bullet repayment or amortising debt repayments with high bullet repayment")]

FOREIGN_EXCHANGE_RISK_CHOICES = [(0,
                                  '(a) There is no foreign exchange risk because there is no difference in the currency of the loan and the income of the project or because the foreign exchange risk is fully hedged.  '),
                                 (1,
                                  "'(b) There is no foreign exchange risk because there is no difference in the currency of the loan and the income of the project or because the foreign exchange risk is fully hedged.  "),
                                 (2,
                                  "'(c) There is a difference in the currency of the loan and the income of the projec"),
                                 (3,
                                  'but the foreign  exchange  risk  is considered low because the exchange rate is stable or because the foreign exchange risk is hedged to a large extent.  '),
                                 (4,
                                  "'(d) There is a difference in the currency of the loan and the income of the projec"),
                                 (5,
                                  'and the foreign  exchange  risk  is considered high because the exchange rate is volatile and the foreign exchange risk is not hedged to a large extent. ')]

POLITICAL_RISK_CHOICES = [(0, '(a) Very low exposure; strong mitigation instrument'), (1, 'if needed'),
                          (2, "'(b) Low exposure; satisfactory mitigation instrument"), (3, 'if needed'),
                          (4, "'(c) Moderate exposure; fair mitigation instruments"),
                          (5, "'(d) High exposure; no or weak mitigation instruments")]

FORCE_MAJEURE_RISK_CHOICES = [(0, '(a) No or very low exposure to force majeure risk'),
                              (1, "'(b) Limited exposure to force majeure risk"), (2,
                                                                                   "'(c) Significant exposure to force  majeure risk which is not  sufficiently mitigated  "),
                              (3, "'(d) Significant exposure to force  majeure risk which is not mitigated  ")]

GOVERNMENT_SUPPORT_CHOICES = [(0,
                               '(a) Project of strategic importance for the country (preferably export-oriented) Strong support from Government'),
                              (1,
                               "'(b) Project considered important for the country. Good level of support from Government"),
                              (2,
                               "'(c) Project may not be strategic but brings unquestionable benefits for the country. Support from Government may not be explicit"),
                              (3, "'(d) Project not key to the country. No or weak support from Government")]

LEGAL_AND_REGULATORY_RISK_CHOICES = [(0, '(a) Favourable and stable regulatory environment over the long term'),
                                     (1, "'(b) Favourable and stable regulatory environment over the medium term"),
                                     (2, "'(c) Regulatory changes can be predicted with a fair level of certainty"),
                                     (3, "'(d) Current or future regulatory issues may affect the project")]

PROJECT_APPROVAL_RISK_CHOICES = [(0, '(a) Strong'), (1, "'(b) Satisfactory"), (2, "'(c) Fair"), (3, "'(d) Weak")]

LEGAL_REGIME_CHOICES = [(0, '(a) Contract'), (1, 'collateral and security are enforceable'), (2, "'(b) Contract"),
                        (3, 'collateral and security are enforceable'), (4, "'(c) Contract"), (5,
                                                                                               'collateral and security are considered enforceable even if certain non-key issues may exist'),
                        (6, "'(d) There are unresolved key issues in respect if actual enforcement of contract"),
                        (7, 'collateral and security')]

DESIGN_AND_TECHNOLOGY_RISK_CHOICES = [(0, '(a) Fully proven technology and design'),
                                      (1, "'(b) Fully proven technology and design"), (2,
                                                                                       "'(c) Proven technology and design - start-up issues are mitigated by a strong completion package"),
                                      (3,
                                       "'(d) Unproven technology and design; technology issues exist and/or complex design")]

PERMITTING_AND_SITING_CHOICES = [(0, '(a) All permits have been obtained'), (
1, "'(b) Some permits are still outstanding but their receipt is considered very likely"), (2,
                                                                                            "'(c) Some permits are still outstanding but the permitting process is well defined and they are considered routine"),
                                 (3,
                                  "'(d) Key permits still need to be obtained and are not considered routine. Significant conditions may be attached")]

TYPE_OF_CONSTRUCTION_CONTRACT_CHOICES = [
    (0, '(a) Fixed-price date-certain turnkey construction EPC (engineering and procurement contract).'),
    (1, "'(b) Fixed-price date-certain turnkey construction EPC"),
    (2, "'(c) Fixed-price date-certain turnkey construction contract with one or several contractors"),
    (3, "'(d) No or partial fixed-price turnkey contract and/or interfacing issues with multiple contractors")]

COMPLETION_RISK_CHOICES = [(0,
                            '(a) It is almost certain that the project will be finished within the agreed time horizon and at the agreed cost.  '),
                           (1,
                            "'(b) It is very likely that the project will be finished within the agreed time horizon and at the agreed cost.  "),
                           (2,
                            "'(c) It is uncertain whether the project will be finished within the agreed time horizon and at the agreed cost.  "),
                           (3,
                            "'(d) There are indications that the project will not be finished within the agreed time horizon and at the agreed cost. ")]

COMPLETION_GUARANTEES_AND_LIQUIDATED_DAMAGES_CHOICES = [(0,
                                                         '(a) Substantial liquidated damages supported by financial substance and/or strong completion guarantee from sponsors with excellent financial standing'),
                                                        (1,
                                                         "'(b) Significant liquidated damages supported by financial substance and/or completion guarantee from sponsors with good financial standing"),
                                                        (2,
                                                         "'(c) Adequate liquidated damages supported by financial substance and/or completion guarantee from sponsors with good financial standing"),
                                                        (3,
                                                         "'(d) Inadequate liquidated damages or not supported by financial substance or weak completion guarantees")]

CONTRACTOR_TRACK_RECORD_CHOICES = [(0, '(a) Strong'), (1, "'(b) Good"), (2, "'(c) Satisfactory"), (3, "'(d) Weak")]

O_AND_M_CONTRACT_CHOICES = [(0, '(a) Strong long-tem O and M contrac'),
                            (1, 'preferably with contractual performance incentive'),
                            (2, 'and/or O and M reserve accounts'), (3, "'(b) Long-term O and M contrac"),
                            (4, 'and/or O and M reserve accounts'),
                            (5, "'(c) Limited O and M contract or O and M reserve account"),
                            (6, "'(d) No O and M contract: risk of high operational cost overruns beyond mitigants")]

OPERATOR_TRACK_RECORD_CHOICES = [(0, '(a) Very stron'), (1, 'or committed technical assistance of the Sponsors'),
                                 (2, "'(b) Strong"), (3, "'(c) Acceptable"), (4, "'(d) Limited/wea"),
                                 (5, 'or local operator dependent on local authorities')]

REVENUE_CONTRACT_ROBUSTNESS_CHOICES = [(0, '(a) Excellent robustness of the revenues'),
                                       (1, "'(b)  Good robustness of the revenues"),
                                       (2, "'(c) Acceptable robustness of the revenues"), (3,
                                                                                           "'(d) The revenues of the project are not certain and there are indications that some of the revenues may not be obtained. ")]

OFFTAKE_CONTRACT_CASE_CHOICES = [(0,
                                  '(a) Excellent creditworthiness of off-taker; strong termination clauses; tenor of contract comfortably exceeds the maturity of the debt'),
                                 (1,
                                  "'(b) Good creditworthiness of off-taker; strong termination clauses; tenor of contract exceeds the maturity of the debt"),
                                 (2,
                                  "'(c) Acceptable financial standing of off-taker; normal termination clauses; tenor of contract generally matches the maturity of the debt"),
                                 (3,
                                  "'(d) Weak off-taker; weak termination clauses; tenor of contract does not exceed the maturity of the debt")]

NO_OFFTAKE_CONTRACT_CASE_CHOICES = [(0,
                                     '(a) Project produces essential services or a commodity sold widely on a world market; output can readily be absorbed at projected prices even at lower than historic market growth rates'),
                                    (1,
                                     "'(b) Project produces essential services or a commodity sold widely on a regional market that will absorb it at projected prices at historical growth rates"),
                                    (2,
                                     "'(c) Commodity is sold on a limited market that may absorb it only at lower than projected prices"),
                                    (3,
                                     "'(d) Project output is demanded by only one or a few buyers or is not generally sold on an organised market")]

SUPPLY_COST_RISKS_CHOICES = [(0, '(a) Long-term supply contract with supplier of excellent financial standing'),
                             (1, "'(b) Long-term supply contract with supplier of good financial standing"), (2,
                                                                                                              "'(c) Long-term supply contract with supplier of good financial standing\\n\\nA degree of price risk may remain"),
                             (3,
                              "'(d) Short-term supply contract or long-term supply contract with financially weak supplier \\n\\nA degree of price risk definitely remains")]

RESERVE_RISK_CHOICES = [(0, '(a) Independently audite'), (
1, 'proven and developed reserves well in excess of requirements over lifetime of the project'),
                        (2, "'(b) Independently audite"),
                        (3, 'proven and developed reserves in excess of requirements over lifetime of the project'),
                        (4, "'(c) Proven reserves can supply the project adequately through the maturity of the debt"),
                        (5, "'(d) Project relies to some extent on potential and undeveloped reserves")]

SPONSOR_FINANCIAL_STRENGTH_CHOICES = [(0, '(a) Strong sponsor with high financial standing'),
                                      (1, "'(b) Good sponsor with good financial standing"),
                                      (2, "'(c) Sponsor with adequate financial standing"),
                                      (3, "'(d) Weak sponsor with clear financial weaknesses")]

SPONSOR_TRACK_RECORD_CHOICES = [(0, '(a) Sponsor with excellent track record and country/sector experience'),
                                (1, "'(b) Good sponsor with satisfactory track record and country/sector experience"),
                                (2, "'(c) Adequate sponsor with adequate track record and country/sector experience"), (
                                3, "'(d) Weak sponsor with questionable track record and/or country/sector experience")]

SPONSOR_SUPPORT_CHOICES = [
    (0, '(a) Strong. Project is highly strategic for the sponsor (core business – long term strategy.'),
    (1, "'(b) Good. Project is strategic for the sponsor (core business – long term strategy."),
    (2, "'(c) Acceptable. Project is considered important for the sponsor (core business)"),
    (3, '"(d) Limited. Project is not key to sponsor\'s long term strategy or core business')]

ASSIGNMENT_OF_CONTRACTS_AND_ACCOUNTS_CHOICES = [(0, '(a) Fully comprehensive'), (1, "'(b) Comprehensive "),
                                                (2, "'(c) Acceptable"), (3, "'(d) Weak")]

PLEDGE_OF_ASSETS_CHOICES = [(0, '(a) First perfected security interest in all project asset'), (1, 'contract'),
                            (2, 'permits and accounts necessary to run the project'),
                            (3, "'(b) Perfected security interest in all project asset"), (4, 'contract'),
                            (5, 'permits and accounts necessary to run the project'),
                            (6, "'(c) Acceptable security interest in all project asset"), (7, 'contract'),
                            (8, 'permits and accounts necessary to run the project'),
                            (9, "'(d) Little security or collateral for lenders; weak negative pledge clause")]

CONTROL_OVER_CASH_FLOW_CHOICES = [(0, '(a) Strong'), (1, "'(b) Satisfactory "), (2, "'(c) Fair"), (3, "'(d) Weak")]

COVENANT_PACKAGE_CHOICES = [
    (0, '(a) Covenant package is strong for this type of project. \\n\\nProject may issue no additional debt'), (1,
                                                                                                                 "'(b) Covenant package is satisfactory for this type of project. \\n\\nProject may issue extremely limited additional debt"),
    (2, "'(c) Covenant package is fair for this type of project. \\n\\nProject may issue limited additional debt"), (3,
                                                                                                                     "'(d) Covenant package is Insufficient for this type of project. \\n\\nProject may issue unlimited additional debt")]

RESERVE_FUNDS_CHOICES = [(0, '(a) Longer than average coverage perio'),
                         (1, 'all reserve funds fully funded in cash or letters of credit from highly rated bank'),
                         (2, "'(b) Average coverage perio"), (3, 'all reserve funds fully funded'),
                         (4, "'(c) Average coverage all reserve funds all reserve funds fully funded"),
                         (5, "'(d) Shorter than average coverage perio"),
                         (6, 'reserve funds funded from operating cash flows')]

IMPACT_CATEGORY_CHOICES = [(0, '(a) Category A'), (1, "'(b) Category B"), (2, "'(c) Category C")]

LEGAL_TYPE_OF_PROJECT_CHOICES = [
    (0, '(a) Listed Corporate is a Corporate entity whose shares are quoted and traded on a Stock Exchange'),
    (1, "'(b) Unlisted Corporate is a Corporate entity whose shares are not quoted and traded on a stock exchange"),
    (2, "'(c) Listed Fund is a fund whose shares are quoted and traded on a Stock exchange"),
    (3, "'(d) Unlisted Fund is a fund whose shares are not quoted and traded on a Stock exchange"),
    (4, "'(e) Partnership is where the Sponsor constitutes a group of individuals who form a legal partnership"),
    (5, "'where profits and liabilities are shared"), (6, "'(f) Private Individual")]

ASSET_CLASS_CHOICES = [(0, '(a) Resi'), (1, "'(b) CRE"), (2, "'(c) SME/Corp"), (3, "'(d) Unsecured"), (4, "'(e) Auto"),
                       (5, "'(f) Leasing / ABF"), (6, "'(g) Specialised")]

PRODUCT_TYPE_CHOICES = [(0, '(a) Term Loans'), (1, "'(b) Revolving Credit Facility"), (2, "'(c) Overdraft")]

AMORTISATION_TYPE_CHOICES = [(0, '(a) Linear (L)'), (1, "'(b) Annuity (A)"),
                             (2, "'(c) Interest Only (IO) i.e. no amortisation with a bullet"),
                             (3, "'(d) Bespoke Repayment")]

ACCOUNTING_STAGES_OF_ASSET_QUALITY_CHOICES = [(0, '(a) IFRS Stage 1'), (1, "'(b) IFRS Stage 2"),
                                              (2, "'(c) IFRS Stage 3 (Impaired)"),
                                              (3, "'(d) Fair Value Through P rofit and Loss"),
                                              (4, "'(e) Other Accounting Standard – Impaired Asset"),
                                              (5, "'(f) Other Accounting Standard – Not Impaired")]

ORIGINAL_INTEREST_RATE_TYPE_CHOICES = [(0, '(a) Fixed'), (1, "'(b) Variable"), (2, "'(c) Mixed")]

ORIGINAL_INTEREST_RATE_REFERENCE_CHOICES = [(0, '(a) 1m EURIBOR'), (1, "'(b) 3m EURIBOR"), (2, "'(c) 6m EURIBOR"),
                                            (3, "'(d) 1m LIBOR"), (4, "'(e) 3m LIBOR"), (5, "'(f) 6m LIBOR"),
                                            (6, "'(g) Standard Variable Rate (SVR)"), (7, "'(h) EONIA")]

CURRENT_INTEREST_RATE_TYPE_CHOICES = [(0, '(a) Fixed'), (1, "'(b) Variable"), (2, "'(c) Mixed")]

CURRENT_INTEREST_RATE_REFERENCE_CHOICES = [(0, '(a) 1m EURIBOR'), (1, "'(b) 3m EURIBOR"), (2, "'(c) 6m EURIBOR"),
                                           (3, "'(d) 1m LIBOR"), (4, "'(e) 3m LIBOR"), (5, "'(f) 6m LIBOR"),
                                           (6, "'(g) Standard Variable Rate (SVR)"), (7, "'(h) EONIA")]

INTEREST_PAYMENT_FREQUENCY_CHOICES = [(0, '(a) Monthly'), (1, "'(b) Quarterly"), (2, "'(c) Semi-Annually"),
                                      (3, "'(d) Annually"), (4, "'(e) Daily"), (5, "'(f) Other")]

PRINCIPAL_PAYMENT_FREQUENCY_CHOICES = [(0, '(a) Monthly'), (1, "'(b) Quarterly"), (2, "'(c) Semi-Annually"),
                                       (3, "'(d) Annually"), (4, "'(e) Daily"), (5, "'(f) Other")]

LOAN_COVENANTS_CHOICES = [
    (0, '(a) Loan to Value (LTV) is the ratio of a loan to the value of the collateral purchased'), (1,
                                                                                                     "'(b) Interest Coverage Ratio (ICR) is the ratio of earnings before interest and tax to the interest expense in the same period"),
    (2,
     "'(c) Debt Service Coverage Ratio (DSCR) is the ratio of annual net operating income to debt obligations owed in the last 12m"),
    (3, "'(d) Other")]

TYPE_OF_LEGAL_OWNER_CHOICES = [
    (0, '(a) Listed Corporate is a Corporate entity whose shares are quoted and traded on a Stock Exchange'),
    (1, "'(b) Unlisted Corporate is a Corporate entity whose shares are not quoted and traded on a stock exchange"),
    (2, "'(c) Listed Fund is a fund whose shares are quoted and traded on a Stock exchange"),
    (3, "'(d) Unlisted Fund is a fund whose shares are not quoted and traded on a Stock exchange"), (4,
                                                                                                     "'(e) Partnership is where the Sponsor constitutes a group of individuals who form a legal partnership where profits and liabilities are shared"),
    (5, "'(f) Private Individual")]

COLLATERAL_TYPE_CHOICES = [(0, '(a) Auto Mobile Vehicles'), (1, "'(b) Industrial Vehicles"),
                           (2, "'(c) Commercial Trucks"), (3, "'(d) Rail Vehicles"),
                           (4, "'(e) Nautical Commercial Vehicles"), (5, "'(f) Nautical Leisure Vehicles"),
                           (6, "'(g) Aeroplanes"), (7, "'(h) Machine Tools"), (8, "'(i) Industrial Equipment"),
                           (9, "'(j) Office Equipment"), (10, "'(k) Medical Equipment"),
                           (11, "'(l) Energy Related Equipment"), (12, "'(m) Other Vehicles"),
                           (13, "'(n) Other Equipment"), (14, "'(o) Other goods/inventory"), (15, "'(p) Securities"),
                           (16, "'(q) Guarantee"), (17, "'(r) Life insurance"), (18, "'(s) Deposit"),
                           (19, "'(t) Floating Charge"), (20, "'(u) Other financial asset")]

TYPE_OF_INITIAL_VALUATION_CHOICES = [(0, '(a) Full Appraisal'), (1, "'(b) Drive-by"),
                                     (2, "'(c) Automated Valuation Model"), (3, "'(d) Indexed"), (4, "'(e) Desktop"),
                                     (5, "'(f) Managing or Estate Agent"), (6, "'(g) Purchase Price"),
                                     (7, "'(h) Hair Cut"), (8, "'(i) Mark to market"),
                                     (9, "'(j) Counterparties Valuation"), (10, "'(k) Other")]

TYPE_OF_LATEST_VALUATION_CHOICES = [(0, '(a) Full Appraisal'), (1, "'(b) Drive-by"),
                                    (2, "'(c) Automated Valuation Model"), (3, "'(d) Indexed"), (4, "'(e) Desktop"),
                                    (5, "'(f) Managing or Estate Agent"), (6, "'(g) Purchase Price"),
                                    (7, "'(h) Hair Cut"), (8, "'(i) Mark to market"),
                                    (9, "'(j) Counterparties Valuation"), (10, "'(k) Other")]

NEW_OR_USED_CHOICES = [(0, '(a) New'), (1, "'(b) Used")]

TYPE_OF_SWAP_CHOICES = [(0, '(a) Interest Rate Swap'), (1, "'(b) Currency Swap"), (2, "'(c) Credit Default swap")]

BASIS_OF_FINANCIAL_STATEMENTS_CHOICES = [(0, '(a) IFRS'), (1, "'(b) National GAAP"), (2, "'(c) Other")]

FINANCIAL_STATEMENTS_TYPE_CHOICES = [(0, '(a) Consolidated'), (1, "'(b) Project level")]
