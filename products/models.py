from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 255)
    slug = models.CharField(max_length= 255)
    icon_url = models.CharField(max_length = 128, null = True)
    created_at = models.DateTimeField(default = timezone.now)
    updated_at = models.DateTimeField(auto_now = True)
    deleted_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)
    unit = models.CharField(max_length=3, blank=True)
    price = models.FloatField()
    discount = models.IntegerField(blank=True)
    amount = models.IntegerField(blank=True)    
    thumbnail = models.CharField(max_length=255, blank=True)    
    reviewCount = models.FloatField(default=0)
    boughtCount = models.FloatField(default=0)
 # sử dụng ForeignKey để khai báo một field là khóa ngoại từ một bảng khác
 # on_delete=models.CASCADE để mô tả khi bảng category bị xóa một record...
 # thì tất cả record product có id tương ứng sẽ bị xóa theo
 # related_name thể hiện khi query ở bảng category...
 # tất cả các record product con sẽ được hiển thị trong một mảng có tên là products
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,
                                    related_name='products', null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at'])
        ]
        
    def __str__(self):
        return self.name
        
class ProductImage(models.Model):
    id = models.AutoField(primary_key=True)
    image_url = models.CharField(max_length=128)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, 
                                    related_name='product_images', null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=timezone.now)

class ProductComment(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    comment = models.CharField(max_length=512)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, 
                                    related_name='product_comments', null=False)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
 # ForeignKey('self',...) diễn tả mối quan hệ cha - con trong cùng một bảng
 # Một comment có nhiều người rep lại, thì comment gốc sẽ không có parent_id...
 # còn các comment rep lại sẽ có parent_id là id của comment gốc
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=timezone.now)
    
