from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from psytest.forms import TestBdiForm, TestBaiForm, TestSeiForm, TestTsccForm
from psytest.models import Psytestsheet, PsytestAnswer
import logging
logger = logging.getLogger(__name__)


#--- 심리검사목록조회 클래스뷰
# class PsytestLV(ListView):
#     model = Psytestsheet


def list(request):
    list = Psytestsheet.objects.all().order_by('id')
    context = {
        'psytestsheets' : list
    }
    return render(request, 'psytest/psytest_list.html', context)


def detail(request, testsheet):
    if request.method == 'POST':
        initial_data = {'psytestsheet': testsheet}
        if testsheet == 1:  # BDI  저장하기
            print('BDI POST')
            form = TestBdiForm(request.POST, initial={'psytestsheet': testsheet})
            print(form)
            # form(initial=initial_data)
            if form.is_valid():
                new_item = form.save()
                print('BDI saved')
                return redirect('psytest:list')
            else:
                print('BDI not saved')
                print(form.errors)
            return redirect('/')
        elif testsheet == 2:  # BAI 저장하기
            print('BAI POST')
            form = TestBaiForm(request.POST, initial={'psytestsheet': testsheet})
            print(form)
            # form(initial=initial_data)
            if form.is_valid():
                new_item = form.save()
                print('BAI saved')
                return redirect('psytest:list')
            else:
                print('BAI not saved')
                print(form.errors)
            return redirect('/')
        elif testsheet == 3:  # SEI 저장하기
            print('SEI POST')
            form = TestSeiForm(request.POST, initial={'psytestsheet': testsheet})
            print(form)
            if form.is_valid():
                new_item = form.save()
                print('SEI saved')
                return redirect('psytest:list')
            else:
                print('SEI not saved')
                print(form.errors)
            return redirect('/')
        elif testsheet == 4:  # TSCC 저장하기
            print('TSCC POST')
            form = TestTsccForm(request.POST, initial={'psytestsheet': testsheet})
            print(form)
            if form.is_valid():
                new_item = form.save()
                print('TSCC saved')
                return redirect('psytest:list')
            else:
                print('TSCC not saved')
                print(form.errors)
            return redirect('/')

    elif request.method == 'GET':
        item = get_object_or_404(Psytestsheet, pk=testsheet)
        if testsheet == 1:  # BDI 검사하기
            form = TestBdiForm(initial={'psytestsheet': item})
            return render(request, 'psytest/testform/psytest_form_bdi.html', {'form': form, 'item': item})
        elif testsheet == 2:  # BAI 검사하기
            form = TestBaiForm(initial={'psytestsheet': item})
            return render(request, 'psytest/testform/psytest_form_bai.html', {'form': form, 'item': item})
        elif testsheet == 3:  # SEI 검사하기
            form = TestSeiForm(initial={'psytestsheet': item})
            return render(request, 'psytest/testform/psytest_form_sei.html', {'form': form, 'item': item})
        elif testsheet == 4:  # TSCC 검사하기
            form = TestTsccForm(initial={'psytestsheet': item})
            return render(request, 'psytest/testform/psytest_form_tscc.html', {'form': form, 'item': item})
    return redirect('psytest')


def detailList(request, testsheet):
    detailList = PsytestAnswer.objects.filter(psytestsheet=testsheet)
    item = get_object_or_404(Psytestsheet, pk=testsheet)
    context = {
        'detailList' : detailList,
        'item': item
    }
    return render(request, 'psytest/psytest_detail_list.html', context)


def testCase(request, testsheet, testCaseId):
    sheet = get_object_or_404(Psytestsheet, pk=testsheet)  # 검사종류 ID 세팅
    if request.method == 'POST':
        print(testsheet, testCaseId)

    elif request.method == 'GET':
        print(testsheet, testCaseId)
        form = get_object_or_404(PsytestAnswer, pk=testCaseId)  # 검사응답지의 상세 레코드를 불러온다
        if testsheet == 1:  # BDI 폼 불러오기
            return render(request, 'psytest/testform/psytest_form_bdi.html', {'form': form, 'item': sheet})
        if testsheet == 2:  # BAI 폼 불러오기
            return render(request, 'psytest/testform/psytest_form_bai.html', {'form': form, 'item': sheet})
        if testsheet == 3:  # SEI 폼 불러오기
            return render(request, 'psytest/testform/psytest_form_sei.html', {'form': form, 'item': sheet})
        if testsheet == 4:  # TSCC 폼 불러오기
            return render(request, 'psytest/testform/psytest_form_tscc.html', {'form': form, 'item': sheet})

