from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from psytest.forms import TestBdiForm, TestBaiForm
from psytest.models import Psytestsheet, PsytestAnswer
import logging
logger = logging.getLogger(__name__)


#--- 심리검사목록조회 클래스뷰
# class PsytestLV(ListView):
#     model = Psytestsheet


def list(request):
    list = Psytestsheet.objects.all()
    context = {
        'psytestsheets' : list
    }
    return render(request, 'psytest/psytest_list.html', context)


def detail(request, testsheet):
    if request.method == 'POST':
        initial_data = {'psytestsheet': testsheet}
        if testsheet == 1:  # BDI 폼
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
        elif testsheet == 2:  # BAI 폼
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

    elif request.method == 'GET':
        item = get_object_or_404(Psytestsheet, pk=testsheet)
        if testsheet == 1:  # BDI 폼
            form = TestBdiForm(initial={'psytestsheet': item})
            return render(request, 'psytest/testform/psytest_form_bdi.html', {'form': form, 'item': item})
        if testsheet == 2:  # BDI 폼
            form = TestBaiForm(initial={'psytestsheet': item})
            return render(request, 'psytest/testform/psytest_form_bai.html', {'form': form, 'item': item})
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
        if testsheet == 1:  # BDI 폼
            return render(request, 'psytest/testform/psytest_form_bdi.html', {'form': form, 'item': sheet})
        if testsheet == 2:  # BDI 폼
            return render(request, 'psytest/testform/psytest_form_bai.html', {'form': form, 'item': sheet})

