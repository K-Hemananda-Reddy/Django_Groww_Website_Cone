from pyexpat import model
from django.db import models

# Create your models here.
class Orders(models.Model):
    CustomerID = models.IntegerField()
    CustomerName = models.CharField(max_length=50)
    OrderNo = models.AutoField
    ShareName = models.CharField(max_length=50)
    Buy_SellPrice = models.IntegerField()
    NumberOfShares = models.IntegerField()
    OrderDate = models.DateField()
    OrderTime = models.TimeField()

    def __str__(self):
        a = str(str(self.CustomerID)+"_Amount_Rs."+str(self.Buy_SellPrice*self.NumberOfShares)+"/-_"+self.ShareName+"_"+str(self.CustomerName)+"_"+str(self.OrderDate)+"_"+str(self.OrderTime))
        return a 


class wallet(models.Model):
    money=models.IntegerField()
    date = models.DateField()
    time=models.TimeField()
    upi_id=models.CharField(max_length=25)
    Total_money=models.IntegerField()
    def __str__(self):
        a = str(str(self.money)+"__"+str(self.date)+"__"+str(self.time))
        return a 