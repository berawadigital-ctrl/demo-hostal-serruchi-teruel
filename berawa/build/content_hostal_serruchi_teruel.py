# Contenido de la demo Hostal Serruchi (Teruel) (es/en/fr/de). Hechos de hostalserruchi.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hostal real.','en':' Images are illustrations and do not show the actual guesthouse.','fr':' Les images sont des illustrations et ne montrent pas l’hostal réel.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hostal.'}
H={'es':['Habitaciones de una a cuatro personas','Apartamentos dobles'],'en':['Rooms for one to four guests','Double apartments'],'fr':['Chambres pour une à quatre personnes','Appartements doubles'],'de':['Zimmer für eine bis vier Personen','Doppel-Apartments']}
RD={
'es':['Dobles, doble con cama de matrimonio, triples y cuádruples, ambientadas en lugares de Teruel como la Plaza del Torico o La Escalinata.','Dos apartamentos dobles y dos abuhardillados, con habitaciones separadas, nevera, microondas y vajilla. Especiales para familias con niños.'],
'en':['Doubles, double with double bed, triples and quadruples, themed on Teruel landmarks such as Plaza del Torico or La Escalinata.','Two double apartments and two attic apartments, with separate rooms, fridge, microwave and crockery. Ideal for families with children.'],
'fr':['Doubles, double avec lit double, triples et quadruples, inspirées de lieux de Teruel comme la Plaza del Torico ou La Escalinata.','Deux appartements doubles et deux mansardés, avec chambres séparées, réfrigérateur, micro-ondes et vaisselle. Parfaits pour les familles avec enfants.'],
'de':['Doppel-, Doppelzimmer mit Doppelbett, Dreibett- und Vierbettzimmer, gestaltet nach Orten in Teruel wie der Plaza del Torico oder La Escalinata.','Zwei Doppel-Apartments und zwei Dachgeschoss-Apartments mit getrennten Zimmern, Kühlschrank, Mikrowelle und Geschirr. Ideal für Familien mit Kindern.']}
ART={
'hero':('skyline',7811,['#1b1b20','#b97d4b','#f0dabd','#694e3a','#45352b','#231d19']),
'intro':('arches',7812,['#f4eee6','#fbf7f0','#96603a','#64432d','#2c2019']),
'r1':('arches',7821,['#efe7dc','#d0a072','#96603a','#64432d','#2c2019']),
'r2':('columns',7822,['#1b1b20','#c48a58','#f1e0c6','#735643','#4b3b2f','#26201b']),
'g1':('hills',7831,['#ece4d7','#f1e2ca','#d0a072','#a28a69','#76624d','#4c3f32']),
'g2':('skyline',7832,['#1b1b20','#b97d4b','#f0dabd','#694e3a','#45352b','#231d19']),
'g3':('columns',7833,['#f2ebe2','#faf5ed','#a0683e','#694e3a','#2c2019']),
'g4':('waves',7834,['#1b1b20','#c48a58','#f1e0c6','#735643','#4b3b2f','#26201b'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hostal Serruchi · Hostal y apartamentos en Teruel',see_rooms='Ver las habitaciones',hero_k='Teruel · C/ Ollerías del Calvario, 4',hero_t='Una ubicación privilegiada y tranquila en Teruel',hero_s='A 5 minutos a pie del Centro Histórico. Habitaciones de una a cuatro personas y apartamentos con nevera y microondas.',
 intro_t='Bienvenidos a nuestra casa',intro_p1='El hostal tiene 16 habitaciones en 4 plantas, restaurante con menús diarios, bar o lounge, recepción y wifi gratis.',
 intro_p2='Cada habitación está ambientada en un rincón de Teruel: la Plaza del Torico, La Escalinata, el Acueducto de los Arcos o la Catedral. Te ayudan con información turística y la compra de entradas.',
 stats=['A 5 min del Centro Histórico','16 habitaciones','Wifi gratis','Restaurante y bar'],nav_rooms='Habitaciones',rooms_t='Habitaciones y apartamentos',rooms_s='Todas con armario, TV de pantalla plana, baño privado con ducha, secador, ropa de cama y cambio de toallas a diario.',
 svcs=['Restaurante con menús diarios','Bar o lounge','Wifi gratis en todas las estancias','Parking privado para motos bajo petición','Asistencia turística y venta de entradas','Habitaciones hasta 4 personas'],
 loc_p='C/ Ollerías del Calvario, 4 · 44003 Teruel. Información y reservas: 978 610 681. Correo: info@hostalserruchi.com.',
 chips=['¿Qué habitaciones tenéis?','¿Tenéis apartamentos?','¿Hay restaurante?','¿Cómo reservo?']),
'en':dict(title='Hostal Serruchi · Guesthouse and apartments in Teruel',see_rooms='See the rooms',hero_k='Teruel · C/ Ollerías del Calvario, 4',hero_t='A privileged, quiet location in Teruel',hero_s='5 minutes’ walk from the Historic Centre. Rooms for one to four people and apartments with fridge and microwave.',
 intro_t='Welcome to our home',intro_p1='The guesthouse has 16 rooms over 4 floors, a restaurant with daily set menus, a bar or lounge, reception and free wifi.',
 intro_p2='Each room is themed on a corner of Teruel: Plaza del Torico, La Escalinata, the Los Arcos Aqueduct or the Cathedral. They help with tourist information and buying tickets.',
 stats=['5 min from the Historic Centre','16 rooms','Free wifi','Restaurant and bar'],nav_rooms='Rooms',rooms_t='Rooms and apartments',rooms_s='All with wardrobe, flat-screen TV, private bathroom with shower, hairdryer, bed linen and daily towel change.',
 svcs=['Restaurant with daily set menus','Bar or lounge','Free wifi in all areas','Private motorbike parking on request','Tourist assistance and ticket booking','Rooms for up to 4 people'],
 loc_p='C/ Ollerías del Calvario, 4 · 44003 Teruel. Information and bookings: +34 978 610 681. Email: info@hostalserruchi.com.',
 chips=['Which rooms do you have?','Do you have apartments?','Is there a restaurant?','How do I book?']),
'fr':dict(title='Hostal Serruchi · Hostal et appartements à Teruel',see_rooms='Voir les chambres',hero_k='Teruel · C/ Ollerías del Calvario, 4',hero_t='Un emplacement privilégié et calme à Teruel',hero_s='À 5 minutes à pied du centre historique. Chambres pour une à quatre personnes et appartements avec réfrigérateur et micro-ondes.',
 intro_t='Bienvenue chez nous',intro_p1='L’hostal compte 16 chambres sur 4 étages, un restaurant avec menus du jour, un bar ou lounge, une réception et le wifi gratuit.',
 intro_p2='Chaque chambre est inspirée d’un lieu de Teruel : la Plaza del Torico, La Escalinata, l’aqueduc de Los Arcos ou la cathédrale. On vous aide avec l’information touristique et l’achat de billets.',
 stats=['À 5 min du centre historique','16 chambres','Wifi gratuit','Restaurant et bar'],nav_rooms='Chambres',rooms_t='Chambres et appartements',rooms_s='Toutes avec armoire, TV écran plat, salle de bains privée avec douche, sèche-cheveux, linge de lit et changement de serviettes quotidien.',
 svcs=['Restaurant avec menus du jour','Bar ou lounge','Wifi gratuit partout','Parking privé pour motos sur demande','Aide touristique et billetterie','Chambres jusqu’à 4 personnes'],
 loc_p='C/ Ollerías del Calvario, 4 · 44003 Teruel. Informations et réservations : +34 978 610 681. E-mail : info@hostalserruchi.com.',
 chips=['Quelles chambres avez-vous ?','Avez-vous des appartements ?','Y a-t-il un restaurant ?','Comment réserver ?']),
'de':dict(title='Hostal Serruchi · Hostal und Apartments in Teruel',see_rooms='Zimmer ansehen',hero_k='Teruel · C/ Ollerías del Calvario, 4',hero_t='Eine bevorzugte, ruhige Lage in Teruel',hero_s='5 Gehminuten vom historischen Zentrum. Zimmer für eine bis vier Personen und Apartments mit Kühlschrank und Mikrowelle.',
 intro_t='Willkommen in unserem Haus',intro_p1='Das Hostal hat 16 Zimmer auf 4 Etagen, ein Restaurant mit Tagesmenüs, eine Bar oder Lounge, Rezeption und kostenloses WLAN.',
 intro_p2='Jedes Zimmer ist einem Ort in Teruel gewidmet: der Plaza del Torico, La Escalinata, dem Aquädukt Los Arcos oder der Kathedrale. Man hilft Ihnen mit Touristeninformationen und beim Ticketkauf.',
 stats=['5 Min. vom historischen Zentrum','16 Zimmer','Kostenloses WLAN','Restaurant und Bar'],nav_rooms='Zimmer',rooms_t='Zimmer und Apartments',rooms_s='Alle mit Schrank, Flachbild-TV, eigenem Bad mit Dusche, Haartrockner, Bettwäsche und täglichem Handtuchwechsel.',
 svcs=['Restaurant mit Tagesmenüs','Bar oder Lounge','Kostenloses WLAN überall','Privater Motorradparkplatz auf Anfrage','Touristenhilfe und Ticketkauf','Zimmer bis 4 Personen'],
 loc_p='C/ Ollerías del Calvario, 4 · 44003 Teruel. Information und Buchung: +34 978 610 681. E-Mail: info@hostalserruchi.com.',
 chips=['Welche Zimmer gibt es?','Haben Sie Apartments?','Gibt es ein Restaurant?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://www.hostalserruchi.com/reservas'
BOOK=dict(mode='engine',url=dict(es=R,en=R,fr=R,de=R))
D=dict(name='Hostal Serruchi',ac='#1f1d22',ac2='#96603a',ac2_a11y='#744828',book=BOOK,around=[],foot=FOOT,
 address='C/ Ollerías del Calvario, 4 · 44003 Teruel',phones=['+34 978 610 681'],emails=['info@hostalserruchi.com'],maps='Hostal Serruchi, Calle Ollerías del Calvario 4, 44003 Teruel',t=T)
META=dict(repo='demo-hostal-serruchi-teruel',name='Hostal Serruchi',legal_name='Serruchi S.C., NIF J44156651 (aviso legal de su web)',registry_ids=['J44156651'],
 url='https://www.hostalserruchi.com/',domain='hostalserruchi.com',municipality='Teruel',province='Teruel',sector='hostal y apartamentos a 5 minutos del centro historico de Teruel',
 read_at='2026-11-02T07:31:00+01:00',created_at='2026-11-02T07:30:00+01:00',built_at='2026-11-02T07:40:00+01:00',audit_date='2026-11-02T07:30:00+01:00',
 rating=dict(value=4.5,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/Hostal+Serruchi/@40.3461647,-1.1050538,17z'),
 book=dict(mode='engine',url=R,note='sistema de reservas propio de su web (boton Reservar del menu): https://www.hostalserruchi.com/reservas, HTTP 200 (02/11/2026 07:30); su web dice «Reserva tu habitación o apartamento llamándonos al teléfono 978 610 681 o por medio de nuestro propio sistema de reservas». Solo en español, mismo enlace en los 4 idiomas.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Tenéis apartamentos?','K02'),('Viajamos en familia, ¿hay sitio para cuatro?','K03'),('¿Hay wifi?','K04'),('¿Hay restaurante?','K05'),('¿Hay parking para motos?','K06'),('¿Dónde estáis?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Qué ver en Teruel?','K09'),('¿Me ayudáis a comprar entradas?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('Do you have apartments?','K02'),('We are a family, is there room for four?','K03'),('Is there wifi?','K04'),('Is there a restaurant?','K05'),('Is there motorbike parking?','K06'),('Where are you?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('What to see in Teruel?','K09'),('Can you help me buy tickets?','K10'),('What is your phone number?','K11'),('How much is a night?',None),('Do you have a pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Avez-vous des appartements ?','K02'),('Nous voyageons en famille, y a-t-il de la place pour quatre ?','K03'),('Y a-t-il le wifi ?','K04'),('Y a-t-il un restaurant ?','K05'),('Y a-t-il un parking pour motos ?','K06'),('Où êtes-vous ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Que voir à Teruel ?','K09'),('Pouvez-vous m’aider à acheter des billets ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Haben Sie Apartments?','K02'),('Wir reisen als Familie, gibt es Platz für vier?','K03'),('Gibt es WLAN?','K04'),('Gibt es ein Restaurant?','K05'),('Gibt es Motorradparkplätze?','K06'),('Wo liegt das Hostal?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Was kann man in Teruel sehen?','K09'),('Können Sie mir beim Ticketkauf helfen?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Was kostet eine Nacht?',None),('Haben Sie einen Pool?',None)]}
