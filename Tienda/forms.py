from django import forms
from .models import Producto

'''class FormVueloCustom(forms.ModelForm):
    #campos del modelo
    class Meta:
        model = Producto
        fields = ('title', 'precio', 'fecha', 'descripcion', 'imagen', 'categoria')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'estilo_title'}),
            'precio': forms.TextInput(attrs={'class': 'estilo_precio'}),
            'fecha': forms.DateInput(attrs={'class': 'estilo_descripcion'}),
        }'''