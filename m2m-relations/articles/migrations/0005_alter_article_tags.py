# Generated by Django 4.2.2 on 2023-07-04 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_scope_is_main_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(through='articles.Scope', to='articles.tag', verbose_name='Раздел'),
        ),
    ]
