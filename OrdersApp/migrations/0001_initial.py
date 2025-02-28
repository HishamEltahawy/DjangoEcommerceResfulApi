# Generated by Django 5.1.6 on 2025-02-28 13:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ProductsApp', '0002_reviews'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='', max_length=400)),
                ('zip_code', models.CharField(default='', max_length=100)),
                ('street', models.CharField(default='', max_length=500)),
                ('state', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('phone_no', models.CharField(default='', max_length=100)),
                ('total_amount', models.IntegerField(default=0)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=30)),
                ('payment_mode', models.CharField(choices=[('COD', 'Cod'), ('CARD', 'Card')], default='COD', max_length=30)),
                ('status', models.CharField(choices=[('Processing', 'Processing'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Processing', max_length=60)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='OrdersApp.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProductsApp.products')),
            ],
        ),
    ]
