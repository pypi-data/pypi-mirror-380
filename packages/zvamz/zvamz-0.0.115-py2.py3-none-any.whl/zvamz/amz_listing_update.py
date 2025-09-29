import requests
from datetime import datetime, timezone, timedelta
import json
from .api import get_sellerId

def get_productType(marketplace_func, access_token, sellerId, sku):
    # get productType
    print('Getting product type...')
    try:
        region_url, marketplace = marketplace_func()
        endpoint = f"/listings/2021-08-01/items/{sellerId}/{sku}?marketplaceIds={marketplace}&includedData=summaries"
        url = region_url + endpoint

        headers = {
            "accept": "application/json",
            "x-amz-access-token": access_token
            }
        response = requests.get(url, headers=headers)
        productType = response.json()['summaries'][0]['productType']
        print(f'SKU product type is: {productType}')
        return productType
    except KeyError as e:
        raise ValueError(f'❌ Error getting product type: {e}')
    
def update_sale_price(marketplace_func, access_token, sku, salePrice):
    # get sellerId
    print('Getting seller ID...')
    try:
        sellerId = get_sellerId(marketplace_func, access_token, sku)
    except KeyError as e:
        raise ValueError(f'❌ Error getting seller ID: {e}')

    # get productType
    productType = get_productType(marketplace_func, access_token, sellerId, sku)

    # set sale dates
    start_date = datetime.now(timezone.utc).isoformat()
    end_date = (datetime.now(timezone.utc) + timedelta(days=365)).isoformat()

    # update sale price
    region_url, marketplaceId = marketplace_func()
    endpoint = f"/listings/2021-08-01/items/{sellerId}/{sku}?marketplaceIds={marketplaceId}&includedData=issues"
    url = region_url + endpoint

    payload = {
        "patches": [
            {
                "op": "replace",
                "path": "/attributes/purchasable_offer",
                "value": [
                    {
                        "discounted_price": [
                            {
                                "schedule": [
                                    {
                                      "end_at": f"{end_date}",
                                      "start_at": f"{start_date}",
                                      "value_with_tax": salePrice
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        "productType": f"{productType}"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-amz-access-token": access_token
    }

    response = requests.patch(url, json=payload, headers=headers)
    if response.status_code == 200:
        return print(f"✅ Success: {json.dumps(response.json(), indent=4)}")
    else:
        raise ValueError(f"❌ Error: {json.dumps(response.json(), indent=4)}")
    
