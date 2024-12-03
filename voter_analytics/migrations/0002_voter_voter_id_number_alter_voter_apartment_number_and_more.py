# Generated by Django 4.2.16 on 2024-11-11 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voter_analytics", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="voter",
            name="voter_id_number",
            field=models.CharField(default="UNKNOWN", max_length=100),
        ),
        migrations.AlterField(
            model_name="voter",
            name="apartment_number",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="voter",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="voter",
            name="date_of_registration",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="voter", name="first_name", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="voter", name="last_name", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="voter", name="party_affiliation", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="voter", name="precinct_number", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="voter", name="street_name", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="voter", name="street_number", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="voter", name="zip_code", field=models.TextField(),
        ),
    ]