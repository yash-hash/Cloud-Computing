from django.db import models
from django.core.exceptions import ValidationError


def phone_val(value):
    """ Validator for phone number"""
    if len(value) > 10 and len(value) < 10:
        raise serializers.ValidationError("Wrong input length")
    return value


class Champion(models.Model):
    """Model for Champions"""

    champion_choices = (('1', "Institutional"),('2','Faculty'), ('3','Organisational'))

    champion_id = models.CharField(max_length=20, unique=True, editable=False)
    champion_type = models.CharField(max_length=10, choices = champion_choices)
    first_name = models.CharField(max_length = 20, blank = False)
    middle_name = models.CharField(max_length = 20, blank = False)
    last_name = models.CharField(max_length = 20, blank = False)
    image_file = models.ImageField()
    contact_one = models.CharField(max_length = 10, blank = False, validators =[phone_val]) # or null = False
    contact_two = models.CharField(max_length = 10, blank = True)
    email_id = models.EmailField(blank = False)
    current_year_choices = [("1","First"), ("2","Second"), ("3","Third"),("4","Fourth"),("5","Fifth")]
    current_year = models.CharField(max_length = 2, choices = current_year_choices, blank = False)
    date_of_birth = models.DateField(blank = False)
    gender_choices = [("Male","M"), ("Female","F"), ("Other","Other")]
    gender = models.CharField(max_length = 10, choices = gender_choices, blank = False)
    local_address = models.TextField(max_length = 100, blank = False)
    country = models.ForeignKey('address.Country', on_delete = models.CASCADE, related_name = 'country')
    state = models.ForeignKey('address.State', on_delete = models.CASCADE, related_name = 'state')
    city = models.CharField(max_length = 15, blank = False)
    pincode = models.CharField(max_length = 6, blank = False)
    aadhar_id = models.CharField(max_length = 12, blank = False)
    aadhar_file = models.ImageField()
    pan_id = models.CharField(max_length = 10, blank = False)
    pan_file = models.ImageField()
    institution = models.ForeignKey('institution.Institution', on_delete=models.PROTECT, related_name='institution')
    # institution_branch =
    # assigned_institutions = models.ManyToManyField('institution.Institution', on_delete = models.PROTECT, related_name='assigned_institutions')
    is_active = models.BooleanField()
    achievements = models.TextField(max_length=200)
    # total_quiz = 10 quizzes
    # quiz_score =
    # rating_choices = [("1","1 Star"), ("2","2 Star"), ("3","3 Star"), ("4","4 Star"),("5","5 Star")]
    # rating = models.CharField(max_length = 10, choices = rating_choices, blank = True)
    # creation_datetime =
    # created_by =
    # updation_datetime =
    # updated_by =


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_champion_id()
        self.validateEmail()


    def validateEmail(self):
        from django.core.exceptions import ValidationError
        from django.core.validators import validate_email
        try:
            validate_email(self.email_id)
            return True
        except ValidationError:
            return False


    def set_champion_id(self):
        """Champion_ID Function"""
        if not self.champion_id:
            champion_id = 'CHAMP' + "_" + str(self.id)
            champion = Champion.objects.get(id=self.id)
            champion.champion_id = champion_id
            champion.save()


    def __str__(self):
        """ Return function """
        return self.champion_id
