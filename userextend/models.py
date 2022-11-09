from django.contrib.auth.models import User
from django.db import models


class UserExtend(User):

    gender_options = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))
    # tuplu, primul elem din tuplu e ce salvam in tabela, al 2-lea este ce apare pe site

    email_confirmation = models.EmailField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.CharField(choices=gender_options, max_length=6)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

