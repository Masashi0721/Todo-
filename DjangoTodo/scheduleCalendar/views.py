from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Event
from .forms import EventForm
from django.http import Http404
import time
from django.template import loader
from django.middleware.csrf import get_token
from django.http import JsonResponse
from .forms import CalendarForm
from django.views.generic import ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    """
    カレンダー画面
    """
    # CSRFのトークンを発行する
    get_token(request)

    template = loader.get_template("scheduleCalendar/index.html")
    return HttpResponse(template.render())

def add_event(request):
    """
    イベント登録
    """

    if request.method == "GET":
        # GETは対応しない
        raise Http404()

    # JSONの解析
    datas = json.loads(request.body)

    # バリデーション
    eventForm = EventForm(datas)
    if eventForm.is_valid() == False:
        # バリデーションエラー
        raise Http404()

    # リクエストの取得
    start_date = datas["start_date"]
    end_date = datas["end_date"]
    event_name = datas["event_name"]

    # 日付に変換。JavaScriptのタイムスタンプはミリ秒なので秒に変換
    formatted_start_date = time.strftime(
        "%Y-%m-%d", time.localtime(start_date / 1000))
    formatted_end_date = time.strftime(
        "%Y-%m-%d", time.localtime(end_date / 1000))

    # 登録処理
    event = Event(
        event_name=str(event_name),
        start_date=formatted_start_date,
        end_date=formatted_end_date,
    )
    event.save()

    # 空を返却
    return HttpResponse("")

def get_events(request):
    """
    イベントの取得
    """

    if request.method == "GET":
        # GETは対応しない
        raise Http404()

    # JSONの解析
    datas = json.loads(request.body)

    # バリデーション
    calendarForm = CalendarForm(datas)
    if calendarForm.is_valid() == False:
        # バリデーションエラー
        raise Http404()

    # リクエストの取得
    start_date = datas["start_date"]
    end_date = datas["end_date"]

    # 日付に変換。JavaScriptのタイムスタンプはミリ秒なので秒に変換
    formatted_start_date = time.strftime(
        "%Y-%m-%d", time.localtime(start_date / 1000))
    formatted_end_date = time.strftime(
        "%Y-%m-%d", time.localtime(end_date / 1000))

    # FullCalendarの表示範囲のみ表示
    events = Event.objects.filter(
        start_date__lt=formatted_end_date, end_date__gt=formatted_start_date
    )

    # fullcalendarのため配列で返却
    list = []
    for event in events:
        list.append(
            {
                "title": event.event_name,
                "start": event.start_date,
                "end": event.end_date,
            }
        )

    return JsonResponse(list, safe=False)

@login_required
def menu(request):
    template = loader.get_template("scheduleCalendar/menu.html")
    return HttpResponse(template.render())

class todolist(ListView):
    template_name = "scheduleCalendar/list.html"
    model = Event

class job(ListView):
    template_name = "scheduleCalendar/job.html"
    model = Event

class hobby(ListView):
    template_name = "scheduleCalendar/hobby.html"
    model = Event

class university(ListView):
    template_name = "scheduleCalendar/university.html"
    model = Event

class others(ListView):
    template_name = "scheduleCalendar/others.html"
    model = Event

class tododelete(DeleteView):
    template_name = "scheduleCalendar/delete.html"
    model = Event
    success_url = reverse_lazy("cal:list")

class todoupdate(UpdateView):
    template_name = "scheduleCalendar/update.html"
    model = Event
    fields = ["event_name", "category"]
    success_url = reverse_lazy("cal:list")

class MyLogoutView(LogoutView):
    template_name = 'scheduleCalendar/logout.html'