# Copyright (c) 2020 - 2024 Open Risk (https://www.openriskmanagement.com)
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


import json

import pandas as pd
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.db.models import Sum
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.urls import reverse_lazy

from portfolio.Asset import ProjectAsset
from portfolio.Contractor import Contractor
from portfolio.EmissionsSource import GPCEmissionsSource, BuildingEmissionsSource
from portfolio.EmissionsSource import GPPEmissionsSource
from portfolio.PortfolioManager import PortfolioManager
from portfolio.Portfolios import ProjectPortfolio
from portfolio.Project import Project
from portfolio.ProjectActivity import ProjectActivity
from portfolio.ProjectEvent import ProjectEvent
from portfolio.models import MultiAreaSource
from reference.NUTS3Data import NUTS3PointData
from reporting.forms import CustomPortfolioAggregatesForm, portfolio_attributes, aggregation_choices
from reporting.models import Calculation, SummaryStatistics, AggregatedStatistics, Visualization

"""

## other

*  Project Asset
*  Building
*  Point Source
*  Area Source
*  Multi Area Source
*  Portfolio Snapshot
*  Portfolio Data
*  Limit Structure
*  Emissions Source
*  GPC Emissions Source
*  Building Emissions Source
*  Borrower
*  Loan
*  Mortgage
*  Operator
*  Project Category
*  Project Company
*  Revenue
*  Primary Effect
*  Secondary Effect
*  Sponsor
*  Stakeholder
*  Swap

"""


@login_required(login_url='/login/')
def portfolio_overview(request):
    t = loader.get_template('reporting/portfolio_overview.html')
    context = RequestContext(request, {})

    """
    Compile a global portfolio overview of all data sets available the database

    ## Focus of this view is on procurement data
    
    *  Portfolio Manager
    *  Project Portfolio
    *  GPP Emissions Source
    *  Contractor
    *  Project Activity
    *  Project

    """

    pm_count = PortfolioManager.objects.count()
    po_count = ProjectPortfolio.objects.count()
    pr_count = Project.objects.count()
    pe_count = ProjectEvent.objects.count()
    pa_count = ProjectActivity.objects.count()
    co_count = Contractor.objects.count()
    gpp_count = GPPEmissionsSource.objects.count()
    as_count = ProjectAsset.objects.count()
    geo_count = MultiAreaSource.objects.count()

    context.update({'pm_count': pm_count,
                    'po_count': po_count,
                    'gpp_count': gpp_count,
                    'pe_count': pe_count,
                    'co_count': co_count,
                    'as_count': as_count,
                    'pa_count': pa_count,
                    'geo_count': geo_count,
                    'pr_count': pr_count})

    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def portfolio_summary(request, pk):
    """
    TODO

    Display an individual `portfolio.Portfolio`.
    Fetch additional data associated with the portfolio
    Invoke function to Compute Portfolio statistics
    - Total number of rows
    - Total exposure
    - Average rating etc.

    **Context**

    ``Portfolio``
        An instance of `portfolio.Portfolio`.

    **Template:**

    `portfolio/portfolio_summary.html`
    """

    portfolio_queryset = None
    try:
        p = ProjectPortfolio.objects.get(pk=pk)
    except ProjectPortfolio.DoesNotExist:
        raise Http404("Portfolio does not exist")

    try:
        project_queryset = ProjectPortfolio.objects.filter(portfolio_id=pk)
    except ProjectPortfolio.DoesNotExist:
        raise Http404("PortfolioData does not exist")

    # Insert into dataframe for statistics
    portfolio_dataframe = pd.DataFrame.from_records(portfolio_queryset.values())

    # Aggregates
    obligor_count = portfolio_dataframe.shape[0]
    total_exposure = portfolio_dataframe['EAD'].sum()

    # TODO Round digits
    pstats = portfolio_dataframe[['EAD', 'LGD', 'Tenor', 'Sector', 'Rating', 'Country', 'Stage']].describe().to_html()

    t = loader.get_template('reporting/portfolio_summary.html')
    context = RequestContext(request, {})
    context.update({'portfolio': p, 'pstats': pstats})
    context.update({'obligor_count': obligor_count, 'total_exposure': total_exposure})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def portfolio_aggregates(request):
    """
    TODO

    Create a custom aggregation report on the basis of form input fields
    Aggregation Function to Apply
    Field to Aggregate

    :param request:
    :return:
    """
    # TODO
    success_url = reverse_lazy('portfolio/portfolio_list')

    result_data = {}
    result_label = {}

    if request.method == 'POST':

        form = CustomPortfolioAggregatesForm(request.POST)
        form.is_valid()
        Attribute = portfolio_attributes[int(form.cleaned_data['attribute'])][1]
        Aggregator_Function = aggregation_choices[int(form.cleaned_data['aggregator_function'])][1]
        print('GLOBALS: ', globals())

        # convert the aggregator function string to a class object
        Method = globals()[Aggregator_Function]
        # result_data = Portfolio.objects.aggregate(Avg('portfoliodata__EAD'))
        #
        aggregation_string = 'portfoliodata__' + Attribute
        result_data = ProjectPortfolio.objects.annotate(aggregated=Method(aggregation_string))
        result_label = Aggregator_Function + ' ' + Attribute

    else:
        form = CustomPortfolioAggregatesForm()


