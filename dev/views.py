import time

from settings import PROJECT_ROOT
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.utils import simplejson
from django.utils.translation import ugettext as _

from dev.models import ACTION, ACTIONS

DESK = (
        ('foo', 'bar'),
        )

GAME = None

def game_init(request):
    global GAME
    GAME = ACTIONS()
    return HttpResponse(_('success'))

def play_page(request, role):
    ret = {'role':role, 'game':GAME}
    ret['cards'] = scan_cards()
    return render(request, 'player.html', ret)

def action(request): # ajax

    global GAME
    data = request.GET
    act = ACTION(data['player'], data['action'], data['card'])
    GAME.insert(act)
    return HttpResponse('success')

def status(request): # ajax
    data = request.GET
    status = data['status']
    ret = {'status':status,'actions':[]}
    for i in range(5):
        if int(status) != GAME.status:
            ret['status'] = GAME.status
            ret['actions'] = GAME.value[int(status):int(GAME.status)]
            return HttpResponse(simplejson.dumps(ret))
        time.sleep(1)
    return HttpResponse(simplejson.dumps(ret))

def hello_page(request):
    ret = {'info':'Hello! This is magic world!'}
    ret['desk'] = DESK
    ret['game'] = GAME
    return render(request, 'hello.html', ret)

def test(request):
    ret = {'info':'Hello! This is magic world!'}
    ret['cards'] = scan_cards()
    return render(request, 'dev.html', ret)

def scan_cards():
    import os
    path = '%s/media/cards' % PROJECT_ROOT
    jpgs = os.listdir(path)
    _ret = []
    for jpg in jpgs:
        _ret.append({'title': jpg.decode('utf8')[:-4],
                     'alt': jpg.decode('utf8')[:-4],
                     'link': 'cards' + '/' + jpg,
                     'min_link': 'cards' + '/' + jpg,
                     })
    return _ret

def css_test(request):
    ret = {} 
    return render(request, 'test-css.html', ret)
