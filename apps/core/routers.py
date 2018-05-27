# Python imports


# Django imports


# Third party apps imports
from rest_framework.routers import DefaultRouter

# Local imports
from ..geolocation.routers import geolocalization
from ..tournament.routers import tournament

# Create your routers here.
routers_tuples = (geolocalization, tournament,)
routers_lists = sum(
    [list(router_tuple) for router_tuple in routers_tuples], [])

router = DefaultRouter()

for router_list in sorted(routers_lists):
    router.register(router_list[0], router_list[1], base_name=router_list[0])
