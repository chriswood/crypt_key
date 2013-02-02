from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def main(request):
    '''
        main page to enter a puzzle
    '''
    context_dict = {}    
    if request.method == 'POST':
        context_dict['rtype'] = 'Is POST'
    else:
        context_dict['rtype'] = 'NOT POST'

    context_dict['title'] = 'decrypting'
    return render_to_response('main.html',
                              context_dict,
                              context_instance=RequestContext(request))


