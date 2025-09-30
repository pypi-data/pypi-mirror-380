from django.contrib import admin
from django.db.models import Q
from edc_crf.modeladmin_mixins import CrfModelAdmin

from ..admin_site import edc_he_admin
from ..forms import HealthEconomicsPatientForm
from ..modeladmin_mixins import HealthEconomicsPatientModelAdminMixin
from ..models import Ethnicities, HealthEconomicsPatient, Religions


@admin.register(HealthEconomicsPatient, site=edc_he_admin)
class HealthEconomicsPatientAdmin(HealthEconomicsPatientModelAdminMixin, CrfModelAdmin):
    form = HealthEconomicsPatientForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if getattr(request, "site", None):
            if db_field.name == "pat_ethnicity":
                kwargs["queryset"] = Ethnicities.objects.filter(
                    Q(extra_value=request.site.siteprofile.country)
                    | Q(extra_value__isnull=True)
                )
            if db_field.name == "pat_religion":
                kwargs["queryset"] = Religions.objects.filter(
                    Q(extra_value=request.site.siteprofile.country)
                    | Q(extra_value__isnull=True)
                )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if getattr(request, "site", None) and db_field.name == "pat_insurance":
            model_cls = getattr(self.model, db_field.name).field.related_model
            kwargs["queryset"] = model_cls.objects.filter(
                Q(extra_value=request.site.siteprofile.country) | Q(extra_value__isnull=True)
            )
        return super().formfield_for_manytomany(db_field, request, **kwargs)
