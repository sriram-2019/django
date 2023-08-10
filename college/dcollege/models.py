from django.db import models

class student_sign(models.Model):
    name=models.CharField(max_length=264,db_column="name")
    roll_no=models.CharField(max_length=264,db_column="roll_no")
    password=models.CharField(max_length=264,db_column="password")
    mobile=models.CharField(max_length=11,db_column="mobile_no")
    email=models.EmailField(db_column="email")
    dob=models.DateField(db_column="dob")
    tenth=models.IntegerField(db_column="tenth_mark")
    twelve=models.IntegerField(db_column="twelth_mark")
    twelth_cutoff=models.IntegerField(db_column="twelth_cutoff")
    address=models.CharField(max_length=255,db_column="address")
    school=models.CharField(max_length=255,db_column="school")
    cgpa=models.IntegerField(db_column="cgpa")
    class Meta:
        managed = False
        db_table = 'student_signup'

class staff_sign(models.Model):
    staffid=models.CharField(max_length=264,db_column="staff_id")
    staffname=models.CharField(max_length=264,db_column="staff_name")
    staffemail=models.EmailField(db_column="staff_email")
    staffconfirm=models.CharField(max_length=264,db_column="staff_password")
    class Meta:
        managed = False
        db_table = 'staff_signup'
class photo_p(models.Model):
    roll_no=models.CharField(max_length=264,db_column='roll_no')
    ids=models.IntegerField(db_column="ids",primary_key=True)
    file_name=models.CharField(max_length=264,db_column="file_name")
    file=models.BinaryField(db_column="file")
    event_name=models.TextField(db_column="event_type")
    from_date=models.DateField(db_column="from_date")
    to_date=models.DateField(db_column="to_date")
    event_org=models.TextField(db_column="event_org")
    academic=models.TextField(db_column="ac_year")
    title=models.TextField(db_column="event_title")
    
    class Meta:
        db_table='pdf_files'
        managed=False
        