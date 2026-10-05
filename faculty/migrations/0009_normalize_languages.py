from django.db import migrations


def normalize_languages_data(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        langs = program.languages.lower()
        langs = langs.replace("english", "англійська")
        program.languages = langs
        program.save(update_fields=["languages"])

class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0008_alter_exchangeprogram_places'),
    ]

    operations = [
        migrations.RunPython(normalize_languages_data, reverse_code=migrations.RunPython.noop),
    ]
