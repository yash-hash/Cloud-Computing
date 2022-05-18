from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class ThinkTankProfile(models.Model):
    """ Model for Think Tank """

    GENDER_CHOICES= [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Others'),
    ]
    think_tank_id = models.CharField(max_length=10, unique=True, editable = False)
    first_name = models.CharField(max_length=200, blank=False, null=False)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    profile_status = models.BooleanField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=None)
    dob = models.DateField(blank=False, null=False)
    email = models.EmailField(max_length=500, blank=False, null=False)
    phone_regex = RegexValidator(
      regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17)
    current_year = models.IntegerField(blank=False, null=False)
    creation_dateTime = models.DateTimeField()
    update_dateTime = models.DateTimeField(auto_now = True)
    is_ebc = models.BooleanField()
    total_family_members = models.IntegerField(blank=False, null=False)
    born_brought_up_at = models.CharField(max_length=200, blank=False, null=False)
    earners_in_family = models.IntegerField(blank=False, null=False)
    no_of_people_doing_jobs = models.IntegerField(blank=False, null=False)
    no_of_people_doing_farming = models.IntegerField(blank=False, null=False)
    no_of_people_doing_business = models.IntegerField(blank=False, null=False)
    branch = models.CharField(max_length=200, blank=False, null=False)

    # institute_id created_by updated_by team_id government_id address economic_background this fields are remaining

    think_tank_image =  models.ImageField(null=True, blank=True, upload_to='ThinkTankProfile/', default="ThinkTankProfile/user-default.png")


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_think_tank_id()


    def set_think_tank_id(self):
        """Think Tank ID Function"""

        if not self.incubation_id:
            think_tank_id = 'THTK' + "_" + str(self.id)
            thinkTankProfile = ThinkTankProfile.objects.get(id=self.id)
            thinkTankProfile.think_tank_id = think_tank_id
            thinkTankProfile.save()

    def __str__(self):
        return self.think_tank_id
