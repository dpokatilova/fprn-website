from django.shortcuts import get_object_or_404, render

from faculty.models import Department, ExchangeProgram, MainPage, Program


def home_view(request):
    main_page = MainPage.objects.first()
    return render(request, "home.html", {"main_page": main_page})


def program_list_view(request):
    programs = Program.objects.all()
    return render(request, "program_list.html", {"programs": programs})


def program_detail_view(request, id):
    program = get_object_or_404(Program, id=id)
    return render(request, "program_detail.html", {"program": program})


def department_list_view(request):
    departments = Department.objects.all()
    return render(request, "department_list.html", {"departments": departments})


def department_detail_view(request, id):
    department = get_object_or_404(Department, id=id)
    return render(request, "department_detail.html", {"department": department})


def exchange_list_view(request):
    programs = ExchangeProgram.objects.all().order_by("deadline")
    return render(request, "exchange_list.html", {"programs": programs})
