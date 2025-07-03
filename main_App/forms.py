from django import forms
from .models import patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = patient
        exclude = ['Outcome']  # Exclude the 'Outcome' field from the form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap classes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'  
            
        # Apply Bootstrap 'form-control' class

   

        # Customize labels if needed
        self.fields['name'].label = 'Full Name'
        self.fields['so'].label = 'Son/Daughter'
        self.fields['address'].label = 'Address'

    # Add Bootstrap classes to the submit button

       
        
  

    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic here if needed
        return cleaned_data





class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Search Here'}))



class editform(forms.ModelForm):


      class Meta:
        model = patient
        exclude = ['Outcome','Age','BMI','gender','Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','DiabetesPedigreeFunction']  # Exclude the 'Outcome' field from the form

      def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap classes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'  
            
        # Apply Bootstrap 'form-control' class

   

        # Customize labels if needed
        self.fields['name'].label = 'Full Name'
        self.fields['so'].label = 'Son/Daughter'
        self.fields['address'].label = 'Address'
          