@login_required(login_url='/login/')
def portfolio_stats_view(request):
    """

    Generate aggregate statistics about the total portfolio.

    year
    country
    sector
    contracts
    currency
    value_total
    """

    portfolio_queryset = SummaryStatistics.objects.all()
    portfolio_dataframe = pd.DataFrame.from_records(portfolio_queryset.values())
    print(portfolio_dataframe.head())

    stats_view = {}
    for attr in ['year', 'country', 'sector', 'currency']:
        # Group Count by attribute
        pstats = portfolio_dataframe.groupby([attr], as_index=True).size().reset_index(name='value_total')
        N = pstats['value_total'].sum()
        # Calculate Percentage
        pstats['%'] = round(100 * pstats['value_total'] / N, 1)
        pstats.set_index(attr)
        stats_view[attr] = pstats.to_html(index=False)

    t = loader.get_template('reporting/portfolio_stats_view.html')
    context = RequestContext(request, {})
    context.update({'stats_view': stats_view, 'portfolio_data': portfolio_queryset})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def credit_portfolio_stats_view(request, pk):
    """
    TODO

    Generate aggregate statistics about the portfolio.
    """

    try:
        p = ProjectPortfolio.objects.get(pk=pk)
    except ProjectPortfolio.DoesNotExist:
        raise Http404("Portfolio does not exist")

    try:
        portfolio_queryset = ProjectPortfolio.objects.filter(portfolio_id=pk)
    except ProjectPortfolio.DoesNotExist:
        raise Http404("PortfolioData does not exist")

    portfolio_dataframe = pd.DataFrame.from_records(portfolio_queryset.values())

    # TODO Improve headers
    stats_view = {}
    for attr in ['Tenor', 'LGD', 'Rating', 'Stage', 'Country', 'Sector']:
        # Group Count by attribute
        pstats = portfolio_dataframe.groupby([attr], as_index=True).size().reset_index(name='Count')
        N = pstats['Count'].sum()
        # Calculate Percentage
        pstats['%'] = pstats['Count'] / N
        pstats.set_index(attr)
        stats_view[attr] = pstats.to_html(index=False)

    t = loader.get_template('reporting/credit_portfolio_stats_view.html')
    context = RequestContext(request, {})
    context.update({'portfolio': p, 'stats_view': stats_view, 'portfolio_data': portfolio_queryset})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def pcaf_mortgage_report(request):
    t = loader.get_template('reporting/pcaf_mortgage_report.html')
    context = RequestContext(request, {})

    """ Construct a PCAF Mortgage Emissions report and a Portfolio Carbon Footprint
    
    Select Emissions Sources where the asset is Residential Building
    asset.asset_class = 0
    
    Aggregate total emission per asset (sum of emissions sources, weighted average DQ score)
    
    
    Select Loans that are 
    - Residential Mortgages (asset_class == 0)
    - with total_balance > 0

    """

    for be in BuildingEmissionsSource.objects.all():
        print(80 * '=')
        print(be.asset.loan_identifier.counterparty_identifier)
        print(be.asset.loan_identifier)
        print(be.asset.loan_identifier.legal_balance)
        print(be.asset.initial_valuation_amount)
        print(be.asset.building_area_m2)
        print(be.emissions_factor.Emission_factor)

    table_header = []
    table_header.append('Borrower')
    table_header.append('Loan')
    table_header.append('Legal Balance')
    table_header.append('Building')
    table_header.append('Initial Valuation')
    table_header.append('Area')
    table_header.append('Emission Factor')
    table_header.append('Attribution Factor')
    table_header.append('Financed Emissions')

    table_rows = {}
    key = 0
    for be in BuildingEmissionsSource.objects.all():
        value = []
        value.append(be.asset.loan_identifier.counterparty_identifier)
        value.append(be.asset.loan_identifier)
        value.append(be.asset.loan_identifier.legal_balance)
        value.append(be.asset_id)
        value.append(be.asset.initial_valuation_amount)
        value.append(be.asset.building_area_m2)
        value.append(be.emissions_factor.Emission_factor)
        value.append(be.asset.loan_identifier.legal_balance / be.asset.initial_valuation_amount)
        value.append(be.asset.building_area_m2 * be.emissions_factor.Emission_factor)
        table_rows[key] = value
        key += 1
        print(key, value)

    context.update({'TableHeader': table_header})
    context.update({'TableRows': table_rows})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def ghg_reduction(request):
    t = loader.get_template('reporting/ghg_reduction.html')
    context = RequestContext(request, {})

    activities = ProjectActivity.objects.all()

    table_header = []
    table_header.append('Project')
    table_header.append('Project Activity')
    table_header.append('Activity Emissions')
    table_header.append('Baseline Emissions')
    table_header.append('GHG Reduction')

    table_rows = {}
    key = 0

    if len(activities) > 0:
        for pa in ProjectActivity.objects.all():
            value = []
            if pa.project:
                value.append(pa.project.project_identifier)
            else:
                value.append(None)
            value.append(pa.project_activity_identifier)
            value.append(pa.project_activity_emissions)
            value.append(pa.baseline_activity_emissions)
            if pa.baseline_activity_emissions and pa.project_activity_emissions:
                value.append(pa.baseline_activity_emissions - pa.project_activity_emissions)
            else:
                value.append(None)
            table_rows[key] = value
            key += 1
            # print(key, value)

    context.update({'TableHeader': table_header})
    context.update({'TableRows': table_rows})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def scope_2_report(request):
    t = loader.get_template('reporting/scope_2_report.html')
    context = RequestContext(request, {})

    activities = ProjectActivity.objects.all()

    table_header = []
    table_header.append('Project')
    table_header.append('Project Activity')
    table_header.append('Activity Emissions')
    table_header.append('Baseline Emissions')
    table_header.append('GHG Reduction')

    table_rows = {}
    key = 0

    if len(activities) > 0:
        for pa in ProjectActivity.objects.all():
            value = []
            if pa.project:
                value.append(pa.project.project_identifier)
            else:
                value.append(None)
            value.append(pa.project_activity_identifier)
            value.append(pa.project_activity_emissions)
            value.append(pa.baseline_activity_emissions)
            if pa.baseline_activity_emissions and pa.project_activity_emissions:
                value.append(pa.baseline_activity_emissions - pa.project_activity_emissions)
            else:
                value.append(None)
            table_rows[key] = value
            key += 1
            # print(key, value)

    context.update({'TableHeader': table_header})
    context.update({'TableRows': table_rows})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def project_nuts3_map(request):
    t = loader.get_template('reporting/portfolio_map.html')
    context = RequestContext(request, {})

    """
    Compile a global portfolio map of portfolio projects using their NUTS3 representative point geometries

    """

    portfolio_data = Project.objects.all()
    nuts_data = []
    iter = 1
    for co in portfolio_data.iterator():
        nuts = co.region
        if iter < 100:
            try:
                nuts_data.append(NUTS3PointData.objects.get(nuts_id=nuts))
            except:
                pass
            iter += 1
        else:
            break
    geodata = json.loads(serialize("geojson", nuts_data))
    context.update({'geodata': geodata})

    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def manager_nuts3_map(request):
    t = loader.get_template('reporting/portfolio_map.html')
    context = RequestContext(request, {})

    """
    Compile a global portfolio map of portfolio managing entities using their NUTS3 representative point geometries

    """

    # ATTN this is not performant for interactive use due to the large number of lookups
    # TODO pre-process geometric elements per mappable entity

    portfolio_data = PortfolioManager.objects.all()
    nuts_data = []
    iter = 1
    marker_limit = 3000  # avoid loading huge datasets

    for co in portfolio_data.iterator():
        nuts = co.region
        if iter < marker_limit:
            try:
                nuts_data.append(NUTS3PointData.objects.get(nuts_id=nuts))
            except:
                pass
            iter += 1
        else:
            break
    geodata = json.loads(serialize("geojson", nuts_data))
    context.update({'geodata': geodata})

    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def contractor_nuts3_map(request):
    t = loader.get_template('reporting/portfolio_map.html')
    context = RequestContext(request, {})

    # ATTN this is not performant for interactive use due to the large number of lookups
    # TODO pre-process geometric elements per mappable entity

    """
    Compile a global portfolio map of contractor entities using their NUTS3 representative point geometries

    """

    marker_limit = 3000  # avoid loading huge datasets

    # geometry = json.loads(serialize("geojson", PointSource.objects.all()))
    # geometry = json.loads(serialize("geojson", AreaSource.objects.all()))
    # geodata = json.loads(serialize("geojson", NUTS3PointData.objects.all()))
    portfolio_data = Contractor.objects.all()
    nuts_data = []
    iter = 1
    for co in portfolio_data.iterator():
        nuts = co.region
        if iter < marker_limit:
            try:
                nuts_data.append(NUTS3PointData.objects.get(nuts_id=nuts))
            except:
                pass
            iter += 1
        else:
            break
    geodata = json.loads(serialize("geojson", nuts_data))
    context.update({'geodata': geodata})

    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def gpp_report(request):
    t = loader.get_template('reporting/gpp_report.html')
    context = RequestContext(request, {})

    """
    Create a report of all GPP emissions sources in the global portfolios
    """

    table_header = []
    table_header.append('Project Title')
    table_header.append('Budget (EUR)')
    table_header.append('Sector')
    table_header.append('Country')
    table_header.append('CO2 (Tonnes)')

    table_rows = {}
    key = 0
    for source in GPPEmissionsSource.objects.all()[:100]:
        value = []
        value.append(source.project.project_title)
        value.append(source.project.project_budget)
        value.append(source.project.cpa_code)
        value.append(source.project.country)
        value.append(source.co2_amount)
        table_rows[key] = value
        key += 1

    context.update({'TableHeader': table_header})
    context.update({'TableRows': table_rows})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def gpc_report(request):
    t = loader.get_template('reporting/gpc_report.html')
    context = RequestContext(request, {})

    """
    1. GPC Reference Number in the format: I.X.X which identifies the GHG Emissions Sources at the level of granularity required by the GPC
    2. Applicable GHG Emission Scope (Numerical: 1, 2, 3). This is linked to the GPC Reference Number (Emissions) Sector/Subsector classifying GHG Emissions Sources according the GPC GHG Emissions Taxonomy (Stationary Energy, Transportation, etc)
    3. GHG Notation Keys (NO, IE, etc. providing context for the included or missing data)
    4. Mass of Greenhouse Gas Emissions per Gas Species (and total CO2e)
    CO2, CH4,  N2O,  HFC,  PFC,  SF6,  NF3, Total CO2e,  CO2(b)
    5. Data Quality assessment for both Activity Data and GHG Emission Factor (H, M, L Scale), AD,  EFD
    6. Explanatory comments (i.e. description of methods or notation keys used)
    
    """

    table_header = []
    table_header.append('GPC Ref No')
    table_header.append('Scope')
    table_header.append('Name')
    table_header.append('Notation Key')
    table_header.append('GHG Reduction')

    table_rows = {}
    key = 0
    for pa in GPCEmissionsSource.objects.all():
        value = []
        value.append(pa.gpc_subsector.gpc_ref_no)
        value.append(pa.gpc_subsector.gpc_scope)
        value.append(pa.gpc_subsector.name)
        value.append(pa.notation_key)
        value.append(pa.co2_amount)
        value.append(pa.ch4_amount)
        value.append(pa.n2o_amount)
        value.append(pa.hfc_amount)
        value.append(pa.pfc_amount)
        value.append(pa.sf6_amount)
        value.append(pa.nf3_amount)
        value.append(pa.tco2e_amount)
        value.append(pa.co2b_amount)
        value.append(pa.AD_DQ)
        value.append(pa.EF_DQ)
        value.append(pa.comments)
        table_rows[key] = value
        key += 1
        print(key, value)

    context.update({'TableHeader': table_header})
    context.update({'TableRows': table_rows})
    return HttpResponse(t.template.render(context))


