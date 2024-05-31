from django import forms
from app.models import *
g=[['MALE','male'],['FEMALE','female']]
c=[('PYTHON','python'),('JAVA','java'),('SQL','sql')]


class StudentForm(forms.Form):
    sid=forms.IntegerField()
    sname=forms.CharField()
    semail=forms.EmailField()
    surl=forms.URLField()
    spassword=forms.CharField(widget=forms.PasswordInput)
    saddrs=forms.CharField(widget=forms.Textarea(attrs={'cols':5,'rows':2}))
  #  gender=forms.ChoiceField(choices=g)
    geder=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
   # c=forms.MultipleChoiceField(choices=c) 
    c=forms.MultipleChoiceField(choices=c,widget=forms.RadioSelect)


