
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views import View

from .models import *

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def home(request):
    return render(request, 'home.html')
def generate_pdf(request):
    # PDF faylini yaratish
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="categories.pdf"'

    # Canvas yaratish
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # PDF ga ma'lumot qo'shish
    p.drawString(100, height - 50, "Kategoriyalar ro'yxati:")
    
    # Kategoriyalarni olish
    categories = Category.objects.all()
    y_position = height - 100  # Boshlang'ich y pozitsiyasi

    for category in categories:
        p.drawString(100, y_position, f"ID: {category.id}, Nomi: {category.name}")
        y_position -= 20  # Har bir kategoriya uchun joy qoldirish

    # PDF ni saqlash
    p.showPage()
    p.save()
    return response


# def searchbar(request):
#     if request.metod=='GET':
#         query = request.GET.query('query')
#         if query:
#             category = Category.objects.filter(name__icontains=query)
#             return render(request, 'search.html', {'category':category})    
# class SearchView(View):
#     def get(self, request):
#         form = SearchForm()
#         result = []

#         if 'query' in request.GET:
#             form = SearchForm(request.GET)
#             if form.is_valid():
#                 query = form.cleaned_data['query']
#                 result = Category.objects.filter(name__icontains=query)
#         return render(request, 'search.html', {'form':form, 'result':result})        

class BasicView:
    def category(self):
        return Category.objects.all()
    def tag(self):
        return Tag.objects.all()

class Home(BasicView, View):
    def get(self,request):
        context = {}
        context['blogs'] = Blog.objects.order_by('-created_at')
        context['categories']= self.category()
        context['tags'] = self.tag()
        return render(request,'home.html',context)

class CategoryBlog(BasicView, View):
    def get(self, request, slug):
        context = {}
        category= Category.objects.get(slug=slug)
        context['blogs'] = Blog.objects.filter(category=category)
        context['category']=category
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return render(request, 'home.html', context)

class TagBlog(BasicView, View):
    def get(self, request, slug):
        context = {}
        tag = Tag.objects.get(slug=slug)
        context['blogs'] = Blog.objects.filter(tags=tag)
        context['tag'] = tag
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return render(request, 'home.html', context)



# def tag_blog(request,slug):
#     tag = Tag.objects.get(slug=slug)
#     blogs = Blog.objects.filter(tags=tag)
#     context = {
#         'tag' : tag,
#         'blogs' : blogs,
#     }
#     return render(request, 'blog.html', context)

class BlogDetail(BasicView,View):
    def get(self, request, slug):
        blog=Blog.objects.get(slug=slug)
        blog.views += 1
        blog.save()
        context = {
            'blog':blog,
            'categories':self.category(),
            'tags':self.tag()
        }
        return render(request,'blog_detail.html',context)

class CategoryList(BasicView, View):
    def get(self, request):
        context = {
            'categories':self.category(),
            'tags':self.tag(),
        }
        return render(request, "category_list.html",context)


def loyiha_list(request):
    form = Loyiha.objects.all()
    context = {
        'form':form,
    }
    
    return render(request, 'loyiha.html', context)
    


# class AddBlogView(BasicView, View):
#     def get(self, request):
#         context={
#             'categories':self.category(),
#             'tags':self.tag(),
#             'form':AddBlogForm(),
#         }
#         return render(request, 'add_blog.html', context)

#     def post(self, request):
#         form = AddBlogForm(request.POST, request.FILES)
#         if form.is_valid():
#             form_create = form.save(commit=False)
#             form_create.slug = slugify(form_create.title)
#             form_create.user = request.user
#             form_create.save()

#             blog = Blog.objects.get(id = form_create.id)
#             tags = form.cleaned_data['tags'].split(',')
#             for tag in tags:
#                 tag, created= Tag.objects.get_or_create(name=tag.strip())
#                 blog.tags.add(tag)
#             return redirect('home')



# def upload(request):
#     context = {
#         if request.method=='POST':
#             uploaded_file = request.FILES['document']
#             fs = FileSystemStorage()
#             name = fs.save(uploaded_file.name, uploaded_file)
#             context = ['url' = fs.url(name)]
#         return render(request, 'upload.html', context)    
#     }    

# class BookListView(ListView):
#     model = Blog
#     template_name = 'book_list.html'
#     context = 'blogs'

