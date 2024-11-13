# Generated by Django 4.2.7 on 2024-11-10 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('CompanyID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('CompanyName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('CountryID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('CountryName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrganization',
            fields=[
                ('SalesOrganizationID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('SalesOrganizationName', models.CharField(max_length=50)),
                ('CompanyID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='CountryID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.country'),
        ),
        migrations.CreateModel(
            name='AccountGroup',
            fields=[
                ('AccountGroupID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('AccountGroupName', models.CharField(max_length=50)),
                ('SalesOrganizationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.salesorganization')),
            ],
        ),
    ]