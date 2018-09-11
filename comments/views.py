from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm


def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:detail', pk=post_pk)

        else:
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
            # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect('blog:detail', pk=post_pk)


def comic_comment(request, comic_pk):
    post = get_object_or_404(Post, pk=comic_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:comic', pk=comic_pk)

        else:
            comment_list = comic.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/comic.html', context=context)
            # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect('blog:comic', pk=comic_pk)


def poem_comment(request, poem_pk):
    post = get_object_or_404(Post, pk=poem_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:poem', pk=poem_pk)

        else:
            comment_list = poem.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/poem.html', context=context)
            # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect('blog:poem', pk=poem_pk)


def nature_comment(request, nature_pk):
    post = get_object_or_404(Post, pk=nature_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:nature', pk=nature_pk)

        else:
            comment_list = nature.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/nature.html', context=context)
            # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect('blog:nature', pk=nature_pk)


def funny_comment(request, funny_pk):
    post = get_object_or_404(Post, pk=funny_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:funny', pk=funny_pk)

        else:
            comment_list = funny.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/funny.html', context=context)
            # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect('blog:funny', pk=funny_pk)

