from django import forms
from django.forms import ModelForm
from psytest.models import Psytestsheet, PsytestAnswer
from django.utils.translation import gettext_lazy as _

BDI_CHOICE = (
    (0,'0'),
    (1,'1'),
    (2,'2'),
    (3,'3'),
)

SEI_CHOICE = (
    (1,'그렇다'),
    (2,'아니다'),
)

TSCC_CHOICE = (
    (0,'결코 그런 일이 없다'),
    (1,'가끔 그런 일이 있다'),
    (2,'그런 일이 빈번하다'),
    (3,'거의 대부분의 시간이 그렇다'),
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


class TestSeiForm(ModelForm):
    class Meta:
        model = PsytestAnswer

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
            'a22',
            'a23',
            'a24',
            'a25',

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
        }
        widgets = {
            'psytestsheet':forms.HiddenInput,
            'a1' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a2' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a3' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a4' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a5' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a6' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a7' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a8' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a9' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a10' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a11' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a12' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a13' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a14' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a15' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a16' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a17' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a18' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a19' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a20' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a21' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a22' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a23' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a24' : forms.RadioSelect(choices=SEI_CHOICE ),
            'a25' : forms.RadioSelect(choices=SEI_CHOICE ),
        }


class TestTsccForm(ModelForm):
    class Meta:
        model = PsytestAnswer

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
            'a22',
            'a23',
            'a24',
            'a25',
            'a26',
            'a27',
            'a28',
            'a29',
            'a30',
            'a31',
            'a32',
            'a33',
            'a34',
            'a35',
            'a36',
            'a37',
            'a38',
            'a39',
            'a40',
            'a41',
            'a42',
            'a43',
            'a44',
            'a45',
            'a46',
            'a47',
            'a48',
            'a49',
            'a50',
            'a51',
            'a52',
            'a53',
            'a54',

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
        }
        widgets = {
            'psytestsheet':forms.HiddenInput,
            'a1' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a2' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a3' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a4' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a5' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a6' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a7' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a8' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a9' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a10' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a11' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a12' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a13' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a14' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a15' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a16' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a17' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a18' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a19' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a20' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a21' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a22' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a23' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a24' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a25' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a26' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a27' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a28' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a29' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a30' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a31' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a32' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a33' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a34' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a35' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a36' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a37' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a38' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a39' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a40' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a41' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a42' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a43' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a44' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a45' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a46' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a47' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a48' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a49' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a50' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a51' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a52' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a53' : forms.RadioSelect(choices=TSCC_CHOICE ),
            'a54' : forms.RadioSelect(choices=TSCC_CHOICE ),
        }