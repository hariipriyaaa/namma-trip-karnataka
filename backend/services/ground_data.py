"""Curated, deterministic Karnataka circuit data. Estimates are illustrative, not live prices."""
from typing import Dict, Any

CIRCUITS: Dict[str, Dict[str, Any]] = {
    "coastal": {"name":"Karavali & Coastal","region":"Coast","description":"Sea temples, palm-lined beaches, ports and unforgettable coastal food.","places":[
        ('Udupi Sri Krishna Matha', 'Visit the revered temple complex; confirm current darshan timings and dress guidance.', 'Heritage & shrine', 0),
        ('Malpe Beach', 'Enjoy a coastal walk and check local sea conditions before water activities.', 'Coast & nature', 30),
        ("St. Mary's Island", 'Check ferry operations and seasonal island access before planning this stop.', 'Geology & coast', 300),
        ('Kapu Lighthouse', 'Visit the lighthouse area and enjoy the sea view when open.', 'Scenic viewpoint', 50),
        ('Karkala Gomateshwara Statue', 'Visit the hilltop monument and check access and footwear guidance.', 'Heritage', 0),
        ('Moodabidri Thousand Pillars Jain Temple', 'Confirm visiting hours and local visitor etiquette.', 'Sacred heritage', 0),
        ('Maravanthe Beach', 'See the striking coastal road landscape; take care crossing roads.', 'Scenic coast', 0),
        ('Kodi Bengre estuary', 'Explore public access areas and respect fishing activity.', 'Coast & nature', 0),
        ('Barkur heritage walk', 'Explore historic temples and settlement remains with local guidance.', 'History & culture', 0),
        ('Mangaluru Kudroli Temple', 'Explore the temple respectfully and check event-day access.', 'Heritage & shrine', 0),
        ('Kadri Manjunath Temple', 'Visit respectfully and confirm current temple timings.', 'Sacred heritage', 0),
        ('Sultan Battery, Mangaluru', 'Explore the historic watchtower area and check access conditions.', 'History', 0),
] ,"food":["Udupi Ghee Roast","Mangalore Buns","Neer Dosa"],"transit":"Reach Mangaluru Central (MAQ) or Udupi (UD) by train; use local buses or a taxi for beaches."},
    "malnad": {"name":"Malnad & Western Ghats","region":"Ghats","description":"Misty coffee hills, rainforest trails, waterfalls and cool mountain air.","places":[
        ('Chikmagalur coffee estate visit', 'Book a visitor-friendly estate in advance; confirm the walking route and tasting options.', 'Coffee & nature', 250),
        ('Mullayanagiri summit viewpoint', "Check weather and road access before heading to Karnataka's highest peak; avoid exposed trails in storms.", 'Mountain viewpoint', 50),
        ('Baba Budangiri hill range', 'Enjoy the highland scenery and follow current access and shrine guidance.', 'Scenic highlands', 30),
        ('Hebbe Falls authorised jeep route', 'Jeep access is managed and may be seasonal; verify permits, operator and weather before travelling.', 'Waterfall & trek', 500),
        ('Hirekolale Lake', 'Visit in daylight for views of the lake and hills; follow local safety guidance.', 'Lake & landscape', 0),
        ('Belavadi Veera Narayana Temple', 'Explore the historic Hoysala temple and its architectural details; check visiting hours.', 'Heritage', 0),
        ('Jhari Falls (Buttermilk Falls) access', 'Check road, jeep and waterfall access locally; do not enter unsafe water.', 'Waterfall & nature', 300),
        ('Kemmanagundi hill station', 'Explore the hill-station gardens and viewpoints when roads and facilities are open.', 'Hill station', 50),
        ('Z Point trail, Kemmanagundi', 'Take the trail only in suitable weather and allow daylight for the return walk.', 'Trek & viewpoint', 0),
        ('Kalhatti Falls', 'Visit the waterfall and nearby temple area; check seasonal flow and safe access.', 'Waterfall & heritage', 30),
        ('Bhadra Wildlife Sanctuary guided safari', 'Use authorised safari providers and verify timings, permits and current wildlife access.', 'Wildlife', 800),
        ('Bhadra reservoir public viewpoint', 'Use permitted public viewpoints only and stay away from restricted dam infrastructure.', 'Reservoir & landscape', 0),
        ('Kudremukh National Park visitor area', 'Check permits, guide requirements and travel time before planning this longer excursion.', 'Rainforest & trekking', 200),
        ('Sringeri Sharada Peetham', 'Visit the temple complex respectfully and confirm current darshan timings.', 'Sacred heritage', 0),
        ('Tunga River ghat, Sringeri', 'Enjoy the riverside from safe public areas and follow local guidance.', 'River & culture', 0),
] ,"food":["Akki Rotti","Malnad Kadubu","Filter Coffee"],"transit":"Use Kadur or Birur rail connections for Chikmagalur; onward travel is mainly by road. Sringeri, Horanadu and Kudremukh are longer excursions, so group nearby stops and confirm road, permit and weather conditions."},
    "north": {"name":"North Karnataka & Deccan","region":"North","description":"Open Deccan skies, grand ruins, stepwells and centuries of layered history.","places":[
        ('Virupaksha Temple', 'Visit respectfully and confirm temple timings.', 'Heritage & shrine', 0),
        ('Hampi Stone Chariot', 'View the iconic stone chariot from the designated visitor area.', 'Architecture', 40),
        ('Vijaya Vittala Temple, Hampi', 'Explore the UNESCO-listed landscape; respect protected monument boundaries.', 'UNESCO & architecture', 40),
        ('Hampi Lotus Mahal', 'Visit the royal enclosure and verify monument ticket rules.', 'Architecture', 40),
        ('Hampi Elephant Stables', 'Explore the royal enclosure in the designated visitor route.', 'Architecture', 40),
        ('Hampi Achyutaraya Temple', 'Walk the historic temple area in daylight.', 'Heritage', 0),
        ('Badami Cave Temples', 'See rock-cut cave architecture; check ticketing and opening hours.', 'Architecture', 50),
        ('Mahakuta temple complex', 'Explore the temple group respectfully and check access.', 'Heritage & shrine', 0),
        ('Banashankari Temple, Badami area', 'Confirm temple hours and festival-day arrangements.', 'Sacred heritage', 0),
        ('Aihole Durga Temple', 'Explore early Chalukyan architecture and the surrounding site.', 'Architecture', 40),
        ('Aihole Lad Khan Temple', 'See the distinctive early Chalukyan design.', 'Architecture', 40),
        ('Aihole Meguti Jain Temple', 'Check hill access and take care on stone steps.', 'Heritage & architecture', 0),
        ('Pattadakal monuments', 'Plan time for the protected monument complex.', 'UNESCO & architecture', 40),
        ('Pattadakal museum (if open)', 'Check current museum hours before visiting.', 'Museum & heritage', 30),
        ('Agastya Lake', 'Walk designated paths and respect the historic surroundings.', 'Landscape & heritage', 0),
] ,"food":["Dharwad Peda","Jolada Rotti Oota","Belagavi Kunda"],"transit":"Hospet Junction (HPT) is a useful rail gateway for Hampi; check local transport and monument timings."},
    "hoysala": {"name":"Hoysala & Royal South","region":"Heritage","description":"Intricate stone carving, palace stories, silk, sandalwood and royal architecture.","places":[
        ('Chennakeshava Temple, Belur', 'Study the detailed sculptures and check current temple visiting rules.', 'Hoysala architecture', 0),
        ('Hoysaleswara Temple, Halebidu', 'Explore the celebrated stone carvings and temple grounds.', 'Hoysala architecture', 0),
        ('Belavadi Veera Narayana Temple', 'Explore the historic Hoysala temple and its architectural details; check visiting hours.', 'Heritage', 0),
        ('Mysore Palace', 'Confirm illumination and visitor hours separately before visiting.', 'Royal heritage', 120),
        ('Jaganmohan Palace art gallery (check hours)', 'District administration lists adult entry at ₹20; confirm the current ticket rate and gallery hours before visiting.', 'Art & heritage', 20),
        ('Mysuru Zoo', 'Adult entry is approximately ₹120 on the official zoo ticket page; child fares and vehicle options differ. Recheck before visiting.', 'Wildlife & family visit', 120),
        ('Chamundi Hill viewpoint', 'Check traffic and temple access, especially on festival days.', 'Viewpoint & shrine', 0),
        ("St. Philomena's Church", 'Visit respectfully and check service-time restrictions.', 'Architecture', 0),
        ('Devaraja Market', 'Explore flower, spice and produce stalls respectfully.', 'Market & culture', 0),
        ('Srirangapatna Ranganathaswamy Temple', 'Visit respectfully and check darshan timings.', 'Sacred heritage', 0),
        ('Daria Daulat Bagh, Srirangapatna', 'Karnataka Tourism lists adult entry at about ₹25 for Indian visitors; confirm current ticket category and opening hours before visiting.', 'Museum & history', 25),
        ('Srirangapatna fort and historic sites', 'Explore only accessible public sections and respect protected areas.', 'History', 0),
        ('Ranganathittu Bird Sanctuary', 'Check boat operations, seasonal conditions and visitor rules.', 'Wildlife', 100),
        ('Brindavan Gardens (check hours)', 'Confirm garden and fountain show timings before travelling.', 'Garden & family', 50),
        ('Karanji Lake, Mysuru', 'Check park hours and bird-viewing access.', 'Lake & nature', 50),
        ('Somanathapura Keshava Temple', 'Visit the historic temple and verify current conservation-related access.', 'Hoysala architecture', 40),
        ('Nanjangud Srikanteshwara Temple', 'Check darshan hours and road journey time.', 'Sacred heritage', 0),
        ('Talakadu temple landscape', 'Check local access and riverbank conditions before travelling.', 'History & heritage', 0),
] ,"food":["Mysore Pak","Maddur Vada","Mysore Masala Dosa"],"transit":"Mysuru Junction (MYS) and Hassan (HAS) connect key stops; use a taxi for Belur–Halebidu–Belavadi."},
    "wildlife": {"name":"Uttara Kannada & Wildlife","region":"Ghats","description":"Rainforests, Kali River adventures, monolithic rocks and spectacular waterfalls.","places":[
        ('Dandeli Kali River rafting', 'Use an authorised operator and confirm river conditions, safety equipment and seasonal availability.', 'River adventure', 1200),
        ('Sykes Point viewpoint', 'Check access rules and daylight hours before visiting this gorge viewpoint.', 'Gorge view', 40),
        ('Syntheri Rocks', 'Verify current forest access, entry requirements and road conditions.', 'Geological wonder', 50),
        ('Supa Dam backwaters viewpoint', 'Visit approved public viewpoints; do not enter restricted dam areas.', 'Scenic waterway', 0),
        ('Kavala Caves authorised visit (if open)', 'Check forest permits, guide rules and current access before planning.', 'Caves & forest', 100),
        ('Ulavi Channabasaveshwara Temple', 'Check road conditions and temple visiting hours.', 'Sacred heritage', 0),
        ('Yana limestone pinnacles', 'Plan the forest walk in daylight and follow posted conservation guidance.', 'Karst rock trek', 50),
        ('Vibhooti Falls access', 'Check local conditions and water safety; avoid swimming when unsafe.', 'Waterfall & nature', 40),
        ('Gokarna Mahabaleshwar Temple', 'Plan the coastal drive and confirm darshan timings.', 'Sacred heritage', 0),
        ('Sirsi Marikamba Temple', 'Visit respectfully and confirm festival-day crowd arrangements.', 'Shakti shrine', 0),
        ('Magod Falls viewpoint', 'Check seasonal access, road conditions and safety barriers.', 'Waterfall viewpoint', 30),
        ('Jog Falls viewpoint', 'Check seasonal water levels and viewpoint access before travelling.', 'Waterfall viewpoint', 50),
        ('Anshi/Dandeli forest interpretation area', 'Use authorised access and follow forest department directions.', 'Forest & wildlife', 100),
        ('Shivapura hanging bridge area (if accessible)', 'Verify current public access and river conditions before travelling.', 'River & viewpoint', 0),
        ('Kali River riverside viewpoint', 'Use designated public areas and follow water-safety notices.', 'River & landscape', 0),
] ,"food":["Bhatkal Biryani","Kalale (bamboo shoot) sukka","Yellapur honey & roasted cashews"],"transit":"Train to Alnavar (LWR) or Hubballi Junction (UBL), then pre-booked taxi or verified local bus. Rafting and forest access are seasonal."},
    "bengaluru": {"name":"Bengaluru & Garden City","region":"Heritage","description":"Urban culture, leafy parks, local markets, craft coffee and contemporary Karnataka.","places":[
        ('Lalbagh Botanical Garden', 'Enjoy the garden paths and check entry rules for special events.', 'Garden & nature', 50),
        ('Cubbon Park', 'Take a morning walk and respect park timings.', 'Garden & nature', 0),
        ('Bengaluru Palace exterior', 'Check current visitor access and photography rules.', 'Architecture', 250),
        ('Bangalore Fort historic area', 'Check which sections are open to visitors.', 'History', 0),
        ("Tipu Sultan's Summer Palace", 'Confirm museum opening hours and ticketing.', 'Museum & history', 30),
        ('National Gallery of Modern Art Bengaluru', 'Check exhibition hours and entry rules.', 'Art & culture', 50),
        ('Visvesvaraya Industrial and Technological Museum', 'Check opening hours and ticketing.', 'Science museum', 100),
        ('Indian Music Experience Museum (check hours)', 'Check current opening hours and exhibitions.', 'Museum & music', 100),
        ('ISKCON Bengaluru', 'Check visitor timings and dress guidance.', 'Sacred heritage', 0),
        ('Bannerghatta Biological Park', 'Check safari schedules, ticketing and animal-welfare visitor rules.', 'Wildlife', 250),
        ('Nandi Hills day trip', 'Check road access, entry timing and crowd restrictions before departure.', 'Hill viewpoint', 50),
        ('Channapatna toy craft visit', 'Look for local makers and ask before photographing workshops.', 'Crafts & culture', 100),
] ,"food":["Benne Dose","Thatte Idli","Filter Coffee"],"transit":"Kempegowda Bus Station and Bengaluru City railway station connect well; Metro is useful for many central stops."},
    "royal": {"name":"Mysuru & Kodagu","region":"Heritage","description":"Royal streets, coffee country, misty estates and Kodava hospitality.","places":[
        ('Mysore Palace', 'Confirm illumination and visitor hours separately before visiting.', 'Royal heritage', 120),
        ("St. Philomena's Church", 'Visit respectfully and check service-time restrictions.', 'Architecture', 0),
        ('Mysuru Zoo', 'Adult entry is approximately ₹120 on the official zoo ticket page; child fares and vehicle options differ. Recheck before visiting.', 'Wildlife & family visit', 120),
        ('Jaganmohan Palace art gallery (check hours)', 'District administration lists adult entry at ₹20; confirm the current ticket rate and gallery hours before visiting.', 'Art & heritage', 20),
        ('Karanji Lake, Mysuru', 'Check park hours and bird-viewing access.', 'Lake & nature', 50),
        ('Chamundi Hill viewpoint', 'Check traffic and temple access, especially on festival days.', 'Viewpoint & shrine', 0),
        ('Devaraja Market', 'Explore flower, spice and produce stalls respectfully.', 'Market & culture', 0),
        ('Srirangapatna Ranganathaswamy Temple', 'Visit respectfully and check darshan timings.', 'Sacred heritage', 0),
        ('Daria Daulat Bagh, Srirangapatna', 'Karnataka Tourism lists adult entry at about ₹25 for Indian visitors; confirm current ticket category and opening hours before visiting.', 'Museum & history', 25),
        ('Srirangapatna fort and historic sites', 'Explore only accessible public sections and respect protected areas.', 'History', 0),
        ('Ranganathittu Bird Sanctuary', 'Check boat operations, seasonal conditions and visitor rules.', 'Wildlife', 100),
        ('Brindavan Gardens (check hours)', 'Confirm garden and fountain show timings before travelling.', 'Garden & family', 50),
        ('Somanathapura Keshava Temple', 'Visit the historic temple and verify current conservation-related access.', 'Hoysala architecture', 40),
        ('Nanjangud Srikanteshwara Temple', 'Check darshan hours and road journey time.', 'Sacred heritage', 0),
        ('Talakadu temple landscape', 'Check local access and riverbank conditions before travelling.', 'History & heritage', 0),
        ('Melukote Cheluvanarayana Swamy Temple', 'Visit the historic temple complex respectfully and confirm current darshan timings.', 'Sacred heritage', 0),
        ('Madikeri Fort', 'Check museum and fort access times.', 'History', 0),
        ("Raja's Seat, Madikeri", 'Enjoy the hilltop garden and sunset views when open.', 'Viewpoint', 20),
        ('Abbey Falls access', 'Follow marked paths and heed water-safety warnings.', 'Waterfall & nature', 30),
        ('Omkareshwara Temple, Madikeri', 'Visit respectfully and confirm temple timings.', 'Sacred heritage', 0),
        ('Dubare Elephant Camp (check operations)', 'Check current visitor activities, operating hours and responsible wildlife interaction rules before travelling.', 'Wildlife & nature', 250),
] ,"food":["Mysore Pak","Coorg Pandi Curry","Kadambuttu"],"transit":"Mysuru is the rail gateway; onward travel to Madikeri is by road. Check waterfall access and estate opening times."},
    "heritage": {"name":"Badami–Aihole–Pattadakal","region":"North","description":"Rock-cut caves and early temple architecture in a remarkable historic landscape.","places":[
        ('Badami Cave Temples', 'Explore the rock-cut caves; check ticketing and opening hours.', 'Architecture', 50),
        ('Agastya Lake', 'Walk designated paths and respect the historic surroundings.', 'Landscape & heritage', 0),
        ('Bhutanatha Temples', 'Visit the temple complex in daylight.', 'Heritage & shrine', 0),
        ('Aihole Durga Temple', 'Explore the early temple architecture and museum if open.', 'Architecture', 40),
        ('Lad Khan Temple', 'See the distinctive early Chalukyan design.', 'Architecture', 40),
        ('Aihole Meguti Jain Temple', 'Check hill access and take care on stone steps.', 'Heritage & architecture', 0),
        ('Pattadakal UNESCO monuments', 'Plan time for the protected monument complex.', 'UNESCO & architecture', 40),
        ('Mahakuta temple complex', 'Explore the temple group respectfully and check access.', 'Heritage & shrine', 0),
        ('Banashankari Temple area', 'Check temple access and local event schedules.', 'Heritage & shrine', 0),
] ,"food":["Jolada Rotti","Ennegayi","Dharwad Peda"],"transit":"Badami (BDM) is a useful rail station. Arrange a local taxi for Aihole and Pattadakal, and confirm monument hours."},
    "tunga": {"name":"Tunga River & Sacred Trails","region":"Ghats","description":"Temple towns, river ghats, green countryside and traditional vegetarian meals.","places":[
        ('Sringeri Sharada Peetham', 'Follow shrine etiquette and current visitor guidance.', 'Sacred heritage', 0),
        ('Tunga River ghat', 'Enjoy the riverfront from safe public areas.', 'River & nature', 0),
        ('Kigga Rishya Shringeshwara Temple', 'Check road conditions and temple hours.', 'Sacred heritage', 0),
        ('Kuppalli Kuvempu birthplace and memorial (check hours)', 'Confirm opening hours and visitor arrangements.', 'Literary heritage', 50),
        ('Kavaledurga Fort trek', 'Check trail conditions and allow enough daylight for the return.', 'Fort & trekking', 0),
        ('Thirthahalli riverside', 'Enjoy the river landscape and keep clear of unsafe banks.', 'River & nature', 0),
        ('Agumbe rainforest viewpoint', 'Check weather and road conditions; avoid night ghat driving.', 'Nature & viewpoint', 0),
        ('Kundadri Jain hill', 'Check road and weather conditions before the hilltop visit.', 'Nature & heritage', 0),
        ('Honnemaradu reservoir area (authorised activities)', 'Verify activity operator, access permissions and water safety.', 'Water & adventure', 250),
        ('Jog Falls main viewpoint', 'Check seasonal flow and viewpoint access before travelling.', 'Waterfall viewpoint', 50),
        ('Tyavarekoppa Lion and Tiger Safari (check operations)', 'Verify current safari schedule and visitor guidance.', 'Wildlife', 250),
        ('Sakrebailu Elephant Camp (check operations)', 'Confirm current public visiting hours and responsible visitor rules.', 'Wildlife & nature', 100),
] ,"food":["Pathrode","Akki Rotti","Traditional oota"],"transit":"Shimoga Town (SMET) is a practical rail gateway; onward connections are mostly by road. Check ghat road conditions."},
    "kalyana": {"name":"Kalyana Karnataka & Deccan","region":"North","description":"Fort towns, Sufi heritage, dramatic stone landscapes and hearty northern cuisine.","places":[
        ('Bidar Fort', 'Explore the fort complex and confirm current visitor access.', 'Fort & history', 30),
        ('Rangin Mahal', 'Check opening status and access rules for the historic structure.', 'Architecture', 30),
        ('Bidar Barid Shahi Tombs', 'Check site access and opening hours.', 'History & architecture', 20),
        ('Bidar Nanak Jhira Sahib', 'Check visitor etiquette and current opening times.', 'Sacred heritage', 0),
        ('Basavakalyan Anubhava Mantapa heritage area', 'Check current visitor access and interpretation options.', 'Cultural history', 0),
        ('Basavakalyan Fort', 'Explore the fort grounds and check local access.', 'Fort & history', 20),
        ('Gulbarga Fort', 'Visit the fort and nearby heritage areas respectfully.', 'Fort & history', 30),
        ('Khwaja Bande Nawaz Dargah', 'Observe local etiquette and any restrictions during prayers.', 'Sacred heritage', 0),
        ('Kalaburagi Haft Gumbaz', 'Check access to the historic tomb complex.', 'History & architecture', 0),
        ('Kalaburagi Sharana Basaveshwara Temple', 'Confirm temple timings and festival arrangements.', 'Sacred heritage', 0),
        ('Yadgir Fort', 'Check local access and hilltop safety conditions.', 'Fort & history', 0),
        ('Raichur Fort', 'Explore accessible public sections and follow local advice.', 'Fort & history', 0),
        ('Kudalasangama heritage complex', 'Check temple timings and road journey time.', 'Sacred heritage', 0),
        ('Vijayapura Gol Gumbaz', 'Check museum and monument ticketing and opening hours.', 'Architecture', 50),
        ('Ibrahim Rauza, Vijayapura', 'Visit respectfully and confirm opening times.', 'Architecture', 30),
] ,"food":["Jolada Rotti Oota","Shenga chutney","Local khanavali meals"],"transit":"Bidar and Kalaburagi have rail links. Check local transport and opening hours for each heritage site."}
}

