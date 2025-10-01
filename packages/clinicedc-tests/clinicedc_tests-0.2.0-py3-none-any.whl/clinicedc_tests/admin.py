from django import forms
from django.contrib import admin
from django_audit_fields import ModelAdminAuditFieldsMixin, audit_fieldset_tuple
from edc_crf.modelform_mixins import CrfModelFormMixin
from edc_fieldsets.fieldset import Fieldset
from edc_fieldsets.fieldsets_modeladmin_mixin import FieldsetsModelAdminMixin
from edc_form_label import FormLabel, FormLabelModelAdminMixin
from edc_model_admin.dashboard import ModelAdminCrfDashboardMixin
from edc_model_admin.mixins import (
    ModelAdminFormInstructionsMixin,
    ModelAdminNextUrlRedirectMixin,
    ModelAdminRedirectOnDeleteMixin,
    TemplatesModelAdminMixin,
)
from edc_visit_tracking.modeladmin_mixins import CrfModelAdminMixin

from .admin_site import clinicedc_tests_admin
from .form_labels import MyCustomLabelCondition
from .forms import MemberForm, TeamForm, TeamWithDifferentFieldsForm, TestModel3Form
from .models import (
    CrfFive,
    CrfFour,
    CrfOne,
    CrfSeven,
    CrfSix,
    CrfThree,
    CrfTwo,
    Member,
    RedirectNextModel,
    SubjectRequisition,
    Team,
    TeamWithDifferentFields,
    TestModel3,
    TestModel4,
    TestModel5,
    TestModel6,
    Venue,
)

visit_two_fieldset = Fieldset(
    "f4",
    "f5",
    section="Visit Two Additional Questions",
)
summary_fieldset = Fieldset("summary_one", "summary_two", section="Summary")


@admin.register(CrfOne)
class CrfOneModelAdmin(
    CrfModelAdminMixin, ModelAdminAuditFieldsMixin, admin.ModelAdmin
):
    def get_field_queryset(self, db, db_field, request):
        return CrfOne.objects.all()


@admin.register(TestModel3)
class TestModel3Admin(ModelAdminFormInstructionsMixin, admin.ModelAdmin):
    form = TestModel3Form

    fieldsets = (
        (
            "Not special fields",
            {"fields": ("subject_visit", "report_datetime", "f1", "f2", "f3")},
        ),
        (
            "Visit Two Additional Questions",
            {"fields": ("f4", "f5")},
        ),
        (
            "Summary",
            {"fields": ("summary_one", "summary_two")},
        ),
        audit_fieldset_tuple,
    )


@admin.register(TestModel4)
class TestModel4Admin(FieldsetsModelAdminMixin, admin.ModelAdmin):
    """Demonstrate that the fieldsets listed in  fieldsets_move_to_end
    will always be last even after a conditional fieldset
    is inserted.

    """

    fieldsets_move_to_end = ["Summary", audit_fieldset_tuple[0]]

    conditional_fieldsets = {"2000": (visit_two_fieldset,)}

    fieldsets = (
        (
            "Not special fields",
            {"fields": ("subject_visit", "report_datetime", "f1", "f2", "f3")},
        ),
        summary_fieldset.fieldset,
        audit_fieldset_tuple,
    )


@admin.register(TestModel5)
class TestModel5Admin(FormLabelModelAdminMixin, admin.ModelAdmin):
    """Demonstrate use of a custom form label."""

    fieldsets = (
        (
            "Not special fields",
            {"fields": ("subject_visit", "report_datetime", "circumcised")},
        ),
    )

    custom_form_labels = [
        FormLabel(
            field="circumcised",
            custom_label=(
                "Since we last saw you in {previous_visit}, were you circumcised?"
            ),
            condition_cls=MyCustomLabelCondition,
        )
    ]


@admin.register(TestModel6)
class TestModel6Admin(FieldsetsModelAdminMixin, admin.ModelAdmin):
    """Demonstrate the use of conditional_fieldsets.

    Fieldset "visit_two_fieldset" will only show on the admin
    form if the visit_code is '2000'
    """

    conditional_fieldsets = {"2000": (visit_two_fieldset,)}

    fieldsets = (
        (
            "Not special fields",
            {"fields": ("subject_visit", "report_datetime", "f1", "f2", "f3")},
        ),
        audit_fieldset_tuple,
    )


class BaseModelAdmin(TemplatesModelAdminMixin):
    search_fields = ("subject_identifier",)


