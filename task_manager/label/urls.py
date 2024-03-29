from django.urls import path
from task_manager.label import views


urlpatterns = [
    path('', views.LabelIndexView.as_view(), name='labels_index'),
    path('create/', views.LabelCreateView.as_view(), name='labels_create'),
    path('<int:pk>/update/', views.LabelUpdateView.as_view(), name='labels_update'),  # noqa: E501
    path('<int:pk>/delete/', views.LabelDeleteView.as_view(), name='labels_delete'),  # noqa: E501
]
