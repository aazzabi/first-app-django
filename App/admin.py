from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib import messages

class MemberShipInline(admin.StackedInline):
    # fieldsets = (
    #     ('Membres', {
    #         'fileds': (('time_allocated_by_member'),)
    #     }),
    # )
    model= MembershipInProject
    extra = 0

class ListFilter(admin.SimpleListFilter):
    parameter_name = 'duree'
    title = 'Durée'

    def lookups(self, request, model_admin):
        return (
            ('2mois','Superieur a 1 mois'),
            ('1mois','Inférieur à 1 mois'),
        )


    def queryset(self, request, queryset):
        if self.value() == '2mois':
            return queryset.filter(duree_du_projet__gte= 30 ,duree_du_projet__lt=60 )
        elif self.value() == '1mois':
            return queryset.filter(duree_du_projet__lt=30)
        else:
            return queryset


class ProjetAdmin(admin.ModelAdmin):
   list_display = ('nom_du_projet' , 'duree_du_projet', 'description', 'est_valide', 'createur', 'superviseur', 'total_allocated_by_membres')
   actions = ['set_to_valid','set_to_invalid']
   list_filter = ['createur', 'est_valide', ListFilter]

   list_per_page = 2
   search_fields = ['nom_du_projet', 'createur__prenom']
   inlines = [MemberShipInline]

   fieldsets = (
       ('Etat', {'fields':('est_valide',)}),
       ('A propos',{
           'fields': ('nom_du_projet',
                      ('createur', 'superviseur'),
                      'besoins',
                      'description',),
       }),
       ('Durée', {
           'fields': (('duree_du_projet', 'temps_alloue_par_le_createur'),)
       }),
       # ('Membres ', {
       #     'fields' : ('membres')
       # })
   )
   def set_to_valid(self,request, queryset):
       queryset.update(est_valide = True)
       messages.info(request, 'Un projet(s) a été validée')
   set_to_valid.short_description = 'Validate'

   def set_to_invalid(self,request, queryset):
       no_valide = queryset.filter(est_valide= False)
       if (no_valide.count() > 0):
           row_updated = queryset.update(est_valide=False)
           messages.error(request, "{} projets no_valide= false".format(no_valide.count()))
       else:
           row_updated = queryset.update(est_valide=False)
           messages.info(request, "{} successfully marked as no valid".format(row_updated))
   set_to_invalid.short_description = 'Refuser'




admin.site.register(Student)
admin.site.register(Coach)
admin.site.register(Project, ProjetAdmin)