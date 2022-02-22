
from django.urls import reverse
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView,
                                  DeleteView,
                                  UpdateView,
                                  )

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
                           Bourse,
                           )

from player.forms import (NewPlayerForm,
                          NewCaracteristiqueBaseForm,
                          NewCaracteristiqueActuelleForm,
                          NewPlanCarriereForm,
                          NewArmeContactForm,
                          NewArmeDistanceForm,
                          NewArmureForm,
                          NewMontureForm,
                          NewMagieForm,
                          NewCompetenceForm,
                          NewEquipementForm,
                          )


# CRUD listView

class PlayerView(ListView):
    model = Player
    template_name = "personnage/player_list.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        players = Player.objects.filter(joueur=self.request.user.id)
        context['players'] = players
        
        return super().get_context_data(**context) # get the default context data
    
   
class MagieView(ListView):
    model = Magie
    template_name = "magie/magie_list.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs['pk'])
        magies = Magie.objects.filter(player=self.kwargs['pk'])
        magies_mineurs = magies.filter(type_magie='Magie mineure')
        magies_batailles = magies.filter(type_magie='Magie de bataille')
        magies_demoniques = magies.filter(type_magie='Magie démonique')
        magies_druidiques = magies.filter(type_magie='Magie druidique')
        magies_elementaires = magies.filter(type_magie='Magie elementaire')
        magies_illusoires = magies.filter(type_magie='Magie illusoire')
        magies_necromantiques = magies.filter(type_magie='Magie necromantique')
        magies_autres = magies.filter(type_magie='Magie autre')
        context['player'] = player
        context['magies'] = magies
        context['magies_mineurs'] = magies_mineurs
        context['magies_batailles'] = magies_batailles 
        context['magies_demoniques'] = magies_demoniques
        context['magies_druidiques'] = magies_druidiques
        context['magies_elementaires'] = magies_elementaires
        context['magies_illusoires'] = magies_illusoires
        context['magies_necromantiques'] = magies_necromantiques
        context['magies_autres'] = magies_autres
        return super().get_context_data(**context) # get the default context data
    

class CompetenceView(ListView):
    model = Competence
    template_name = "competence/competences_list.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs['pk'])
        competences = Competence.objects.filter(player=self.kwargs['pk'])
        context['player'] = player
        context['competences'] = competences
        return super().get_context_data(**context) # get the default context data


class EquipementView(ListView):
    model = Equipement
    template_name = "equipement/equipement_list.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs['pk'])
        equipements = Equipement.objects.filter(player=self.kwargs['pk'])
        
        context['player'] = player
        context['equipements'] = equipements
        
        return super().get_context_data(**context) # get the default context data
    

class MontureView(ListView):
    model = Monture
    template_name = "monture/monture_list.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs['pk'])
        montures = Monture.objects.filter(player=self.kwargs['pk'])
        context['player'] = player
        context['montures'] = montures
        return super().get_context_data(**context) # get the default context data

   
# CRUD DetailView

class PlayerDetail(DetailView):
    model = Player
    context_object_name = "player"
    template_name = "personnage/player_details.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        try:
            profil_initial = CaracteristiqueBase.objects.get(player=self.kwargs['pk'])
            profil_actuel = CaracteristiqueActuelle.objects.get(player=self.kwargs['pk'])
            plan_carrieres = PlanCarriere.objects.filter(player=self.kwargs['pk'])
            armes_contacts = ArmeContact.objects.filter(player=self.kwargs['pk'])
            armes_distances = ArmeDistance.objects.filter(player=self.kwargs['pk'])
            armures = Armure.objects.filter(player=self.kwargs['pk'])
            context['profil_initial'] = profil_initial
            context['profil_actuel'] = profil_actuel
            context['plan_carrieres'] = plan_carrieres
            context['armes_contacts'] = armes_contacts
            context['armes_distances'] = armes_distances
            context['armures'] = armures
        except:
            context['profil_initial'] = 0 
        return super().get_context_data(**context) # get the default context data


class ResumeDetail(DetailView):
    model = Player
    context_object_name = "player"
    template_name = "description/resume_details.html"


class DeadNoteDetail(DetailView):
    model = Player
    context_object_name = "player"
    template_name = "note_mort/note_morts_details.html"


# CRUD CreateView

class PlayerCreate(CreateView):
    model = Player
    form_class = NewPlayerForm
    template_name = "personnage/player_create.html"
    success_url = '/liste_personnages/'

    def form_valid(self, form):
        form.instance.joueur = self.request.user
        return super().form_valid(form)
    
    # def get_success_url(self):
    #     return reverse("playeur:creation_carac_base")


