from django.shortcuts import render_to_response
from django.template import RequestContext
    
def main(request, action=None):
    '''
    Process the requests for updating values in the puzzle, and generating
    new puzzles (coming soon).
    I hardcoded 9x9, but all code in this program is flexible
    for any dimension, providing it is a square. So we should be able to
    handle different puzzle square type games just by writing a new solver.
    '''
    context_dict = {}
    context_dict['title'] = 'decrypting'
    return render_to_response('main.html',
                              context_dict,
                              context_instance=RequestContext(request))
