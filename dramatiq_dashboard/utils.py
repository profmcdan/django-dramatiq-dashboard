from django.utils import timezone
from django.views.generic.dates import DateMixin


class DynamicDateFieldMixin(DateMixin):
    def get_date_field(self):
        date_field = self.request.GET.get("field", "created_at")
        return date_field


class DateTimeMixin:
    def get_context_data(self, **kwargs):
        context = super(DateTimeMixin, self).get_context_data(**kwargs)
        context["date"] = timezone.now()
        return context
