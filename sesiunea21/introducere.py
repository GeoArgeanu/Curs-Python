'''
API-urile sau interfete de programare a aplicatiilor (Aplication Programing Interfeace)
    permit aplicatiile softwear sa comunoce intre ele
    Actioneaza ca un mediator intre 2 aplicatii, permitand uneia sa solicite date sau
    servicii de la cealalta si sa primeasca raspuns in schimb
API-urile fac posibil ca aplicatiile sa accceseze functii sau date
    ale altor platforme deschizand posibilitati infine de inovare si intregare
'''

'''
REST -- REprezentation State Transfer
     Este un stil arhitectural pt furnizarea de standarde intre sisteme computerizate de pe web
     facilitand comunicarea intre ele 
     Sistemele compatibile REST, numite si RESTful, se caracterizeaza prin modul in care sunt
     indepedente si separa preocuparile clientului si ale serverului
     
Pt ca un API sa fie considerat RESTful trebuie sa respecte urm constrangeri:
   1-- arhitectura client-server: clientul si serverul sunt separate si actioneaza independent
   permitand utilizarea a diferite tehnologii pt fiecare
   
   2-- Statelass(fara stres): severul nu stocheaza nici un context pt client intre cereri
   astfel incat fiecare cerere contine toate informatiile necesare pt ao finaliza
   
   3-- Capacitate de cache: clientii pot stoca in cache datele de raspuns reducand numarul
   de solicitari catre server si astfel imbunatatind performanta

   4-- Utilizarea metodelor HTTP
   5-- Utilizarea codurilor de stare HTTP: API-urle  si RESTful folosesc 
   aceste coduri pt a indica starea rezultatului unei solicitari, cum ar fi 
   succes(200), esec(400) sau negasit(404)
   (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
'''

'''
METODELE HTTP sunt verde standard utilizate pt a indica actiunea dorita care trebuie exploatata
Cele 4 metode principale sunt:
1-- GET: preia date dintr-o resursa si este folosita pt citire
2-- POST; creaza o noua resursa si este folosita pt a trimite date catre un server
3-- PUT: actualizeaza o resursa curenta si este folosita pt a modifica datele existente
4-- DELETE: sterge o resursa  si este folosita pt a elimina date
'''