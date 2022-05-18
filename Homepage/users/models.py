from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from .manager import CustomUserManager


class Profile(AbstractUser):

  GENDER_CHOICES= [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Others'),
    ]

  PROFESSION_CHOICES= [
    ('student', 'Student'),
    ('budding', 'Budding Entrepreneur'),
    ('trainer', 'Corporate Trainer'),
    ('faculty', 'Faculty'),
    ('working', 'Working Professional'),
    ('freelancer', 'Freelancer'),
    ]

  LEVEL_CHOICES= [
    ('unenrolled', 'Unenrolled'),
    ('beginner', 'Beginner'),
    ('advance','Advance'),
    ('practitioner','Practitioner')
    ]

  QUALIFICATION_CHOICES= [
    ('grad', 'Graduation'),
    ('postgrad', 'Post Graduation'),
    ('phd', 'Ph.D/M.Phil'),
    ]

  objects = CustomUserManager()
# user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
  first_name = models.CharField(max_length=200, blank=False)
  middle_name = models.CharField(max_length=200, blank=True)
  last_name = models.CharField(max_length=200, blank=False)
  dob = models.DateField(blank=True)
  gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Male')
  profession = models.CharField(max_length=10, choices=PROFESSION_CHOICES, default='Student')
  email = models.EmailField(max_length=500, blank=False, null=False, unique = True)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
  phone = models.CharField(validators=[phone_regex], max_length=17)
  institute = models.CharField(max_length=200, blank=False)
  # institute = models.ForeignKey('institution.Institution', on_delete=models.CASCADE)
  country = models.ForeignKey('address.Country', on_delete = models.CASCADE, related_name = 'user_country')
  state = models.ForeignKey('address.State', on_delete = models.CASCADE, related_name = 'user_state')
  city = models.CharField(max_length=200, blank=False)
  qualification = models.CharField(max_length=10, choices=QUALIFICATION_CHOICES, default="")
  specialization = models.CharField(max_length=200, blank=True, null=True)
  years = models.IntegerField(blank=False)
  summary = models.TextField(blank=True, null=True)
  profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
  # social_github = models.CharField(max_length=200, blank=True, null=True)
  address = models.CharField(max_length=500, blank=False)
  enrollment_status = models.BooleanField(default=False)
  user_level = models.CharField(max_length=12, choices=LEVEL_CHOICES, default='Unenrolled')
  # created = models.DateTimeField(auto_now_add=True)
  # is_superuser = models.BooleanField(False)
  id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)

  def __str__(self) :
    return str(self.first_name)


class Platinum_club(models.Model):
    id = models.OneToOneField(Profile, on_delete = models.CASCADE, related_name = 'platinum_id', primary_key=True)
    first_name = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'platinum_fname')
    last_name = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'platinum_lname')
