from rest_framework.pagination import PageNumberPagination

class BookPagination(PageNumberPagination):
    page_size = 5  # Customize the number of books per page
    page_size_query_param = 'page_size'  # Allow dynamic page size
    max_page_size = 100  # Set a maximum limit to prevent excessive queries
