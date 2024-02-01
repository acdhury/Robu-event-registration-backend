from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Soccerbot(models.Model):
    team_Name = models.CharField(max_length=64, unique=True, default='Default Team Name')
    team_Lead_Name = models.CharField(max_length=64)
    team_Lead_StudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], unique=True)
    team_Lead_Email = models.EmailField(unique=True)
    team_Lead_Phone = models.CharField(max_length=11, validators=[RegexValidator(regex='^[0-9]{11}$')])
    team_Lead_FacebookID = models.URLField(unique = True, default = "Default Facebook ID")
    
    member_2_name = models.CharField(max_length=100, blank=True, null=True)
    member_2_StudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], blank=True, null=True, unique=True)
    member_2_Email = models.EmailField(blank=True, null=True, unique=True)
    
    member_3_name = models.CharField(max_length=100, blank=True, null=True)
    member_3_StudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], blank=True, null=True, unique=True)
    member_3_Email = models.EmailField(blank=True, null=True, unique=True)

    member_4_name = models.CharField(max_length=100, blank=True, null=True)
    member_4_StudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], blank=True, null=True, unique=True)
    member_4_Email = models.EmailField(blank=True, null=True, unique=True)

    member_count = models.IntegerField(default=1)  # Default to 1 for the team lead
    payment_status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.team_Name
    
    def total_members(self):
        # Counting non-null member names
        members = [self.member_2_name, self.member_3_name, self.member_4_name]
        non_null_members = filter(None, members)
        return sum(1 for member in non_null_members) + 1  # Add 1 for the team lead
    
    def save(self, *args, **kwargs):
        self.member_count = self.total_members()
        super().save(*args, **kwargs)


class LineFollow(models.Model):
    team_Name = models.CharField(max_length=64, unique=True, default='Default Team Name')
    team_Lead_Name = models.CharField(max_length=64)
    team_Lead_StudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], unique=True)
    team_Lead_Email = models.EmailField(unique=True)
    team_Lead_Phone = models.CharField(max_length=11, validators=[RegexValidator(regex='^[0-9]{11}$')])
    team_Lead_FacebookID = models.URLField(unique = True, default = "Default Facebook ID")

    member_2_name = models.CharField(max_length=100, blank=True, null=True)
    member_2_StudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], blank=True, null=True, unique=True)
    member_2_Email = models.EmailField(blank=True, null=True, unique=True)
    
    member_3_name = models.CharField(max_length=100, blank=True, null=True)
    member_3_StudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], blank=True, null=True, unique=True)
    member_3_Email = models.EmailField(blank=True, null=True, unique=True)

    member_4_name = models.CharField(max_length=100, blank=True, null=True)
    member_4_StudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], blank=True, null=True, unique=True)
    member_4_Email = models.EmailField(blank=True, null=True, unique=True)

    member_count = models.IntegerField(default=1)  # Default to 1 for the team lead
    payment_status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.team_Name
    
    def total_members(self):
        members = [self.member_2_name, self.member_3_name, self.member_4_name]
        non_null_members = filter(None, members)
        return sum(1 for member in non_null_members) + 1  # Add 1 for the team lead
    
    def save(self, *args, **kwargs):
        self.member_count = self.total_members()
        super().save(*args, **kwargs)


class RoboRace(models.Model):
    team_Name = models.CharField(max_length=64, unique=True, default='Default Team Name')
    team_Lead_Name = models.CharField(max_length=64)
    team_Lead_StudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], unique=True)
    team_Lead_Email = models.EmailField(unique=True)
    team_Lead_Phone = models.CharField(max_length=11, validators=[RegexValidator(regex='^[0-9]{11}$')])
    team_Lead_FacebookID = models.URLField(unique = True, default = "Default Facebook ID")
    
    member_2_name = models.CharField(max_length=100, blank=True, null=True)
    member_2_StudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], blank=True, null=True, unique=True)
    member_2_Email = models.EmailField(blank=True, null=True, unique=True)
    
    member_3_name = models.CharField(max_length=100, blank=True, null=True)
    member_3_StudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], blank=True, null=True, unique=True)
    member_3_Email = models.EmailField(blank=True, null=True, unique=True)

    member_4_name = models.CharField(max_length=100, blank=True, null=True)
    member_4_StudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], blank=True, null=True, unique=True)
    member_4_Email = models.EmailField(blank=True, null=True, unique=True)

    member_count = models.IntegerField(default=1)  # Default to 1 for the team lead
    payment_status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.team_Name
    
    def total_members(self):
        members = [self.member_2_name, self.member_3_name, self.member_4_name]
        non_null_members = filter(None, members)
        return sum(1 for member in non_null_members) + 1  # Add 1 for the team lead
    
    def save(self, *args, **kwargs):
        self.member_count = self.total_members()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.team_Name

    def total_members(self):
    # Counting non-null member names
        members = [self.member1_name, self.member2_name, self.member3_name, self.member4_name]
    # Filter out None values and count
        non_null_members = filter(None, members)
        return sum(1 for member in non_null_members) + 1  # Add 1 for the team lead

class IdeaGen(models.Model):
    team_Name = models.CharField(max_length=64, unique=True, default='Default Team Name')
    team_Lead_Name = models.CharField(max_length=64)
    team_Lead_StudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], unique=True)
    team_Lead_Email = models.EmailField(unique=True)
    team_Lead_Phone = models.CharField(max_length=11, validators=[RegexValidator(regex='^[0-9]{11}$')])
    team_Lead_FacebookID = models.URLField(unique = True, default = "Default Facebook ID")
    
    member_2_name = models.CharField(max_length=100, blank=True, null=True)
    member_2_StudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], blank=True, null=True, unique=True)
    member_2_Email = models.EmailField(blank=True, null=True, unique=True)
    
    member_3_name = models.CharField(max_length=100, blank=True, null=True)
    member_3_StudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], blank=True, null=True, unique=True)
    member_3_Email = models.EmailField(blank=True, null=True, unique=True)

    member_4_name = models.CharField(max_length=100, blank=True, null=True)
    member_4_StudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], blank=True, null=True, unique=True)
    member_4_Email = models.EmailField(blank=True, null=True, unique=True)

    member_count = models.IntegerField(default=1)  
    payment_status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.team_Name
    
    def total_members(self):
        members = [self.member_2_name, self.member_3_name, self.member_4_name]
        non_null_members = filter(None, members)
        return sum(1 for member in non_null_members) + 1  # Add 1 for the team lead
    
    def save(self, *args, **kwargs):
        self.member_count = self.total_members()
        super().save(*args, **kwargs)


class ChatGPT(models.Model):
    teamName = models.CharField(max_length = 64, unique = True)
    teamLeadName = models.CharField(max_length = 64)
    teamLeadStudentID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], unique = True)
    teamLeadPhone = models.CharField(max_length = 11, validators=[RegexValidator(regex='^[0-9]{11}$')])
    payment_status = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.teamLeadName


class SoccerbotMember(models.Model):
    student_ID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], unique = True)

    def __str__(self):
        return self.student_ID
    
class lineFollowMember(models.Model):
    student_ID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], unique = True)

    def __str__(self):
        return self.student_ID
    
class RoboRaceMember(models.Model):
    student_ID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], unique = True)

    def __str__(self):
        return self.student_ID
    
class IdeaGenMember(models.Model):
    student_ID = models.CharField(max_length=8, validators=[RegexValidator(regex='^[0-9]{8}$')], unique = True)

    def __str__(self):
        return self.student_ID