class CaracteristiqueBaseCreate(CreateView):
    model = CaracteristiqueBase
    form_class = NewCaracteristiqueBaseForm
    template_name = "carac_base/caracbase_create.html"
    
    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs["pk"])
        context['player'] = player.id
        try:
            profil_initial = CaracteristiqueBase.objects.get(player=player.id)
            context['profil_initial'] = profil_initial.player.id
        except:
            context['profil_initial'] = 0
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        return reverse("playeur:creation_carac_actuelle", kwargs={"pk": self.kwargs["pk"]})


class CaracteristiqueActuelleCreate(CreateView):
    model = CaracteristiqueActuelle
    form_class = NewCaracteristiqueActuelleForm
    template_name = "carac_actuelle/caracactuelle_create.html"
    success_url = '/liste_personnages/'
    
    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)


class PlanCarriereCreate(CreateView):
    model = PlanCarriere
    form_class = NewPlanCarriereForm
    template_name = "plan_carriere/plan_carriere_create.html"
    
    
    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs['pk'])
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        return reverse("playeur:details_personnage", kwargs={"pk": self.kwargs["pk"]})


class ArmeContactCreate(CreateView):
    model = ArmeContact
    form_class = NewArmeContactForm
    template_name = "arme_contact/armes_contacts_create.html"
    
    
    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs['pk'])
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        return reverse("playeur:details_personnage", kwargs={"pk": self.kwargs["pk"]})


class ArmeDistanceCreate(CreateView):
    model = ArmeDistance
    form_class = NewArmeDistanceForm
    template_name = "arme_distance/armes_distances_create.html"
    
    
    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs['pk'])
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        return reverse("playeur:details_personnage", kwargs={"pk": self.kwargs["pk"]})


class ArmureCreate(CreateView):
    model = Armure
    form_class = NewArmureForm
    template_name = "armure/armures_create.html"
    
    
    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs['pk'])
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        return reverse("playeur:details_personnage", kwargs={"pk": self.kwargs["pk"]})


class MontureCreate(CreateView):
    model = Monture
    form_class = NewMontureForm
    template_name = "monture/monture_create.html"
    
    
    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs['pk'])
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        return reverse("playeur:montures", kwargs={"pk": self.kwargs["pk"]})


class MagieCreate(CreateView):
    model = Magie
    form_class = NewMagieForm
    template_name = "magie/magie_create.html"
    
    
    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs['pk'])
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        return reverse("playeur:magie", kwargs={"pk": self.kwargs["pk"]})    


class CompetenceCreate(CreateView):
    model = Competence
    form_class = NewCompetenceForm
    template_name = "competence/competence_create.html"
    
    
    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs['pk'])
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        return reverse("playeur:competences", kwargs={"pk": self.kwargs["pk"]}) 


class EquipementCreate(CreateView):
    model = Equipement
    form_class = NewEquipementForm
    template_name = "equipement/equipement_create.html"
    
    
    def form_valid(self, form):
        form.instance.player = Player.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = {}
        player = Player.objects.get(id=self.kwargs['pk'])
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        return reverse("playeur:equipements", kwargs={"pk": self.kwargs["pk"]})
    
    
# CRUD UpdateView

class PlayerUpdate(UpdateView):
    model = Player
    form_class = NewPlayerForm
    template_name = "personnage/player_update.html"
    
    def get_success_url(self):
        return reverse("playeur:details_personnage", kwargs={"pk": self.kwargs["pk"]})


class CaracteristiqueBaseUpdate(UpdateView):
    model = CaracteristiqueBase
    form_class = NewCaracteristiqueBaseForm
    template_name = "carac_base/caracbase_create.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        carac_base = CaracteristiqueBase.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=carac_base.player.id)
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        carac_base = CaracteristiqueBase.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=carac_base.player.id)
        return reverse("playeur:details_personnage", kwargs={"pk": player.id})


class CaracteristiqueActuelleUpdate(UpdateView):
    model = CaracteristiqueActuelle
    form_class = NewCaracteristiqueActuelleForm
    template_name = "carac_actuelle/caracactuelle_create.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        carac_actuelle = CaracteristiqueActuelle.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=carac_actuelle.player.id)
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        carac_actuelle = CaracteristiqueActuelle.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=carac_actuelle.player.id)
        return reverse("playeur:details_personnage", kwargs={"pk": player.id})


class PlanCarriereUpdate(UpdateView):
    model = PlanCarriere
    form_class = NewPlanCarriereForm
    template_name = "plan_carriere/plan_carriere_create.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        plan_carriere = PlanCarriere.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=plan_carriere.player.id)
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        plan_carriere = PlanCarriere.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=plan_carriere.player.id)
        return reverse("playeur:details_personnage", kwargs={"pk": player.id})


class ArmeContactUpdate(UpdateView):
    model = ArmeContact
    form_class = NewArmeContactForm
    template_name = "arme_contact/armes_contacts_create.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        arme_contact = ArmeContact.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=arme_contact.player.id)
        context['player'] = player
        return super().get_context_data(**context) # get the default context data

    def get_success_url(self):
        arme_contact = ArmeContact.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=arme_contact.player.id)
        return reverse("playeur:details_personnage", kwargs={"pk": player.id})

    
