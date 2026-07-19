from django.urls import path
from booking import views

urlpatterns = [
    path('events/', views.events_list_view, name='events-list'),
    path('event/detail/<int:pk>/', views.event_detail_view, name='event-detail'),
    path('event/create/', views.event_create_view, name='event-create'),
    path('event/update/<int:pk>/', views.event_update_view, name='event-update'),
    path('event/delete/<int:pk>/', views.event_delete_view, name='event-delete'),
    path('tickets/', views.tickets_list_view, name='tickets-list'),
    path('ticket/create/', views.ticket_create_view, name='ticket-create'),
    path('ticket/update/<int:pk>/', views.ticket_update_view, name='ticket-update'),
    path('ticket/delete/<int:pk>/', views.ticket_delete_view, name='ticket-delete'),
]