from django.db import models

class login_table(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    type=models.CharField(max_length=20)

class manufacturer_table(models.Model):
    LOGIN=models.ForeignKey(login_table, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    ph_no=models.BigIntegerField()
    photo=models.FileField()
    proof=models.FileField()
    email=models.CharField(max_length=100)

class distributor_table(models.Model):
    LOGIN=models.ForeignKey(login_table, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    ph_no=models.BigIntegerField()
    photo=models.FileField()
    proof=models.FileField()
    email=models.CharField(max_length=100)

class shop_table(models.Model):
    LOGIN=models.ForeignKey(login_table, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    ph_no=models.BigIntegerField()
    photo=models.FileField()
    proof=models.FileField()
    email=models.CharField(max_length=100)

class user_table(models.Model):
    LOGIN=models.ForeignKey(login_table, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    post=models.CharField(max_length=20)
    pin=models.BigIntegerField()
    ph_no=models.BigIntegerField()
    email=models.CharField(max_length=100)

class category(models.Model):
    category=models.CharField(max_length=100)
    details=models.TextField()



class product(models.Model):
    pname=models.CharField(max_length=50)
    description=models.TextField()
    CATEGORY=models.ForeignKey(category, on_delete=models.CASCADE)
    photo=models.FileField()
    price=models.FloatField()
    stock = models.IntegerField()
    size=models.CharField(max_length=60)

class manufacture_product(models.Model):
    MANFACTURER=models.ForeignKey(manufacturer_table, on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(product, on_delete=models.CASCADE)
    stock=models.IntegerField()
    date=models.DateField()
    size=models.CharField(max_length=60)

class distributor_req_master(models.Model):
    DISTRIBUTOR=models.ForeignKey(distributor_table, on_delete=models.CASCADE)
    MANFACTURER=models.ForeignKey(manufacturer_table, on_delete=models.CASCADE)
    status=models.CharField(max_length=100)
    date=models.DateField()
    amount=models.FloatField()

class distributor_req_details(models.Model):
    DISTRIBUTOR_MASTER=models.ForeignKey(distributor_req_master, on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(manufacture_product, on_delete=models.CASCADE)
    quantity=models.IntegerField()

class distributor_product(models.Model):
    DISTRIBUTOR_REQUEST=models.ForeignKey(distributor_req_details, on_delete=models.CASCADE)
    status=models.CharField(max_length=100)
    date=models.DateField()

class shop_req_master(models.Model):
    SHOP=models.ForeignKey(shop_table, on_delete=models.CASCADE)
    DISTRIBUTOR=models.ForeignKey(distributor_table, on_delete=models.CASCADE)
    status=models.CharField(max_length=100)
    date=models.DateField()
    amount = models.FloatField()

class shop_req_details(models.Model):
    SHOP_MASTER=models.ForeignKey(shop_req_master, on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(manufacture_product, on_delete=models.CASCADE)
    quantity=models.IntegerField()

class shop_product(models.Model):
    DISTRIBUTOR_PRODUCT=models.ForeignKey(distributor_product, on_delete=models.CASCADE)
    SHOP=models.ForeignKey(shop_table, on_delete=models.CASCADE)
    status=models.CharField(max_length=100)
    date=models.DateField()

class order(models.Model):
    USER=models.ForeignKey(user_table, on_delete=models.CASCADE)
    status=models.CharField(max_length=100)
    date=models.DateField()
    amount=models.IntegerField()
    gst=models.IntegerField()

class order_details(models.Model):
    ORDER=models.ForeignKey(order, on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(shop_req_details, on_delete=models.CASCADE)
    size=models.CharField(max_length=10)
    quantity=models.IntegerField()



class return_table(models.Model):
    ORDER=models.ForeignKey(order_details,on_delete=models.CASCADE)
    date=models.DateField()
    reason=models.CharField(max_length=30)
    status=models.CharField(max_length=30)

class bill(models.Model):
    SHOP = models.ForeignKey(shop_table, on_delete=models.CASCADE)
    user=models.CharField(max_length=20)
    ph_no=models.BigIntegerField()
    date=models.DateField()
    amount=models.IntegerField()
    status=models.CharField(max_length=100)


class bill_details(models.Model):
    BILL=models.ForeignKey(bill, on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    quantity=models.IntegerField()



