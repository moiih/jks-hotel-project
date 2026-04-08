from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm, ProfileCreationForm, BookingForm, PostForm
from .models import UserProfile, Booking, ChatRoom, PostModel
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def user_signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Account Created Successfully!!')
            return redirect('login')
    else:
        form = UserSignUpForm()

    context = { 'form': form, 'user': request.user }
    return render(request, 'jks/signup.html', context)




def user_login_index(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    # print('\n\nUser id :', request.user.id, end='\n\n\n')
                    # return redirect('index')
                    redirect_path = '/user_profile/' + str(request.user.id)
                    return redirect(redirect_path)

        else:
            form = AuthenticationForm()

        context = { 'form': form, 'user': request.user }
        return render(request, 'jks/login.html', context)

    else:
        return redirect('index')




def user_logout(request):
    logout(request)
    return redirect('index')




def index(request):
    return render(request, 'jks/index.html')



def team(request):

    prime = UserProfile.objects.filter(id__lt=300)
    print('\nPrime Members :', prime, end='\n\n')

    context = { 'p_user': prime }
    return render(request, 'jks/team.html', context)



def gallary(request):
    return render(request, 'jks/gallary.html')



def profile(request, id):
    if request.user.is_authenticated:

        print('\nUser ID (Profile)', request.user.id, end='\n\n')
        print('\nUser ID (type)', type(request.user.id), end='\n\n')
        # profile = UserProfile.objects.get(pk=request.user.id)

        if request.method == 'POST':
            if UserProfile.objects.filter(user_id__exact=request.user.id).exists():
                eprofile = UserProfile.objects.get(user_id__exact=request.user.id)
                profile_form = ProfileCreationForm(request.POST, request.FILES, instance = eprofile)
            else:
                profile_form = ProfileCreationForm(request.POST, request.FILES)
            post = PostForm(request.POST, request.FILES)

            if profile_form.is_valid():
                instance = profile_form.save(commit=False)
                instance.user = request.user
                instance.save()
                # profile = UserProfile.objects.get(pk=request.user.id)
                # messages.success(request, 'Your Profile Created Successfully...!!')
                # return redirect('profile')
                redirect_path = '/user_profile/' + str(request.user.id)
                return redirect(redirect_path)

            if post.is_valid():
                prof = UserProfile.objects.get(user_id=request.user.id)

                pst = post.save(commit=False)
                pst.profile = prof
                pst.save()
                # post.save()
                # return redirect('profile')
                redirect_path = '/user_profile/' + str(request.user.id)
                return redirect(redirect_path)

        else:
            if UserProfile.objects.filter(user_id__exact=request.user.id).exists():
                eprofile = UserProfile.objects.get(user_id__exact=request.user.id)
                profile_form = ProfileCreationForm(instance = eprofile)
            else:
                profile_form = ProfileCreationForm()
            post = PostForm()

        if UserProfile.objects.filter(user_id__exact=request.user.id).exists():
            postm = PostModel.objects.all()

            profile = UserProfile.objects.filter(user_id__exact=id)
            print('\nProfile Object :', profile, end='\n')

            context = { 'pform': profile_form, 'profile': profile, 'postm': postm, 'post': post, 'friend_id': id }
        else:
            context = { 'pform': profile_form, 'post': post }

        return render(request, 'jks/profile.html', context)

    else:
        return redirect('index')
        # return redirect('profile')




def booking(request):
    print('\n\nBooking :', request.user.id, end='\n\n\n')
    if request.user.is_authenticated:
        print('\n\nBooking (Auth) :', request.user.id, end='\n\n\n')
        if request.method == 'POST':
            print('\n\nBooking (POST) :', request.user.id, end='\n\n\n')
            booking_form = BookingForm(request.POST)
            if booking_form.is_valid():
                print('\n\nBooking (IsValid) :', request.user.id, end='\n\n\n')
                book = booking_form.save(commit=False)
                book.user = request.user
                book.save()
                return redirect('index')

        else:
            booking_form = BookingForm()

        context = { 'book': booking_form }
        return render(request, 'jks/booking_form.html', context)

    else:
        return redirect('login')




# @csrf_exempt
def contact(request):
    if request.user.is_authenticated:

        user_profile = UserProfile.objects.all()
        message = ChatRoom.objects.all()
        context = { 'msg': message, 'user': user_profile, 'curr_user': request.user.id }
        # context = { 'msg': message, 'curr_user': request.user.id }

        if request.method == 'POST':
            msg = request.POST.get('message')
            chat = ChatRoom()
            chat.message = msg
            chat.user = request.user
            chat.save()
            message = ChatRoom.objects.all()  ## For passing in context

            message = ChatRoom.objects.values()  ##  ( !Important: Must to use [Model.objects.values()] for sending in AJAX ) For sending data to AJAX
            print(message)
            message_list = list(message)

            return JsonResponse({ 'status': 'Message Accepted', 'chat': message_list })

        else:
            return render(request, 'jks/contact_us.html', context)
            return JsonResponse({ 'status': '0' })

        # context = { 'msg': message }
        # return render(request, 'jks/contact_us.html', context)

    else:
        return render(request, 'jks/contact_us.html')




def about(request):
    if request.user.is_authenticated:

        postm = PostModel.objects.all()

        if request.method == 'POST':

            post = PostForm(request.POST, request.FILES)

            if post.is_valid():
                prof = UserProfile.objects.get(user_id=request.user.id)

                pst = post.save(commit=False)
                pst.profile = prof
                pst.save()
                # post.save()
                return redirect('about')

        else:
            post = PostForm()

        context = { 'post': post, 'postm': postm }
        return render(request, 'jks/about_us.html', context)

    else:
        return render(request, 'jks/about_us.html')




def delete_post(request, id):
    if request.user.is_authenticated:

        post = PostModel.objects.get(pk=id)
        post.delete()

        return redirect('about')

    else:
        return render(request, 'jks/about_us.html')



def search(request):
    if request.user.is_authenticated:

        if request.method == 'GET':

            msearch = request.GET.get('psearch')
            # print('\n\n\tString :', search, end='\n\n')
            members = UserProfile.objects.all().filter(name__icontains=msearch) ## "__icontains" is called the "Lookup" which filter the results by removing Case-Sensitivity.

        context = { 'members': members, 'search': search }
        return render(request, 'jks/index.html', context)

    else:
        return redirect('login')