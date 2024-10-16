from django import forms

class BaseSharesForm(forms.Form):
    dividends = forms.DecimalField(
        required=True,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Dividends',
        }),
        help_text='Enter the dividend of the preference share.',
    )

    rate_of_return = forms.DecimalField(
        required=True,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter rate of return (e.g., 0.08)',
        }),
        help_text='Enter the required rate of return (as a decimal, e.g., 0.08 for 8%).',
    )

class BaseROEGrowthRateForm(forms.Form):
    net_profit = forms.DecimalField(
        required=True,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Net profit',
        }),
        help_text='Enter the net profit of the company',
    )

    equity_capital= forms.DecimalField(
        required=True,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Equity capital ',
        }),
        help_text='Enter the equity capital of the company'
    )


class PreferencesSharesForm(BaseSharesForm):
   pass


class OrdinarySharesPrice(BaseSharesForm):
    growth_rate = forms.DecimalField(
        required=True,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter growth rate',
        }),
        help_text='Enter the growth rate of dividends (as a decimal, e.g., 0.02 for 2%)',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['dividends'].widget.attrs['placeholder'] = 'Enter expected dividend'
        self.fields['dividends'].help_text = 'Enter the expected dividend for the next period'
        self.fields['rate_of_return'].help_text = ('Enter the required rate of return (as a decimal, e.g., 0.08 for 8%;<br>'
                                                   'The required rate of return must be greater than the growth rate.)')


class ReturnOnEquityForm(BaseROEGrowthRateForm):
    pass


class GrowthRateOfDividendsForm(BaseROEGrowthRateForm):
    retention_ratio = forms.DecimalField(
        required=True,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter retention ratio',
        }),
        help_text='Enter the Retention Ratio (Ki) of the company'
    )

class CAPMForm(forms.Form):
    pass
