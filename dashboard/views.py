from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django import template
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import *
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


def is_superuser(user):
    return user.is_superuser

### home ##
def index(request):
    project = Category.objects.all().count()
    product = Image.objects.all().count()
    if request.user.is_authenticated:
        user = request.user.username #.id
        context = {'project':project,'images':product}
        return render(request, 'index.html', context)
    else:
        return HttpResponseRedirect('/dashboard/login')

####### category ######
@user_passes_test(lambda u: u.is_superuser)
def category(request):
    category = Category.objects.all()
    ##
    context = {'category':category}
    return render(request, 'dashboard/category.html', context)
####
@login_required(login_url="/dashboard/")
def category_add(request):
    #formm = Category.objects.get(id=id)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f' لقد تم حفظ التعديل بنجاح') 

            return HttpResponseRedirect('/dashboard/category') 
    else:
        form = CategoryForm()
    context={
        'form':form,
    
    }
    return render(request, 'dashboard/category_add.html', context)
#
@user_passes_test(lambda u: u.is_superuser)
def category_edite(request, id ):
    formm = Category.objects.get(id=id)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=formm)
        if form.is_valid():
            form.save()
            messages.success(request, f' لقد تم حفظ التعديل بنجاح')
            return HttpResponseRedirect('/dashboard/category')
    else:
        form = CategoryForm(instance=formm)
    context={
        'form':form,
    }
    return render(request, 'dashboard/category_edite.html', context)
##
@login_required(login_url="/dashboard/")
def category_delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    messages.success(request, f"  تم الحذف بنجاح")
    return redirect(reverse('dashboard:category'))


##### page ###
@user_passes_test(lambda u: u.is_superuser)
def page(request):
    post = Pages.objects.all()
    context = {'post':post,}
    return render(request, 'dashboard/page.html', context)

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Pages
    template_name = 'dashboard/page_add.html'
    form_class = PagesForm
    post_slug = None

    def form_valid(self, form):
        form_2 = form.save(commit=False)
        form_2.save()
        messages.success(self.request, f'"{form.instance.name}" has been created successfully')
            
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('page')


@user_passes_test(lambda u: u.is_superuser)
def page_edite(request, id ):
    formm = Pages.objects.get(id=id)
    if request.method == "POST":
        form = PagesForm(request.POST, request.FILES, instance=formm)
        if form.is_valid():
            form.save()
            messages.success(request, f' لقد تم حفظ التعديل بنجاح')
            return HttpResponseRedirect('/dashboard/post')
    else:
        form = PagesForm(instance=formm)
    context={
        'form':form,
    }
    return render(request, 'dashboard/page_edite.html', context)

#@login_required(login_url="/dashboard/")
#def page_delete(request, id):
  #  product = Post.objects.get(id=id)
  #  product.delete()
 #   messages.success(request, f"  تم الحذف بنجاح")
  #  return redirect(reverse('dashboard:page'))

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Pages
    template_name = 'dashboard/confirm_delete3.html'
    success_url = reverse_lazy('dashboard:page')     
  
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, f'"{self.get_object()}"  تم الحذف بنجاح')
        return super().delete(request, *args, **kwargs)

###### edite_informaion ###
@user_passes_test(lambda u: u.is_superuser)
def page_about(request):

    form_id = PageAbout.objects.first()
    if request.method == 'POST':
        form_infor = PageAboutForm(request.POST, instance=form_id)
        if form_infor.is_valid():
            form_infor.save()
            messages.success(request, f"تم التعديل  بنجاح")
    else:
        form_infor = PageAboutForm(instance=form_id)

    context = {
        'form':form_infor,}
    return render(request, 'dashboard/page_about.html', context)







######### gallery ####


@user_passes_test(lambda u: u.is_superuser)
def gallery(request):
    categories = Category.objects.all()

    selected_category = request.GET.get('category', None)
    images = Image.objects.all()  # Get all images initially

    if selected_category:
        images = Image.filter(category__name=selected_category)


    
    if request.method == 'POST':
        form= PhotosForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            messages.success(request, f"تم الاضافة  بنجاح")
            return redirect(reverse('dashboard:gallery'))
    else:
        form = PhotosForm()
        print('hhhh')

    context = { 'images':images  ,'categories':categories,'form':form }
    return render(request, 'dashboard/gallery.html', context )

@user_passes_test(lambda u: u.is_superuser)
def delete(request):
    # Get the list of selected images
    selected_images = request.POST.getlist("images[]")

    # Delete the selected images
    if request.method == 'POST':

        for image_id in selected_images:
            image = Image.objects.get(id=image_id)
            #image.is_deleted = True
            image.delete()
        messages.success(request, f"تم الحذف بنجاح")


        return redirect(reverse('dashboard:gallery'))


#### auth_logout ######
@user_passes_test(lambda u: u.is_superuser)
def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/dashboard/login')

##### profile #####
@user_passes_test(lambda u: u.is_superuser)
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='dashboard:profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

###### edite_informaion ###
@user_passes_test(lambda u: u.is_superuser)
def edite_informaion(request):

    form_id = InformaionSite.objects.first()
    if request.method == 'POST':
        form_infor = InformaionSiteForm(request.POST,request.FILES, instance=form_id)
        if form_infor.is_valid():
            form_infor.save()
            messages.success(request, f"تم التعديل  بنجاح")
    else:
        form_infor = InformaionSiteForm(instance=form_id)



    context = {
        'form':form_infor,
    }

    return render(request, 'dashboard/edit_information.html', context)


## user ##
@method_decorator(user_passes_test(is_superuser), name="dispatch")
class ADeleteUser(SuccessMessageMixin, DeleteView):
    model = User
    template_name='dashboard/confirm_delete3.html'
    success_url = reverse_lazy('dashboard:aluser')
    success_message = "Data successfully deleted"
##
@method_decorator(user_passes_test(is_superuser, login_url="/dashboard/"), name="dispatch")
class AEditUser(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'dashboard/edit_user.html'
    success_url = reverse_lazy('dashboard:aluser')
    success_message = "Data successfully updated"

##
@user_passes_test(lambda u: u.is_superuser)
def user_show(request):
    users = User.objects.all()
    if request.method == "POST":
        active = request.POST.get('active')
        if active == '1':
            active = True
        else:
            active = False
        user_id= title = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        user.is_staff =  active
        user.is_active = active
        user.is_superuser = active
        user.save()
    context = { 'users': users }
    return render(request, 'dashboard/list_users.html', context)

####
@method_decorator(user_passes_test(is_superuser, login_url="/dashboard/"), name="dispatch")
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')

####
@method_decorator(user_passes_test(is_superuser, login_url="/dashboard/"), name="dispatch")
class ALViewUser(DetailView):
    model = User
    template_name='dashboard/user_detail.html'

@user_passes_test(lambda u: u.is_superuser)
def create_user(request):
    msg = None
    success = False
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            messages.success(request, f'نجحت إضافة المستخدم')
            success = True
            return redirect("/dashboard/aluser")
    else:
        form = CreateUserForm()
    return render(request, "dashboard/add_user.html", {"form": form, "msg": msg, "success": success})
    