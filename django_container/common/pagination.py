from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class Pagination(PageNumberPagination):
    page_size_query_param = 'perpage'

    def get_paginated_response(self, data, meta=None):
        meta = {} if meta is None else meta
        meta['count'] = self.page.paginator.count
        meta['next'] = self.get_next_link()
        meta['previous'] = self.get_previous_link()

        return Response({
            'items': data,
            'meta': meta
        })
