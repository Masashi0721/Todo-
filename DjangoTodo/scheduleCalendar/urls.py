from django.urls import include, path
from . import views
from .views import todolist

app_name = "cal"
urlpatterns = [
    path("", views.menu, name="menu"),
    path("scheduleCalendar/", views.index, name="index"),
    path("todolist/", views.todolist.as_view(), name="list"),
    path("job/", views.job.as_view(), name="job"),
    path("hobby/", views.hobby.as_view(), name="hobby"),
    path("university/", views.university.as_view(), name="university"),
    path("others/", views.others.as_view(), name="others"),
    path("tododelete/<int:pk>/", views.tododelete.as_view(), name="tododelete"),
    path("todoupdate/<int:pk>/", views.todoupdate.as_view(), name="todoupdate"),
    path("add/", views.add_event, name="add_event"),
    path("list/", views.get_events, name="get_events"),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
]