from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from player.views import (PlayerView,
                          MagieView,
                          PlayerDetail,
                          ResumeDetail,
                          CompetenceView,
                          EquipementView,
                          MontureView,
                          DeadNoteDetail,
                          PlayerCreate,
                          CaracteristiqueBaseCreate,
                          CaracteristiqueActuelleCreate,
                          PlanCarriereCreate,
                          ArmeContactCreate,
                          ArmeDistanceCreate,
                          ArmureCreate,
                          PlayerDelete,
                          PlanCarriereDelete,
                          ArmeContactDelete,
                          ArmeDistanceDelete,
                          ArmureDelete,
                          PlayerUpdate,
                          MontureCreate,
                          MontureDelete,
                          MontureUpdate,
                          ArmureUpdate,
                          ArmeDistanceUpdate,
                          ArmeContactUpdate,
                          PlanCarriereUpdate,
                          CaracteristiqueBaseUpdate,
                          CaracteristiqueActuelleUpdate,
                          MagieCreate,
                          MagieDelete,
                          MagieUpdate,
                          CompetenceDelete,
                          CompetenceCreate,
                          CompetenceUpdate,
                          EquipementCreate,
                          EquipementDelete,
                          EquipementUpdate,
                          
                          )


app_name = 'playeur'

urlpatterns = [
    path('', PlayerView.as_view(), name='liste_personnages'),
    path('creation_personnage/', PlayerCreate.as_view(), name='creation_personnage'),
    path('<int:pk>/details_personnage/', PlayerDetail.as_view(), name='details_personnage'),
    path('<int:pk>/effacer_personnage/', PlayerDelete.as_view(), name='effacer_personnage'),
    path('<int:pk>/edit_personnage/', PlayerUpdate.as_view(), name='editter_personnage'),
    
    path('<int:pk>/creation_carac_base/', CaracteristiqueBaseCreate.as_view(), name='creation_carac_base'),
    path('<int:pk>/editter_carac_base/', CaracteristiqueBaseUpdate.as_view(), name='editter_carac_base'),
    
    path('<int:pk>/creation_carac_actuelle/', CaracteristiqueActuelleCreate.as_view(), name='creation_carac_actuelle'),
    path('<int:pk>/editter_carac_actuelle/', CaracteristiqueActuelleUpdate.as_view(), name='editter_carac_actuelle'),
    
    path('<int:pk>/plan_carriere/', PlanCarriereCreate.as_view(), name='plan_carriere'),
    path('<int:pk>/editter_carriere/', PlanCarriereUpdate.as_view(), name='editter_carriere'),
    path('<int:pk>/effacer_carriere/', PlanCarriereDelete.as_view(), name='effacer_carriere'),
    
    path('<int:pk>/armes_contacts/', ArmeContactCreate.as_view(), name='armes_contacts'),
    path('<int:pk>/editter_arme_contact/', ArmeContactUpdate.as_view(), name='editter_arme_contact'),
    path('<int:pk>/effacer_arme_contact/', ArmeContactDelete.as_view(), name='effacer_arme_contact'),
    
    path('<int:pk>/armes_distances/', ArmeDistanceCreate.as_view(), name='armes_distances'),
    path('<int:pk>/editter_arme_distance/', ArmeDistanceUpdate.as_view(), name='editter_arme_distance'),
    path('<int:pk>/effacer_arme_distance/', ArmeDistanceDelete.as_view(), name='effacer_arme_distance'),
    
    path('<int:pk>/armures/', ArmureCreate.as_view(), name='armures'),
    path('<int:pk>/editter_armure/', ArmureUpdate.as_view(), name='editter_armure'),
    path('<int:pk>/effacer_armure/', ArmureDelete.as_view(), name='effacer_armure'),
    
    path('<int:pk>/montures/', MontureView.as_view(), name='montures'),
    path('<int:pk>/nouvelle_montures/', MontureCreate.as_view(), name='nouvelle_montures'),
    path('<int:pk>/editter_montures/', MontureUpdate.as_view(), name='editter_montures'),
    path('<int:pk>/effacer_montures/', MontureDelete.as_view(), name='effacer_montures'),
    
    path('<int:pk>/magie/', MagieView.as_view(), name='magie'),
    path('<int:pk>/nouveau_sort/', MagieCreate.as_view(), name='nouveau_sort'),
    path('<int:pk>/editter_sort/', MagieUpdate.as_view(), name='editter_sort'),
    path('<int:pk>/effacer_sort/', MagieDelete.as_view(), name='effacer_sort'),
    
    path('<int:pk>/competences/', CompetenceView.as_view(), name='competences'),
    path('<int:pk>/nouvelle_competence/', CompetenceCreate.as_view(), name='nouvelle_competence'),
    path('<int:pk>/editter_competence/', CompetenceUpdate.as_view(), name='editter_competence'),
    path('<int:pk>/effacer_competence/', CompetenceDelete.as_view(), name='effacer_competence'),
    
    path('<int:pk>/equipements/', EquipementView.as_view(), name='equipements'),
    path('<int:pk>/nouvel_equipement/', EquipementCreate.as_view(), name='nouvel_equipement'),
    path('<int:pk>/editter_equipement/', EquipementUpdate.as_view(), name='editter_equipement'),
    path('<int:pk>/effacer_equipement/', EquipementDelete.as_view(), name='effacer_equipement'),
    
    path('<int:pk>/morts_tuer/', DeadNoteDetail.as_view(), name='morts_tuer'),
    
    path('<int:pk>/description/', ResumeDetail.as_view(), name='description'),
    
    
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)