from django.db import models
import random


class Semester(models.Model):
		start_date = models.DateField()
		end_date = models.DateField()
		lottery_date = models.DateTimeField()

class DiningMember(models.Model):
		coop = models.ForeignKey(DiningInformation)
		member = models.ForeignKey(User)
		semester = models.ForeignKey(Semester)

class HousingMember(models.Model):
		coop = models.ForeignKey(DiningInformation)
		member = models.ForeignKey(User)
		semester = models.ForeignKey(Semester)
		
"option one for coop system"
class Coop(models.Model):
    name = models.CharField(max_length=20)
    street_address = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to=self.name/filename)


class DiningCoop(models.Model):
		coop = models.OneToOneField(Coop, related_name='dining')
		members = models.ManyToManyField(User, through=DiningMember)
		capacity = models.PositiveIntegerField()


class HousingCoop(models.Model):
		coop = models.OneToOneField(Coop, related_name='housing')
		members = models.ManyToManyField(User, through=HousingMember)
		capacity = models.PositiveIntegerField()


"option two for coop system" 
class Coop(models.Model):
    name = models.CharField(max_length=20)
    street_address = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    description = models.TextField()
    picture = models.ImageField(upload_to=self.name/filename) 
    class Meta:
        abstract = True

class Dining_Coop(Coop):
		members = ManyToManyField(User, through=DiningMember)
	
class Housing_Coop(Coop):
		members = ManyToManyField(User, through=HousingMember)

class Application(models.Model):
	waitlist = models.ForeignKey(Waitlist)
	applicant = models.ForeignKey(User) 
	
class Preference(models.Model):
		application = models.ForeignKey(Application)
		coop = models.ForeignKey(Coop)
		order = models.PositiveSmallIntegerField()
			
class Waitlist(models.Model):
    semester = models.OneToOneField(Semester)
    applicants = ManyToManyField(User, through=Application)
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
    
