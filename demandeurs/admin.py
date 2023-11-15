from django.contrib import admin
from demandeurs.models import ExtraitModel, ReclamationModel, ValidationModel, ContactModel

# Register your models here.
admin.site.register(ExtraitModel)
admin.site.register(ReclamationModel)
admin.site.register(ValidationModel)
admin.site.register(ContactModel)