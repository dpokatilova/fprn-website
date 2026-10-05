from django.urls import path

from faculty.views import (
    department_detail_view,
    department_list_view,
    exchange_list_view,
    home_view,
    program_detail_view,
    program_list_view,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("programs/", program_list_view, name="program-list"),
    path("programs/<int:id>/", program_detail_view, name="program-detail"),
    path("departments/", department_list_view, name="department-list"),
    path("departments/<int:id>/", department_detail_view, name="department-detail"),
    path("exchange/", exchange_list_view, name="exchange-list"),
]
