# Generated by Django 2.2.4 on 2019-08-31 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20190831_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=7)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('impostos', models.DecimalField(decimal_places=2, max_digits=5)),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.Person')),
            ],
        ),
    ]
