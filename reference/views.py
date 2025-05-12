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

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader


@login_required(login_url='/login/')
def nace_list(request):
    """
    Display the NACE pictogram list

    """

    img_list = ['A_Agriculture.svg', 'I_Accommodation.svg', 'P_Education.svg',
                'B_Mining.svg', 'J_ICT.svg', 'Q_Health.svg',
                'C_Manufacture.svg', 'K_Finance.svg', 'R_Recreation.svg',
                'D_Electricity.svg', 'L_RealEstate.svg', 'S_OtherServices.svg',
                'E_Water.svg', 'M_Professional.svg', 'T_Households.svg',
                'F_Construction.svg', 'N_Administrative.svg', 'U_NGO.svg',
                'G_Trading.svg', 'O_PublicSector.svg', 'H_Transport.svg', 'Other.svg'
                ]

    t = loader.get_template('reference/nace_list.html')
    context = RequestContext(request, {})
    context.update({'img_list': img_list})
    return HttpResponse(t.template.render(context))
