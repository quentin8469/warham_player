from xml.dom import NoModificationAllowedErr
from django.db import models

from account.models import CustomUser
# Create your models here.

class Player(models.Model):
    """"""
    nom = models.CharField(max_length=50, blank=False, null=False)
    race = models.CharField(max_length=50, blank=True, null=True)
    sexe = models.CharField(max_length=50, blank=True, null=True)
    vocation = models.CharField(max_length=50, blank=True, null=True)
    alignement = models.CharField(max_length=50, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    taille = models.CharField(max_length=50, blank=True, null=True)
    poids = models.CharField(max_length=50, blank=True, null=True)
    cheveux = models.CharField(max_length=50, blank=True, null=True)
    yeux = models.CharField(max_length=50, blank=True, null=True)
    carriere_actuelle = models.CharField(max_length=50, blank=True, null=True)
    cheminement_professionel = models.TextField(blank=True, null=True)
    debouches = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="photo_perso/", blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    point_magie = models.IntegerField(blank=True, null=True)
    point_destin = models.IntegerField(blank=True, null=True)
    point_folie = models.IntegerField(blank=True, null=True)
    famillier = models.CharField(max_length=50, blank=True, null=True)
    nombre_sort = models.IntegerField(blank=True, null=True)
    langue = models.CharField(max_length=50, blank=True, null=True)
    description_perso = models.TextField(blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    encombrement_max = models.IntegerField(blank=True, null=True)
    encombrement_actuel = models.IntegerField(blank=True, null=True)
    recuperation_pm = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    mort_tuer = models.TextField(blank=True, null=True)
    joueur = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"
    
    def __str__(self):
        return f"{self.nom} - {self.joueur}"


class CaracteristiqueBase(models.Model):
    """"""
    mouvement = models.PositiveIntegerField(blank=False, null=False)
    capacite_combat =models.PositiveIntegerField(blank=False, null=False)
    capacité_tir = models.PositiveIntegerField(blank=False, null=False)
    force = models.PositiveIntegerField(blank=False, null=False)
    endurance = models.PositiveIntegerField(blank=False, null=False)
    point_blessure = models.PositiveIntegerField(blank=False, null=False)
    initiative = models.PositiveIntegerField(blank=False, null=False)
    nb_attaque = models.PositiveIntegerField(blank=False, null=False)
    dexterite = models.PositiveIntegerField(blank=False, null=False)
    commandement = models.PositiveIntegerField(blank=False, null=False)
    intelligence = models.PositiveIntegerField(blank=False, null=False)
    calme = models.PositiveIntegerField(blank=False, null=False)
    force_mentale = models.PositiveIntegerField(blank=False, null=False)
    sociabilite = models.PositiveIntegerField(blank=False, null=False)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Caracteristique de base"
        verbose_name_plural = "Caracteristiques de bases"


class CaracteristiqueActuelle(models.Model):
    """"""
    mouvement = models.PositiveIntegerField(blank=True, null=True)
    capacite_combat =models.PositiveIntegerField(blank=True, null=True)
    capacité_tir = models.PositiveIntegerField(blank=True, null=True)
    force = models.PositiveIntegerField(blank=True, null=True)
    endurance = models.PositiveIntegerField(blank=True, null=True)
    point_blessure = models.PositiveIntegerField(blank=True, null=True)
    initiative = models.PositiveIntegerField(blank=True, null=True)
    nb_attaque = models.PositiveIntegerField(blank=True, null=True)
    dexterite = models.PositiveIntegerField(blank=True, null=True)
    commandement = models.PositiveIntegerField(blank=True, null=True)
    intelligence = models.PositiveIntegerField(blank=True, null=True)
    calme = models.PositiveIntegerField(blank=True, null=True)
    force_mentale = models.PositiveIntegerField(blank=True, null=True)
    sociabilite = models.PositiveIntegerField(blank=True, null=True)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Caracteristique actuelle"
        verbose_name_plural = "Caracteristiques actuelles"


class PlanCarriere(models.Model):
    """"""
    nom = models.CharField(max_length=50, blank=True, null=True)
    mouvement = models.PositiveIntegerField(blank=True, null=True)
    capacite_combat =models.PositiveIntegerField(blank=True, null=True)
    capacité_tir = models.PositiveIntegerField(blank=True, null=True)
    force = models.PositiveIntegerField(blank=True, null=True)
    endurance = models.PositiveIntegerField(blank=True, null=True)
    point_blessure = models.PositiveIntegerField(blank=True, null=True)
    initiative = models.PositiveIntegerField(blank=True, null=True)
    nb_attaque = models.PositiveIntegerField(blank=True, null=True)
    dexterite = models.PositiveIntegerField(blank=True, null=True)
    commandement = models.PositiveIntegerField(blank=True, null=True)
    intelligence = models.PositiveIntegerField(blank=True, null=True)
    calme = models.PositiveIntegerField(blank=True, null=True)
    force_mentale = models.PositiveIntegerField(blank=True, null=True)
    sociabilite = models.PositiveIntegerField(blank=True, null=True)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Plan de carriere"
        verbose_name_plural = "Plans de carrieres"


class Competence(models.Model):
    """ """
    nom = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    bonus = models.PositiveIntegerField(blank=True, null=True)
    malus = models.PositiveIntegerField(blank=True, null=True)
    apprentissage = models.TextField(blank=True, null=True)
    cout_xp = models.PositiveIntegerField(blank=True, null=True)
    niveau = models.CharField(max_length=50, blank=True, null=True)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Competence"
        verbose_name_plural = "Competences"
    
    def __str__(self):
        return f"{self.nom}"


class ArmeContact(models.Model):
    """"""
    nom = models.CharField(max_length=50, blank=False, null=False)
    initiative = models.CharField(max_length=50, blank=True, null=True)
    toucher = models.CharField(max_length=50, blank=True, null=True)
    degats = models.CharField(max_length=50, blank=True, null=True)
    parade = models.CharField(max_length=50, blank=True, null=True)
    encombrement = models.PositiveIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Arme de contact"
        verbose_name_plural = "Armes de contacts"
    
    def __str__(self):
        return f"{self.nom}"
    

class ArmeDistance(models.Model):
    """"""
    nom = models.CharField(max_length=50, blank=False, null=False)
    porte_courte = models.PositiveIntegerField(blank=True, null=True)
    porte_longue = models.PositiveIntegerField(blank=True, null=True)
    porte_extreme = models.PositiveIntegerField(blank=True, null=True)
    force_effective = models.CharField(max_length=50, blank=True, null=True)
    armer_tirer = models.CharField(max_length=50, blank=True, null=True)
    encombrement = models.PositiveIntegerField(blank=True, null=True)
    munitions = models.CharField(max_length=50, blank=True, null=True)
    nb_munitions = models.PositiveIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Arme de distance"
        verbose_name_plural = "Armes de distances"
    
    def __str__(self):
        return f"{self.nom}"


class Armure(models.Model):
    """"""
    choix_loc = [('Toutes', 'Toutes'),
                 ('Tête', 'Tête'),
                 ('Tronc', 'Tronc'),
                 ('Bras', 'Bras'),
                 ('Jambes', 'Jambes'),
                 ]
    
    nom = models.CharField(max_length=50, blank=False, null=False)
    protection = models.CharField(max_length=50, blank=False, null=False)
    localisation = models.CharField(max_length=50, choices=choix_loc, blank=False, null=False)
    encombrement = models.PositiveIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Armure"
        verbose_name_plural = "Armures"
    
    def __str__(self):
        return f"{self.nom} - {self.localisation}"


class Magie(models.Model):
    """"""
    choix_type_magie = [('Magie mineure', 'Magie mineure'),
                        ('Magie de bataille', 'Magie de bataille'),
                        ('Magie démonique', 'Magie démonique'),
                        ('Magie druidique', 'Magie druidique'),
                        ('Magie elementaire', 'Magie elementaire'),
                        ('Magie illusoire', 'Magie illusoire'),
                        ('Magie necromantique', 'Magie necromantique'),
                        ('Magie autre', 'Magie autre'),
                        ]
    
    choix_niveau_sort = [('0','0'),
                         ('1','1'),
                         ('2','2'),
                         ('3','3'),
                         ('4','4'),
                         ]
    
    
    nom = models.CharField(max_length=50, blank=False, null=False)
    type_magie = models.CharField(max_length=50, choices=choix_type_magie, blank=False, null=False)
    niveau_sort = models.CharField(max_length=50, choices=choix_niveau_sort, blank=False, null=False)
    point_magie = models.PositiveIntegerField(blank=True, null=True)
    porte = models.CharField(max_length=50, blank=True, null=True)
    duree = models.CharField(max_length=50, blank=True, null=True)
    degats = models.CharField(max_length=50, blank=True, null=True)
    composants = models.CharField(max_length=50, blank=True, null=True)
    description_sort = models.TextField(blank=True, null=True)
    incantation = models.TextField(blank=True, null=True)
    apprentissage = models.CharField(max_length=50, blank=True, null=True)
    cout_xp = models.PositiveIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Magie"
        verbose_name_plural = "Magies"
    
    def __str__(self):
        return f"{self.nom}"


class Equipement(models.Model):
    """ """
    nom = models.CharField(max_length=50, blank=False, null=False)
    quantite = models.PositiveIntegerField(blank=True, null=True)
    encombrement = models.PositiveIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Equipement"
        verbose_name_plural = "Equipements"
    
    def __str__(self):
        return f"{self.nom}"


class Bourse(models.Model):
    """"""
    couronne = models.PositiveIntegerField(blank=True, null=True)
    pistole = models.PositiveIntegerField(blank=True, null=True)
    sous = models.PositiveIntegerField(blank=True, null=True)
    encombrement = models.PositiveIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Bourse"
        verbose_name_plural = "Bourses"
    
    def __str__(self):
        return f"{self.couronne} - {self.pistole} - {self.sous}"


class Monture(models.Model):
    """"""
    nom = models.CharField(max_length=50, blank=True, null=True)
    mouvement = models.PositiveIntegerField(blank=True, null=True)
    capacite_combat =models.PositiveIntegerField(blank=True, null=True)
    capacité_tir = models.PositiveIntegerField(blank=True, null=True)
    force = models.PositiveIntegerField(blank=True, null=True)
    endurance = models.PositiveIntegerField(blank=True, null=True)
    point_blessure = models.PositiveIntegerField(blank=True, null=True)
    initiative = models.PositiveIntegerField(blank=True, null=True)
    nb_attaque = models.PositiveIntegerField(blank=True, null=True)
    dexterite = models.PositiveIntegerField(blank=True, null=True)
    commandement = models.PositiveIntegerField(blank=True, null=True)
    intelligence = models.PositiveIntegerField(blank=True, null=True)
    calme = models.PositiveIntegerField(blank=True, null=True)
    force_mentale = models.PositiveIntegerField(blank=True, null=True)
    sociabilite = models.PositiveIntegerField(blank=True, null=True)
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Monture"
        verbose_name_plural = "Montures"