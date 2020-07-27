from django.contrib import admin
from psytest.models import Psytestsheet


@admin.register(Psytestsheet)
class PsytestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'psytest_nm',
        'is_effect_verify',
        'start_age',
        'end_age',
        'end_age',
        'q1',
        'q1_1',
        'q1_2',
        'q1_3',
        'q1_4',
        'q1_5',
        'q1_6',
        'q1_7',
        'q2',
        'q2_1',
        'q2_2',
        'q2_3',
        'q2_4',
        'q2_5',
        'q2_6',
        'q2_7',
        'q3',
        'q3_1',
        'q3_2',
        'q3_3',
        'q3_4',
        'q3_5',
        'q3_6',
        'q3_7',
    )


# Register your models here.
