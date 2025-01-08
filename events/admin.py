from django.contrib import admin
from .models import UpcomingEventsModel
from .forms import CardConfigForm
from solo.admin import SingletonModelAdmin
from django.db import models
from django.contrib import admin

class SingletonModelAdmin(admin.ModelAdmin):
    # def has_add_permission(self, request):
    #     # If there's already an entry, don't allow adding another
    #     count = self.model.objects.count()
    #     if count > 0:
    #         return False
    #     return True

    def has_delete_permission(self, request, obj=None):
        # Don't allow deleting if there's only one entry
        count = self.model.objects.count()
        if count == 1:
            return False
        return True

class CardConfigAdmin(SingletonModelAdmin):
    form = CardConfigForm
admin.site.register(UpcomingEventsModel, CardConfigAdmin)



