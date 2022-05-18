from django.db import models


class Catalyst(models.Model):
    """ Catalyst Model """

    gender_choices = [("1","M"), ("2","F"), ("3","Other")]
    current_year_choices = [("1","First"), ("2","Second"), ("3","Third"),("4","Fourth"),("5","Fifth"), ("6", "NA")]
    rating_choices = [("1","1 Star"), ("2","2 Star"), ("3","3 Star"), ("4","4 Star"),("5","5 Star")]
    catalyst_choices = [('1', 'Student'), ('2','Faculty')]

    catalyst_id = models.CharField(max_length=10, unique = True, editable = False)
    user_image = models.ImageField()
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_active = models.BooleanField()
    gender = models.CharField(max_length=10, choices = gender_choices)
    date_of_birth = models.DateField()
    email_id = models.EmailField()
    contact_one = models.CharField(max_length=10)
    contact_two = models.CharField(max_length=10, blank = True)
    local_address = models.TextField(max_length=100)
    country = models.ForeignKey('address.Country', on_delete = models.PROTECT, related_name = 'cat_cont')
    state = models.ForeignKey('address.State', on_delete = models.PROTECT, related_name = 'cat_state')
    city = models.CharField(max_length=30)
    pincode = models.CharField(max_length=6)
    institution = models.ForeignKey('institution.Institution', on_delete = models.PROTECT, related_name = 'cat_insti')
    aadhar_id = models.CharField(max_length = 12, blank = False)
    aadhar_file = models.ImageField()
    pan_id = models.CharField(max_length = 10, blank = False)
    pan_file = models.ImageField()
    catalyst_type = models.CharField(max_length=10, choices = catalyst_choices)
    current_year = models.CharField(max_length=5, choices = current_year_choices, blank = True)
    years_of_experience = models.IntegerField()
    rating = models.CharField(max_length = 10, choices = rating_choices, blank = True)
    number_of_quizzes = models.IntegerField()
    # quiz_scores = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_catalyst_id()


    def set_catalyst_id(self):
        """Catalyst Function"""
        if not self.catalyst_id:
            catalyst_id = 'CAT' + "_" + str(self.id)
            catalyst = Catalyst.objects.get(id=self.id)
            catalyst.catalyst_id = catalyst_id
            catalyst.save()


    def __str__(self):
        """ Return function """
        return self.catalyst_id
