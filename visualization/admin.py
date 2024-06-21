from django.contrib import admin
from django.db.models import JSONField
from jsoneditor.forms import JSONEditor

from visualization.models import VegaSpecification, VegaLiteSpecification


class VegaSpecificationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': JSONEditor},
    }
    #
    # Searchable fields
    #
    search_fields = ['description']
    list_display = ('title', 'width', 'height', 'description',)
    save_as = True
    view_on_site = False


class VegaLiteSpecificationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': JSONEditor},
    }

    search_fields = ['description']
    list_display = ('title', 'description',)
    save_as = True
    view_on_site = False


admin.site.register(VegaSpecification, VegaSpecificationAdmin)
admin.site.register(VegaLiteSpecification, VegaLiteSpecificationAdmin)
