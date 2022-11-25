from django import forms

def validate_name(name):
    # check if there are numbers in the name
    if (name.isalpha() == False):
        print("Veuillez n'entrer que des alphabets")  
        raise forms.ValidationError(f'La syntaxe du nom {name} est invalide')


class PersonneForm(forms.Form):
    nom = forms.CharField(
        required=True, 
        validators=[validate_name], # Call the validate_name function here
        widget = forms.TextInput(
            attrs={
               'placeholder': 'le nom de la personne'
            }
          )
        )

    prenom = forms.CharField(
        required=True, 
        min_length=3,
        validators=[validate_name], # Call the validate_name function here
        widget = forms.TextInput(
            attrs={
                'placeholder': 'le prenom de la personne'
            }
         )
        )

    ville = forms.CharField(
        required=True, 
        min_length=3,
        validators=[validate_name], # Call the validate_name function here
        widget = forms.TextInput(
            attrs={
                'placeholder': 'entrez la ville dorigine'
            }
           )
        )

    age = forms.CharField(
        required=False, 
        widget = forms.TextInput(
            attrs={
                'placeholder': 'entrez son age ici'
            }
           )
        )

   
    commentaire = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'placeholder': 'Veuillez rensiegnez ici des informations supplémentaires si nécessaire'
                }
                )
            )


    photo = forms.CharField(
        required=False, 
        widget = forms.ImageField(
            attrs={
                'placeholder': 'Ajouter la photo de la personne ici'
            }
            )
        )