@admin.register(CrfOne, site=clinicedc_tests_admin)
class CrfOneAdmin(BaseModelAdmin, admin.ModelAdmin):
    pass


# using ModelAdminNextUrlRedirectMixin


@admin.register(RedirectNextModel, site=clinicedc_tests_admin)
class RedirectNextModelAdmin(
    BaseModelAdmin, ModelAdminNextUrlRedirectMixin, admin.ModelAdmin
):
    pass


@admin.register(CrfTwo, site=clinicedc_tests_admin)
class CrfTwoAdmin(BaseModelAdmin, ModelAdminNextUrlRedirectMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = True


@admin.register(CrfThree, site=clinicedc_tests_admin)
class CrfThreeAdmin(BaseModelAdmin, ModelAdminNextUrlRedirectMixin, admin.ModelAdmin):
    pass


@admin.register(SubjectRequisition, site=clinicedc_tests_admin)
class SubjectRequisitionAdmin(
    BaseModelAdmin, ModelAdminNextUrlRedirectMixin, admin.ModelAdmin
):
    show_save_next = True
    show_cancel = True


# using ModelAdminRedirectOnDeleteMixin


@admin.register(CrfFour, site=clinicedc_tests_admin)
class CrfFourAdmin(BaseModelAdmin, ModelAdminRedirectOnDeleteMixin, admin.ModelAdmin):
    post_url_on_delete_name = "dashboard_url"

    def post_url_on_delete_kwargs(self, request, obj):
        return {"subject_identifier": obj.subject_identifier}


@admin.register(CrfFive, site=clinicedc_tests_admin)
class CrfFiveAdmin(BaseModelAdmin, ModelAdminRedirectOnDeleteMixin, admin.ModelAdmin):
    post_url_on_delete_name = "dashboard2_url"

    def post_url_on_delete_kwargs(self, request, obj):
        return {"subject_identifier": obj.subject_identifier}


@admin.register(CrfSix, site=clinicedc_tests_admin)
class CrfSixAdmin(BaseModelAdmin, ModelAdminRedirectOnDeleteMixin, admin.ModelAdmin):
    post_url_on_delete_name = None

    def post_url_on_delete_kwargs(self, request, obj):
        return {"subject_identifier": obj.subject_identifier}


class CrfSevenForm(CrfModelFormMixin, forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = CrfSeven


@admin.register(CrfSeven, site=clinicedc_tests_admin)
class CrfSevenAdmin(ModelAdminCrfDashboardMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = False

    form = CrfSevenForm


# edc_form_runners
class MemberInlineAdmin(admin.TabularInline):
    model = Member
    form = MemberForm

    extra = 0


@admin.register(Venue, site=clinicedc_tests_admin)
class VenueAdmin(BaseModelAdmin, ModelAdminRedirectOnDeleteMixin, admin.ModelAdmin):
    post_url_on_delete_name = "dashboard_url"

    def post_url_on_delete_kwargs(self, request, obj):
        return {"subject_identifier": obj.subject_identifier}


@admin.register(Team, site=clinicedc_tests_admin)
class TeamAdmin(BaseModelAdmin, ModelAdminRedirectOnDeleteMixin, admin.ModelAdmin):
    post_url_on_delete_name = "dashboard_url"

    form = TeamForm
    inlines = [MemberInlineAdmin]
    fieldsets = ((None, ({"fields": ("name", "created", "modified")})),)

    def post_url_on_delete_kwargs(self, request, obj):
        return {"subject_identifier": obj.subject_identifier}


@admin.register(TeamWithDifferentFields, site=clinicedc_tests_admin)
class TeamWithDifferentFieldsAdmin(
    BaseModelAdmin, ModelAdminRedirectOnDeleteMixin, admin.ModelAdmin
):
    post_url_on_delete_name = "dashboard_url"

    form = TeamWithDifferentFieldsForm

    # do not include "name" to show that the field is ignored
    # by FormRunner.run even though blank=False
    fieldsets = ((None, ({"fields": ("size", "color", "mood")})),)

    def post_url_on_delete_kwargs(self, request, obj):
        return {"subject_identifier": obj.subject_identifier}


@admin.register(Member, site=clinicedc_tests_admin)
class MemberAdmin(BaseModelAdmin, ModelAdminRedirectOnDeleteMixin, admin.ModelAdmin):
    post_url_on_delete_name = "dashboard_url"

    form = MemberForm

    def post_url_on_delete_kwargs(self, request, obj):
        return {"subject_identifier": obj.subject_identifier}
