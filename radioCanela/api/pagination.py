from rest_framework import pagination

# Clase que sirve para la paginacion de los datos de los partidos
class PartidosPagination(pagination.PageNumberPagination):
    page_size_query_param = 'cantidad_partidos' # Parametro para indicar la cantidad de partidos
    page_query_param = 'pagina' # Parametro para indicar la pagina

class NoticiasPagination(pagination.PageNumberPagination):
    page_size_query_param = 'limite'
    page_query_param = 'pagina'

class EncuestaPagination(pagination.PageNumberPagination):
    '''
    Paginacion para las encuestas
    '''
    page_size_query_param = 'cantidad_encuestas'
    page_query_param = 'pagina'