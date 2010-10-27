from django.db import models


class Applicant(models.User):"this class extends Django's built-in user model"
    lottery = models.IntegerField() 
    preferences = []
    def add_preference(coop,rank):"adds a preference to the preference list, replaces preference if it already exists"
        if(preferences.in(coop)):
            i = preferences.index(coop)
            preferences = preferences.ext[:i].extend(preferences[i+1:])
        preferences.insert(rank,coop)
                
    def get_rank(coop):"returns the rank of the element in the preference list"
        if(preferences.in(coop)):
            return preferences.index(coop)
        else:
            return None

    class Members(models.Model):
        "The object that represents a member of OSCA"
        housing_coop = models.ForeignKey(Housing_Coop,housing_coops)"a many-to-one relationship of members to housing coops"
        dining_coop = models.ForeignKey(Dining_Coop,dining_coops)"a many-to-one relationship of members to dining coops"
        job = models.ForeignKey(staff.Job)
    
    class Non_Members(models.Model):
        

class Coop(models.Model):
    "The object that represents a coop within OSCA"
    name = models.CharField(max_length=20)
    street_address = models.CharField(max_length=100)
    wait_list = models.ManyToMany
    class Housing_Coop(models.Model):
    class Dining_Coop(models.Model):
        has_robot_coupe = models.BooleanField()
    
" TODO: move to a new app entitled staff
class Job(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()    
    jumps_housing = models.BooleanField()
    jumps_dining = models.BooleanField()
"
