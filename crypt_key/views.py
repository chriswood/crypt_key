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
        #This is the bare encrypted string
        enc_data = decrypt(values['enc_data'])
        context_dict['debug'] = "debug: %s" % enc_data

    context_dict['title'] = 'decrypting'
    return render_to_response('main.html',
                              context_dict,
                              context_instance=RequestContext(request))


