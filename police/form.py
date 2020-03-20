from django import forms
from police.models import police_info,criminal,lost_and_found,notice,search_help

class police_infoForm(forms.ModelForm):
    class Meta:
        model = police_info
        fields = ['pol_id','pol_name','pol_post','pol_join','pol_pass','pol_dept','secret_key','off_day','gender']
        #fields ="__all__"
class criminal_form(forms.ModelForm):
    class Meta:
        model = criminal
        fields = ['cri_name','victim_name','victim_address','victim_ph','victim_age','cri_loc','cri_date','cri_sec','description','pol_name','pol_id']

class lost_found_form(forms.ModelForm):
    class Meta:
        model = lost_and_found
        fields ="__all__"

class noticeinfoForm(forms.ModelForm):
    class Meta:
        model = notice
        fields ="__all__"

class search_helpForm(forms.ModelForm):
    class Meta:
        model = search_help
        fields = "__all__"