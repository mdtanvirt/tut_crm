from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Client, Order, Service, Product

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'


# Create Add client form
class AddClientForm(forms.ModelForm):
	full_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}))
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	phone = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}))
	address = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}))
	city = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}))
	state = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}))
	zip_code = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}))

	class Meta:
		model = Client
		exclude = ("user",)

# New order form
class NewOrderForm(forms.ModelForm):
	amount = forms.DecimalField(label="", max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Amount'}))

	class Meta:
		model = Order
		fields = ['amount']

	def __init__(self, *args, **kwargs):
		self.client = kwargs.pop('client', None)
		super().__init__(*args, **kwargs)

	
	
# New Service form
class NewServiceForm(forms.ModelForm):
	amount = forms.DecimalField(label="", max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Amount'}))
	service_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Service Name'}))

	class Meta:
		model = Service
		fields = ['service_name', 'amount']

	def __init__(self, *args, **kwargs):
		self.client = kwargs.pop('client', None)
		super().__init__(*args, **kwargs)	
		
class NewProductForm(forms.ModelForm):
	price = forms.DecimalField(label="", max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Price'}))
	product_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Product Name'}))

	class Meta:
		model = Product
		fields = ['product_name', 'price']

	def __init__(self, *args, **kwargs):
		self.client = kwargs.pop('client', None)
		super().__init__(*args, **kwargs)