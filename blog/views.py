import markdown
from django.shortcuts import render, get_object_or_404
# from comments.forms import CommentForm
from comments.forms import CommentForm
from .models import Post

# Create your views here.
def index(request):
	post_list = Post.objects.all().order_by('-created_time')
	return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
	post_list = Post.objects.all().exclude(id__in=pk).order_by('-created_time')
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