from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import users,blogs

#url:social/post/{pid}
#method:post
class PostView(APIView):
    def get(self,request,*args,**kwargs):
        if "limit" in request.query_params:
            limit=int(request.query_params.get("limit"))
            data=blogs[0:limit]
            return Response(data=data)

        elif "liked_by" in request.query_params:
            id=int(request.query_params.get("liked_by"))
            liked_post=[blog for blog in blogs if id in blog["liked_by"]]
            return Response(data=liked_post)
        else:
            return Response(data=blogs)

    def post(self,request,*args,**kwargs):
        blog=request.data
        blogs.append(blog)
        return Response(data=blog)


#url: social/post/{pid}
#method:get
class PostDetailView(APIView):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        blog=[blg for blg in blogs if blg["postId"]==pid].pop()
        return Response(data=blog)

    def delete(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        blog=[blg for blg in blogs if blg["postId"]==pid].pop()
        blogs.remove(blog)
        return Response(data=blog)

    def put(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        blog=[blg for blg in blogs if blg["postId"]==pid].pop()
        blog.update(request.data)
        return Response(data=blog)

#url:social/posts/likes/<int:pid>/
#method:post
#data:{userid:1}
class AddLikeView(APIView):
    def post(self,request,*args,**kwargs):
        postid=kwargs.get("pid")
        blog=[blg for blg in blogs if blg["postId"]==postid].pop()
        user=request.data.get("userid")
        blog["liked_by"].append(user)
        return Response(data=blog)


