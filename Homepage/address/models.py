from django.db import models

class Country(models.Model):
    """Table For Country"""

    country_choices = [('India', 'India')]
    country_id = models.CharField(max_length=20, unique=True, editable=False)
    country_name = models.CharField(max_length=30, choices = country_choices)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_countryid()

    def set_countryid(self):
        """Country ID Function"""
        if not self.country_id:
            country_id = 'CON' + "_" + str(self.id)
            country = Country.objects.get(id=self.id)
            country.country_id = country_id
            country.save()

    def __str__(self):
        return str(self.country_name)



class State(models.Model):
    """Table for country"""

    state_choices = [
        ('Andhra Pradesh', 'Andhra Pradesh'),('Arunachal Pradesh','Arunachal Pradesh'),('Assam','Assam'),('Bihar','Bihar'),
        ('Karnataka','Karnataka'),('Kerala','Kerala'),('Chhattisgarh','Chhattisgarh'),
        ('Uttar Pradesh','Uttar Pradesh'),('Goa','Goa'),('Gujarat','Gujarat'),('Haryana','Haryana'),
        ('Himachal Pradesh','Himachal Pradesh'),('jammu & Kashmir','jammu & Kashmir'),('Jharkhand','Jharkhand'),
        ('West Bengal','West Bengal'),('Madhya Pradesh','Madhya Pradesh'),('Maharashtra','Maharashtra'),
        ('Manipur','Manipur'),('Meghalaya','Meghalaya'),('Mizoram','Mizoram'),
        ('Nagaland','Nagaland'),('Orissa','Orissa'),('Punjab','Punjab'),('Rajasthan','Rajasthan'),
        ('Sikkim','Sikkim'),('Tamil Nadu','Tamil Nadu'),('Telangana','Telangana'),('Tripura','Tripura'),
        ('Uttarakhand','Uttarakhand'),
            ]

    state_id = models.CharField(max_length=10, editable=False, unique=True)
    state_name = models.CharField(max_length=20, choices = state_choices)
    # country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_stateid()

    def set_stateid(self):
        """State ID Function"""
        if not self.state_id:
            state_id = 'STA' + "_" + str(self.id)
            state = State.objects.get(id=self.id)
            state.state_id = state_id
            state.save()

    def __str__(self):
        return str(self.state_name)


class District(models.Model):
    """Table for District"""

    district_id = models.CharField(max_length=10, unique=True, editable=False)
    district_name = models.CharField(max_length=30)
    state_id = models.ForeignKey(State, on_delete = models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_districtid()

    def set_districtid(self):
        """District ID Function"""
        if not self.district_id:
            district_id = 'DIST' + "_" + str(self.id)
            district = District.objects.get(id=self.id)
            district.district_id = district_id
            district.save()

    def __str__(self):
        return str(self.district_id)


class Region(models.Model):
    """Table for Region"""

    region_choices = [('Vidarbha', 'vidarbha'), ('Marathwada', 'marathwada'), ('Konkan', 'konkan'), ('Khandesh', 'khandesh'), ('Paschim Maharashtra', 'paschim maharashtra')]

    region_id = models.CharField(max_length=10, unique=True, editable=False)
    region_name = models.CharField(max_length=20, choices = region_choices)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.set_region_id()

    def set_region_id(self):
        """District ID Function"""
        if not self.region_id:
            region_id = 'REG' + "_" + str(self.id)
            region = Region.objects.get(id=self.id)
            region.region_id = region_id
            region.save()

    def __str__(self):
        return str(self.region_name)