def get_circuit_list():
    return [{"id": key, "name": value["name"], "region": value["region"],
             "description": value["description"], "places_count": len(value["places"]),
             "foods": value["food"], "transit_recommendation": value["transit"]}
            for key, value in CIRCUITS.items()]

# Maximum recommended duration for each regional circuit. These are planning limits,
# not claims that a region has nothing else to see.
CIRCUIT_MAX_DAYS = {
    "coastal": 4, "malnad": 5, "north": 5, "hoysala": 6,
    "wildlife": 5, "bengaluru": 4, "royal": 7, "heritage": 3,
    "tunga": 4, "kalyana": 5,
}


def build_grounded_itinerary(payload: dict) -> dict:
    key = payload.get("circuit", "wildlife")
    circuit = CIRCUITS.get(key, CIRCUITS["wildlife"])
    requested_days = max(1, min(10, int(payload.get("days", 3))))
    style = payload.get("style", "Comfort")
    interests = payload.get("interests", [])
    max_days = 10 if interests else CIRCUIT_MAX_DAYS.get(key, 5)
    days = min(requested_days, max_days)
    # Use only curated, named attractions. Never pad a short circuit with generic
    # “market walk / viewpoint / local experience” placeholders.
    source_places = list(circuit["places"])
    # Add destination-appropriate food/craft experiences only when the traveller selected them.
    food_names = {"coastal":"Coastal Karnataka food tasting: neer dosa & Udupi favourites", "malnad":"Malnad food tasting: akki rotti & filter coffee", "north":"North Karnataka food stop: jolada rotti oota", "hoysala":"Mysuru food trail: masala dosa, Mysore Pak & filter coffee", "wildlife":"Uttara Kannada local food stop", "bengaluru":"Bengaluru darshini food trail: benne dose & filter coffee", "royal":"Mysuru–Kodagu food trail: Mysore Pak & Kodava flavours", "heritage":"Badami local food stop: jolada rotti oota", "tunga":"Sringeri vegetarian oota stop", "kalyana":"Kalyana Karnataka khanavali food stop"}
    craft_names = {"hoysala":"Mysuru silk & sandalwood craft visit", "royal":"Mysuru silk and sandalwood shopping stop", "bengaluru":"Channapatna toy craft visit"}
    extras = []
    if "Native Cuisines & Oota" in interests:
        extras.append((food_names[key], "A regional food stop. Meal spending is included in the daily food estimate; no extra ticket charge is added.", "Regional food", 0))
    if "Silk, Sandalwood & Toys" in interests and key in craft_names:
        extras.append((craft_names[key], "Browse local makers or established shops; purchases are optional and are not included in the trip estimate.", "Crafts & culture", 0))
    # Preserve geographic clusters and insert optional selected food/craft stops after the first cluster.
    source_places = list(source_places)
    source_places[3:3] = extras

    # Canonical six-vibe vocabulary; accept legacy UI values during transition.
    aliases = {
        "UNESCO & Architecture": "Heritage", "Ghats, Falls & Treks": "Nature",
        "Native Cuisines & Oota": "Food", "Sacred Shrines & Mathas": "Shrines",
        "Water Sports & Rafting": "Adventure", "Silk, Sandalwood & Toys": "Crafts",
    }
    vibe_patterns = {
        "Heritage": ("heritage", "architecture", "history", "temple", "shrine", "palace", "fort", "museum", "market", "church", "monument", "unesco", "art", "historic", "archaeolog", "royal enclosure", "cave temple"),
        "Nature": ("nature", "waterfall", "falls", "forest", "lake", "viewpoint", "wildlife", "coast", "beach", "island", "dam", "landscape", "bird", "rainforest", "river", "hill station", "scenic", "garden", "sanctuary"),
        "Food": ("food", "meal", "cuisine", "dosa", "rotti", "pak", "oota", "tasting", "darshini", "coffee", "snack", "thali", "bakery", "culinary", "regional food"),
        "Shrines": ("temple", "shrine", "matha", "peetham", "dargah", "gurdwara", "sacred", "spiritual", "pilgrim", "religious", "prayer"),
        "Adventure": ("rafting", "river adventure", "kayak", "water sport", "surf", "cycling", "trek", "climb", "hike", "trail", "camp", "safari", "outdoor activity", "rock formation", "adventure"),
        "Crafts": ("craft", "silk", "sandalwood", "toy", "handmade", "artisan", "weav", "pottery", "embroidery", "woodwork", "carving", "textile", "handloom", "bidriware", "painting demonstration"),
    }
    adventure_names = {
        "coastal": ["Gokarna beach trek (check tide and trail conditions)", "Mulki surfing or kayaking (operator and sea conditions must be confirmed)", "Coastal cycling route (check safe, suitable roads)"],
        "malnad": ["Guided Western Ghats trek (permit, guide and weather dependent)", "Agumbe guided rainforest walk (guide and seasonal access dependent)", "Hill-country cycling route (weather and road conditions dependent)"],
        "north": ["Badami fort and hill trail (access and heat conditions dependent)", "Aihole countryside cycling route (route and bike availability to confirm)", "Tungabhadra riverside walk (safe public access only)"],
        "hoysala": ["Devarayanadurga guided trek (weather and access dependent)", "Madhugiri Fort trek (access, guide and weather dependent)", "Hassan countryside cycling route (route and operator to confirm)"],
        "wildlife": ["Dandeli white-water rafting (river conditions, permits and operator availability dependent)", "Kali River kayaking (operator and river conditions dependent)", "Yana rock-formation trek (trail access and weather dependent)"],
        "bengaluru": ["Skandagiri sunrise trek (permit and booking dependent)", "Ramanagara guided rock climbing (permitted route and certified operator required)", "Savandurga trek (access and weather dependent)"],
        "royal": ["Tadiandamol guided trek (permit, guide and weather dependent)", "Brahmagiri trek (permit and access dependent)", "Madikeri cycling route (safe route and bike availability to confirm)"],
        "heritage": ["Badami fort trail (heat and access dependent)", "Sandstone landscape walk near Badami (permitted paths only)", "Countryside cycling near Aihole (route and bike availability to confirm)"],
        "tunga": ["Guided Western Ghats trek (permit, guide and weather dependent)", "Agumbe guided rainforest walk (guide and seasonal access dependent)", "Shivamogga countryside cycling route (route and bike availability to confirm)"],
        "kalyana": ["Bidar Fort-area heritage walk (public access and opening times dependent)", "Kalaburagi countryside cycling route (safe route and bike availability to confirm)", "Guided outdoor trail near an accessible local hill (site and operator must be verified)"],
    }
    craft_names = {
        "coastal": "Coastal artisan visit: Yakshagana costume, mask or woodcraft demonstration (maker availability to confirm)",
        "malnad": "Malnad bamboo, cane or woodcraft artisan visit (maker availability to confirm)",
        "north": "Ilkal or Guledagudd textile / handloom artisan visit (verify location and travel)",
        "hoysala": "Mysuru silk or Mysore painting artisan demonstration (venue and hours to confirm)",
        "wildlife": "Uttara Kannada cane, bamboo or coastal woodcraft artisan visit (maker availability to confirm)",
        "bengaluru": "Channapatna wooden-toy artisan visit (day-trip extension; workshop availability to confirm)",
        "royal": "Mysuru silk, Mysore painting or local handicraft artisan visit (venue and hours to confirm)",
        "heritage": "Badami-area stone-carving or pottery demonstration (actual artisan/venue must be confirmed)",
        "tunga": "Shivamogga–Malnad weaving, cane or woodcraft artisan visit (maker availability to confirm)",
        "kalyana": "Bidriware artisan experience in Bidar (workshop availability and hours to confirm)",
    }
    canonical_interests = [aliases.get(v, v) for v in interests]
    if "Adventure" in canonical_interests:
        for name in adventure_names.get(key, []):
            extras.append((name, "Adventure activity suggestion. Confirm operator, permissions, weather, seasonal restrictions and availability before departure.", "Adventure · availability-dependent", 0))
    if "Crafts" in canonical_interests and key in craft_names:
        extras.append((craft_names[key], "Craft experience suggestion. Schedule as a workshop only after confirming a real artisan or venue; otherwise treat it as a visit to be arranged.", "Crafts · availability-dependent", 0))

    # Additional region-specific experiences keep single-vibe plans useful without
    # inserting unrelated categories or inventing confirmed bookings.
    nature_names = {
        "coastal": ["Kaup Beach and lighthouse coastal nature walk", "Maravanthe beach-and-estuary landscape stop", "Kodi Bengre estuary nature observation"],
        "malnad": ["Jog Falls designated viewpoints (seasonal flow dependent)", "Hirekolale Lake landscape walk", "Kudremukh visitor-area nature walk (permits/access dependent)"],
        "north": ["Tungabhadra river landscape observation", "Agastya Lake and surrounding landscape walk", "Daroji Sloth Bear Sanctuary visit (official visitor rules apply)"],
        "hoysala": ["Karanji Lake nature walk", "Kukkarahalli Lake birdwatching", "Ranganathittu bird sanctuary (boat and seasonal access dependent)"],
        "wildlife": ["Kali River viewpoint nature stop", "Yana rock formations nature walk (trail access dependent)", "Sharavathi landscape viewpoint (permitted public access only)"],
        "bengaluru": ["Lalbagh Botanical Garden nature walk", "Cubbon Park green-space walk", "Hesaraghatta landscape and birdwatching (access dependent)"],
        "royal": ["Abbey Falls viewpoint (seasonal flow and safe access dependent)", "Raja's Seat landscape viewpoint", "Coffee-estate nature walk (owner permission required)"],
        "heritage": ["Agastya Lake landscape walk", "Malaprabha River surroundings (permitted access only)", "Badami sandstone landscape viewpoint"],
        "tunga": ["Jog Falls designated viewpoints (seasonal flow dependent)", "Agumbe rainforest observation (guide/access dependent)", "Tunga River public viewpoint (safe access only)"],
        "kalyana": ["Chandrampalli Dam viewpoint (public access must be verified)", "Bidar countryside landscape walk", "Basavakalyan rural landscape observation (public access only)"],
    }
    food_activity_names = {
        "coastal": ["Udupi vegetarian meal and local breakfast tasting", "Mangaluru neer dosa and local snack trail", "Kundapura coastal cuisine tasting (restaurant availability dependent)"],
        "malnad": ["Malnad akki rotti and kadubu meal tasting", "Seasonal jackfruit dishes and local produce tasting", "Coffee-estate tasting (visitor access must be arranged)"],
        "north": ["Jolada rotti and ennegayi regional meal", "Shenga chutney and local snack tasting", "North Karnataka sweets and bakery stop"],
        "hoysala": ["Mysuru masala dosa breakfast trail", "Mysore Pak and traditional sweet-shop visit", "Maddur vada and local snack tasting"],
        "wildlife": ["Karwar coastal cuisine tasting", "Seasonal jackfruit and local produce tasting", "Sirsi-area regional snack and meal stop"],
        "bengaluru": ["Bengaluru darshini breakfast trail", "Benne dose and local bakery tasting", "Regional street-food walk (vendor and hours to verify)"],
        "royal": ["Kodava akki otti and local cuisine tasting", "Mysore Pak and traditional sweet-shop visit", "Coffee-estate tasting (visitor access must be arranged)"],
        "heritage": ["Jolada rotti and ennegayi regional meal", "Badami-area local sweets tasting", "Village food experience (host and availability to confirm)"],
        "tunga": ["Malnad kadubu and regional meal tasting", "Seasonal banana and jackfruit dishes", "Shivamogga traditional snacks and local meal stop"],
        "kalyana": ["Kalaburagi jolada rotti regional meal", "Tahari tasting where available", "Local bakery snacks and traditional sweets"],
    }
    if "Nature" in canonical_interests:
        extras.extend((name, "Nature-focused stop. Check opening/access conditions and local safety guidance before travel.", "Nature · access-dependent", 0) for name in nature_names.get(key, []))
    if "Food" in canonical_interests:
        extras.extend((name, "Regional food experience suggestion; verify that the eatery/vendor is operating and check opening hours. Meal cost is not a live quote.", "Regional food", 0) for name in food_activity_names.get(key, []))

    if interests:
        filtered_places = []
        for item in source_places:
            text = f"{item[0]} {item[2]}".lower()
            if any(any(word in text for word in vibe_patterns.get(vibe, ())) for vibe in canonical_interests):
                filtered_places.append(item)
        extra_places = [item for item in extras if any(any(word in f"{item[0]} {item[2]}".lower() for word in vibe_patterns.get(vibe, ())) for vibe in canonical_interests)]
        source_places = filtered_places + extra_places
        # Do not insert unrelated filler when a selected vibe has limited curated data.
        if not source_places:
            raise ValueError("No curated stops match the selected travel vibes in this region. Try another region or select an additional vibe.")
    total = days * 3
    if len(source_places) < total:
        # For a selected vibe, keep a shorter final day instead of discarding valid stops
        # or padding with unrelated places. Unfiltered plans retain the full-slot rule.
        available_days = (len(source_places) + 2) // 3 if interests else len(source_places) // 3
        days = max(1, min(days, available_days))
        total = days * 3
    if interests:
        days = max(1, min(days, (len(source_places) + 2) // 3))
        total = days * 3
    selected_places = source_places[:total]
    times = ["Morning", "Afternoon", "Evening"]
    # Per-person budget ranges, based on local-eatery meal estimates, twin-share
    # accommodation and shared/local transport. These are planning estimates, not quotes.
    style_profile = {
        "Budget": {"stay": (450, 850), "transport": (180, 400), "meal_factor": 0.82},
        "Comfort": {"stay": (1000, 2000), "transport": (400, 900), "meal_factor": 1.0},
        "Premium": {"stay": (2500, 5000), "transport": (900, 2000), "meal_factor": 1.85},
    }.get(style, {"stay": (1000, 2000), "transport": (400, 900), "meal_factor": 1.0})
    # Approximate meal ranges (INR/person) by circuit and day-area. Values are
    # planning ranges, not live restaurant quotes. The notes identify local food context.
    daily_food_profiles = {
        "coastal": [
            ((50,100),(100,220),(130,280),(30,90),"Udupi: idli, dosa and Udupi meals; seafood is an optional higher-cost choice."),
            ((50,110),(120,240),(140,300),(35,100),"Karkala–Moodabidri: vegetarian meals, neer dosa and tea/coffee."),
            ((55,120),(130,260),(150,330),(40,110),"Kundapura coast: rice meals and coastal curry; seafood varies by restaurant."),
            ((60,130),(150,300),(180,380),(45,130),"Mangaluru: neer dosa, kori rotti or vegetarian coastal meals; seafood may cost more.")],
        "malnad": [
            ((50,110),(120,240),(140,290),(35,100),"Chikkamagaluru town: idli/dosa, rice meals and filter coffee."),
            ((60,130),(140,280),(160,330),(45,120),"Mullayanagiri–Baba Budangiri: hill cafés may cost more; carry water/snacks."),
            ((50,110),(120,250),(140,300),(40,110),"Kemmanagundi area: food options near viewpoints may be limited."),
            ((50,110),(120,240),(140,290),(35,100),"Bhadra/Kudremukh area: local rice meals; pack food for longer excursions."),
            ((50,110),(120,230),(140,280),(35,100),"Sringeri: vegetarian oota, akki rotti and seasonal Malnad dishes.")],
        "north": [
            ((60,130),(150,300),(170,350),(40,120),"Hampi: local thali and breakfast cafés; tourist-zone cafés can cost more."),
            ((55,120),(130,260),(150,300),(35,100),"Hampi–Hospet: jolada rotti meals and simple South Indian breakfast."),
            ((45,100),(100,210),(120,250),(30,85),"Badami: jolada rotti meals and simple breakfast."),
            ((45,100),(100,210),(120,250),(30,85),"Aihole–Pattadakal: fewer nearby options; plan meal stops in advance."),
            ((50,110),(110,230),(130,270),(35,95),"Deccan towns: jolada rotti, ennegayi and local khanavali meals.")],
        "hoysala": [
            ((50,110),(110,230),(130,270),(35,95),"Belur: simple vegetarian breakfast and local meals near the temple town."),
            ((50,110),(110,230),(130,270),(35,95),"Halebidu–Belavadi: arrange a meal stop between temple visits."),
            ((70,140),(140,280),(160,330),(45,120),"Mysuru: masala dosa, meals, Mysore Pak and filter coffee."),
            ((70,150),(150,300),(180,380),(50,140),"Mysuru city: broad choice of eateries; tourist-area cafés may cost more."),
            ((60,130),(130,260),(150,320),(40,110),"Srirangapatna: local vegetarian meals and snacks."),
            ((55,120),(120,250),(140,300),(40,110),"Somanathapura–Talakadu: check meal availability before rural excursions.")],
        "wildlife": [
            ((60,130),(150,300),(170,350),(45,130),"Dandeli: check whether an adventure package includes meals."),
            ((55,120),(130,260),(150,310),(40,110),"Supa–Kavala area: eat in town before remote viewpoints; carry water."),
            ((50,110),(120,240),(140,290),(35,100),"Yana–Vibhooti Falls: rural food options can be sparse; plan lunch around Sirsi."),
            ((60,130),(140,280),(160,330),(45,120),"Gokarna: simple meals are available; beach cafés and seafood may cost more."),
            ((50,110),(120,240),(140,290),(35,100),"Sirsi–Yellapur: local meals; carry snacks for waterfall trips.")],
        "bengaluru": [
            ((70,150),(150,300),(180,380),(50,140),"Central Bengaluru: darshini breakfast, South Indian meals and cafés."),
            ((70,150),(160,320),(190,400),(50,150),"Palace/central area: budget eateries are available; tourist cafés cost more."),
            ((70,150),(150,300),(180,380),(50,140),"Museum and park day: allow for café pricing and snacks."),
            ((60,130),(130,270),(160,330),(45,120),"Nandi Hills/Channapatna excursion: options may be limited along the route.")],
        "royal": [
            ((70,140),(140,280),(160,330),(45,120),"Mysuru: masala dosa, meals, Mysore Pak and filter coffee."),
            ((60,130),(130,260),(150,310),(40,110),"Srirangapatna: local meals and snacks."),
            ((60,130),(130,260),(150,320),(40,110),"Mysuru outskirts: rural stops may have fewer meal options."),
            ((70,150),(150,300),(180,380),(50,140),"Madikeri: Kodava-style dishes and cafés; specialty meat dishes may cost more."),
            ((70,150),(160,320),(180,400),(50,150),"Coorg estate/waterfall day: check whether homestay meals are included."),
            ((60,130),(140,280),(160,340),(45,120),"Kodagu town: kadambuttu and local curry."),
            ((60,130),(130,270),(150,320),(40,110),"Return toward Mysuru: town restaurants offer more choice.")],
        "heritage": [
            ((45,100),(100,210),(120,250),(30,85),"Badami: local jolada rotti meals and simple breakfast."),
            ((45,100),(100,210),(120,250),(30,85),"Aihole: fewer nearby options; arrange lunch around the monument visit."),
            ((45,100),(100,220),(120,260),(30,90),"Pattadakal–Mahakuta: plan meal timing and carry water.")],
        "tunga": [
            ((50,110),(110,230),(130,270),(35,95),"Sringeri: vegetarian oota, akki rotti and simple breakfast."),
            ((50,110),(120,240),(140,290),(35,100),"Thirthahalli–Kuppalli: Malnad meals; check food options before leaving town."),
            ((50,110),(120,240),(140,290),(35,100),"Agumbe–Kundadri: limited hilltop options; bring water and snacks."),
            ((55,120),(130,260),(150,310),(40,110),"Jog Falls–Sagara: local meals in town; activities may not include food.")],
        "kalyana": [
            ((50,110),(110,230),(130,270),(35,95),"Bidar: jolada rotti, shenga chutney and local khanavali meals."),
            ((50,110),(110,230),(130,270),(35,95),"Basavakalyan: simple local meals; check restaurant timings."),
            ((55,120),(120,250),(140,290),(35,100),"Kalaburagi: jolada rotti meals and local snacks."),
            ((50,110),(110,230),(130,270),(35,95),"Yadgir–Raichur: plan meal breaks around road distances."),
            ((55,120),(120,250),(140,290),(35,100),"Vijayapura: Deccan cuisine; tourist-site cafés may cost more.")]
    }
    food_days = daily_food_profiles.get(key, daily_food_profiles["hoysala"])
    meal_factor = style_profile["meal_factor"]
    day_meals = []
    for day_idx in range(days):
        row = food_days[min(day_idx, len(food_days)-1)]
        ranges = {name: [round(bound * meal_factor) for bound in row[idx]]
                  for idx, name in enumerate(("breakfast", "lunch", "dinner", "snacks"))}
        ranges["total"] = [sum(ranges[k][side] for k in ("breakfast", "lunch", "dinner", "snacks")) for side in (0,1)]
        day_meals.append({"meals": ranges, "food_note": row[4]})
    meal_total = [sum(day_meals[d]["meals"]["total"][side] for d in range(days)) for side in (0,1)]
    meal_ranges = {name: [round(sum(day_meals[d]["meals"][name][side] for d in range(days))/days) for side in (0,1)]
                   for name in ("breakfast", "lunch", "dinner", "snacks")}
    meal_ranges["total"] = [round(meal_total[side]/days) for side in (0,1)]
    stay_range = list(style_profile["stay"])
    transport_range = list(style_profile["transport"])
    factor = {"Budget": 0.75, "Comfort": 1.0, "Premium": 1.6}.get(style, 1.0)
    stay_suggestions = {
        "coastal": [("Udupi town / temple quarter", "A calm homestay or small guesthouse near the temple streets."), ("Karkala or Moodabidri", "A family-run lodge near the temple cluster; keep the evening slow."), ("Kundapura / Maravanthe side", "A coastal homestay or clean town guesthouse with easy road access."), ("Mangaluru city", "A boutique guesthouse near central food and transport options.")],
        "malnad": [("Chikkamagaluru town", "A coffee-themed homestay or garden guesthouse."), ("Chikkamagaluru town", "Stay in town for food and easy early hill access."), ("Kalasa / Mudigere side", "A quiet plantation homestay; confirm road access and meals."), ("Kadur / Chikkamagaluru side", "A practical lodge near your next route."), ("Sringeri town", "A peaceful guesthouse near the temple and riverfront.")],
        "north": [("Hampi village / Hosapete", "A courtyard guesthouse or simple heritage stay; verify river crossing and transfers."), ("Hampi / Hosapete", "A shaded courtyard stay or town hotel depending on tomorrow’s route."), ("Badami town", "A small guesthouse near the cave-temple area."), ("Badami town", "Keep the same base and arrange local transport for Aihole/Pattadakal."), ("Vijayapura / onward town", "Choose a central guesthouse close to onward transport.")],
        "hoysala": [("Belur town", "A calm heritage guesthouse near the temple town."), ("Hassan / Belur side", "A family-run stay with easy road access."), ("Mysuru city", "A cosy boutique stay near walkable evening food."), ("Mysuru city centre", "A quiet room away from busy traffic roads."), ("Mysuru / Srirangapatna side", "Stay toward the next day’s route to avoid backtracking."), ("Mysuru outskirts / onward base", "Choose a homestay after confirming rural transport and dinner.")],
        "wildlife": [("Dandeli town / approved riverside resort zone", "A nature lodge with a garden or sit-out; verify meal and activity inclusions."), ("Dandeli town", "Keep the same room for night two; a shaded outdoor sitting area is a bonus."), ("Kumta town / Yana approach", "A small coastal homestay or town guesthouse; remote trail areas have fewer services."), ("Karwar town", "A breezy guesthouse near the town or beach approach."), ("Sirsi / Yellapur town", "A simple nature stay near town; confirm onward transport.")],
        "bengaluru": [("Jayanagar / Basavanagudi", "A quiet serviced room or boutique guesthouse near cafés and transit."), ("Central Bengaluru / MG Road edge", "A comfortable stay with metro access, preferably on a quieter side street."), ("Central Bengaluru", "Keep one hotel base for the city-centre cluster."), ("South Bengaluru / departure route", "A practical guesthouse close to onward transport.")],
        "royal": [("Mysuru city centre", "A heritage-style guesthouse or cosy boutique room."), ("Mysuru / Srirangapatna side", "Stay in Mysuru unless an early transfer makes another base useful."), ("Mysuru outskirts", "A garden homestay can be restful; check town travel time."), ("Madikeri town", "A coffee-estate homestay or cottage with a covered sit-out."), ("Madikeri outskirts", "A plantation stay with views; arrange transport before dark."), ("Madikeri town", "Stay central for restaurants and hill-road departures."), ("Madikeri / onward route", "Choose according to your actual departure point.")],
        "heritage": [("Badami town", "A sandstone-toned guesthouse or family-run lodge near the caves."), ("Badami town", "Keep the same stay and arrange a local cab for Aihole/Pattadakal."), ("Badami / onward route", "Stay near onward transport or depart after the visit.")],
        "tunga": [("Sringeri town", "A quiet guesthouse near the riverfront and temple complex."), ("Sringeri town", "Keep the same accommodation for the Kigga day trip."), ("Sringeri / Thirthahalli route", "A riverside homestay only if it fits the onward route."), ("Sagara / onward route", "A practical town stay near transport.")],
        "kalyana": [("Bidar old town / fort approach", "A heritage guesthouse or comfortable lodge near the fort area."), ("Bidar town", "Keep the same room for spiritual sites and avoid repacking."), ("Kalaburagi city centre", "A clean city hotel near food and transport."), ("Kalaburagi city centre", "Stay central for the fort, mosque and tomb visits."), ("Kalaburagi / onward route", "Choose a stay near your actual departure route if extending.")]
    }
    stay_factors = {"coastal": [1.0,1.08,1.1,1.25], "malnad": [1.0,1.1,.95,.9,.85], "north": [1.15,1.1,.8,.8,.9], "hoysala": [.9,.85,1.15,1.2,1.0,.85], "wildlife": [1.25,1.25,.85,1.0,.8], "bengaluru": [1.2,1.35,1.3,.9], "royal": [1.15,1.0,.95,1.2,1.25,1.05,.9], "heritage": [.85,.85,.8], "tunga": [.85,.85,.8,.9], "kalyana": [.85,.8,.9,.9,.9]}
    stay_ranges = []
    stay_rows = stay_suggestions.get(key, stay_suggestions["heritage"])
    for idx in range(days):
        base_area, base_vibe = stay_rows[min(idx, len(stay_rows)-1)]
        factor = stay_factors.get(key, [1.0])[min(idx, len(stay_factors.get(key, [1.0]))-1)]
        stay_ranges.append([int(round(style_profile["stay"][0] * factor / 50) * 50), int(round(style_profile["stay"][1] * factor / 50) * 50)])
    schedule = []
    activity_total = 0
    for day_idx in range(days):
        day_stops = []
        selected = selected_places[day_idx*3:day_idx*3+3]
        def priority_match(item, interest):
            text = (item[0] + " " + item[2]).lower()
            canonical = aliases.get(interest, interest)
            return any(word in text for word in vibe_patterns.get(canonical, ()))
        reordered = []
        used = set()
        added = True
        while added:
            added = False
            for interest in interests:
                next_item = next((item for item in selected if item[0] not in used and priority_match(item, interest)), None)
                if next_item:
                    reordered.append(next_item); used.add(next_item[0]); added = True
        reordered.extend(item for item in selected if item[0] not in used)
        selected = reordered
        for slot, item in enumerate(selected):
            name, desc, category, cost = item
            cost = int(cost)
            activity_total += cost
            day_stops.append({"time": times[slot], "name": name, "description": desc,
                              "category": category, "cost": cost})
        stay_area, stay_vibe = stay_rows[min(day_idx, len(stay_rows)-1)]
        stop_names = " ".join(st["name"] for st in day_stops).lower()
        if key in ("hoysala", "royal") and any(word in stop_names for word in ("mysuru", "mysore", "jaganmohan", "devaraja market")):
            stay_area, stay_vibe = ("Mysuru city centre / Palace area", "A central guesthouse or cosy room for palace, gallery and market visits; compare nearby areas before booking.")
        elif key == "hoysala" and any(word in stop_names for word in ("belur", "halebidu", "belavadi")):
            stay_area, stay_vibe = ("Belur / Halebidu / Hassan side", "A practical heritage-town guesthouse; confirm dinner and morning transport before check-in.")
        elif key in ("north", "heritage") and any(word in stop_names for word in ("badami", "aihole", "pattadakal", "mahakuta")):
            stay_area, stay_vibe = ("Badami town", "A small guesthouse near the cave-temple area; ask about breakfast and local cab arrangements.")
        elif key == "north" and any(word in stop_names for word in ("hampi", "vijaya vittala", "virupaksha")):
            stay_area, stay_vibe = ("Hampi village / Hosapete", "A shaded courtyard guesthouse or simple town hotel; check river crossing and transport arrangements.")
        elif key == "wildlife" and any(word in stop_names for word in ("dandeli", "syntheri", "kali river", "sykes point")):
            stay_area, stay_vibe = ("Dandeli town / approved resort zone", "A nature lodge with a garden or sit-out; confirm meal inclusions and safe transport.")
        day_transport = list(style_profile["transport"])
        day_activity = sum(int(st["cost"]) for st in day_stops)
        schedule.append({"day": day_idx+1, "title": f"Day {day_idx+1}: {selected[0][0]}",
                         "stops": day_stops,
                         "budget": {"meals": day_meals[day_idx]["meals"], "food_note": day_meals[day_idx]["food_note"],
                                    "stay": stay_ranges[day_idx], "stay_info": {"area": stay_area, "vibe": stay_vibe, "range": stay_ranges[day_idx]},
                                    "transport": day_transport, "activity_cost": day_activity}})
    nights = max(days - 1, 0)
    stay_total_min = sum(stay_ranges[idx][0] for idx in range(nights))
    stay_total_max = sum(stay_ranges[idx][1] for idx in range(nights))
    transport_total_min = transport_range[0] * days
    transport_total_max = transport_range[1] * days
    day_totals = []
    for idx in range(days):
        overnight_min = stay_ranges[idx][0] if idx < nights else 0
        overnight_max = stay_ranges[idx][1] if idx < nights else 0
        day_activity = sum(int(st["cost"]) for st in schedule[idx]["stops"])
        day_totals.append([day_meals[idx]["meals"]["total"][0] + transport_range[0] + overnight_min + day_activity,
                           day_meals[idx]["meals"]["total"][1] + transport_range[1] + overnight_max + day_activity])
        schedule[idx]["budget"]["daily_total_range"] = day_totals[idx]
    daily_min = min(row[0] for row in day_totals)
    daily_max = max(row[1] for row in day_totals)
    trip_min = meal_total[0] + transport_total_min + stay_total_min + activity_total
    trip_max = meal_total[1] + transport_total_max + stay_total_max + activity_total
    daily_mid = round((daily_min + daily_max) / 2)
    return {
        "circuit_id": key, "circuit_name": circuit["name"], "region": circuit["region"],
        "description": circuit["description"], "days": days, "max_days": max_days, "requested_days": requested_days, "style": style,
        "interests": interests, "transit_recommendation": circuit["transit"],
        "estimated_total": round((trip_min + trip_max) / 2),
        "estimated_total_min": trip_min, "estimated_total_max": trip_max,
        "daily_budget": daily_mid,
        "budget_breakdown": {
            "basis": f"Per person, assuming a room shared by two travellers and {nights} accommodation night(s) for this {days}-day trip; excludes travel to/from the circuit start and shopping. Food estimates vary by day-area; shared/local transport is estimated.",
            "meals": meal_ranges,
            "daily_meals": [d["meals"] for d in day_meals],
            "stay_per_person_per_night": stay_ranges[0],
            "stay_total_range": [stay_total_min, stay_total_max],
            "nights_assumed": nights,
            "local_transport_per_day": transport_range,
            "tickets_and_listed_activities_for_trip": activity_total,
            "daily_total_range": [daily_min, daily_max],
            "daily_totals": day_totals,
            "trip_total_range": [trip_min, trip_max],
        },
        "foods": [{"name": food, "where": "Local eateries, traditional food stalls or speciality shops",
                   "description": "A regional favourite; availability and preparation vary by season and establishment."}
                  for food in circuit["food"]],
        "days_schedule": schedule,
        "notes": ([f"This circuit is planned for up to {max_days} days. Your {requested_days}-day request was adjusted to {days} days to avoid repeating or padding the itinerary."] if requested_days != days else []) + [
            "Travel costs and entry/activity prices are indicative estimates, not live prices or bookings.",
            "Confirm opening hours, access, permits, road conditions and transport schedules before departure.",
            "For rafting, waterfalls, caves and forest activities, use authorised operators and follow current safety advice."
        ],
        "generated_by": "curated-ground-data"
    }
