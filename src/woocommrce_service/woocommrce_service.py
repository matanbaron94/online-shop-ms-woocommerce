from woocommerce import API
from datetime import datetime


class WooCommerceService:
    def __init__(self, url, consumer_key, consumer_secret,app_name, version="wc/v3", verify_ssl=True, ):
        self.app_name = app_name
        self.api = API(url=url, consumer_key=consumer_key, consumer_secret=consumer_secret, version=version, verify_ssl=verify_ssl)

    def get_products(self):
        response = self.api.get("products", params={"per_page": 30, "status": "publish",})
        shipping_methods = self.api.get("shipping/zones/1/locations", params={"per_page": 30}).json()
        print(shipping_methods)
        response = response.json()

        attributes = {}
        products = {}
        # ATTRIBUTES
        
        keys = response[0].keys()

        for key in keys:
            print(key, ": ", response[0][key])

        for product in response:


            for attribute in product['attributes']:
                attribute_id = self.app_name.lower().replace(" ", "_") + "_" +"attribute" + "_" + str(attribute['id'])
                attribute["id"] = attribute_id
                attribute["attribute_options"] = attribute['options']
                attribute["attribute_id"] = attribute_id
                attribute["filter_type"] = "listField"
                attribute["status"] = "public"
                attribute["created_at"] = datetime.now()
                attribute["source"] = self.app_name
                attribute["filter"] = {
                    "name": attribute['name'],
                    "label": attribute['name'],
                    "size": "small",
                    "value": [],
                    "select_type":"text",
                    "sortBy": "alphabetically",
                    "search": False,
                    "multiple": True,
                }
                del attribute['name']
                del attribute['options']
                del attribute['id']
                del attribute['position']
                del attribute['visible']
                del attribute['variation']

                if attribute_id not in attributes:
                    attributes[attribute_id] = attribute
                    attributes[attribute_id]['attribute_options'] = set(attribute['attribute_options'])
                else:
                    attributes[attribute_id]['attribute_options'].update(attribute['attribute_options'])

            # print(product.keys())
            # for brand in product['brands']:
            #     print(brand)

        # for key, value in attributes.items():
        #     print(key, value)


        # CATEGORIES




      

    def get_product(self, product_id):
        return self.api.get(f"products/{product_id}")

    # def create_product(self, product):