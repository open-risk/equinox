import json

from django.core.serializers import serialize

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext, loader

from model_server.models import ReportingModeDescription, ReportingModeMatch, \
    ReportingModeName, ModelModes, ModelModesShort
from portfolio.EmissionsSource import GPCEmissionsSource, BuildingEmissionsSource, GPPEmissionsSource
from portfolio.ProjectActivity import ProjectActivity
from portfolio.Project import Project
from portfolio.models import AreaSource, PointSource
from reporting.models import Calculation, Visualization

root_view = settings.ROOT_VIEW


@login_required(login_url='/login/')
def pcaf_mortgage_report(request):
    t = loader.get_template('pcaf_mortgage_report.html')
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
        print(80*'=')
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
    t = loader.get_template('ghg_reduction.html')
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
def portfolio_map(request):
    t = loader.get_template('portfolio_map.html')
    context = RequestContext(request, {})

    """
    Compile a portfolio map

    """

    # geometry = json.loads(serialize("geojson", PointSource.objects.all()))
    geometry = json.loads(serialize("geojson", AreaSource.objects.all()))
    context.update({'geometry': geometry})

    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def gpp_report(request):
    t = loader.get_template('gpp_report.html')
    context = RequestContext(request, {})

    """

    """

    table_header = []
    table_header.append('Project Title')
    table_header.append('Budget (EUR)')
    table_header.append('CPV')
    table_header.append('CO2 (Tonnes)')

    table_rows = {}
    key = 0
    for source in GPPEmissionsSource.objects.all():
        pr = source.project
        value = []
        value.append(pr.project_title)
        value.append(pr.project_budget)
        value.append(pr.cpv_code)
        value.append(source.co2_amount)
        table_rows[key] = value
        key += 1

    context.update({'TableHeader': table_header})
    context.update({'TableRows': table_rows})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def gpc_report(request):
    t = loader.get_template('gpc_report.html')
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


@login_required(login_url='/login/')
def result_types(request):
    t = loader.get_template('result_types.html')
    context = RequestContext(request, {})

    # create a table with model result mode information
    # header row
    table_header = []
    table_header.append('Result Type ID')
    table_header.append('Name')
    for key, entry in ModelModesShort.items():
        table_header.append(entry)
    table_header.append('Description')

    table_rows = {}
    for key, entry in ReportingModeName.items():
        value = []
        value.append(key)
        value.append(ReportingModeName[key])
        matched_modes = ReportingModeMatch[key]
        for i in range(len(matched_modes)):
            if matched_modes[i] == 0:
                value.append('N')
            elif matched_modes[i] == 1:
                value.append('Y')
            else:
                print('ERROR in MODE')
        value.append(ReportingModeDescription[key])
        table_rows[key] = value

    context.update({'ModelModes': ModelModes})
    context.update({'TableRows': table_rows})
    context.update({'TableHeader': table_header})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def results_view(request, pk):
    try:
        R = Calculation.objects.get(pk=pk)
    except Calculation.DoesNotExist:
        raise Http404("Calculation does not exist")

    t = loader.get_template('result_view.html')
    context = RequestContext(request, {})
    context.update({'root_view': root_view, 'Result': json.dumps(R.results_data)})
    return HttpResponse(t.template.render(context))


@login_required(login_url='/login/')
def visualization_view(request, pk):
    """
    Interactive modification / calculation of Visualizations using Ajax calls

    **Context**

    ``Visualization``
        An instance of :model:`reporting.Visualization`.

    **Template:**

    :template:`reporting/Visualization_interactive.html`
    """

    # get the Visualization object
    visualization = Visualization.objects.get(pk=pk)
    t = loader.get_template('visualization.html')
    context = RequestContext(request, {})
    context.update({'root_view': root_view, 'object': visualization})
    return HttpResponse(t.template.render(context))
