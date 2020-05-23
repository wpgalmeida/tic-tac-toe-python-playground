# Generated by Django 3.0.5 on 2020-05-23 10:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('num_cols', models.IntegerField()),
                ('num_rows', models.IntegerField()),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('birth', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('bot', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlayerBoard',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('symbol', models.CharField(default=None, max_length=1)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Board')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Movements',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position', models.IntegerField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Board')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('draw', models.BooleanField(default=False)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Board')),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Player')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='playerboard',
            constraint=models.UniqueConstraint(fields=('player', 'board'), name='unique_player_board'),
        ),
        migrations.AddConstraint(
            model_name='movements',
            constraint=models.UniqueConstraint(fields=('position', 'board'), name='unique_position_board'),
        ),
    ]
