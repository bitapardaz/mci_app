from django import forms
from rbt.models import CatAdvert,Category,Album


class AlbumSelectForm(forms.Form):

    category = forms.ChoiceField()
    album = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(AlbumSelectForm,self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ChoiceField( choices= [('empty','----------')] + [ (o.id, o.farsi_name) for o in Category.objects.all()]  )
        #self.fields['album'] = forms.ChoiceField( choices=[ (o.id, o.farsi_name) for o in Album.objects.all()])
