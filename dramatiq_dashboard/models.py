from django.urls import reverse
from django_dramatiq.models import Task


class DramatiqTask(Task):
    def get_absolute_url(self):
        return reverse(
            "django_dramatiq_dashboard:executed_detail", kwargs={"id": self.id}
        )

    class Meta:
        proxy = True
