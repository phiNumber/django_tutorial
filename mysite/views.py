from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hello(request):
    addr = request.META['REMOTE_ADDR']
    return HttpResponse("Your IP is %s" % addr)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})
#    t = get_template('current_datetime.html')
#    html = t.render(Context({'current_date': now}))
#    html = "<html><body>It is now %s.</body></html>" % now
#    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

