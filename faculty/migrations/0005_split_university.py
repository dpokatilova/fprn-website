import re
from django.db import migrations


def split_university_data(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        raw = program.university
        parts = re.split(r"[,(-]\s*", raw.strip(")"))
        program.university_name = parts[0].strip()
        if len(parts) > 1:
            program.country = parts[1].strip()
        else:
            program.country = ""

        program.save(update_fields=["university_name", "country"])


def join_university_data(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.university = f"{program.university_name}, {program.country}".strip()
        program.save(update_fields=["university"])

class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0004_exchangeprogram_country_and_more'),
    ]

    operations = [
        migrations.RunPython(split_university_data, reverse_code=join_university_data),
    ]
