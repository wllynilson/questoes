# Generated by Django 2.2.2 on 2019-06-13 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CGU', models.CharField(max_length=9, null=True)),
                ('pontuacao', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ['pontuacao'],
            },
        ),
        migrations.CreateModel(
            name='Anexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('tipoanexo', models.IntegerField(choices=[(1, 'Imagem'), (2, 'Pdf')], default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Questoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.TextField(max_length=200, null=True)),
                ('alternativaA', models.TextField(max_length=200, null=True)),
                ('alternativaB', models.TextField(max_length=200, null=True)),
                ('alternativaC', models.TextField(max_length=200, null=True)),
                ('alternativaD', models.TextField(max_length=200, null=True)),
                ('nivel', models.IntegerField(choices=[(1, 'Fácil'), (2, 'Média'), (3, 'Difícil')], default=1)),
                ('anexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oslive.Anexo')),
            ],
            options={
                'ordering': ['enunciado'],
            },
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.CharField(max_length=5, null=True)),
                ('academico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oslive.Academico')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oslive.Questoes')),
            ],
        ),
    ]