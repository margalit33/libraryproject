from django.db import models
from enum import Enum



class BookType(Enum):
   ten_days = 1
   five_days = 2
   two_days = 3


class Book(models.Model):
    name = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    year_published = models.IntegerField(default=0) 
    type= models.IntegerField(default=0)
    book_id = models.AutoField(primary_key=True, editable=False)
    image= models.ImageField(upload_to="book_images",default="https://loremflickr.com/cache/resized/65535_52464844953_602e80cc9e_320_320_nofilter.jpg")

    
    
    def __str__(self):
        return f"{self.name} - {self.author} - {self.year_published} - {self.type} - {self.book_id}"
    
    

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100, null=False)
    city=  models.CharField(max_length=100, null=False)
    age= models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.customer_id} - {self.name} - {self.city} - {self.age} "
    
    
class Loan(models.Model):
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loandate = models.DateField()
    returndate = models.DateField()
    returned = models.BooleanField(default=False)  


    def __str__(self):
        return f"{self.customer} - {self.book} - {self.loandate} - {self.returndate}"


    
    
    





    
    
    