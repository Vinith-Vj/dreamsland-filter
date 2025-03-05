# from django import forms

# class ContactForm(forms.Form):
#     fullname = forms.CharField(label='Full Name', max_length=100)
#     phone = forms.CharField(label='Phone Number', max_length=15)
#     listingtype = forms.ChoiceField(label='Listing Type', choices=[('Seller', 'Seller'), ('Buyer', 'Buyer')])
#     address = forms.CharField(label='Comments', widget=forms.Textarea, max_length=500)


from django import forms
from .models import Property, Location

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        widgets = {
            'property_name': forms.TextInput(attrs={'class': 'form-control'}),
            'property_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'property_location': forms.Select(attrs={'class': 'form-select'}),
            'property_status': forms.Select(attrs={'class': 'form-select'}),
            'bhk': forms.NumberInput(attrs={'class': 'form-control'}),
            'square_feet': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'property_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'property_main_image':  forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'gallery_1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'gallery_2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'gallery_3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'possession_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'plot_area': forms.TextInput(attrs={'class': 'form-control'}),
            'plot_unit': forms.Select(attrs={'class': 'form-select'}),
            'property_type': forms.Select(attrs={'class': 'form-select'}),
            'property_subtype': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        locations_queryset = kwargs.pop('locations_queryset', Location.objects.none())
        super(PropertyForm, self).__init__(*args, **kwargs)

        self.fields['property_location'].queryset = locations_queryset


# from django import forms
# from .models import Property, Location

# class PropertyForm(forms.ModelForm):
#     class Meta:
#         model = Property
#         fields = '__all__'

#         widgets = {
#             'property_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'property_price': forms.NumberInput(attrs={'class': 'form-control'}),
#             'property_description': forms.Textarea(attrs={'class': 'form-control'}),
#             'property_location': forms.Select(attrs={'class': 'form-control'}),
#             'property_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#         }

#     def __init__(self, *args, **kwargs):
#         locations_queryset = kwargs.pop('locations_queryset', Location.objects.none())
#         super(PropertyForm, self).__init__(*args, **kwargs)

#         # Filter property_location field
#         self.fields['property_location'] = forms.ModelChoiceField(
#             queryset=locations_queryset,
#             required=True,
#             label="Property Location",
#              widget=forms.Select(attrs={'class': 'form-control'})  # Add class here too
#         )

# from django import forms
# from .models import Property, Location

# class PropertyForm(forms.ModelForm):
#     class Meta:
#         model = Property
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         locations_queryset = kwargs.pop('locations_queryset', Location.objects.none())
#         super(PropertyForm, self).__init__(*args, **kwargs)

#         # Filter property_location field
#         self.fields['property_location'] = forms.ModelChoiceField(
#             queryset=locations_queryset,
#             required=True,
#             label="Property Location"
#         )