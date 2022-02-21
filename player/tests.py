from django.test import TestCase

# Create your tests here.
from account.models import CustomUser
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
                           )


class TestPlayerModels(TestCase):
    """ """
    def setUp(self):
        """ """
        user = CustomUser.object.create(username='Usertest', 
                                        email='test@test.fr',
                                        password='motdepasse445')
        player = Player.objects.create(nom='TestnomPlayer', joueur=user)
        caracteristique_base = CaracteristiqueBase.objects.create(mouvement=4,
                                                                  capacite_combat=20,
                                                                  capacité_tir=20,
                                                                  force=4,
                                                                  endurance=5,
                                                                  point_blessure=10,
                                                                  initiative=20,
                                                                  nb_attaque=2,
                                                                  dexterite =20,
                                                                  commandement=20,
                                                                  intelligence=20,
                                                                  calme=20,
                                                                  force_mentale=20,
                                                                  sociabilite=20,
                                                                  player=player,
                                                                  )
        caracteristique_actuelle = CaracteristiqueActuelle.objects.create(mouvement=4,
                                                                        capacite_combat=20,
                                                                        capacité_tir=20,
                                                                        force=5,
                                                                        endurance=5,
                                                                        point_blessure=10,
                                                                        initiative=20,
                                                                        nb_attaque=4,
                                                                        dexterite =20,
                                                                        commandement=20,
                                                                        intelligence=20,
                                                                        calme=20,
                                                                        force_mentale=20,
                                                                        sociabilite=20,
                                                                        player=player,
                                                                        )
        plan_carriere = PlanCarriere.objects.create(mouvement=4,
                                                    capacite_combat=20,
                                                    capacité_tir=20,
                                                    force=6,
                                                    endurance=5,
                                                    point_blessure=10,
                                                    initiative=20,
                                                    nb_attaque=4,
                                                    dexterite =20,
                                                    commandement=20,
                                                    intelligence=20,
                                                    calme=20,
                                                    force_mentale=20,
                                                    sociabilite=20,
                                                    player=player,
                                                    )
        competence = Competence.objects.create(nom='deplacements silencieux', 
                                               player=player
                                               )
        arme_contact = ArmeContact.objects.create(nom='épée à deux mains',
                                                  player=player
                                                  )
        arme_distance = ArmeDistance.objects.create(nom='arc long', 
                                                    player=player
                                                    )
        armure = Armure.objects.create(nom='bouclier', 
                                       protection='1', 
                                       localisation='Toutes',
                                       player=player
                                       )
        magie = Magie.objects.create(nom='boule de feu',
                                     type_magie='Magie de bataille',
                                     niveau_sort='1',
                                     player=player,
                                     )
        equipement = Equipement.objects.create(nom='lampe torche',
                                               quantite=12,
                                               encombrement=20,
                                               note="les torches c'est cool",
                                               player=player,
                                               )
        bourse = Bourse.objects.create(couronne=10,
                                       pistole=120,
                                       sous=547,
                                       player=player,
                                       )
        user.save()
        player.save()
        caracteristique_base.save()
        caracteristique_actuelle.save()
        plan_carriere.save()
        competence.save()
        arme_contact.save()
        arme_distance.save()
        armure.save()
        magie.save()
        equipement.save()
        bourse.save()
    
    def test_player_model(self):
        """ """
        player_test = Player.objects.get(nom='TestnomPlayer')
        self.assertEqual(player_test.nom, 'TestnomPlayer')
    
    def test_caracteristique_base_model(self):
        """ """
        caracteristique_base_test = CaracteristiqueBase.objects.get(mouvement=4)
        self.assertEqual(caracteristique_base_test.mouvement, 4 )
    
    def test_caracteristique_actuelle_model(self):
        """ """
        caracteristique_actuelle_test = CaracteristiqueActuelle.objects.get(force=5)
        self.assertEqual(caracteristique_actuelle_test.force, 5 )
        
    def test_plan_carriere_model(self):
        """ """
        plan_carriere_test = PlanCarriere.objects.get(force=6)
        self.assertEqual(plan_carriere_test.force, 6 )
    
    
    def test_competence_model(self):
        """ """
        competence_test = Competence.objects.get(nom='deplacements silencieux')
        self.assertEqual(competence_test.nom, 'deplacements silencieux' )
    
    
    def test_arme_contact_model(self):
        """ """
        arme_contact_test = ArmeContact.objects.get(nom='épée à deux mains')
        self.assertEqual(arme_contact_test.nom, 'épée à deux mains' )
    
    
    def test_arme_distance_model(self):
        """ """
        arme_distance_test = ArmeDistance.objects.get(nom='arc long')
        self.assertEqual(arme_distance_test.nom, 'arc long' )
    
    
    def test_armure_model(self):
        """ """
        armure_test = Armure.objects.get(nom='bouclier')
        self.assertEqual(armure_test.nom, 'bouclier')
        
    def test_magie_model(self):
        """ """
        magie_test = Magie.objects.get(type_magie='Magie de bataille')
        self.assertEqual(magie_test.type_magie, 'Magie de bataille' )
    
    
    def test_equipement_model(self):
        """ """
        equipement_test = Equipement.objects.get(note="les torches c'est cool")
        self.assertEqual(equipement_test.note, "les torches c'est cool")
    
    
    def test_bourse_model(self):
        """ """
        bourse_test = Bourse.objects.get(couronne=10)
        self.assertEqual(bourse_test.couronne, 10)