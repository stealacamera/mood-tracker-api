from rest_framework.pagination import LimitOffsetPagination

class MoodEntryPagination(LimitOffsetPagination):
    page_size = 25
    max_page_size = 100