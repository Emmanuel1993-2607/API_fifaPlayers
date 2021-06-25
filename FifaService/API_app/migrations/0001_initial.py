

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commonName', models.CharField(max_length=65)),
                ('firstName', models.CharField(max_length=65)),
                ('lastName', models.CharField(max_length=65)),
                ('position', models.CharField(max_length=65)),
                ('fifa_id', models.CharField(max_length=65)),
            ],
        ),
    ]
