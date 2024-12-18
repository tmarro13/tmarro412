# Generated by Django 4.2.16 on 2024-12-05 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0005_rename_date_review_created_at"),
    ]

    operations = [
        migrations.RemoveField(model_name="tag", name="description",),
        migrations.RemoveField(model_name="tag", name="movies",),
        migrations.AddField(
            model_name="movie",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="tagged_movies", to="project.tag"
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
