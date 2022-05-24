executable_path = r'.\sources\chromedriver.exe'
csv_file_path = r'.\output\avito_car_dataset.csv'
all_car_equipments = ['Jantes aluminium','Airbags','Climatisation','Système de navigation/GPS','Toit ouvrant','Sièges cuir','Radar de recul','Caméra de recul','Vitres électriques','ABS','ESP','Régulateur de vitesse','Limiteur de vitesse','CD/MP3/Bluetooth','Ordinateur de bord','Verrouillage centralisé à distance']
all_car_specifics = ['Marque','Modèle','Année-Modèle','Kilométrage','Type de carburant','Puissance fiscale','Boite de vitesses','Nombre de portes','Origine','Première main','État']
general_search_url = 'https://www.avito.ma/fr/maroc/voitures-%C3%A0_vendre?brand=1,3,5,10,12,13,17,18,24,29,30,33,41,42,44,45,46,49,50,51,55,56,58&price_min=60000&mileage_max=36&regdate_min=10&regdate_max=42&pfiscale_min=2&pfiscale_max=11'#'https://www.avito.ma/fr/maroc/voitures-%C3%A0_vendre'
start_page_index = 0
last_page_index = 1000
decalge = 20
max_pages = 1500
test_item = {'Lien': 'https://www.avito.ma/fr/anfa/voitures/FORD_Fiesta__V%C3%89HICULE_EXPERTIS%C3%89__49395750.htm', 'Prix': 137900, 'Ville': 'Casablanca', 'Type de carburant': 'Diesel', 'Puissance fiscale': '6', 'Boite de vitesses': 'Manuelle', 'Secteur': 'Anfa', 'État': 'Excellent', 'Kilométrage': '65 000 - 69 999', 'Année-Modèle': '2019', 'Marque': 'Ford', 'Modèle': 'Fiesta', 'Nombre de portes': '5', 'Origine': 'WW au Maroc', 'Première main': 'Oui', 'Jantes aluminium': False, 'Airbags': True, 'Climatisation': True, 'Système de navigation/GPS': False, 'Toit ouvrant': False, 'Sièges cuir': False, 'Radar de recul': False, 'Caméra de recul': False, 'Vitres électriques': False, 'ABS': True, 'ESP': True, 'Régulateur de vitesse': False, 'Limiteur de vitesse': False, 'CD/MP3/Bluetooth': True, 'Ordinateur de bord': False, 'Verrouillage centralisé à distance': False}

