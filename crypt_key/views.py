from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from crypt_key.utilities import decrypt

@csrf_exempt  
def main(request):
    '''
        main page to enter a puzzle
    '''
    context_dict = {}
    context_dict['debug'] = '' #TODO remove

    if request.method == 'POST':
        values = request.POST
        enc_data = values['enc_data']
        enc_data = decrypt(enc_data)
        context_dict['debug'] = "debug: %s" % enc_data
    else:
        context_dict['rtype'] = 'NOT POST'

    context_dict['title'] = 'decrypting'
    return render_to_response('main.html',
                              context_dict,
                              context_instance=RequestContext(request))


