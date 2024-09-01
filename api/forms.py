from django import forms 


USER_TYPE= [
        ('', 'Choose user type'),
        ('admin', 'admin'),
        ('user', 'user')
]

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})) 
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})) 
    usertype = forms.ChoiceField(choices=USER_TYPE, widget=forms.Select(attrs={'class': 'form-control mb-3', 'placeholder': 'Choose user type'}))


class LoginForm(forms.Form): 
    email = forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})) 
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class NewProductForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username' }))
    mainImg = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    carousel1 = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    carousel2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    carousel3 = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    dimensions = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    category = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    discount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))

PAYMENT_METHOD = {
    ('UPI', 'UPI'),
    ('Credit/Debit Card', 'Credit/Debit Card'),
    ('Paypal', 'Paypal'),
    ('Cash on Delivery', 'Cash on Delivery'),
}

QUANTITY = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6)
]

class BuyProductForm(forms.Form):
    quantity = forms.ChoiceField(choices=QUANTITY, widget=forms.Select(attrs={'class': 'form-control'}))
    name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    pincode = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    paymentMethod = forms.ChoiceField(choices=PAYMENT_METHOD, widget=forms.Select(attrs={'class': 'form-control mb-3'}))

class AddToCartForm(forms.Form):
    quantity = forms.ChoiceField(choices=QUANTITY, widget=forms.Select(attrs={'class': '', 'id': 'productQuantity'}))


class BuyCartForm(forms.Form):
    name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    pincode = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    paymentMethod = forms.ChoiceField(choices=PAYMENT_METHOD, widget=forms.Select(attrs={'class': 'form-control mb-3'}))


ORDER_STATUS = [
    ('order placed', 'order placed'),
    ('In Transit', 'In Transit'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
]

class UpdateOrderForm(forms.Form):
    orderId = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices=ORDER_STATUS, widget=forms.Select(attrs={'class': 'form-control'}))