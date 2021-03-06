from django import forms


class ReviewForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Представьтесь', 'class': 'form-control'}),
        label='Имя')
    description = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Содержание', 'class': 'form-control'}),
        label='Содержание')
    radio_mark = forms.TypedChoiceField(widget=forms.RadioSelect,
                                        choices=((1,'1',), (2, '2',),(3, '3',), (4, '4',), (5, '5',))
                                        )