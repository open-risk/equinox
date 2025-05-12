# Copyright (c) 2020 - 2025 Open Risk (https://www.openriskmanagement.com)
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


# from django_countries.fields import CountryField


class EmissionFactor(models.Model):
    """
    The Emissions Factor model holds IPCC reference data (EFDB database) about activity related emission factors


    """

    EF_ID = models.IntegerField(blank=True, null=True,
                                help_text='Standard Description')

    IPCC_Category = models.CharField(max_length=80, blank=True, null=True,
                                     help_text='Standard Description')

    Gases = models.CharField(max_length=80, blank=True, null=True,
                             help_text='Standard Description')

    Fuel = models.CharField(max_length=80, blank=True, null=True,
                            help_text='Standard Description')

    Parameter_Type = models.CharField(max_length=80, blank=True, null=True,
                                      help_text='Standard Description')

    Description = models.TextField(blank=True, null=True,
                                   help_text='Standard Description')

    Technology_Practices = models.CharField(max_length=80, blank=True, null=True,
                                            help_text='Standard Description')

    Parameter_Conditions = models.CharField(max_length=80, blank=True, null=True,
                                            help_text='Standard Description')

    Regional_Conditions = models.CharField(max_length=80, blank=True, null=True,
                                           help_text='Standard Description')

    Control_Technologies = models.CharField(max_length=80, blank=True, null=True,
                                            help_text='Standard Description')

    Other_Properties = models.CharField(max_length=80, blank=True, null=True,
                                        help_text='Standard Description')

    Value = models.CharField(max_length=20, blank=True, null=True,
                             help_text='Standard Description')

    Unit = models.CharField(max_length=20, blank=True, null=True,
                            help_text='Standard Description')

    Equation = models.CharField(max_length=80, blank=True, null=True,
                                help_text='Standard Description')

    IPCC_Worksheet = models.CharField(max_length=80, blank=True, null=True,
                                      help_text='Standard Description')

    Data_Source = models.CharField(max_length=80, blank=True, null=True,
                                   help_text='Standard Description')

    Technical_Reference = models.CharField(max_length=80, blank=True, null=True,
                                           help_text='Standard Description')

    English_Abstract = models.CharField(max_length=80, blank=True, null=True,
                                        help_text='Standard Description')

    Lower_Bound = models.CharField(max_length=20, blank=True, null=True,
                                   help_text='Standard Description')

    Upper_Bound = models.CharField(max_length=20, blank=True, null=True,
                                   help_text='Standard Description')

    Data_Quality = models.CharField(max_length=80, blank=True, null=True,
                                    help_text='Standard Description')

    Data_Quality_Reference = models.CharField(max_length=80, blank=True, null=True,
                                              help_text='Standard Description')

    Other_Data_Quality = models.CharField(max_length=80, blank=True, null=True,
                                          help_text='Standard Description')

    Data_Provider_Comments = models.CharField(max_length=80, blank=True, null=True,
                                              help_text='Standard Description')

    Other_Comments = models.CharField(max_length=80, blank=True, null=True,
                                      help_text='Standard Description')

    Data_Provider = models.CharField(max_length=80, blank=True, null=True,
                                     help_text='Standard Description')

    Link = models.URLField(blank=True, null=True,
                           help_text='Standard Description')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.EF_ID)

    def get_absolute_url(self):
        return reverse('reference:EmissionFactor_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Emissions Factor"
        verbose_name_plural = "Emissions Factors"


class BuildingEmissionFactor(models.Model):
    """
    The Building Emissions Factor model holds EF reference data about emission factors compiled by PCAF

    `ORM Docs <https://www.openriskmanual.org/wiki/PCAF_European_Building_Emission_Factor_Database>`_

    * Emission Factor ID (PCAF Serial Number)
    * Country
    * Asset Class (Residential / Commercial Real Estate)
    * Emission Factor Type (Emissions or Energy)
    * Data Level 1 Information
    * Data Level 2 Information
    * [[EPC Rating]]
    * Emission Factor Functional Unit (name)
    * Emission Factor Functional Unit (unit)
    * Emission Factor (name)
    * Emission Factor (unit)
    * PCAF Data Quality score (Range in 1 - 5)
    * Emission Factor (value)
    * Emission Factor methodology description
    * Emission Factor Source (Slots for up to 4 historical values)
    * Emission Factor Year (Slots for up to 4 historical values)
    * Link to emission factor documentation
    * Status (Published)
    * Inserted By (User Data)

    """

    # IDENTITY

    # ATTN DB field is ID
    # EF_ID = models.IntegerField(blank=True, null=True, help_text='The unique ID of the emission factor (Integer)')

    # CHARACTERISTICS

    Asset_class = models.CharField(max_length=40, blank=True, null=True,
                                   help_text='The asset class')

    EF_TYPE_CHOICES = [(0, 'Emissions'), (1, 'Energy')]

    Emission_factor_type = models.CharField(max_length=20, blank=True, null=True,
                                            help_text='Specify whether it is an a) emission intensity factor or an b) energy intensity factor')

    # TODO Utilize proper country field
    # Country = CountryField(blank=True, null=True,
    #                        help_text='Specify the country where the building is located (European Countries Only')

    Country = models.CharField(max_length=40, blank=True, null=True,
                               help_text='Specify the country where the building is located (European Countries Only')

    Data_level_1_information = models.CharField(max_length=80, blank=True, null=True,
                                                help_text='Features of the emission factor (such as the broad real estate asset class) at the highest aggregation level (Example: Residential or Commercial)')

    Data_level_2_information = models.CharField(max_length=80, blank=True, null=True,
                                                help_text='Features of the emission factor (such as the building type) at the lowest aggregation level (Example: Multi-family or Single-Family house)')

    # Data_level_3_information
    EPC_Rating = models.CharField(max_length=10, blank=True, null=True,
                                  help_text='The EPC rating of the building (Example: A, B, A++ etc) - if available, otherwise blank')

    # ATTN original field has parenthesis
    Emission_factor_functional_unit_name = models.CharField(max_length=40, blank=True, null=True,
                                                            help_text='The functional unit of the emission factor expressed as name. (Example: Dwelling Numbers or Floor Area)')

    # ATTN original field has parenthesis
    Emission_factor_functional_unit_unit = models.CharField(max_length=80, blank=True, null=True,
                                                            help_text='The functional unit of the emission factor expressed as unit. (Example: Area in m^2 or Count)')

    # ATTN original field has parenthesis
    Emission_factor_name = models.CharField(max_length=80, blank=True, null=True,
                                            help_text='Label of the emission factor. (Example: EPC Energy Intensity per m^2)')

    # ATTN original field has parenthesis
    Emission_factor_unit = models.CharField(max_length=80, blank=True, null=True,
                                            help_text='Unit of the emission factor. (Example: tCO2e/m^2)')

    DQ_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    PCAF_data_quality_score = models.IntegerField(blank=True, null=True,
                                                  choices=DQ_CHOICES,
                                                  help_text='The emission factor data quality as defined by PCAF (score 1 = highest quality, score 5 = lowest quality).')

    Emission_factor = models.FloatField(blank=True, null=True,
                                        help_text='The value of the Emission Factor. Example (0.34159')

    Emission_factor_methodology_description = models.TextField(blank=True, null=True,
                                                               help_text='Information on the methodology used to derive the respective emission factor')

    YEAR_CHOICES = [(2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021),
                    (2022, 2022)]

    Emission_factor_source_1 = models.CharField(max_length=80, blank=True, null=True,
                                                help_text='The name of the emission factor source(s) 1')

    Emission_factor_year_1 = models.CharField(max_length=20, blank=True, null=True,
                                              help_text='The emission factor source(s) 1 base year (i.e. the actual year of the underlying data used to calculate the emission factor).')

    Emission_factor_source_2 = models.CharField(max_length=80, blank=True, null=True,
                                                help_text='The name of the emission factor source(s) 2')

    Emission_factor_year_2 = models.CharField(max_length=20, blank=True, null=True,
                                              help_text='The emission factor source(s) 2 base year (i.e. the actual year of the underlying data used to calculate the emission factor).')

    Emission_factor_source_3 = models.CharField(max_length=80, blank=True, null=True,
                                                help_text='The name of the emission factor source(s) 3')

    Emission_factor_year_3 = models.CharField(max_length=20, blank=True, null=True,
                                              help_text='The emission factor source(s) 3 base year (i.e. the actual year of the underlying data used to calculate the emission factor).')

    Emission_factor_source_4 = models.CharField(max_length=80, blank=True, null=True,
                                                help_text='The name of the emission factor source(s) 4')

    Emission_factor_year_4 = models.CharField(max_length=20, blank=True, null=True,
                                              help_text='The emission factor source(s) 4 base year (i.e. the actual year of the underlying data used to calculate the emission factor).')

    Link_to_emission_factor = models.CharField(max_length=80, blank=True, null=True,
                                               help_text='A link to the emission factor source and/or methodology.')

    Status = models.CharField(max_length=40, blank=True, null=True,
                              help_text='Publication status of the Emission Factor.')

    Inserted_By_Users = models.CharField(max_length=40, blank=True, null=True,
                                         help_text='Which user added the emission factor to the database')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('reference:BuildingEmissionFactor_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Building Emissions Factor"
        verbose_name_plural = "Building Emissions Factors"
