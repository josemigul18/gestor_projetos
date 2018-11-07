from django.urls import path
from .views import proj_new
from .views import proj_list
from .views import proj_detail
from .views import proj_edit
from .views import proj_delete
from .views import assignment_new
from .views import assignment_detail
from .views import programer_page
from .views import assignment_mark_finished_confirm

urlpatterns = [
    path('new/', proj_new, name="proj_new"),
    path('list/', proj_list, name="proj_list"),
    path('detail/<int:id>/', proj_detail, name="proj_detail"),
    path('edit/<int:id>/', proj_edit, name="proj_edit"),
    path('delete/<int:id>/', proj_delete, name="proj_delete"),
    path('assignment_new/<int:id>/', assignment_new, name="assignment_new"),
    path('assignment_detail/<int:id>/', assignment_detail, name="assignment_detail"),
    path('programer_page', programer_page, name="programer_page"),
    path('assignment_mark_finished_confirm/<int:id>/', assignment_mark_finished_confirm, name="assignment_mark_finished_confirm"),
]
