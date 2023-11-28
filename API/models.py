from django.db import models
from django.utils import timezone

class Vendor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Vendor's name")
    contact_details = models.TextField(verbose_name="Contact information of the vendor")
    address = models.TextField(verbose_name="Physical address of the vendor")
    vendor_code = models.CharField(max_length=50, unique=True, verbose_name="Unique identifier for the vendor")
    on_time_delivery_rate = models.FloatField(verbose_name="Percentage of on-time deliveries", default=0.0, null= True)
    quality_rating_avg = models.FloatField(verbose_name="Average rating of quality based on purchase orders", default=0.0, null= True)
    average_response_time = models.FloatField(verbose_name="Average time taken to acknowledge purchase orders", default=0.0, null= True)
    fulfillment_rate = models.FloatField(verbose_name="Percentage of purchase orders fulfilled successfully", default=0.0, null= True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Vendors"
 
class Purchase(models.Model):
    # po_number is not required as it is already given by django
    # po_number = models.CharField(max_length=50, default= "0" , verbose_name="Unique number identifying the PO")
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name="Link to the Vendor model")
    order_date = models.DateTimeField(verbose_name="Date when the order was placed", auto_now_add=True)
    # delivery date will be set as current date + 7 days 
    delivery_date = models.DateTimeField(verbose_name="Expected or actual delivery date of the order", default=timezone.now() + timezone.timedelta(days=7))
    items = models.JSONField(verbose_name="Details of items ordered")
    quantity = models.IntegerField(verbose_name="Total quantity of items in the PO")
    status = models.CharField(max_length=20, verbose_name="Current status of the PO", default= 'pending' ,choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ])
    # quality rating will be provided by user, if user doesn't provide it by default it will be 0.0
    quality_rating = models.FloatField(verbose_name="Rating given to the vendor for this PO", default= 0.0)
    # this date will automatically get set whenever anyone buys anything
    issue_date = models.DateTimeField(verbose_name="Timestamp when the PO was issued to the vendor",auto_now_add=True)
    # acknowledgement date will be updated by vendor when vendor will change status as completed
    acknowledgment_date = models.DateTimeField(verbose_name="Timestamp when the vendor acknowledged", null=True, blank=True)


    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_obj = Purchase.objects.get(pk=self.pk)
            # Check if the status has changed
            if old_obj.status != self.status:
                self.update_status_fields()
        super().save(*args, **kwargs)

    def update_status_fields(self):
        now = timezone.now()

        if self.status == 'completed' and not self.acknowledgment_date:
            self.acknowledgment_date = now 
            
    def __str__(self):
        return f"PO {self.id} - {self.vendor.name}"

    class Meta:
        verbose_name_plural = "Purchases"
        
class HistoricPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name="Link to the Vendor model")
    # this date will keep on changing on each updation
    date = models.DateTimeField(verbose_name="Date of the performance record")
    on_time_delivery_rate = models.FloatField(verbose_name="Historical record of on-time delivery rate")
    quality_rating_avg = models.FloatField(verbose_name="Historical record of quality rating average")
    average_response_time = models.FloatField(verbose_name="Historical record of average response time")
    fulfillment_rate = models.FloatField(verbose_name="Historical record of fulfilment rate")
    
    def save(self, *args, **kwargs):
        # Update the date field with the current timestamp
        self.date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"

    class Meta:
        verbose_name_plural = "Historic Performances"