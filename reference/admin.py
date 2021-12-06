from django.contrib import admin

from reference.EmissionFactor import EmissionFactor


@admin.register(EmissionFactor)
class EmissionFactorAdmin(admin.ModelAdmin):

    """Emission Factor admin"""
    view_on_site = False
    search_fields = ['Description', 'Gases', 'Fuel']
    list_display = ('EF_ID', 'IPCC_Category', 'Gases', 'Fuel', 'Parameter_Type', 'Description')
    list_filter = ('Gases', 'Fuel', 'Parameter_Type')

    fieldsets = (
        ('Identification', {
            'fields': ('EF_ID', 'IPCC_Category', 'Gases', 'Fuel', 'Parameter_Type', 'Description')
        }),
        ('Practices/Conditions', {
            'fields': ('Technology_Practices', 'Parameter_Conditions', 'Regional_Conditions', 'Control_Technologies',
                       'Other_Properties'),
        }),
        ('Quantitative', {
            'fields': ('Value', 'Unit', 'Lower_Bound', 'Upper_Bound', 'Equation', 'Data_Quality'),
        }),
        ('Reference', {
            'fields': (
                'Data_Source', 'Technical_Reference', 'Data_Quality_Reference', 'Data_Provider', 'Link'),
        }),
        ('Other', {
            'fields': (
                'IPCC_Worksheet', 'English_Abstract', 'Other_Data_Quality', 'Data_Provider_Comments', 'Other_Comments'),
        }),
    )
