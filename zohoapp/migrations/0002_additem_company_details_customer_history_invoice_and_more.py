# Generated by Django 4.2 on 2023-05-02 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(max_length=255)),
                ('Name', models.TextField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('s_desc', models.TextField(max_length=255)),
                ('p_desc', models.TextField(max_length=255)),
                ('creat', models.CharField(max_length=255)),
                ('s_price', models.CharField(max_length=255)),
                ('p_price', models.TextField(max_length=255)),
                ('satus', models.TextField(default='active')),
                ('interstate', models.CharField(max_length=255)),
                ('intrastate', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='company_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(blank=True, max_length=100, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('company_email', models.CharField(blank=True, max_length=255, null=True)),
                ('business_name', models.CharField(blank=True, max_length=255, null=True)),
                ('company_type', models.CharField(blank=True, max_length=255, null=True)),
                ('industry_type', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='image/patient')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(blank=True, max_length=100, null=True)),
                ('customerType', models.CharField(blank=True, max_length=100, null=True)),
                ('companyName', models.CharField(blank=True, max_length=100, null=True)),
                ('customerEmail', models.CharField(blank=True, max_length=100, null=True)),
                ('customerWorkPhone', models.CharField(blank=True, max_length=100, null=True)),
                ('customerMobile', models.CharField(blank=True, max_length=100, null=True)),
                ('skype', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('GSTTreatment', models.CharField(blank=True, max_length=100, null=True)),
                ('placeofsupply', models.CharField(blank=True, max_length=100, null=True)),
                ('Taxpreference', models.CharField(blank=True, max_length=100, null=True)),
                ('currency', models.CharField(blank=True, max_length=100, null=True)),
                ('OpeningBalance', models.IntegerField(blank=True, null=True)),
                ('PaymentTerms', models.CharField(blank=True, max_length=100, null=True)),
                ('PriceList', models.CharField(blank=True, max_length=100, null=True)),
                ('PortalLanguage', models.CharField(blank=True, max_length=100, null=True)),
                ('Facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('Twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('Attention', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('Address1', models.CharField(blank=True, max_length=100, null=True)),
                ('Address2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=100, null=True)),
                ('phone1', models.CharField(blank=True, max_length=100, null=True)),
                ('fax', models.CharField(blank=True, max_length=100, null=True)),
                ('CPsalutation', models.CharField(blank=True, max_length=100, null=True)),
                ('Firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('Lastname', models.CharField(blank=True, max_length=100, null=True)),
                ('CPemail', models.CharField(blank=True, max_length=100, null=True)),
                ('CPphone', models.CharField(blank=True, max_length=100, null=True)),
                ('CPmobile', models.CharField(blank=True, max_length=100, null=True)),
                ('CPskype', models.CharField(blank=True, max_length=100, null=True)),
                ('CPdesignation', models.CharField(blank=True, max_length=100, null=True)),
                ('CPdepartment', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('message', models.CharField(max_length=255)),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.additem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.TextField(max_length=255)),
                ('terms', models.TextField(max_length=255)),
                ('order_no', models.IntegerField()),
                ('inv_date', models.DateField()),
                ('due_date', models.DateField()),
                ('igst', models.TextField(max_length=255)),
                ('cgst', models.TextField(max_length=255)),
                ('sgst', models.TextField(max_length=255)),
                ('t_tax', models.FloatField()),
                ('subtotal', models.FloatField()),
                ('grandtotal', models.FloatField()),
                ('cxnote', models.TextField(max_length=255)),
                ('file', models.ImageField(upload_to='documents')),
                ('terms_condition', models.TextField(max_length=255)),
                ('status', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='invoice_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.TextField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('hsn', models.TextField(max_length=255)),
                ('tax', models.IntegerField()),
                ('total', models.FloatField()),
                ('desc', models.TextField(max_length=255)),
                ('rate', models.TextField(max_length=255)),
                ('inv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_type', models.TextField(max_length=255)),
                ('Account_name', models.TextField(max_length=255)),
                ('Acount_code', models.TextField(max_length=255)),
                ('Account_desc', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_type', models.TextField(max_length=255)),
                ('Account_name', models.TextField(max_length=255)),
                ('Acount_code', models.TextField(max_length=255)),
                ('Account_desc', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.TextField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='customer_details',
        ),
        migrations.AddField(
            model_name='additem',
            name='purchase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.purchase'),
        ),
        migrations.AddField(
            model_name='additem',
            name='sales',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.sales'),
        ),
        migrations.AddField(
            model_name='additem',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.unit'),
        ),
        migrations.AddField(
            model_name='additem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]