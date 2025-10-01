# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_affiliate_inventory.api.customization_api import CustomizationApi
    from wink_sdk_affiliate_inventory.api.embeddable_inventories_api import EmbeddableInventoriesApi
    from wink_sdk_affiliate_inventory.api.grids_api import GridsApi
    from wink_sdk_affiliate_inventory.api.inventory_links_api import InventoryLinksApi
    from wink_sdk_affiliate_inventory.api.items_api import ItemsApi
    from wink_sdk_affiliate_inventory.api.maps_api import MapsApi
    from wink_sdk_affiliate_inventory.api.ranked_grids_api import RankedGridsApi
    from wink_sdk_affiliate_inventory.api.supplier_links_api import SupplierLinksApi
    from wink_sdk_affiliate_inventory.api.syndicated_item_api import SyndicatedItemApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_affiliate_inventory.api.customization_api import CustomizationApi
from wink_sdk_affiliate_inventory.api.embeddable_inventories_api import EmbeddableInventoriesApi
from wink_sdk_affiliate_inventory.api.grids_api import GridsApi
from wink_sdk_affiliate_inventory.api.inventory_links_api import InventoryLinksApi
from wink_sdk_affiliate_inventory.api.items_api import ItemsApi
from wink_sdk_affiliate_inventory.api.maps_api import MapsApi
from wink_sdk_affiliate_inventory.api.ranked_grids_api import RankedGridsApi
from wink_sdk_affiliate_inventory.api.supplier_links_api import SupplierLinksApi
from wink_sdk_affiliate_inventory.api.syndicated_item_api import SyndicatedItemApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
