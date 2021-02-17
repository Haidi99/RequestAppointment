from django.forms import ModelForm
from .models import Person, Company

from searchableselect.widgets import SearchableSelect

class RequestForm(ModelForm):
    class Meta:
        model = Person
        fields = ['firstname', 'lastname', 'email', 'phone_number', 'country', 'company', 'objective', 'description']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['company'].queryset = Company.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Company queryset
        elif self.instance.pk:
            self.fields['company'].queryset = self.instance.country.company_set.order_by('name')