from django.forms import ModelForm
from stars.models import Constellation

# Create the form class.
class ConstellationForm(ModelForm):
    class Meta:
        model = Constellation
        fields = '__all__'
