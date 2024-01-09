from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import Re_class

def search(request,s_val):
    mymembers = Member.objects.filter(name__icontains=s_val).values()
    all_class = Re_class.objects.all().values()
    template = loader.get_template('search.html')
    context={
        'mymembers':mymembers,
        's_val':s_val,
        'all_class':all_class,
    }
    return HttpResponse(template.render(context,request))

def all_class(request,id):
    mymembers = Member.objects.filter(class_val=id).values()
    re_class = Re_class.objects.get(id=id)
    all_class = Re_class.objects.all().values()
    template = loader.get_template('all_class.html')
    context={
        'mymembers':mymembers,
        're_class':re_class,
        'all_class':all_class,
    }
    return HttpResponse(template.render(context,request))

def members(request):
    mymembers = Member.objects.all().values()
    re_class = Re_class.objects.all().values()
    template = loader.get_template('members.html')
    all_class = Re_class.objects.all().values()
    context={
        'mymembers':mymembers,
        're_class':re_class,
        'all_class':all_class,
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('detail.html')
    all_class = Re_class.objects.all().values()
    context={
        'mymember':mymember,
        'Ingredients':mymember.Ingredients.split('-'),
        'all_class':all_class,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    
    mymembers = Member.objects.all().values()
    all_class = Re_class.objects.all().values()
    template = loader.get_template('main.html')
    context={
        'mymembers':mymembers,
        'all_class':all_class,
    }
    return HttpResponse(template.render(context,request))







    # template = loader.get_template('main.html')
    # return HttpResponse(template.render())