from django.db import models

class Re_class(models.Model):
    
    name=models.CharField(max_length=255,null=True)
    e_name=models.CharField(max_length=255,null=True)

    def __str__ (self):
        return f"{self.name} {self.e_name}"
    
    
class Member(models.Model):
    # STATIC_CHOICES=[
    #     ('rice', '飯'),
    #     ('noddles', '麵'),
    #     ('dessert', '甜點'),
    # ]
    name=models.CharField(max_length=255,null=True) #名稱
    s_name=models.CharField(max_length=255,null=True) #副標
    Ingredients=models.CharField(max_length=255,null=True) 
    cook=models.CharField(max_length=255,null=True) 
    img=models.CharField(max_length=255,null=True) 
    joined_date = models.DateField(null=True)
    class_val =models.ForeignKey(Re_class, on_delete=models.SET_NULL, null=True)

    
    def __str__ (self):
        return f"{self.name} {self.s_name} {self.Ingredients} {self.cook} {self.img} {self.class_val}"

        

#新增

        
