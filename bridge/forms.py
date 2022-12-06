from django import forms


class TextInputForm(forms.Form):
    """
    Форма для входных данных на анализ текста
    :param Text: текст(максимальное кол-во знаков = 1000)
    """
    Text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        label='Text', min_length=10, max_length=1000, required=True
    )
