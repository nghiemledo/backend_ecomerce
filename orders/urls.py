from django.urls import path
from orders import views

urlpatterns = [
    path("orders/", views.OrderAPIView.as_view()),
    path("orders/<int:id>/", views.OrderDetailAPIView.as_view()),
    path("orders/<int:order_id>/detail/", views.OrderDetailWithProductAPIView.as_view()),
    path("orders/<slug:order_id_slug>/detail/<slug:id_slug>/", views.OrderDetailWithProductDetailAPIView.as_view()),
]
