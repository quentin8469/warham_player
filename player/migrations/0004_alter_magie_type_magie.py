# Generated by Django 4.0.1 on 2022-02-16 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_competence_apprentissage_competence_cout_xp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magie',
            name='type_magie',
            field=models.CharField(choices=[('Magie mineure', 'Magie mineure'), ('Magie de bataille', 'Magie de bataille'), ('Magie démonique', 'Magie démonique'), ('Magie druidique', 'Magie druidique'), ('Magie elementaire', 'Magie elementaire'), ('Magie illusoire', 'Magie illusoire'), ('Magie necromantique', 'Magie necromantique'), ('Magie autre', 'Magie autre')], max_length=50),
        ),
    ]