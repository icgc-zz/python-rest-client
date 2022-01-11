from delta_rest_client import DeltaRestClient
  
delta_client = DeltaRestClient(
    base_url='https://testnet-api.delta.exchange',
    api_key='UntpySbhUumFTxPr3pxFWJpkqm2fKq',
    api_secret='tDbzEaEX4C5VPYZWs5EDsCh4vJAjpo7r8ATsQvuMBItm0Dd3JV8b5U9e1836'
  )
orders = delta_client.get_live_orders()
print("Live orders: " , str(orders))
#delta_client.cancel_order(84, 42585917)
#orders = delta_client.get_live_orders()
#print("Live orders: " , str(orders))
delta_client.edit_order(84, 42585989,43002,2)
orders = delta_client.get_live_orders()
print("Live orders: " , str(orders))
