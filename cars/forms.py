from django import forms
from .models import Car,CarDetail,Category,Review,Order





class FilterCarForm(forms.ModelForm):
   
    class Meta:
        model = Car
        fields = ['brand']

    category = forms.MultipleChoiceField(
        choices=[(cat, cat) for cat in Category.objects.values_list("name", flat=True).distinct()],
        widget=forms.CheckboxSelectMultiple(attrs={
            'placeholder': 'Выберите категорию автомобиля',
            "class": "",
            "name": "category"
        }),
        label="Категория",
        required=False
    )
    
    brand = forms.MultipleChoiceField(
        choices=[(brand, brand) for brand in Car.objects.values_list('brand', flat=True).distinct()],
        widget=forms.CheckboxSelectMultiple(attrs={
            'placeholder': 'Выберите бренд автомобиля',
            "class": "",
            "name": "brand"
        }),
        label="Марка",
        required=False
    )
    
    year = forms.MultipleChoiceField(
        choices=[(year, year) for year in Car.objects.values_list('year', flat=True).distinct()],
        widget=forms.RadioSelect(attrs={
            'placeholder': 'Выберите год выпуска автомобиля',
            "class": "",
            "name": "year"
        }),
        label="Год выпуска",
        required=False
    )
    

class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update(
            {
                'class': 'block p-2.5 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-1/2 ',
            }
        )

    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'class': 'text-center mx-auto'}),
        }


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = Order
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(OrderForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name