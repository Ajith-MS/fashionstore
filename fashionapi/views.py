from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from functools import reduce


class HelloWorldView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Hello World"})

class GoodMorningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Good Morning"})

class GoodEveningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Good Evening"})

class GoodNightView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Good Night"})

class Nameview(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"My Name is Ajith MS"})

class placeview(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"My place is in Varapuzha"})
class GreetingsView(APIView):
    def get(self,request,*args,**kwargs):
        cur_time=datetime.datetime.now()
        cur_hour=cur_time.hour
        msg=""
        if cur_hour<12:
            msg="Good Morning"
        elif cur_hour<18:
            msg="Good Afternoon"
        elif cur_hour<24:
            msg="Good Night"
        return Response({"data":msg})
class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        n=request.data.get("num")
        res=n**3
        return Response({"msg":res})

class FactorialView(APIView):
    def post(self,request,*args,**kwargs):
        n=request.data.get("num")
        # res=1
        # for i in range(1,n+1):
        #     res*=i
        res=reduce(lambda n1,n2:n1*n2,range(1,n+1))

        return Response({"msg":res})

class WordCountView(APIView):
    def post(self,request,*args,**kwargs):
        text=request.data.get("text")
        wc={}
        words=text.split(" ")
        for word in words:
            if word in wc:
                wc[word]+=1
            else:
                wc[word]=1
        return Response({"data":wc})