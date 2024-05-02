from rest_framework.pagination import PageNumberPagination

class ProductCreatePagination(PageNumberPagination):
    page_size = 4