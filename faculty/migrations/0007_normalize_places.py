import re
from django.db import migrations

def normalize_places_data(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        match = re.search(r"\d+", program.places)
        program.places = match.group(0) if match else "0"
        program.save(update_fields=["places"])

class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0006_remove_exchangeprogram_university'),
    ]

    operations = [
        migrations.RunPython(normalize_places_data, reverse_code=migrations.RunPython.noop),
    ]
