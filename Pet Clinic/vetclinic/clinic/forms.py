from django import forms
from .models import Appointment, Owner, Pet
# ฟอร์มจองคิว
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['pet', 'vet', 'appointment_date', 'status', 'note']


# ฟอร์มเจ้าของ (เพิ่มใหม่)
class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'phone', 'email', 'address']

from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['owner', 'name', 'species', 'breed', 'gender', 'birthdate']