from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
import rsa


def chavesForm(request):
    username =  request.POST['username']
    (pubkey, privkey) = rsa.newkeys(512)

    import os
    try:
        os.mkdir('./chaves/'+username)
    except: 
        print('Diretório Já existe')
    finally:
        f1 = open('./chaves/'+username+'/privkey.pem', 'wb')
        f1.write(privkey.save_pkcs1(format="PEM"))
        f1.close()

        f2 = open('./chaves/'+username+'/pubkey.pem', 'wb')
        f2.write(pubkey.save_pkcs1(format="PEM"))
        f2.close()

        return HttpResponse("<html><body> Chaves Criadas no diretório <b>"+ username +"</b> <br><br> <button onclick=location.href="+"'/polls/';>Menu Principal</button> </body></html>")

def autenticarForm(request):
    mensagem = request.POST['myfile']
    mensagem_encoded = mensagem.encode('utf-8')
    chavePublicaPem = request.POST['chavePublica']
    assinaturaFile = request.POST['assinatura']
    usuario = request.POST['username']

    with open('./chaves/'+usuario+'/'+chavePublicaPem, mode='rb') as privatefile:
        keydata = privatefile.read()
    rsaPublicKey = rsa.PublicKey.load_pkcs1(keydata)

    with open('./chaves/'+usuario+'/'+assinaturaFile, mode='rb') as ass:
        assinatura = ass.read()

    try:
        rsa.verify(mensagem_encoded, assinatura, rsaPublicKey)
    except:
        return HttpResponse("<html><body> <h1>Erro de Verificação!</h1> O documento foi <b>modificado</b> ou as chaves foram <b>alteradas.</b> <br><br> <button onclick=location.href="+"'/polls/';>Menu Principal</button> </body></html>")
    else:
        return HttpResponse("<html><body> <h1>Verificado!</h1> A assinatura do emissor é compatível! <br><br> <button onclick=location.href="+"'/polls/';>Menu Principal</button> </body></html>")

def assinarForm(request):
    mensagem = request.POST['myfile']
    mensagem_encoded = mensagem.encode('utf-8')
    chavePrivadaPem = request.POST['chavePrivada']
    usuario = request.POST['username']

    with open('./chaves/'+usuario+'/'+chavePrivadaPem, mode='rb') as privatefile:
        keydata = privatefile.read()
    rsaPrivateKey = rsa.PrivateKey.load_pkcs1(keydata)

    hash = rsa.compute_hash(mensagem_encoded, 'SHA-256')
    print(hash)
    signature = rsa.sign_hash(hash, rsaPrivateKey, 'SHA-256')
    
    f = open('./chaves/'+ usuario +'/assinatura', 'wb')
    f.write(signature)
    f.close()
    
    html = "<html><body><h1>Assinado!</h1> <button onclick=location.href="+"'/polls/';>Menu Principal</button> </body></html>"
    return HttpResponse(html)

def index(request):
    return render(request, 'polls/index.html')
def chaves(request):
    return render(request, 'polls/chaves.html')
def autenticar(request):
    return render(request, 'polls/autenticar.html')
def assinar(request):
    return render(request, 'polls/assinar.html')