from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from start.models import ORMKeyword, DocPage


class ORMKeywordAdmin(admin.ModelAdmin):
    save_as = True


class DocPageAdmin(admin.ModelAdmin):
    #
    # Searchable fields
    #
    search_fields = ['title', 'content']
    list_display = ('title', 'category')
    list_filter = ('category', 'doc_type')
    save_as = True

    def response_change(self, request, obj, post_url_continue=None):
        """This makes the response after adding go to another apps changelist for some model"""
        return HttpResponseRedirect(reverse("start:documentation", args=[obj.slug]))


admin.site.register(ORMKeyword, ORMKeywordAdmin)
admin.site.register(DocPage, DocPageAdmin)

