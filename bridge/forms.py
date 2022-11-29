from django import forms


class TextInputForm(forms.Form):
    """
    Форма для входных данных на анализ текста
    :param Text: текст(максимальное кол-во знаков = 1000)
    """
    Text = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Text', min_length=10, max_length=1000, required=True
    )
