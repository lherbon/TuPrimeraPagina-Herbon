from django.shortcuts import render
from .forms import AuthorForm, CategoryForm, PostForm
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

def search(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(title__icontains=query)
    return render(request, 'blog/search.html', {'posts': posts, 'query': query})