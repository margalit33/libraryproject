# Generated by Django 4.2.4 on 2023-08-21 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('book', models.CharField(max_length=100)),
                ('loandate', models.DateTimeField()),
                ('returndate', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='https://loremflickr.com/cache/resized/65535_52464844953_602e80cc9e_320_320_nofilter.jpg', upload_to='book_images'),
        ),
    ]
