from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def test(request):
    ret = {'info':'Hello, This is magic world!'}
    ret['cards'] = scan_cards()
    return render_to_response('dev.html', ret, context_instance=RequestContext(request))

def scan_cards():
    import os
    path = '/home/huangkun/celtics/magics/dev/cards'
    jpgs = os.listdir(path)
    _ret = []
    for jpg in jpgs:
        _ret.append({'title': jpg.decode('utf8')[:-4],
                     'alt': 'Img loading...',
                     'link': path + '/' + jpg,
                     'min_link': path + '/' + jpg,
                     })
    return _ret

def media(request, x):
    return x
