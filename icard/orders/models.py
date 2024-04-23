from django.db import models

StatusEnum = [
    ('PENDING', 'PENDING'),
    ('IN_PROGRESS', 'IN_PROGRESS'),
    ('COMPLETED', 'COMPLETED'),
    ('CANCELLED', 'CANCELLED'),
]

class Order(models.Model):
    table = models.ForeignKey('tables.Table', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=StatusEnum, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    close = models.BooleanField(default=False)
    
    
    def __str__(self):
        return str(self.table)
    