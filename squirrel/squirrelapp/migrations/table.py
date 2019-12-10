from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
                ]
    operations = [
            migrations.CreateModel(
                name='Squirrels',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                     ('Latitude', models.IntegerField()),
                     ('Longitude', models.IntegerField()),
                     ('Squirrel_Id', models.CharField(help_text="Squirrel's Unique ID", max_length=30)),
                     ('Shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=2)),
                     ('Date', models.DateField(help_text='Date of the sighting')),
                     ('Age', models.CharField(choices=[('adult', 'Adult'), ('juvenile', 'Juvenile'), ('', ''), ('?', '?')], help_text='Age of the Squirrel', max_length=50)),
                     ('Primary_Fur_Color', models.CharField(choices=[('black', 'Black'), ('cinnamon', 'Cinnamon'), ('gray', 'Gray')], help_text='Color of the squirrel', max_length=20)),
                     ('Running', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Is it running?', max_length=20)),
                     ('Chasing', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Is it chasing?', max_length=20)),
                     ('Climbing', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Is it climbing?', max_length=20)),
                     ('Eating', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Is it eating?', max_length=20)),
                     ('Foraging', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='is it foraging?', max_length=20)),
                     ('Other_Activities', models.CharField(help_text='What other activities is it doing?', max_length=100)),
                     ('kuk', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Does it kuks?', max_length=20)),
                     ('quaas', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Does it quaas?', max_length=20)),
                     ('moan', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Does it moan?', max_length=20)),
                     ('Tail_flags', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Does it flag its tail?', max_length=20)),
                     ('Tail_twitch', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Does it twitch its tail?', max_length=20)),
                     ('Approaches', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Does it approach?', max_length=20)),
                     ('Indifferent', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Is it indifferent?', max_length=20)),
                     ('Runs_from', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Does it run away?', max_length=20)),
                ],
            ),
        ]

