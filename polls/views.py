from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
import rsa

from .models import assinado
from .models import Question



def chaves(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/chaves.html', context)

def autenticar(request):
    return render(request, 'polls/autenticar.html')

def autenticarForm(request):
    mensagem = request.POST['myfile']
    mensagem_encoded = mensagem.encode('utf-8')
    chavePublicaPem = request.POST['chavePublica']
    assinaturaFile = request.POST['assinatura']

    with open('./chaves/'+chavePublicaPem, mode='rb') as privatefile:
        keydata = privatefile.read()
    rsaPublicKey = rsa.PublicKey.load_pkcs1(keydata)

    with open('./chaves/'+assinaturaFile, mode='rb') as ass:
        assinatura = ass.read()

    try:
        rsa.verify(mensagem_encoded, assinatura, rsaPublicKey)
    except:
        return HttpResponse("<html><body> <h1>Erro de Verificação!</h1> O documento foi <b>modificado</b> ou as chaves foram <b>alteradas.</b> <br><br> <button onclick=location.href="+"'/polls/';>Menu Principal</button> </body></html>")
    else:
        return HttpResponse("<html><body> <h1>Verificado!</h1> A assinatura do emissor é compatível! <br><br> <button onclick=location.href="+"'/polls/';>Menu Principal</button> </body></html>")

def assinar(request):
    (pubkey, privkey) = rsa.newkeys(512)

    f1 = open('./chaves/privkey.pem', 'wb')
    f1.write(privkey.save_pkcs1(format="PEM"))
    f1.close()

    f2 = open('./chaves/pubkey.pem', 'wb')
    f2.write(pubkey.save_pkcs1(format="PEM"))
    f2.close()

    return render(request, 'polls/assinar.html')

def assinarForm(request):
    mensagem = request.POST['myfile']
    mensagem_encoded = mensagem.encode('utf-8')
    chavePrivadaPem = request.POST['chavePrivada']

    with open('./chaves/'+chavePrivadaPem, mode='rb') as privatefile:
        keydata = privatefile.read()
    rsaPrivateKey = rsa.PrivateKey.load_pkcs1(keydata)

    hash = rsa.compute_hash(mensagem_encoded, 'SHA-256')
    signature = rsa.sign_hash(hash, rsaPrivateKey, 'SHA-256')
    
    f = open('./chaves/assinatura', 'wb')
    f.write(signature)
    f.close()
    
    html = "<html><body><h1>Assinado!</h1> <button onclick=location.href="+"'/polls/';>Menu Principal</button> </body></html>"
    return HttpResponse(html)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))