from django.db import models

# Create your models here.
# Create your models here.
class Broker(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=10, null=True)

class Buyer(models.Model):
    vat_regno = models.CharField(max_length=30)
    name = models.CharField(max_length=50)

class packetType(models.Model):
    packet_weight_id = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)

    class Meta:
        db_table = 'packetType'

class teaCategory(models.Model):
    category_id = models.CharField(max_length=10)
    description = models.CharField(max_length=10)

    class Meta:
        db_table = 'teaCategory'

class categoryProduct(models.Model):
    cp_id = models.CharField(max_length=10)
    price = models.FloatField()
    category_id = models.ForeignKey(teaCategory, on_delete=models.CASCADE, null=True)
    packet_weight_id = models.ForeignKey(packetType, on_delete=models.CASCADE, null=True)

class preorder(models.Model):
    preorder_level = models.CharField(max_length=10)
    cp_id = models.ForeignKey(categoryProduct, on_delete=models.CASCADE, null=True)

class Accumulate(models.Model):
    noOf_Packets = models.IntegerField()
    cp_id = models.ForeignKey(categoryProduct, on_delete=models.CASCADE, null=True)

class Packet_stock(models.Model):
    product_ID = models.CharField(max_length=10)
    no_ofPackets = models.IntegerField()
    date = models.DateField()
    cp_id = models.ForeignKey(categoryProduct, on_delete=models.CASCADE, null=True)

class Sales_Transactions(models.Model):
    noOfPackets = models.IntegerField()
    total_Price = models.FloatField()
    cp_id = models.ForeignKey(categoryProduct, on_delete=models.CASCADE, null=True)
    product_ID = models.ForeignKey(Packet_stock, on_delete=models.CASCADE, null=True)