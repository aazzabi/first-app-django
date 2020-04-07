from django.urls import  path
from . import views

urlpatterns= [
    path('affiche', views.Affiche),
    path('projects/', views.AllProject , name='project_index'),
    path('projects/<int:id>', views.Detail , name='project_detail'),
    path('projects/new', views.AddProject , name='project_add'),
    path('projects/edit/<int:id>', views.EditProject , name='project_edit'),
    path('projects/delete/<int:id>', views.DeleteProject , name='project_delete'),
]