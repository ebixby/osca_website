from django.db import models
import random

class Applicant(models.Model):
	user = models.OneToOneField(User_Profile)
	is_member = models.BooleanField()
	def __unicode__(self):
		return self.user
	class Meta:
		ordering = ['user']
	
    
class Semester(models.Model):
	start_date = models.DateField()
	end_date = models.DateField()
	is_current = models.BooleanField()
	lottery_date = models.DateTimeField()
	def __unicode__(self):
		return self.start_date
	class Meta:
		ordering = ['start_date']

class Dining_Member(models.Model):
	coop = models.ForeignKey(Dining_Coop)
	applicant = models.ForeignKey(Applicant)
	semester = models.ForeignKey(Semester)
	def __unicode__(self):
		return self.applicant
	class Meta:
		ordering = ['applicant']

class Housing_Member(models.Model):
	coop = models.ForeignKey(Housing_Coop)
	applicant = models.ForeignKey(Applicant)
	semester = models.ForeignKey(Semester)
	def __unicode__(self):
		return self.applicant
	class Meta:
		ordering = ['applicant']

class Coop(models.Model):
	name = models.CharField(max_length=20)
	street_address = models.CharField(max_length=100)
	capacity = models.PositiveIntegerField()
	description = models.TextField()
	picture = models.ImageField(upload_to=self.name/filename)
	def __unicode__(self):
		return self.name
	class Meta:
		abstract = True
		ordering = ['name']

class Dining_Coop(Coop):
	members = ManyToManyField(Applicant, through=DiningMember)
	
class Housing_Coop(Coop):
	members = ManyToManyField(Applicant, through=HousingMember)

class Application(models.Model):
	waitlist = models.ForeignKey(Waitlist)
	applicant = models.ForeignKey(Applicant)
	lottery_number = models.PositiveIntegerField()
	def __unicode__(self):
		return self.applicant
	class Meta:
		order_with_respect_to = 'waitlist'
		ordering = ['lottery_number']

class Preference(models.Model):
	application = models.ForeignKey(Application)
	coop = models.ForeignKey(Coop)
	order = models.PositiveSmallIntegerField()
	def __unicode__(self):
		return self.coop
	class Meta:
		unique_together = ((application, order),(application, coop))
		order_with_respect_to = 'application'
		ordering = ['order']

class Waitlist(models.Model):
	semester = models.OneToOneField(Semester)
	applicants = ManyToManyField(Applicant, through=Application)
	size = models.PositiveIntegerField()
	def do_lottery():
		numbers = range(self.size)
		for appl in self.applicants_set.all():
			i = random.randint(0,self.size)
			appl.lottery_number = i
			numbers.remove(i)
	def add(Applicant):
		if(self.semester.lottery_date. is before now):
		   add person to end of waitlist
		else:
		   do nothing (person should be added to applicants.)
	def remove(user):
		if(applicants.in(user)):
			applicants.in(user)
	def __unicode__(self):
		return self.semester
	class Meta:
		ordering = ['semester']
