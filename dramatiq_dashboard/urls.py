from django.urls import path

from dramatiq_dashboard.views import (
    TaskArchiveView,
    TaskDayArchiveView,
    TaskDetailView,
    TaskListView,
    TaskMonthArchiveView,
    TaskYearArchiveView,
)

app_name = "django_dramatiq_dashboard"

urlpatterns = [
    path("executed/", TaskListView.as_view(), name="executed_list"),
    path("executed/<str:id>/", TaskDetailView.as_view(), name="executed_detail"),
    path("archive/", TaskArchiveView.as_view(), name="task_archive"),
    path(
        "archive/<int:year>/", TaskYearArchiveView.as_view(), name="task_year_archive"
    ),
    path(
        "archive/<int:year>/<int:month>/",
        TaskMonthArchiveView.as_view(month_format="%m"),
        name="task_month_archive",
    ),
    path(
        "archive/<int:year>/<int:month>/<int:day>/",
        TaskDayArchiveView.as_view(month_format="%m"),
        name="task_day_archive",
    ),
]
