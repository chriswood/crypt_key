from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from crypt_key.utilities import CryptKeeper

@csrf_exempt  
def main(request):
    '''
        main page to enter a puzzle,
        also display any information and result
    '''
    context_dict = {}
    context_dict['debug'] = '' #TODO remove
     

    if request.method == 'POST':
        values = request.POST
        #This is the bare encrypted string
        crypt = CryptKeeper(values['enc_data'])

        context_dict['debug'] = "hey"
        context_dict['total'] = crypt.check_frequencies()
    context_dict['title'] = 'decrypting'

    return render_to_response('main.html',
                              context_dict,
                              context_instance=RequestContext(request))


