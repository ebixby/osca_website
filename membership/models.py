from django.db import models
import random


class Applicant(User):"this class extends Django's built-in user model and is an abstract class"
    preferences = []
    lottery_number = models.IntegerField()
    def set_preference(coop,rank):
        "adds a preference to the preference list, replaces preference if it already exists"
        remove_preference(coop)
        preferences.insert(rank,coop)
    
    def remove_preference(coop):
        if(preferences.in(coop)):
            preferences.remove(coop)
        
    def get_rank(coop):
        "returns the rank of the element in the preference list"
        if(preferences.in(coop)):
            return preferences.index(coop)
        else:
            return None
    class Meta:
        abstract = True;
        
class Members(Applicant):
        "The object that represents a member of OSCA"
    housing_coop = models.ForeignKey(Housing_Coop)"a many-to-one relationship of members to housing coops"
    dining_coop = models.ForeignKey(Dining_Coop)"a many-to-one relationship of members to dining coops"
    job = models.ForeignKey(staff.Job)
    
class Non_Members(Applicant):
    

class Coop(models.Model):
    name = models.CharField(max_length=20)
    street_address = models.CharField(max_length=100)
    size = models.IntegerField()
    description = models.TextField()
    picture = models.ImageField(upload_to=self.name/filename)
    class Meta:
        abstract = True;

class Dining_Coop(Coop):

class Housing_Coop(Coop):
    
" TODO: move to a new app entitled staff
class Job(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()    
    jumps_housing = models.BooleanField()
    jumps_dining = models.BooleanField()
"       

class Waitlist(models.Model):
    loterry_date = models.DateField()
    valid_until = models.DateField()
    applicants = ManyToManyField(Applicants)
    
    def populate():
        numbers = range(self.applicants_set.len+1)
        numbers.remove(0)
        for appl in self.applicants_set.all():
            i = random.randint(1,numbers.len)
            appl.lottery_number = i
            numbers.remove(i)
            
    def add:
        if(lottery_date is before now):
            add person to end of waitlist
        else:
            do nothing (person should be added to applicants.) 
        

    def remove(user):
        if(applicants.in(user)):
            applicants.in(user):
    
