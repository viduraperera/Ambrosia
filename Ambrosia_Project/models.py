from django.db import models


class Broker(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=10, null=True)


class Buyer(models.Model):
    vat_regno = models.CharField(max_length=30)
    name = models.CharField(max_length=50)


class packetType(models.Model):
    WEIGHT = (
        ('1kg', '1Kg'),
        ('500g', '500g'),
        ('400g', '400g'),
        ('250g', '250g'),
        ('200g', '200g'),
    )
    packet_weight_id = models.CharField(max_length=10)
    weight = models.CharField(max_length=10, choices=WEIGHT)

    #class Meta:
    #    db_table = 'packetType'


class teaCategory(models.Model):
    CATEGORY = (
        ('bopf', 'BOPF'),
        ('dust1', 'DUST 1'),
        ('dust2', 'DUST 2'),
        ('fgs', 'FGS'),
    )

    category_id = models.CharField(max_length=10)
    description = models.CharField(max_length=10, choices=CATEGORY)

    #class Meta:
     #   db_table = 'teaCategory'


class categoryProduct(models.Model):
    cp_id = models.CharField(max_length=10)
    price = models.FloatField()
    category_id = models.ForeignKey(teaCategory, on_delete=models.CASCADE, null=True)
    packet_weight_id = models.ForeignKey(packetType, on_delete=models.CASCADE, null=True)


class addPackets(models.Model):
    CATEGORY = (
        ('bopf', 'BOPF'),
        ('dust1', 'DUST 1'),
        ('dust2', 'DUST 2'),
        ('fgs', 'FGS'),
    )
    WEIGHT = (
        ('1kg', '1Kg'),
        ('500g', '500g'),
        ('400g', '400g'),
        ('250g', '250g'),
        ('200g', '200g'),
    )
    date = models.DateField()
    noOfPackets = models.IntegerField()
    category = models.CharField(max_length=10, choices=CATEGORY)
    weight = models.CharField(max_length=10, choices=WEIGHT)


class preorder(models.Model):
    CATEGORY = (
        ('bopf', 'BOPF'),
        ('dust1', 'DUST 1'),
        ('dust2', 'DUST 2'),
        ('fgs', 'FGS'),
    )
    WEIGHT = (
        ('1kg', '1Kg'),
        ('500g', '500g'),
        ('400g', '400g'),
        ('250g', '250g'),
        ('200g', '200g'),
    )
    category = models.CharField(max_length=10, choices=CATEGORY)
    weight = models.CharField(max_length=10, choices=WEIGHT)
    preorder_level = models.IntegerField()


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