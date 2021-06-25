from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nameteam', models.CharField(max_length=65)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='teamId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.team'),
            preserve_default=False,
        ),
    ]