class ArmeDistanceUpdate(UpdateView):
    model = ArmeDistance
    form_class = NewArmeDistanceForm
    template_name = "arme_distance/armes_distances_create.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        armes_distances = ArmeDistance.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=armes_distances.player.id)
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        arme_distance = ArmeDistance.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=arme_distance.player.id)
        return reverse("playeur:details_personnage", kwargs={"pk": player.id})


class ArmureUpdate(UpdateView):
    model = Armure
    form_class = NewArmureForm
    template_name = "armure/armures_create.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        armure = Armure.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=armure.player.id)
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        armure = Armure.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=armure.player.id)
        return reverse("playeur:details_personnage", kwargs={"pk": player.id})


class MontureUpdate(UpdateView):
    model = Monture
    form_class = NewMontureForm
    template_name = "monture/monture_create.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        monture = Monture.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=monture.player.id)
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        monture = Monture.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=monture.player.id)
        return reverse("playeur:montures", kwargs={"pk": player.id})


class MagieUpdate(UpdateView):
    model = Magie
    form_class = NewMagieForm
    template_name = "magie/magie_create.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        magie = Magie.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=magie.player.id)
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        magie = Magie.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=magie.player.id)
        return reverse("playeur:magie", kwargs={"pk": player.id})   


class CompetenceUpdate(UpdateView):
    model = Competence
    form_class = NewCompetenceForm
    template_name = "competence/competence_create.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        competence = Competence.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=competence.player.id)
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        competence = Competence.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=competence.player.id)
        return reverse("playeur:competences", kwargs={"pk": player.id})
    

class EquipementUpdate(UpdateView):
    model = Equipement
    form_class = NewEquipementForm
    template_name = "equipement/equipement_create.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        equipement = Equipement.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=equipement.player.id)
        context['player'] = player
        return super().get_context_data(**context) # get the default context data
    
    def get_success_url(self):
        equipement = Equipement.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=equipement.player.id)
        return reverse("playeur:equipements", kwargs={"pk": player.id})
    
    
# CRUD DeleteView


class PlayerDelete(DeleteView):
    model = Player
    context_object_name = "player"
    template_name ='personnage/player_delete.html'
    success_url = '/liste_personnages/'


class PlanCarriereDelete(DeleteView):
    model = PlanCarriere
    context_object_name = "plan_carriere"
    template_name ='plan_carriere/plan_carriere_delete.html'
    
    def get_success_url(self):
        plan_carriere = PlanCarriere.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=plan_carriere.player.id)
        return reverse("playeur:details_personnage", kwargs={"pk": player.id})


class ArmeContactDelete(DeleteView):
    model = ArmeContact
    context_object_name = "arme_contact"
    template_name ='arme_contact/arme_contact_delete.html'
    
    def get_success_url(self):
        arme_contact = ArmeContact.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=arme_contact.player.id)
        return reverse("playeur:details_personnage", kwargs={"pk": player.id})


class ArmeDistanceDelete(DeleteView):
    model = ArmeDistance
    context_object_name = "arme_distance"
    template_name ='arme_distance/arme_distance_delete.html'
    
    def get_success_url(self):
        arme_distance = ArmeDistance.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=arme_distance.player.id)
        return reverse("playeur:details_personnage", kwargs={"pk": player.id})


class ArmureDelete(DeleteView):
    model = Armure
    context_object_name = "armure"
    template_name ='armure/armure_delete.html'
    
    def get_success_url(self):
        armure = Armure.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=armure.player.id)
        return reverse("playeur:details_personnage", kwargs={"pk": player.id})


class MontureDelete(DeleteView):
    model = Monture
    context_object_name = "monture"
    template_name ='monture/monture_delete.html'
    
    def get_success_url(self):
        monture = Monture.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=monture.player.id)
        return reverse("playeur:montures", kwargs={"pk": player.id})


class MagieDelete(DeleteView):
    model = Magie
    context_object_name = "sortilege"
    template_name ='magie/magie_delete.html'
    
    def get_success_url(self):
        magie = Magie.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=magie.player.id)
        return reverse("playeur:magie", kwargs={"pk": player.id})


class CompetenceDelete(DeleteView):
    model = Competence
    context_object_name = "competence"
    template_name ='competence/competence_delete.html'
    
    def get_success_url(self):
        competence = Competence.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=competence.player.id)
        return reverse("playeur:competences", kwargs={"pk": player.id})


class EquipementDelete(DeleteView):
    model = Equipement
    context_object_name = "equipement"
    template_name ='equipement/equipement_delete.html'
    
    def get_success_url(self):
        equipement = Equipement.objects.get(id=self.kwargs["pk"])
        player = Player.objects.get(id=equipement.player.id)
        return reverse("playeur:equipements", kwargs={"pk": player.id})