# Generated by Django 2.1.7 on 2019-04-02 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salao', '0003_auto_20190402_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_venda', models.DateTimeField(verbose_name='data published')),
                ('soma_pontos_venda', models.IntegerField(default=0)),
                ('cliente_venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salao.Cliente')),
                ('produto_venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salao.Produto')),
                ('servico_venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salao.Servico')),
            ],
        ),
    ]
