from django import forms
from django.forms import ModelForm
from psytest.models import Psytestsheet, PsytestAnswer
from django.utils.translation import gettext_lazy as _

BDI_CHOICE = (
    ('0',0),
    ('1',1),
    ('2',2),
    ('3',3),
)


class TestBdiForm(ModelForm):
    class Meta:
        model = PsytestAnswer

        # def __init__(self, *args, **kwargs):
        #     super(TestBdiForm, self).__init__(*args, **kwargs)
        #     # 각 input 태그의 help_text, label을 제거함.  https://technerd.tistory.com/49
        #     for field in self.fields:
        #         self.fields[field].help_text=None
        #         self.fields[field].label=''

        fields = [
            'psytestsheet',
            'client_nm',
            'birth_dt',
            'test_dt',
            'a1',
            'a2',
            'a3',
            'a4',
            'a5',
            'a6',
            'a7',
            'a8',
            'a9',
            'a10',
            'a11',
            'a12',
            'a13',
            'a14',
            'a15',
            'a16',
            'a17',
            'a18',
            'a19',
            'a20',
            'a21',

        ]
        labels = {
            'client_nm': _('수검자명'),
            'birth_dt': _('수검자 생년월일'),
            'test_dt': _('검사일자'),
        }
        help_texts = {
            'client_nm': _('이름을 입력해주세요'),
            'birth_dt': _(' '),
            'test_dt': _(' '),
            'a1' : _(' ')
        }
        widgets = {
            'psytestsheet':forms.HiddenInput,
            'a1' : forms.Select(choices=BDI_CHOICE ),
            'a2' : forms.Select(choices=BDI_CHOICE ),
            'a3' : forms.Select(choices=BDI_CHOICE ),
            'a4' : forms.Select(choices=BDI_CHOICE ),
            'a5' : forms.Select(choices=BDI_CHOICE ),
            'a6' : forms.Select(choices=BDI_CHOICE ),
            'a7' : forms.Select(choices=BDI_CHOICE ),
            'a8' : forms.Select(choices=BDI_CHOICE ),
            'a9' : forms.Select(choices=BDI_CHOICE ),
            'a10' : forms.Select(choices=BDI_CHOICE ),
            'a11' : forms.Select(choices=BDI_CHOICE ),
            'a12' : forms.Select(choices=BDI_CHOICE ),
            'a13' : forms.Select(choices=BDI_CHOICE ),
            'a14' : forms.Select(choices=BDI_CHOICE ),
            'a15' : forms.Select(choices=BDI_CHOICE ),
            'a16' : forms.Select(choices=BDI_CHOICE ),
            'a17' : forms.Select(choices=BDI_CHOICE ),
            'a18' : forms.Select(choices=BDI_CHOICE ),
            'a19' : forms.Select(choices=BDI_CHOICE ),
            'a20' : forms.Select(choices=BDI_CHOICE ),
            'a21' : forms.Select(choices=BDI_CHOICE ),
        }


class TestBaiForm(ModelForm):
    class Meta:
        model = PsytestAnswer

        # def __init__(self, *args, **kwargs):
        #     super(TestBdiForm, self).__init__(*args, **kwargs)
        #     # 각 input 태그의 help_text, label을 제거함.  https://technerd.tistory.com/49
        #     for field in self.fields:
        #         self.fields[field].help_text=None
        #         self.fields[field].label=''

        fields = [
            'psytestsheet',
            'client_nm',
            'birth_dt',
            'test_dt',
            'a1',
            'a2',
            'a3',
            'a4',
            'a5',
            'a6',
            'a7',
            'a8',
            'a9',
            'a10',
            'a11',
            'a12',
            'a13',
            'a14',
            'a15',
            'a16',
            'a17',
            'a18',
            'a19',
            'a20',
            'a21',

        ]
        labels = {
            'client_nm': _('수검자명'),
            'birth_dt': _('수검자 생년월일'),
            'test_dt': _('검사일자'),
        }
        help_texts = {
            'client_nm': _('이름을 입력해주세요'),
            'birth_dt': _(' '),
            'test_dt': _(' '),
            'a1' : _(' ')
        }
        widgets = {
            'psytestsheet':forms.HiddenInput,
            'a1' : forms.Select(choices=BDI_CHOICE ),
            'a2' : forms.Select(choices=BDI_CHOICE ),
            'a3' : forms.Select(choices=BDI_CHOICE ),
            'a4' : forms.Select(choices=BDI_CHOICE ),
            'a5' : forms.Select(choices=BDI_CHOICE ),
            'a6' : forms.Select(choices=BDI_CHOICE ),
            'a7' : forms.Select(choices=BDI_CHOICE ),
            'a8' : forms.Select(choices=BDI_CHOICE ),
            'a9' : forms.Select(choices=BDI_CHOICE ),
            'a10' : forms.Select(choices=BDI_CHOICE ),
            'a11' : forms.Select(choices=BDI_CHOICE ),
            'a12' : forms.Select(choices=BDI_CHOICE ),
            'a13' : forms.Select(choices=BDI_CHOICE ),
            'a14' : forms.Select(choices=BDI_CHOICE ),
            'a15' : forms.Select(choices=BDI_CHOICE ),
            'a16' : forms.Select(choices=BDI_CHOICE ),
            'a17' : forms.Select(choices=BDI_CHOICE ),
            'a18' : forms.Select(choices=BDI_CHOICE ),
            'a19' : forms.Select(choices=BDI_CHOICE ),
            'a20' : forms.Select(choices=BDI_CHOICE ),
            'a21' : forms.Select(choices=BDI_CHOICE ),
        }