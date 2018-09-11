import markdown
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from comments.forms import CommentForm

# Create your views here.
def index(request):
	post_list = Post.objects.all().order_by('-created_time')
	return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post_list = Post.objects.all().filter(category_id=1).exclude(id__in=pk).order_by('-created_time')
    # post_list = Post.objects.filter(category=category_pk).order_by('-created_time')
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
		extensions=[
		             'markdown.extensions.extra',
                     'markdown.extensions.codehilite',
                     'markdown.extensions.toc',
                   ])

    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
               'post': post,
               'post_list': post_list,
               'form': form,
               'comment_list': comment_list
              }
    return render(request, 'blog/detail.html', context=context)


def comic(request, pk):
    comic_list = Post.objects.all().filter(category_id=2).exclude(id__in=pk).order_by('-created_time')
    comic = get_object_or_404(Post, pk=pk)
    comic.body = markdown.markdown(comic.body,
        extensions=[
                     'markdown.extensions.extra',
                     'markdown.extensions.codehilite',
                     'markdown.extensions.toc',
                   ])

    form = CommentForm()
    comment_list = comic.comment_set.all()
    context = {
               'comic': comic,
               'comic_list': comic_list,
               'form': form,
               'comment_list': comment_list
              }
    return render(request, 'blog/comic.html', context=context)


def poem(request, pk):
    poem_list = Post.objects.all().filter(category_id=3).exclude(id__in=pk).order_by('-created_time')
    poem = get_object_or_404(Post, pk=pk)
    poem.body = markdown.markdown(poem.body,
        extensions=[
                     'markdown.extensions.extra',
                     'markdown.extensions.codehilite',
                     'markdown.extensions.toc',
                   ])

    form = CommentForm()
    comment_list = poem.comment_set.all()
    context = {
               'poem': poem,
               'poem_list': poem_list,
               'form': form,
               'comment_list': comment_list
              }
    return render(request, 'blog/poem.html', context=context)


def nature(request, pk):
    nature_list = Post.objects.all().filter(category_id=4).exclude(id__in=pk).order_by('-created_time')
    nature = get_object_or_404(Post, pk=pk)
    nature.body = markdown.markdown(nature.body,
        extensions=[
                     'markdown.extensions.extra',
                     'markdown.extensions.codehilite',
                     'markdown.extensions.toc',
                   ])

    form = CommentForm()
    comment_list = nature.comment_set.all()
    context = {
               'nature': nature,
               'nature_list': nature_list,
               'form': form,
               'comment_list': comment_list
              }
    return render(request, 'blog/nature.html', context=context)


def funny(request, pk):
    funny_list = Post.objects.all().filter(category_id=5).exclude(id__in=pk).order_by('-created_time')
    funny = get_object_or_404(Post, pk=pk)
    funny.body = markdown.markdown(funny.body,
        extensions=[
                     'markdown.extensions.extra',
                     'markdown.extensions.codehilite',
                     'markdown.extensions.toc',
                   ])

    form = CommentForm()
    comment_list = funny.comment_set.all()
    context = {
               'funny': funny,
               'funny_list': funny_list,
               'form': form,
               'comment_list': comment_list
              }
    return render(request, 'blog/funny.html', context=context)

