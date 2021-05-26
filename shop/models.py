from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=60)
    cost = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    def __str__(self):
        return '<Item:id=' + str(self.id) + ', ' + \
            self.name + '(' + str(self.cost) + ') : ' + \
            self.description + '>'
            

class Shop(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return '<Item:id=' + str(self.id) + ', ' + \
            self.name + '>'
            
            
class Stock(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    num = models.IntegerField(default=0)
    def __str__(self):
        return '<Item:id=' + str(self.id) + ', ' + \
            str(self.shop.name) + ', ' + \
            str(self.item.name) + ', ' + \
            str(self.num) + '>'
            
