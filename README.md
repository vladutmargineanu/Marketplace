# Marketplace
Homework for the Computing Systems Architecture course @ ACS, UPB 2020

Tema 1 - Marketplace
Deadline soft: 5 aprilie 2020, ora 23:55. Primiți un bonus de 10% pentru trimiterea temei cu 3 zile înaintea acestui termen, adică înainte de 2 aprilie 2020, ora 23:55.
Deadline hard: 12 aprilie 2020, ora 23:55. Veți primi o depunctare de 10% din punctajul maxim al temei pentru fiecare zi de întârziere, până la maxim 7 zile, adică până pe 12 aprilie 2020, ora 23:55.
Responsabili: Luca Istrate, Adriana Drăghici, Loredana Soare, Alexandru Georgescu
Obiective
Utilizarea eficientă a elementelor de sincronizare studiate la laborator
Implementarea unei aplicații concurente utilizând o problemă clasică (Multi Producer, Multi Consumer)
Aprofundarea anumitor elemente din Python (clase, elemente de sintaxă, thread-uri, sincronizare, precum și folosirea modulelor Python pentru lucrul cu thread-uri)
Descriere
În cadrul acestei teme veți avea de implementat un Marketplace prin intermediul căruia mai mulți producători își vor oferi produsele spre vânzare, iar mai mulți cumpărători vor achiziționa produsele puse la dispoziție.

Marketplace:

Marketplace-ul este unul destul de simplu, cu două tipuri de produse (ceai și cafea) ce vor fi comercializate de către producători. Acesta va fi intermediarul dintre producători și consumatori, prin el realizându-se achiziția de produse: producătorul (producer) va produce o anumită cantitate de produse de un anumit tip / mai multe tipuri cumpărătorul (consumer) va cumpăra o anumită cantitate de produse de un tip / de mai multe tipuri. De asemenea, Marketplace-ul va pune la dispoziția fiecărui cumpărător câte un coș de produse (cart) (acesta va fi folosit pentru rezervarea produselor care se doresc a fi cumpărate).

Producător:

Vor exista mai mulți producători ce vor produce obiectele de tip cafea / ceai. Fiecare produs va fi furnizat într-o anumită cantitate. Un producător poate produce atât obiecte de tip cafea, cât și de tip ceai.

Consumator:

În momentul în care un client își dorește să cumpere anumite produse dintr-un magazin, acesta va avea nevoie de un coș de cumpărături pe care să îl folosească în scopul rezervării acestora. Astfel, de fiecare dată când un client își începe cumpărăturile, acesta va primi din partea Marketplace-ului un coș de cumpărături, căruia îi va fi asociat un id. Clientul poate:

adăuga produse în coș ⇒ produsele respective devin indisponibile pentru ceilalți clienți
șterge produse din coș ⇒ produsele respective devin disponibile pentru ceilalți clienți
plasa o comandă
Descrierea implementării
Marketplace-ul ce va trebui implementat va simula problema Multi Producer Multi Consumer (MPMC). Pentru rezolvarea acestei teme va trebui să completați clasele Marketplace, Producer, și Consumer (clase ce vor fi documentate în schelet) cu o implementare corectă a metodelor deja definite.

Rezolvarea temei va fi concentrată preponderent pe metodele clasei Marketplace, metode ce vor fi apelate atât de producător, cât și de cumpărător în clasele aferente ale acestora.

Operația efectuată de către producător este cea de publicare a produselor sale. Implementarea metodei publish va fi făcută în clasa Marketplace.

Vor exista doua tipuri de operații pe care clientul le poate efectua asupra coșului de cumpărături:

add_to_cart ⇒ adaugă produse într-o anumită cantitate în coș
remove_from_cart ⇒ șterge din coș o anumită cantitate de produse
Ambele metode (add_to_cart și remove_from_cart) vor trebui implementate în clasa Marketplace.

În momentul în care un consumator adaugă un produs în coșul pentru cumpărături, produsul respectiv va deveni indisponibil pentru ceilalți clienți ai Marketplace-ului. Clientul își va putea plasa comanda prin apelarea metodei place_order (din clasa Marketplace).

Funcționalitatea clasei Producer este să:

furnizeze produselor pe care producătorul le pune la dispoziție
Funcționalitatea clasei Consumer este să:

primească id-ului coșului de cumpărături
adauge / elimine din coșul de cumpărături anumite cantități de produse
plaseze comenzi
Modulul Product conține reprezentările claselor Coffee și Tea.

