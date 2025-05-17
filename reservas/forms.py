from django import forms
from .models import Reserva
from clientes.models import Cliente
from parceiros.models import Parceiro
import re

class ReservaForm(forms.ModelForm):
    cpf_cliente = forms.CharField(
        label="CPF do Cliente",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    cnpj = forms.CharField(
        max_length=14, 
        required=True,  
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        label="CNPJ do Parceiro"
    )

    class Meta:
        model = Reserva
        exclude = (
            'numero_reserva', 
            'data_entrada', 
            'nome_cliente', 
            'nome_fantasia', 
            'colaborador_responsavel',
            'cpf_cliente',
        )
        widgets = {
            'data_ida': forms.TextInput(
                attrs={
                    'class': 'form-control datepicker-br',
                    'placeholder': 'DD/MM/AAAA'
                }
            ), 
            'data_volta': forms.TextInput(
                attrs={
                    'class': 'form-control datepicker-br',
                    'placeholder': 'DD/MM/AAAA'
                }
            ), 
            'comentarios_adicionais': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        instance = kwargs.get('instance')
        if instance and instance.cpf_cliente:
            self.fields['cpf_cliente'].initial = instance.cpf_cliente.cpf_cliente

        if instance and instance.cnpj:
            self.fields['cnpj'].initial = instance.cnpj.cnpj

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if cnpj:
            cnpj_limpo = re.sub(r'\D', '', cnpj)
            try:
                parceiro = Parceiro.objects.get(cnpj=cnpj_limpo)
            except Parceiro.DoesNotExist:
                raise forms.ValidationError('Parceiro não encontrado.')
            return parceiro  
        return None

    def clean_cpf_cliente(self):
        cpf = self.cleaned_data.get('cpf_cliente')
        if cpf:
            cpf_limpo = re.sub(r'\D', '', cpf)
            try:
                cliente = Cliente.objects.get(cpf_cliente=cpf_limpo)
            except Cliente.DoesNotExist:
                raise forms.ValidationError('Cliente não encontrado com esse CPF.')
            return cliente  
        return None


class ConsultaReservaForm(forms.Form):
    numero_reserva = forms.CharField(max_length=10, required=False, label='Número da Reserva')
    cpf_cliente = forms.CharField(max_length=14, required=False, label='CPF do Cliente')

    def clean_cpf_cliente(self):
        cpf = self.cleaned_data.get('cpf_cliente')
        if cpf:
            return re.sub(r'\D', '', cpf)  
        return cpf
