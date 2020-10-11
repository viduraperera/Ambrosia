# Generated by Django 3.1.1 on 2020-10-11 13:56

import Ambrosia_Project.common_utills.validators
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('amount', models.FloatField()),
            ],
            options={
                'db_table': 'advance',
            },
        ),
        migrations.CreateModel(
            name='Allowance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allowance_by_price', models.FloatField()),
                ('incentive_1', models.FloatField()),
                ('incentive_2', models.FloatField()),
            ],
            options={
                'db_table': 'allowance',
            },
        ),
        migrations.CreateModel(
            name='Auction_NotSoldStocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MainID', models.IntegerField(blank=True)),
                ('SubID', models.IntegerField(blank=True)),
                ('active', models.IntegerField(blank=True, default=1)),
            ],
            options={
                'db_table': 'Auction_NotSoldStock',
            },
        ),
        migrations.CreateModel(
            name='Auction_NotSoldStocksLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LastUpdated', models.DateTimeField(auto_now_add=True)),
                ('Description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'Auction_NotSoldStockLog',
            },
        ),
        migrations.CreateModel(
            name='Auction_RePreparedNotSoldStocksDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NotSoldStockID', models.IntegerField(blank=True)),
                ('PreviousSubStockMainID', models.IntegerField(blank=True)),
                ('NewSubStockMainID', models.IntegerField(blank=True)),
                ('LastUpdated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Auction_NotSoldStockDetails',
            },
        ),
        migrations.CreateModel(
            name='BillItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_id', models.IntegerField(blank=True)),
                ('itemname', models.CharField(choices=[('BOPF', 'BOPF'), ('DUST 1', 'DUST 1'), ('DUST 2', 'DUST 2'), ('FGS', 'FGS')], max_length=10)),
                ('weight', models.CharField(choices=[('1Kg', ' 1Kg'), ('500g', '500g'), ('400g', '400g'), ('250g', '250Kg'), ('200g', '200g')], max_length=10)),
                ('itemPrice', models.FloatField(blank=True)),
                ('price', models.FloatField(blank=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(null=True)),
                ('vat_regno', models.CharField(blank=True, max_length=15, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='Vat Reg.No is Invalid', message='Vat Registration Number must contain only numbers', regex='^[0-9-]*$')])),
                ('phone', models.CharField(max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='Phone Number is Invalid', message='Phone Number must contain only numbers.', regex='^[0-9]*$'), django.core.validators.RegexValidator(code='Phone Number is Invalid', message='Phone Number length is invalid', regex='^.{10}$')])),
            ],
            options={
                'db_table': 'Broker',
            },
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vat_regno', models.CharField(blank=True, max_length=15, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='Vat Reg.No is Invalid', message='Vat Registration Number must contain only numbers', regex='^[0-9-]*$')])),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Buyer',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licence_no', models.CharField(max_length=10)),
                ('epfNo', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nic', models.CharField(max_length=12, unique=True, validators=[
                    Ambrosia_Project.common_utills.validators.nic_validator])),
                ('epfNo', models.IntegerField(null=True, unique=True, validators=[django.core.validators.RegexValidator(code='EPF No is invalid', message='EPF No can only contain numbers', regex='^[0-9]*$')])),
                ('empImage', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('dob', models.DateField(null=True)),
                ('maritalStatus', models.CharField(choices=[('Married', 'Married'), ('UnMarried', 'Unmarried')], max_length=50)),
                ('contactNo', models.CharField(max_length=10, null=True, validators=[django.core.validators.RegexValidator(code='Invalid Contact No ', message='Contact No can only contain numbers', regex='^[0-9]*$'), django.core.validators.RegexValidator(code='Invalid Contact No ', message='Contact No length is invalid', regex='^.{10}$')])),
                ('doa', models.DateField(null=True)),
                ('basicSalary', models.FloatField(null=True)),
                ('empType', models.CharField(choices=[('Permanent', 'Permanent'), ('Temparory', 'Temparory')], max_length=50, null=True)),
                ('empGroup', models.CharField(choices=[('staff', 'Staff'), ('factory_Worker', 'FactoryWorker')], max_length=50, null=True)),
                ('designation', models.CharField(blank=True, choices=[('Factory_Officer', 'Factory_Officer'), ('AssistantFactory_Officer', 'AssistantFactory_Officer'), ('Clerk', 'Clerk'), ('Trainee', 'Trainee'), ('Supervisor', 'Supervisor'), ('Cashier', 'Cashier'), ('Driver', 'Driver')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('attendance_on_month', models.FloatField()),
                ('year', models.CharField(max_length=4)),
                ('month', models.CharField(max_length=20)),
                ('allowance_b_price', models.FloatField(null=True)),
                ('incentive_1', models.FloatField(null=True)),
                ('incentive_2', models.FloatField(null=True)),
                ('basic_salary_of_day', models.FloatField()),
                ('basic_salary_of_month', models.FloatField()),
                ('etf_of_month', models.FloatField()),
                ('epf_employee_month', models.FloatField()),
                ('epf_employer_month', models.FloatField()),
                ('ot_hours', models.IntegerField(null=True)),
                ('loan', models.FloatField(null=True)),
                ('advance', models.FloatField(null=True)),
                ('tea_advance', models.FloatField(null=True)),
                ('ot_amount_for_month', models.FloatField(null=True)),
                ('total_salary', models.FloatField(null=True)),
                ('total_deduction', models.FloatField(null=True)),
                ('remaining_salary', models.FloatField(null=True)),
            ],
            options={
                'db_table': 'Employee_salary',
            },
        ),
        migrations.CreateModel(
            name='Final_product_Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subID', models.IntegerField(blank=True)),
                ('totalWeight', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'Final_product_Main',
            },
        ),
        migrations.CreateModel(
            name='Funds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_etf', models.FloatField()),
                ('epf_employee', models.FloatField()),
                ('epf_employer', models.FloatField()),
            ],
            options={
                'db_table': 'funds',
            },
        ),
        migrations.CreateModel(
            name='LeafInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_Date', models.DateField()),
                ('in_Time', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23.59)])),
                ('tray_Id', models.IntegerField()),
                ('temp', models.FloatField()),
                ('weight', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('out_Date', models.DateField()),
                ('out_Time', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23.59)])),
            ],
            options={
                'db_table': 'inventory',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('date_of_loan_request', models.DateField(default=datetime.datetime.now)),
                ('amount_loan', models.FloatField()),
                ('time_duration', models.IntegerField()),
                ('remaining_loan_amount', models.FloatField()),
                ('loan_status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'loan',
            },
        ),
        migrations.CreateModel(
            name='OverTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('data', models.DateField(default=datetime.datetime.now)),
                ('ot_hours', models.FloatField()),
            ],
            options={
                'db_table': 'Over_Time',
            },
        ),
        migrations.CreateModel(
            name='Price_Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('BOPF', 'BOPF'), ('DUST 1', 'DUST 1'), ('DUST 2', 'DUST 2'), ('FGS', 'FGS')], max_length=10)),
                ('weight', models.CharField(choices=[('1Kg', ' 1Kg'), ('500g', '500g'), ('400g', '400g'), ('250g', '250Kg'), ('200g', '200g')], max_length=10)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sup_Name', models.CharField(max_length=50)),
                ('proPic', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('nicNo', models.CharField(max_length=10, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10, null=True, validators=[django.core.validators.RegexValidator(code='Phone Number is Not Valid!', message='ERROR!! Phone Number Should Contain Only Numbers', regex='^[0-9]*$'), django.core.validators.RegexValidator(code='Phone Number is Not Valid!', message='ERROR!! Phone Number is Invalid!', regex='^.{10}$')])),
                ('email', models.CharField(max_length=100, null=True)),
                ('DOB', models.DateField()),
                ('Reg_Date', models.DateField(default=datetime.datetime.now)),
                ('est_name', models.CharField(max_length=50)),
                ('route', models.CharField(choices=[('WE', 'WE'), ('BR', 'BR'), ('BNR', 'BNR')], max_length=3)),
                ('sup_scale', models.CharField(choices=[('sm', 'Small-Scale'), ('lg', 'Large-Scale')], max_length=2)),
                ('pay_Type', models.CharField(choices=[('C', 'Cash'), ('CH', 'Check'), ('BD', 'Bank-Deposit')], max_length=3)),
                ('acc_No', models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator(code='Acc No is Not Valid!', message='ERROR!!', regex='^[0-9]*$')])),
                ('bank', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ambrosia_project_register',
            },
        ),
        migrations.CreateModel(
            name='TeaAdvance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('amount', models.FloatField()),
            ],
            options={
                'db_table': 'tea_advance',
            },
        ),
        migrations.CreateModel(
            name='TeaGrades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teaGrade', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'tea_grade',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('total_Price', models.FloatField(blank=True)),
                ('invoice_id', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehicleNo', models.CharField(max_length=20, unique=True)),
                ('Driverid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ambrosia_Project.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
                ('available_stock', models.IntegerField()),
            ],
            options={
                'unique_together': {('category', 'weight')},
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bill_No', models.CharField(max_length=10)),
                ('Description', models.TextField()),
                ('Service_Date', models.DateField(default=datetime.datetime.now)),
                ('Amount', models.FloatField()),
                ('VehicleNo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ambrosia_Project.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additions', models.FloatField()),
                ('pay_Date', models.DateField(default=datetime.datetime.now)),
                ('pay_Time', models.TimeField(default=datetime.datetime.now)),
                ('advances', models.FloatField()),
                ('transport_costs', models.FloatField()),
                ('other_costs', models.FloatField()),
                ('tot_weight', models.FloatField()),
                ('per_kilo_price', models.FloatField()),
                ('payment', models.FloatField(blank=True, null=True)),
                ('nic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='Ambrosia_Project.registration', to_field='nicNo')),
            ],
            options={
                'db_table': 'ambrosia_project_payment',
            },
        ),
        migrations.CreateModel(
            name='LeafStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('rec_Date', models.DateField(default=datetime.datetime.now)),
                ('rec_Time', models.TimeField(default=datetime.datetime.now)),
                ('nic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leaf_stock', to='Ambrosia_Project.registration', to_field='nicNo')),
            ],
            options={
                'db_table': 'ambrosia_project_leafstock',
            },
        ),
        migrations.CreateModel(
            name='Final_product_sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subID', models.IntegerField(blank=True)),
                ('gradeWeight', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('teaGrade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ambrosia_Project.teagrades')),
            ],
            options={
                'db_table': 'Final_product_sub',
            },
        ),
        migrations.CreateModel(
            name='Driving_Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(default=datetime.datetime.now)),
                ('Start_Reading', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(code='Start date is invalid', message='Start reading must contain only numbers', regex='^[0-9]*$')])),
                ('End_Reading', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(code='End date is invalid', message='End reading must contain only numbers', regex='^[0-9]*$')])),
                ('Meter_Difference', models.IntegerField(blank=True)),
                ('VehicleNo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ambrosia_Project.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp_name', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
            ],
            options={
                'unique_together': {('category', 'weight')},
            },
        ),
        migrations.CreateModel(
            name='Auction_SubStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubID', models.IntegerField(blank=True)),
                ('invoice', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('no_of_packets', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('net_weight', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
                ('total_weight', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
                ('packetType', models.CharField(blank=True, choices=[('DPBS', 'DPBS'), ('MNBS', 'MNBS')], max_length=10)),
                ('date_prepared', models.DateField(blank=True, default=datetime.datetime.now)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('active', models.IntegerField(blank=True, default=1)),
                ('grade', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Ambrosia_Project.teagrades', to_field='teaGrade')),
            ],
            options={
                'db_table': 'Auction_SubStock',
            },
        ),
        migrations.CreateModel(
            name='Auction_SoldStocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MainID', models.IntegerField(blank=True)),
                ('SubID', models.IntegerField(blank=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
                ('total_price', models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('sold_Date', models.DateField()),
                ('active', models.IntegerField(blank=True, default=1)),
                ('Buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Ambrosia_Project.buyer')),
            ],
            options={
                'db_table': 'Auction_SoldStock',
            },
        ),
        migrations.CreateModel(
            name='Auction_MainStock',
            fields=[
                ('SubID', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('Date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('total_netWeight', models.FloatField(blank=True)),
                ('total_grossWeight', models.FloatField(blank=True)),
                ('total_packets', models.IntegerField(blank=True)),
                ('Broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ambrosia_Project.broker')),
            ],
            options={
                'db_table': 'Auction_MainStock',
            },
        ),
        migrations.CreateModel(
            name='AddPackets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('noOfPackets', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('categoryProductID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ambrosia_Project.categoryproduct')),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True)),
                ('daytype', models.CharField(blank=True, choices=[('FD', 'FullDay'), ('HD', 'HalfDay')], max_length=20)),
                ('attendaceStatus', models.CharField(blank=True, choices=[('Pres', 'Present'), ('Abs', 'Absent')], max_length=50)),
                ('empID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='Ambrosia_Project.employee')),
            ],
            options={
                'unique_together': {('date', 'empID')},
            },
        ),
    ]