Marketplace-ul limitează numărul de produse ce pot fi publicate de către un producător. În momentul în care s-a atins limita, producătorul nu mai poate publica altele până nu sunt cumpărate. El va reîncerca să publice după un timp definit în fișierul de test.

Dacă un cumpărător nu găsește un produs în marketplace, el va încerca mai târziu, după un timp definit în fișierul de test.

Formatul Testelor
Testarea se va face cu ajutorul a două tipuri de fișiere, cele de input și cele de output ({id}.in și {id}.out), primul fiind în format JSON. Fișierul {id}.in va reprezenta fișierul de intrare și va conține configurările necesare pentru fiecare clasă în parte, iar fișierul {id}.out va reprezenta fișierul de ieșire prin intermediul căruia se va verifica corectitudinea implementării temei.

Fișierele de input vor fi fișiere JSON ce vor conține următoarele chei:

marketplace
products
producers
consumers
Exemplu conținut fișier de intrare și fișierul corespunzător de ieșire:

Click pentru exemplu 

Atât conținutul fișierului de intrare, cât și conținutul fișierului de ieșire sunt descrise în README-ul aferent al temei pus la dispoziție.
Pentru a putea compara fișierele de ieșire obținute de voi cu cele de referința, scriptul de testare va ordona output-ul rezultat, întrucât avem de-a face cu multithreading.

Notare
Tema va fi verificată automat, folosind infrastructura de testare, pe baza unor teste definite în directorul tests.
Tema se va implementa Python>=3.7. Arhiva temei (fişier .zip) va fi uploadată pe site-ul cursului şi trebuie să conţină:

fişierele marketplace.py, producer.py, consumer.py cu implementarea entităților temei
alte surse .py folosite de soluţia voastră (nu includeţi fişierele infrastructurii de testare)
fişierul README cu detaliile implementării temei (poate fi în engleză)
Notarea va consta în 100 pct acordate egale între teste. Depunctări posibile sunt:

folosirea incorectă a variabilelor de sincronizare (ex: lock care nu protejează toate accesele la o variabilă partajată, notificări care se pot pierde) (-2 pct)
prezența print-urilor de debug (maxim -10 pct în funcție de gravitate)
folosirea lock-urilor globale (-10 pct)
folosirea variabilelor globale/statice (-5 pct)
Variabilele statice pot fi folosite doar pentru constante
folosirea inutilă a variabilelor de sincronizare (ex: se protejează operații care sunt deja thread-safe) (-5 pct)
alte ineficiențe (ex: creare obiecte inutile, alocare obiecte mai mari decât e necesar, etc.) (-5 pct)
lipsa organizării codului, implementare încâlcită și nemodulară, cod duplicat, funcții foarte lungi (între -1pct și -5 pct în funcție de gravitate)
cod înghesuit/ilizibil, inconsistenţa stilului - vedeți secțiunea Pylint
pentru code-style recomandăm ghidul oficial PEP-8
cod comentat/nefolosit (-1 pct)
lipsa comentariilor utile din cod (-5 pct)
fişier README sumar (până la -5 pct)
nerespectarea formatului .zip al arhivei (-2 pct)
alte situaţii nespecificate, dar considerate inadecvate având în vedere obiectivele temei; în special situațiile de modificare a interfeței oferite
Temele vor fi testate împotriva plagiatului. Orice tentativă de copiere va fi depunctată conform regulamentului.
Pylint
Vom testa sursele voastre cu pylint configurat conform fișierului pylintrc din arhiva temei. Atenție, rulăm pylint doar pe modulele completate și adăugate de voi, nu și pe cele ale testerului.

Deoarece apar diferențe de scor între versiuni diferite de pylint, vom testa temele doar cu ultima versiune. Vă recomandăm să o folosiți și voi tot pe aceasta.

Vom face depunctări de până la -5pct dacă verificarea făcută cu pylint vă dă un scor mai mic de 8.

Observații
Pot exista depunctări mai mari decât este specificat în secţiunea Notare pentru implementări care nu respectă obiectivele temei și pentru situatii care nu sunt acoperite în mod automat de către sistemul de testare
Implementarea şi folosirea metodelor oferite în schelet este obligatorie
Puteți adăuga variabile/metode/clase, însă nu puteți schimba antetul metodelor oferite în schelet
Bug-urile de sincronizare, prin natura lor sunt nedeterministe; o temă care conţine astfel de bug-uri poate obţine punctaje diferite la rulări succesive; în acest caz punctajul temei va fi cel dat de tester în momentul corectării
Recomandăm testarea temei în cât mai multe situații de load al sistemului și pe cât mai multe sisteme pentru a descoperi bug-urile de sincronizare
