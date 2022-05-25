from decimal import Decimal

from django.db import models

from django.contrib.auth.models import User



class Users(models.Model):
    username=models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    cpassword = models.CharField(max_length=40)

    class Meta:
        db_table = "Users"


class item(models.Model):
    name = models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    price = models.IntegerField()
    image= models.URLField(max_length=300)

    class Meta:
        db_table = "item"


class storeItems(models.Model):
    a=0
    users=models.ForeignKey(Users,on_delete=models.CASCADE)
    items = models.ForeignKey(item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    add=models.IntegerField(default=0)
    def total(self):
        b=self.items.price*self.quantity
        return b
    def get_cart_deal_total(self):
        a=self.a+self.total()
        return a

    class Meta:
        db_table="storeItems"

class order(models.Model):
    ordername=models.CharField(max_length=60)

    class Meta:
        db_table="order"
class bill(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    address=models.CharField(max_length=40)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zip=models.IntegerField()
    name_on_card = models.CharField(max_length=50)
    cardno=models.IntegerField()
    expmonth=models.IntegerField()
    expyear=models.IntegerField()
    cvv=models.IntegerField()
    class Meta:
        db_table="bill"
class book_tables(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    phone = models.IntegerField()
    guest = models.IntegerField()
    date_table = models.DateField(max_length=50)
    time_table = models.TimeField(max_length=60)
    category = models.CharField(max_length=50)
    msg = models.CharField(max_length=50)

    class Meta:
        db_table="book_tables"

class Catering_order_table(models.Model):
    cid = models.AutoField(primary_key=True, serialize=False),
    uname=models.CharField(max_length=50)
    dcategory=models.CharField(max_length=50)
    dcapacity=models.CharField(max_length=50)
    dprice=models.CharField(max_length=50)
    dicategory = models.CharField(max_length=50)
    dicapacity = models.CharField(max_length=50)
    diprice = models.CharField(max_length=50)
    tcategory = models.CharField(max_length=50)
    tcapacity = models.CharField(max_length=50)
    tprice = models.CharField(max_length=50)
    pcategory = models.CharField(max_length=50)
    pcapacity = models.CharField(max_length=50)
    pprice = models.CharField(max_length=50)
    rcategory = models.CharField(max_length=50)
    rcapacity = models.CharField(max_length=50)
    rprice = models.CharField(max_length=50)
    decategory = models.CharField(max_length=50)
    decapacity = models.CharField(max_length=50)
    deprice = models.CharField(max_length=50)
    drcategory = models.CharField(max_length=50)
    drcapacity = models.CharField(max_length=50)
    drprice = models.CharField(max_length=50)
    maincategory = models.CharField(max_length=50)
    maincapacity = models.CharField(max_length=50)
    mprice = models.CharField(max_length=50)

    class Meta:
        db_table="Catering_order_table"
class Feedback(models.Model):
    firstname=models.CharField(max_length=50)
    mailid=models.CharField(max_length=50)
    service=models.CharField(max_length=50)
    food=models.CharField(max_length=50)
    cleanliness=models.CharField(max_length=50)
    ResponseTime=models.CharField(max_length=50)
    recommend=models.CharField(max_length=50)
    rating=models.IntegerField()

    class Meta:
        db_table="Feedback"
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    query = models.CharField(max_length=50)

    class Meta:
        db_table="Contact"
class orders_foods(models.Model):
    cart_items = models.ForeignKey(storeItems, on_delete=models.CASCADE)
    total=models.IntegerField()

    class Meta:
        db_table="orders_foods"

class ritems(models.Model):
    name = models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    price = models.IntegerField()
    image= models.URLField(max_length=300)

    class Meta:
        db_table = "ritems"
class recommendation(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    age=models.IntegerField()
    phone=models.IntegerField()
    kind=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    newvar=models.CharField(max_length=10)

    class Meta:
        db_table="recommendation"