from django.shortcuts import render
from .models import Enemy, Boss, NPC, Item, Weapon

# Create your views here.
def index(request):
    enemys = Enemy.objects.order_by('id')
    context = {'enemys' :enemys}

    return render(request, 'protoWiki11\index.html', context)

def AstelPage(request):    
    bosses = Boss.objects.order_by('id')
    context = {'bosses' :bosses}

    return render(request, 'protoWiki11\AstelPage.html', context)

def FirePotPage(request):
    items = Item.objects.order_by('id')
    context = {'items' :items}

    return render(request, 'protoWiki11\FirePotPage.html', context)

def MelinasPage(request):
    npces = NPC.objects.order_by('id')
    context = {'npces' :npces}

    return render(request, 'protoWiki11\MelinasPage.html', context)

def WeaponPage(request):
    weapons = Weapon.objects.order_by('id')
    context = {'weapons' :weapons}

    return render(request, 'protoWiki11\WeaponPage.html', context)



def header(request):
    return render(request, '\includes\header.html')