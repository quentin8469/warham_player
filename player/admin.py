from django.contrib import admin

from player.models import (Player, 
                           CaracteristiqueBase, 
                           CaracteristiqueActuelle,
                           PlanCarriere,
                           Competence,
                           ArmeContact,
                           ArmeDistance,
                           Armure,
                           Magie,
                           Equipement,
                           Bourse,
                           Monture,
                           )


# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "nom", 
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
                    "date_creation",
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
                    "joueur",
                    
                    )


@admin.register(CaracteristiqueBase)
class CaracteristiqueBaseAdmin(admin.ModelAdmin):
    list_display = ("mouvement", 
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
                    "player",                   
                    )


@admin.register(CaracteristiqueActuelle)
class CaracteristiqueActuelleAdmin(admin.ModelAdmin):
    list_display = ("mouvement", 
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
                    "player",                   
                    )


@admin.register(PlanCarriere)
class PlanCarriereAdmin(admin.ModelAdmin):
    list_display = ("nom",
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
                    "player",                   
                    )


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ("nom",
                    "description",
                    "bonus",
                    "malus",
                    "apprentissage",
                    "cout_xp",
                    "niveau",
                    "player",                   
                    )


@admin.register(ArmeContact)
class ArmeContactAdmin(admin.ModelAdmin):
    list_display = ("nom",
                    "initiative",
                    "toucher",
                    "degats",
                    "parade",
                    "encombrement",
                    "note",
                    "player",                   
                    )


@admin.register(ArmeDistance)
class ArmeDistanceAdmin(admin.ModelAdmin):
    list_display = ("nom",
                    "porte_courte",
                    "porte_longue",
                    "porte_extreme",
                    "force_effective",
                    "armer_tirer",
                    "encombrement",
                    "munitions",
                    "nb_munitions",
                    "note",
                    "player",                   
                    )


@admin.register(Armure)
class ArmureAdmin(admin.ModelAdmin):
    list_display = ("nom",
                    "protection",
                    "localisation",
                    "encombrement",
                    "note",
                    "player",                   
                    )


@admin.register(Magie)
class MagieAdmin(admin.ModelAdmin):
    list_display = ("nom",
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
                    "player",                   
                    )


@admin.register(Equipement)
class EquipementAdmin(admin.ModelAdmin):
    list_display = ("nom",
                    "quantite",
                    "encombrement",
                    "note",
                    "player",                   
                    )


@admin.register(Bourse)
class BourseAdmin(admin.ModelAdmin):
    list_display = ("couronne",
                    "pistole",
                    "sous",
                    "encombrement",
                    "note",
                    "player",                   
                    )


@admin.register(Monture)
class MontureAdmin(admin.ModelAdmin):
    list_display = ("nom",
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
                    "player",                   
                    )