from django.views.generic import ArchiveIndexView, DetailView, ListView, YearArchiveView
from django.views.generic.dates import DayArchiveView, MonthArchiveView

from dramatiq_dashboard.models import DramatiqTask
from dramatiq_dashboard.utils import DateTimeMixin, DynamicDateFieldMixin


class TaskListView(DateTimeMixin, ListView):
    model = DramatiqTask
    template_name = "dramatiq_dashboard/list.html"


class TaskDetailView(DateTimeMixin, DetailView):
    model = DramatiqTask
    template_name = "dramatiq_dashboard/detail.html"
    pk_url_kwarg = "id"

    def get_result(self, obj):
        message = getattr(obj, "message", None)
        try:
            return message.get_result() if message else None
        except Exception:
            return None

    def get_context_data(self, **kwargs):
        context = {}
        obj = self.get_object()
        obj.result = self.get_result(obj)
        context["object"] = obj
        return super(TaskDetailView, self).get_context_data(**context)


class TaskArchiveView(DateTimeMixin, DynamicDateFieldMixin, ArchiveIndexView):
    model = DramatiqTask
    template_name = "archive.html"


class TaskYearArchiveView(DateTimeMixin, DynamicDateFieldMixin, YearArchiveView):
    model = DramatiqTask
    template_name = "archive_year.html"
    make_object_list = True
    allow_empty = True
    allow_future = True


class TaskMonthArchiveView(DateTimeMixin, DynamicDateFieldMixin, MonthArchiveView):
    model = DramatiqTask
    template_name = "archive_month.html"
    allow_future = True
    allow_empty = True


class TaskDayArchiveView(DateTimeMixin, DynamicDateFieldMixin, DayArchiveView):
    model = DramatiqTask
    template_name = "archive_day.html"
    week_format = "%W"
    allow_future = True
    allow_empty = True
