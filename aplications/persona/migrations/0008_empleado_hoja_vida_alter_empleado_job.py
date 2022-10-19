# Generated by Django 4.0.5 on 2022-08-23 19:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0007_empleado_habilidades_alter_empleado_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='texto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='job',
            field=models.CharField(choices=[('3', 'OTRO'), ('0', 'CONTADOR'), ('2', 'ECONOMISTA'), ('1', 'ADMINISTRADOR')], max_length=1, verbose_name='trabajo'),
        ),
    ]
