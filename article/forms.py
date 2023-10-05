from django import forms
from article.models import ArticleModel, CategoryModel

class ArticleForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=CategoryModel.objects.all(), to_field_name='category', label="Category", empty_label='Choose Category')
    category.widget.attrs.update({'class':'form-control'})
    class Meta:
        model = ArticleModel
        fields = ('title', 'image', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }