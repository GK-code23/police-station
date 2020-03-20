from django.db import models

class police_info(models.Model):
    pol_id   = models.IntegerField(primary_key=True)
    pol_name = models.CharField(max_length=20)
    pol_post = models.CharField(max_length=10)
    pol_join = models.DateField()
    gender = models.CharField(max_length=20,default="Male")
    pol_pass = models.CharField(max_length=10)
    pol_dept = models.CharField(max_length=20)
    secret_key = models.CharField(max_length=20)
    off_day = models.CharField(max_length=20,default="null")
    schedule = models.CharField(max_length=20,default="null")
    daily_cnt  = models.IntegerField(default=0)
    overtime = models.IntegerField(default=0)
    clas = models.CharField(max_length=20,default="None")
    set = models.CharField(max_length=20,default="None")
    salary = models.CharField(max_length=20,default="0")

    class Meta:
        db_table = "police"

    def __str__(self):
        return self.pol_name

class criminal(models.Model):
    cri_name = models.CharField(max_length=30)
    victim_name   = models.CharField(max_length=20)
    victim_address = models.CharField(max_length=30)
    victim_ph  = models.CharField(max_length=30)
    victim_age = models.CharField(max_length=30)
    cri_loc = models.CharField(max_length=30)
    cri_date = models.DateField()
    cri_sec = models.CharField(max_length=30)
    description = models.TextField(max_length=2000)
    pol_name = models.CharField(max_length=30)
    pol_id = models.IntegerField()
    status = models.CharField(max_length=20,default="ongoing")
    def __str__(self):
        return self.cri_name




class petrolling(models.Model):
    vehicle_no = models.CharField(max_length=30)
    pet_area = models.CharField(max_length=30)
    pol_name = models.CharField(max_length=30)

    def __str__(self):
        return self.vehicle_no



class daily(models.Model):
    day=models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    pol_id = models.ForeignKey(police_info,on_delete=models.CASCADE)

    def __str__(self):
        return self.day

class lost_and_found(models.Model):
    full_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    report_type= models.CharField(max_length=100)
    article_type= models.CharField(max_length=50)
    loc_of_incedent=models.CharField(max_length=100)
    date=models.DateField()
    doc_id=models.CharField(max_length=30)
    descrip=models.CharField(max_length=100)
    police_station = models.CharField(max_length=40,default="NASHIK CITY POLICE STATION")
    pol_name=models.CharField(max_length=100)
    pol_id = models.IntegerField()


    def __str__(self):
        return self.full_name

class notice(models.Model):
    note1=models.CharField(max_length=300)

    def __str__(self):
        return self.note1


class search_help(models.Model):
    name = models.CharField(max_length=30)
    ph= models.CharField(max_length=10)
    case_id = models.CharField(max_length=10)