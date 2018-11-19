from django.contrib import admin
from models import Formula
from django.contrib import auth

# Register your models here.

class FormulaAdmin(admin.ModelAdmin):
    list_display = ('name', 'operandA', 'operator', 'operandB')

    
admin.site.register(Formula, FormulaAdmin)
admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)

