from django.forms import ModelForm
from pets.models import Kind

# Create the form class.
class KindForm(ModelForm):
    class Meta:
        model = Kind
        fields = '__all__'
