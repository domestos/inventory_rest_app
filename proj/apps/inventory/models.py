from django.db import models

#=================__PERSON__===========================
class Person(models.Model):
    fname = models.CharField(max_length=30)
    sname = models.CharField(max_length=30)

    class  Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.fname+" "+self.sname

#=================__LOCATION__=========================
class Location(models.Model):
    location = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.location

#=================__DIVECE_TYPE__========================
class TypeDivece(models.Model):
    dtype = models.CharField(max_length=50) 

    class Meta:
        verbose_name = 'Type of Divece'
        verbose_name_plural = 'Type of Diveces'

    def __str__(self):
        return self.dtype


#=================__DIVECE__=========================
class Device(models.Model):
    inventory_number = models.CharField(max_length=30)
    person_id = models.ForeignKey(Person, on_delete=models.PROTECT)
    type_id = models.ForeignKey(TypeDivece, on_delete=models.PROTECT)
    location_id = models.ForeignKey(Location, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
       

    def __str__(self):
        return self.inventory_number