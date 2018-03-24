from django.db import models
from django.contrib.auth.models import User

# User is defined using django's default auth_user

"""
User becomes advanced user when he/she wants to do more than just searching for apartments
Namely, when the user wants to search for potential roommates, save potential match, create a group, etc
AdvancedUser will be assigned a gid by default, which is an auto-increment counter
"""
class AdvancedUser(models.Model): 
    uid = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE) 
    gender = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    ehtinicity = models.CharField(max_length=10, null=True)
    quiteness = models.IntegerField(null=True) #0-5 
    sanitary = models.IntegerField(null=True) #0-5
    timetobed = models.IntegerField(null=True) #0-5 late
    # otherthings to consider: study often, date, loud music, invite friends to home.
    pet = models.IntegerField(null=True) #0-1 yes or no
    major = models.CharField(max_length=10, null=True)
    hobbies = models.CharField(max_length=256, null=True)
    language = models.CharField(max_length=10, null=True)
    graduationyear = models.IntegerField(null=True)
    note = models.CharField(max_length=256, null=True)

    gid = models.IntegerField(null=True)

    def __str__(self):
        return "Advance User with uid: " + self.uid
    
    # def save(self, *args, **kwargs):
    #     if self._state.adding:
    #         # Get the maximum display_id value from the database
    #         last_id = self.objects.all().aggregate(largest=models.Max('gid'))['largest']
            
    #         if last_id is not None:
    #             self.gid = last_id + 1

    #     super(MyModel, self).save(*args, **kwargs)
    
"""
Apartment record is created when a group is created
Namely, when a user create a group, he/she needs to create an apartment record
We allow two duplicate apartment information (with different aid) 
"""
class Apartment(models.Model):
    aid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    price = models.IntegerField()
    address = models.CharField(max_length=50)
    floorplan = models.CharField(max_length=5)
    occupied = models.BooleanField() # True if this unit is intended for sublease, false if not
    
    def __str__(self):
        return "id " + str(self.aid)
    
"""
Group is a unit of operation, a group 'owns' or 'interested in' an apartment
Namely, we require a group to have a 'apartment' in mind,
and creating a group requires creating an apartment. 
"""    
class Group(models.Model):
    # TODO: gid duplicate with aid?
    gid = models.AutoField(primary_key=True)
    
    group_name = models.CharField(max_length=10, null=False) # for display in potential match
    aid = models.OneToOneField(Apartment, on_delete=models.DO_NOTHING, null=False, unique=True)
    peopleleft = models.IntegerField(null=False)
    admin_uid = models.OneToOneField(AdvancedUser, on_delete=models.DO_NOTHING, null=False)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return "Group " + self.gid

"""
User select some group as his/her 'PotentialMatch' after filter_group operation
"""
class PotentialMatch(models.Model):
    pid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(AdvancedUser, on_delete=models.CASCADE)
    gid = models.ForeignKey(Group, on_delete=models.CASCADE)


# TODO
#
# 1. Admin verifies the group_adding request from individual user
#    This might need a new table storing a many-to-one relationship between 2 advanced users
#
# 2. When a user leave a group, broadcast a notification to all user in this group
#    Think about how to implement this. Might require an augment in AdvancedUser table
