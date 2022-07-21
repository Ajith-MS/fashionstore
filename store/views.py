from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from store.models import products

class ProductView(APIView):
    def get(self,request,*args,**kwargs):
        return Response(data=products)

    def post(self,request,*args,**kwargs):
        prdt=request.data
        products.append(prdt)
        return Response(data=prdt)

class ProductDetailView(APIView):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        product=[pro for pro in products if pro["id"]==pid].pop()
        return Response(data=product)

    def delete(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        product=[pro for pro in products if pro["id"]==pid].pop()
        products["id"].remove(product)
        return Response(data=product)

    def put(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        product=[pro for pro in products if pro["id"]==pid].pop()
        product.update(request.data)
        return Response(data=product)
