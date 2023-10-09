from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response 
import json

@api_view(('POST',))
@renderer_classes(( JSONRenderer,))
def ProcessOrder(request):
    if request.method=='POST':
        mount=0
        orders=json.loads(request.body).get('orders')
        criterion=json.loads(request.body).get('criterion')
        
        for order in orders:
            if order['price']<=0:
                return Response('the price of object '+order['item']+' is a wrong value')
        
        
        if criterion =='all':
            for order in orders:
                object_price=0
                
                object_price=order['quantity']*order["price"]                

                mount+=object_price

            return Response(mount)
        if criterion not in  ['completed','canceled','pending']:
                    return Response('the criterion dont match......')
        
        
            
        
        
        for order in orders:
                object_price=0
                if order['status']==criterion:
                     object_price=order['quantity']*order["price"]                

                mount+=object_price
        

        return Response(mount)
    else:
      return Response('Must be a Post')

# Create your views here.
