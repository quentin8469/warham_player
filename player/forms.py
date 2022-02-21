from django import forms

from player.models import (Player, 
                           CaracteristiqueBase, 
                           CaracteristiqueActuelle, 
                           PlanCarriere, 
                           ArmeContact,
                           ArmeDistance,
                           Armure,
                           Magie,
                           Competence,
                           Equipement,
                           Monture,
                           
                           )



class NewPlayerForm(forms.ModelForm):
    """"""
    class Meta:
        model = Player
        fields = ["nom", 
                    "race", 
                    "sexe", 
                    "vocation",
                    "alignement",
                    "age", 
                    "taille", 
                    "poids",
                    "cheveux", 
                    "yeux", 
                    "carriere_actuelle",
                    "cheminement_professionel",
                    "debouches",
                    "photo",
                    "point_magie",
                    "point_destin",
                    "point_folie",
                    "famillier",
                    "nombre_sort",
                    "langue",
                    "description_perso",
                    "experience",
                    "encombrement_max",
                    "encombrement_actuel",
                    "recuperation_pm",
                    "note",
                    "mort_tuer",
                  ]


class NewCaracteristiqueBaseForm(forms.ModelForm):
    """"""
    class Meta:
        model = CaracteristiqueBase
        fields = ["mouvement",
                  "capacite_combat", 
                    "capacité_tir", 
                    "force",
                    "endurance",
                    "point_blessure", 
                    "initiative", 
                    "nb_attaque",
                    "dexterite", 
                    "commandement", 
                    "intelligence",
                    "calme",
                    "force_mentale",
                    "sociabilite",
                    
                  ]
    

class NewCaracteristiqueActuelleForm(forms.ModelForm):
    """"""
    class Meta:
        model = CaracteristiqueActuelle
        fields = ["mouvement",
                  "capacite_combat", 
                    "capacité_tir", 
                    "force",
                    "endurance",
                    "point_blessure", 
                    "initiative", 
                    "nb_attaque",
                    "dexterite", 
                    "commandement", 
                    "intelligence",
                    "calme",
                    "force_mentale",
                    "sociabilite",
                    
                  ]


class NewPlanCarriereForm(forms.ModelForm):
    """"""
    class Meta:
        model = PlanCarriere
        fields = ["nom",
                  "mouvement",
                  "capacite_combat", 
                    "capacité_tir", 
                    "force",
                    "endurance",
                    "point_blessure", 
                    "initiative", 
                    "nb_attaque",
                    "dexterite", 
                    "commandement", 
                    "intelligence",
                    "calme",
                    "force_mentale",
                    "sociabilite",
                    
                  ]
    

class NewArmeContactForm(forms.ModelForm):
    """"""
    class Meta:
        model = ArmeContact
        fields = ["nom",
                    "initiative",
                    "toucher",
                    "degats",
                    "parade",
                    "encombrement",
                    "note",
                    
                  ]
        
        
class NewArmeDistanceForm(forms.ModelForm):
    """"""
    class Meta:
        model = ArmeDistance
        fields = ["nom",
                    "porte_courte",
                    "porte_longue",
                    "porte_extreme",
                    "force_effective",
                    "armer_tirer",
                    "encombrement",
                    "munitions",
                    "nb_munitions",
                    "note",
                  ]


class NewArmureForm(forms.ModelForm):
    """"""
    class Meta:
        model = Armure
        fields = ["nom",
                    "protection",
                    "localisation",
                    "encombrement",
                    "note",
                  ]


class NewMontureForm(forms.ModelForm):
    """"""
    class Meta:
        model = Monture
        fields = ["nom",
                  "mouvement", 
                  "capacite_combat", 
                  "capacité_tir", 
                  "force",
                  "endurance",
                  "point_blessure", 
                  "initiative", 
                  "nb_attaque",
                  "dexterite", 
                  "commandement", 
                  "intelligence",
                  "calme",
                  "force_mentale",
                  "sociabilite",
                  ]


class NewMagieForm(forms.ModelForm):
    """"""
    class Meta:
        model = Magie
        fields = ["nom",
                  "type_magie",
                  "niveau_sort",
                  "point_magie",
                  "porte",
                  "duree",
                  "degats",
                  "composants",
                  "description_sort",
                  "incantation",
                  "apprentissage",
                  "cout_xp",
                  "note",
                  ]


class NewCompetenceForm(forms.ModelForm):
    """"""
    class Meta:
        model = Competence
        fields = ["nom",
                  "description",
                  "bonus",
                  "malus",
                  "apprentissage",
                  "cout_xp",
                  "niveau",
                  ]


class NewEquipementForm(forms.ModelForm):
    """"""
    class Meta:
        model = Equipement
        fields = ["nom",
                  "quantite",
                  "encombrement",
                    "note",
                  ]