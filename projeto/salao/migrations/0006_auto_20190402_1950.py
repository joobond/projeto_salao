# Generated by Django 2.2 on 2019-04-02 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salao', '0005_auto_20190402_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='produto_venda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salao.Produto'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='servico_venda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salao.Servico'),
        ),
    ]
