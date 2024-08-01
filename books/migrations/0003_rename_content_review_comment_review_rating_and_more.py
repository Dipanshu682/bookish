# Generated by Django 4.2.14 on 2024-07-31 11:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_review"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review", old_name="content", new_name="comment",
        ),
        migrations.AddField(
            model_name="review",
            name="rating",
            field=models.PositiveIntegerField(
                default=3,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="books.book"
            ),
        ),
    ]
