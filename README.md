# Django Dramatiq Dashboard
A dashboard for [django_dramatiq]

It comes in the form of a Django application

## Requirements
* [django_dramatiq]

## Installation
*In progress*: ```pip install django_dramatiq_dashboard ```

Add dramatiq_dashboard to installed apps:
```python
INSTALLED_APPS = (
    ...
    "django_dramatiq",
    "dramatiq_dashboard",
    ...
)
```
Add dramatiq_dashboard urls:
```python
urlpatterns = [
    (...),
    path("dramatiq_dashboard/", include("dramatiq_dashboard.urls")),
]
```

To use GraphQL API endpoints, check [graphql_api] branch 

To configure dramatiq, check [django_dramatiq]


[django_dramatiq]: https://github.com/Bogdanp/django_dramatiq
[graphql_api]: https://gitlab.com/99q/django-dramatiq-dashboard/-/tree/graphql_api