# Generated by Django 5.0.3 on 2024-04-08 23:50

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producao',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='producao.basemodel')),
                ('title', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(1)])),
                ('advisory_certificate', models.CharField(choices=[('G', 'General Audiences'), ('PG', 'Parental Guidance Suggested'), ('PG13', 'Parents Strongly Cautioned'), ('R', 'Restricted'), ('NC17', 'Adults Only')], default='PG13', max_length=20, validators=[django.core.validators.MinLengthValidator(1)])),
                ('length', models.DurationField()),
                ('genre', models.CharField(choices=[('AC', 'Action'), ('ADV', 'Adventure'), ('ANI', 'Animation'), ('BIO', 'Biography'), ('DOC', 'Documentary'), ('COM', 'Comedy'), ('CRI', 'Crime'), ('DRM', 'Drama'), ('FAM', 'Family'), ('FNT', 'Fantasy'), ('HIS', 'History'), ('HRR', 'Horror'), ('MUS', 'Musical'), ('MYS', 'Mystery'), ('ROM', 'Romance'), ('SCIFI', 'Science Fiction'), ('SHRT', 'Short'), ('SPO', 'Sport'), ('THR', 'Thriller'), ('WR', 'War'), ('WST', 'Western')], default='AC', max_length=20, validators=[django.core.validators.MinLengthValidator(1)])),
                ('trendimeter', models.IntegerField()),
                ('reviews', models.FloatField()),
                ('specs', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5)])),
                ('synopsis', models.TextField(max_length=500, validators=[django.core.validators.MinLengthValidator(10)])),
                ('release_date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
            bases=('producao.basemodel',),
        ),
    ]