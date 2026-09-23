import re

def generate_card(title, desc, img, one_way, round_trip, avg, driver, pax, bags):
    is_premium = "PREMIUM" if "Crysta" in title else ""
    is_popular = "POPULAR" if "Sedan" in title else ""
    is_luxury = "ULTRA LUXURY" if "Urbania" in title else ""
    
    badge = ""
    if is_popular:
        badge = f'<div class="absolute top-4 right-4 bg-dark text-white text-xs font-bold px-3 py-1 rounded-full">{is_popular}</div>'
    elif is_premium:
        badge = f'<div class="absolute top-4 right-4 bg-brand text-white text-xs font-bold px-3 py-1 rounded-full">{is_premium}</div>'
    elif is_luxury:
        badge = f'<div class="absolute top-4 right-4 bg-dark text-brand font-bold text-xs px-3 py-1 rounded-full border border-brand">{is_luxury}</div>'

    icon_class = "fa-suitcase"
    if "Urbania" in title:
        icon_class = "fa-couch"

    if "Tempo" in title or "Urbania" in title:
        return_kms_text = "Return kms chargeable"
    else:
        return_kms_text = "Return kms not chargeable"

    return f'''
                <!-- {title} -->
                <div class="bg-white rounded-2xl overflow-hidden card-hover shadow-lg border border-gray-100 flex flex-col">
                    <div class="h-48 bg-white relative overflow-hidden flex items-center justify-center p-2">
                        <img src="assets/images/{img}?v=3" alt="{title}" class="w-full h-full object-contain object-center transition duration-500 hover:scale-110">
                        {badge}
                    </div>
                    <div class="p-5 flex-grow flex flex-col">
                        <h4 class="text-2xl font-bold text-dark mb-1">{title}</h4>
                        <p class="text-gray-500 text-sm mb-3">{desc}</p>
                        
                        <div class="grid grid-cols-2 gap-3 mb-4 border-b border-gray-100 pb-4">
                            <div class="flex items-center text-sm text-gray-700">
                                <i class="fas fa-users w-5 text-gray-400"></i> {pax}
                            </div>
                            <div class="flex items-center text-sm text-gray-700">
                                <i class="fas fa-snowflake w-5 text-blue-400"></i> AC
                            </div>
                            <div class="flex items-center text-sm text-gray-700 col-span-2">
                                <i class="fas {icon_class} w-5 text-gray-400"></i> {bags}
                            </div>
                        </div>
                        
                        <div class="space-y-4 flex-grow mb-5">
                            <!-- One Way -->
                            <div class="bg-gray-50 rounded-lg p-3 border border-gray-100 flex justify-between items-center relative mt-2">
                                <div class="absolute -top-2.5 left-3 bg-dark text-brand text-[10px] font-bold px-2 py-0.5 rounded uppercase tracking-wider shadow-sm">One Way</div>
                                <div class="mt-1">
                                    <span class="text-xl font-bold text-dark">₹{one_way}</span><span class="text-gray-500 text-xs">/km</span>
                                </div>
                                <div class="text-right">
                                    <p class="text-[10px] font-bold text-dark uppercase">{return_kms_text}</p>
                                </div>
                            </div>
                            <!-- Round Trip -->
                            <div class="bg-gray-50 rounded-lg p-3 border border-gray-100 flex justify-between items-center relative mt-4">
                                <div class="absolute -top-2.5 left-3 bg-brand text-white text-[10px] font-bold px-2 py-0.5 rounded uppercase tracking-wider shadow-sm">Round Trip</div>
                                <div class="mt-1">
                                    <span class="text-xl font-bold text-dark">₹{round_trip}</span><span class="text-gray-500 text-xs">/km</span>
                                </div>
                                <div class="text-right">
                                    <p class="text-[10px] font-bold text-dark">{avg} km/day avg</p>
                                </div>
                            </div>
                            <!-- Driver Allowance -->
                            <div class="flex justify-between items-center text-sm border-b border-dashed border-gray-200 pb-2 mt-3">
                                <span class="text-gray-600 font-medium"><i class="fas fa-id-card text-brand mr-2"></i>Driver Allowance</span>
                                <span class="font-bold text-dark">₹{driver}/day</span>
                            </div>
                            <!-- Note -->
                            <div class="text-[11px] text-gray-500 leading-tight pt-1">
                                * Night allowance extra for round trips (10PM-6AM).<br>
                                * Toll, permit & parking charges extra.
                            </div>
                        </div>
                        
                        <div class="mt-auto flex gap-2">
                            <a href="tel:9666576797" class="flex-1 text-center border-2 border-dark text-dark py-2.5 rounded-lg font-bold hover:bg-dark hover:text-white transition">Call</a>
                            <a href="https://wa.me/919666576797" class="flex-1 text-center bg-brand text-white py-2.5 rounded-lg font-bold hover:bg-brand-dark transition shadow-md">Book Now</a>
                        </div>
                    </div>
                </div>'''

vehicles = [
    ("Sedan AC", "Etios, Dzire or Equivalent", "fleet_sedan.jpg", "15", "13", "250", "400", "4 Passengers", "2 Bags"),
    ("Ertiga", "Standard MPV", "fleet_ertiga.jpg", "19", "16", "250", "400", "6 Passengers", "3 Bags"),
    ("Kia Carens", "Comfort MPV", "fleet_carens.jpg", "20", "17", "300", "400", "6 Passengers", "3 Bags"),
    ("Innova", "Premium SUV", "fleet_innova.jpg", "20", "17", "300", "400", "7 Passengers", "4 Bags"),
    ("Innova Crysta", "Luxury SUV", "fleet_crysta.jpg", "25", "19", "300", "400", "7 Passengers", "4 Bags"),
    ("Tempo Traveller", "Group Travel Van", "fleet_tempo.jpg", "23", "23", "300", "500", "12-14 Pax", "Ample Space"),
    ("Urbania", "Luxury Group Travel", "fleet_urbania.jpg", "40", "40", "300", "700", "10-17 Pax", "Recliners")
]

cards_html = "\\n".join([generate_card(*v) for v in vehicles])

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Restore mb-16 on the fleet header
pattern_header = r'(<div class="text-center max-w-3xl mx-auto )mb-8(">\s*<h2)'
html = re.sub(pattern_header, r'\g<1>mb-16\g<2>', html)

# Restore the original grid and the original cards
pattern_grid = r'(<div class="grid [^>]+>).*?(</div>\s*</div>\s*</section>)'
match = re.search(pattern_grid, html, flags=re.DOTALL)

if match:
    grid_container = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">'
    new_html = html[:match.start(1)] + grid_container + '\\n' + cards_html + '\\n            ' + match.group(2) + html[match.end(2):]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully reverted all 3:00 PM changes")
else:
    print("Could not find grid container")
