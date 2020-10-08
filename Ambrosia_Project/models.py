from django.db import models


class CategoryProduct(models.Model):

    cp_name = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)

    class Meta:
        unique_together = (('category', 'weight'),)

    def __str__(self):
        return self.cp_name


class AddPackets(models.Model):

    date = models.DateField()
    noOfPackets = models.IntegerField()
    categoryProductID = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)


class Stock(models.Model):
    category = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    available_stock = models.IntegerField()

    class Meta:
        unique_together = (('category', 'weight'),)







