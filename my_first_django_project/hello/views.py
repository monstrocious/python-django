
# Create your views here.

import textwrap

from django.http import HttpResponse
from django.views.generic.base import View


class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Greetings to the world</h1>
                <p>Hello, world!</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)
        
        
        
class SecondPageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>This is page number 2!</title>
            </head>
            <body>
                <h1>This is Page number 2!!!</h1>
                <p>Hello, world page 2!</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)