from django.db import models


class InstitutionFocal(models.Model):
    """Model for Institution Focal"""

    focal_choices = (('1', 'Primary'), ('2', 'Escalation'))
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=40, blank=False)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    designation = models.CharField(max_length=100, blank = False)
    focal_type = models.CharField(max_length=10, choices = focal_choices, blank = False)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Institution(models.Model):
    """Model for Institution"""

    institution_id = models.CharField(max_length=10, unique=True, editable=False)
    institution_name = models.CharField(max_length = 200, blank = False)
    institution_logo = models.ImageField(blank = False)
    ed_cell = models.BooleanField(blank = False)
    total_no_students = models.IntegerField(blank = False)
    incubation_centre = models.ForeignKey('incubation.Incubation', on_delete=models.CASCADE, related_name='incub')
    country = models.ForeignKey('address.Country', on_delete = models.CASCADE, related_name = 'country_insti')
    state = models.ForeignKey('address.State', on_delete = models.CASCADE, related_name = 'state_insti')
    region = models.ForeignKey('address.Region',max_length=6, on_delete = models.PROTECT, related_name= 'region_insti')
    city = models.CharField(max_length = 15, blank = False)
    pincode = models.CharField(max_length = 6, blank = False)
    institution_reg_no = models.CharField(max_length = 100, blank = False, unique = True)
    insti_focals = models.ForeignKey(InstitutionFocal, on_delete=models.CASCADE)
    # category_choices = [("1","Engineering"), ("2","Agricultural"), ("3","MBA"), ("4","Arts"), ("5","Research Institution"), ("6","Architechture"), ("7","Medical")]
    # category = models.CharField(max_length = 10, choices = category_choices, blank = False)
    # Branch = ForeignKey()
    # event_ids = ForeignKey()
    # regional_event_id = Array Of ForeignKey()
    # sponsored_amounts = models.IntegerField(editable = False)
    # created_by = Foreignkey()
    # Updated_by = Foreignkey()


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_institution_id()

    def set_institution_id(self):
        """Institution ID Function"""
        if not self.institution_id:
            institution_id = 'INSTI' + "_" + str(self.id)
            institution = Institution.objects.get(id=self.id)
            institution.institution_id = institution_id
            institution.save()

    def __str__(self):
        return self.institution_name


class InstitutionSponsor(models.Model):
    """ Model For Institution Sponosr"""

    sponsor_choices = [("1","Title"), ("2","Campaign"), ("3","Travel"),
    ("4","Techonology"),("5","Media"), ("6","Regional"),('7','Hospitality')]

    sponsor_id = models.CharField(max_length=10, unique=True, editable = False)
    name = models.CharField(max_length=100)
    email_id = models.EmailField()
    contact = models.CharField(max_length=10)
    local_address = models.TextField(max_length = 100, blank = False)
    country = models.ForeignKey('address.Country', on_delete = models.CASCADE, related_name = 'insti_country')
    state = models.ForeignKey('address.State', on_delete = models.CASCADE, related_name = 'insit_state')
    city = models.CharField(max_length = 15, blank = False)
    pincode = models.CharField(max_length = 6, blank = False)
    sponsor_type = models.CharField(max_length= 20, choices = sponsor_choices)
    creation_datetime = models.DateTimeField()
    updated_datetime = models.DateTimeField()
    # sponsored_institutions = models.ForeginKey(Institution, on_delete = models.CASCADE)
    # created_by = models.ForeginKey
    # updated_by = models.ForeginKey()


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_sponsorid()

    def set_sponsorid(self):
        """Sponsor ID Function"""

        if not self.sponsor_id:
            sponsor_id = 'SPON' + "_" + str(self.id)
            institutiion_sponsor = InstitutionSponsor.objects.get(id=self.id)
            institutiion_sponsor.sponsor_id = sponsor_id
            institutiion_sponsor.save()

    def __str__(self):
        return self.sponsor_id
