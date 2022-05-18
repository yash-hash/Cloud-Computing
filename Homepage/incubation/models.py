from django.db import models

class IncubationFocal(models.Model):
    """Incubational Focal Model"""

    focal_choices = (('Primary', 'Primary'), ('Escalation', 'Escalation'))

    focal_id = models.CharField(max_length=10, unique=True, editable=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=40, blank=False)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    designation = models.CharField(max_length=100, blank = False)
    focal_type = models.CharField(max_length=10, choices = focal_choices, blank = False)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_focal_id()


    def set_focal_id(self):
        """Sponsor ID Function"""
        if not self.focal_id:
            focal_id = 'FOC' + "_" + str(self.id)
            incubation_focal = IncubationFocal.objects.get(id=self.id)
            incubation_focal.focal_id = focal_id
            incubation_focal.save()


    def __str__(self):
        """return Function for focal"""
        return self.first_name + " " + self.last_name




class Incubation(models.Model):
    """Model For Incubation"""

    supported_by_choices = [('1','MSME'), ('2','AIC'),('3','MSINS'),('4','Private Organisation'),
    ('5','Government Organisation'), ('6','Other')]

    incubation_id = models.CharField(max_length=10, unique=True, editable = False)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    incubation_logo = models.ImageField()
    incubation_focal = models.ForeignKey(IncubationFocal, on_delete = models.PROTECT, related_name = 'focal')
    supported_by = models.CharField(max_length=20, choices = supported_by_choices)
    address = models.TextField(max_length=100)
    country = models.ForeignKey('address.country', on_delete = models.CASCADE, related_name = 'inc_country')
    state = models.ForeignKey('address.state', on_delete = models.CASCADE, related_name = 'inc_state')
    region = models.ForeignKey('address.Region', on_delete = models.PROTECT, related_name = 'inc_region')
    city = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_incubation_id()


    def set_incubation_id(self):
        """Sponsor ID Function"""

        if not self.incubation_id:
            incubation_id = 'INCUB' + "_" + str(self.id)
            incubation = Incubation.objects.get(id=self.id)
            incubation.incubation_id = incubation_id
            incubation.save()

    def __str__(self):
        return self.incubation_id