# @login_required(login_url='/login/')
# def result_types(request):
#     t = loader.get_template('reporting/result_types.html')
#     context = RequestContext(request, {})
#
#     # create a table with model result mode information
#     # header row
#     table_header = []
#     table_header.append('Result Type ID')
#     table_header.append('Name')
#     for key, entry in ModelModesShort.items():
#         table_header.append(entry)
#     table_header.append('Description')
#
#     table_rows = {}
#     for key, entry in ReportingModeName.items():
#         value = []
#         value.append(key)
#         value.append(ReportingModeName[key])
#         matched_modes = ReportingModeMatch[key]
#         for i in range(len(matched_modes)):
#             if matched_modes[i] == 0:
#                 value.append('N')
#             elif matched_modes[i] == 1:
#                 value.append('Y')
#             else:
#                 print('ERROR in MODE')
#         value.append(ReportingModeDescription[key])
#         table_rows[key] = value
#
#     context.update({'ModelModes': ModelModes})
#     context.update({'TableRows': table_rows})
#     context.update({'TableHeader': table_header})
#     return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def results_view(request, pk):
    try:
        R = Calculation.objects.get(pk=pk)
    except Calculation.DoesNotExist:
        raise Http404("Calculation does not exist")

    t = loader.get_template('reporting/result_view.html')
    context = RequestContext(request, {})
    context.update({'Result': json.dumps(R.results_data)})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def visualization_grid(request):
    """
    Visualization - Country-Sector Grid View

    """
    img_list_raw = ['A_Agriculture.svg',
                    'B_Mining.svg',
                    'C_Manufacture.svg',
                    'D_Electricity.svg',
                    'E_Water.svg',
                    'F_Construction.svg',
                    'G_Trading.svg',
                    'H_Transport.svg',
                    'I_Accommodation.svg',
                    'J_ICT.svg',
                    'K_Finance.svg',
                    'L_RealEstate.svg',
                    'M_Professional.svg',
                    'N_Administrative.svg',
                    'O_PublicSector.svg',
                    'P_Education.svg',
                    'Q_Health.svg',
                    'R_Recreation.svg',
                    'S_OtherServices.svg',
                    'T_Households.svg',
                    'U_NGO.svg'
                    ]

    name_list = [s[2:-4] for s in img_list_raw]
    entries = AggregatedStatistics.objects.all()
    countryset = [x[0] for x in AggregatedStatistics.objects.all().values_list('country').distinct()]
    sectorset = [x[0] for x in AggregatedStatistics.objects.all().values_list('sector').distinct()]
    countryset.sort()
    sectorset.sort()

    values = {}
    my_countries = {}
    sectors = {}
    for entry in entries:
        i = countryset.index(entry.country)
        j = sectorset.index(entry.sector)
        my_countries[i] = entry.country.code
        sectors[j] = entry.sector
        if entry.co2_amount:
            values[(i, j)] = entry.co2_amount
        else:
            values[(i, j)] = 0

    s_keys = list(my_countries.keys())
    s_keys.sort()
    s_countries = {}
    for key in s_keys:
        s_countries[key] = my_countries[key]

    s_keys = list(sectors.keys())
    s_keys.sort()
    s_sectors = {}
    for key in s_keys:
        s_sectors[key] = sectors[key]

    t = loader.get_template('reporting/visualization_grid.html')
    context = RequestContext(request, {})
    context.update({'img_list': img_list_raw, 'name_list': name_list})
    context.update({'values': values, 'sectors': s_sectors, 'my_countries': s_countries})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def visualization_country(request):
    """
    Visualization - Country View

    """

    dataset = {}

    # aggregate over sectors and years
    entries = SummaryStatistics.objects.values('country').annotate(Sum('value_total'))

    for full_entry in entries:
        entry = {}
        if full_entry['country']:
            dataid = full_entry['country']
            entry['values'] = full_entry['value_total__sum']
            dataset[dataid] = entry

    t = loader.get_template('reporting/visualization_country.html')
    context = RequestContext(request, {})
    context.update({'dataset': json.dumps(dataset)})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def visualization_sector(request):
    """
    Visualization - Sector View

    """
    dataset = {}

    # aggregate over countries and years
    entries = SummaryStatistics.objects.values('sector').annotate(Sum('value_total'))

    # aggregate further EEIO sectors to top-level CPA/NACE sectors
    # some ad-hoc scaling
    top_level = {}
    total = 0
    for entry in entries:
        dataid = entry['sector'][:1]
        if dataid in top_level.keys():
            top_level[dataid] += entry['value_total__sum']
            total += entry['value_total__sum']
        else:
            top_level[dataid] = entry['value_total__sum']
            total += entry['value_total__sum']

    for entry in top_level:
        top_level[entry] = top_level[entry] * 100 / total
    print(top_level)

    img_list_raw = ['A_Agriculture.svg', 'I_Accommodation.svg', 'P_Education.svg',
                    'B_Mining.svg', 'J_ICT.svg', 'Q_Health.svg',
                    'C_Manufacture.svg', 'K_Finance.svg', 'R_Recreation.svg',
                    'D_Electricity.svg', 'L_RealEstate.svg', 'S_OtherServices.svg',
                    'E_Water.svg', 'M_Professional.svg', 'T_Households.svg',
                    'F_Construction.svg', 'N_Administrative.svg', 'U_NGO.svg',
                    'G_Trading.svg', 'O_PublicSector.svg', 'H_Transport.svg'
                    ]

    img_list = [(s, s[:1], s[2:-4]) for s in img_list_raw]

    t = loader.get_template('reporting/visualization_sector.html')
    context = RequestContext(request, {})
    context.update({'img_list': img_list})
    context.update({'dataset': top_level})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def visualization_vega(request, pk):
    """

    """

    # get the Visualization object
    visualization = Visualization.objects.get(pk=pk)
    context = RequestContext(request, {})

    t = loader.get_template('vega_viz.html')
    spec = json.dumps(visualization.vega_specification)
    data = json.dumps(visualization.visualization_data)
    context.update({'object': visualization})
    context.update({'visualization_data': data})
    context.update({'vega_specification': spec})

    return HttpResponse(t.template.render(context))
