from django.db import migrations, models


def create_default_category(apps, _schema_editor):
    Category = apps.get_model('home', 'Category')
    Category.objects.get_or_create(id=1, defaults={'name': 'Uncategorized'})


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),

        migrations.RunPython(create_default_category),

        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(
                to='home.Category',
                on_delete=models.CASCADE,
                default=1,
            ),
            preserve_default=False,
        ),
    ]
