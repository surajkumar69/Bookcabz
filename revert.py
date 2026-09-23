import re

def generate_card(title, desc, img, one_way, round_trip, avg, driver, pax, bags):
    is_premium = "PREMIUM" if "Crysta" in title else ""
    is_popular = "POPULAR" if "Sedan" in title else ""
    is_luxury = "ULTRA LUXURY" if "Urbania" in title else ""
    
    badge = ""
    if is_popular:
        badge = f'<div class="absolute top-2 right-2 bg-dark text-white text-[10px] font-bold px-2 py-0.5 rounded-full">{is_popular}</div>'
    elif is_premium:
        badge = f'<div class="absolute top-2 right-2 bg-brand text-white text-[10px] font-bold px-2 py-0.5 rounded-full">{is_premium}</div>'
    elif is_luxury:
        badge = f'<div class="absolute top-2 right-2 bg-dark text-brand font-bold text-[10px] px-2 py-0.5 rounded-full border border-brand">{is_luxury}</div>'

    icon_class = "fa-suitcase"
    if "Urbania" in title:
        icon_class = "fa-couch"

    if "Tempo" in title or "Urbania" in title:
        return_kms_text = "Return kms chargeable"
    else:
        return_kms_text = "Return kms not chargeable"

    return f'''
                <!-- {title} -->
                <div class="bg-white rounded-xl overflow-hidden card-hover shadow-lg border border-gray-100 flex flex-col">
                    <div class="h-40 bg-white relative overflow-hidden flex items-center justify-center p-2">
                        <img src="assets/images/{img}?v=3" alt="{title}" class="w-full h-full object-contain object-center transition duration-500 hover:scale-110">
                        {badge}
                    </div>
                    <div class="p-4 flex-grow flex flex-col">
                        <h4 class="text-xl font-bold text-dark mb-0.5 leading-tight">{title}</h4>
                        <p class="text-gray-500 text-[11px] mb-2">{desc}</p>
                        
                        <div class="grid grid-cols-2 gap-x-2 gap-y-1.5 mb-3 border-b border-gray-100 pb-3">
                            <div class="flex items-center text-[11px] text-gray-700">
                                <i class="fas fa-users w-4 text-gray-400"></i> {pax}
                            </div>
                            <div class="flex items-center text-[11px] text-gray-700">
                                <i class="fas fa-snowflake w-4 text-blue-400"></i> AC
                            </div>
                            <div class="flex items-center text-[11px] text-gray-700 col-span-2">
                                <i class="fas {icon_class} w-4 text-gray-400"></i> {bags}
                            </div>
                        </div>
                        
                        <div class="space-y-2 mb-4 mt-auto">
                            <!-- One Way -->
                            <div class="bg-gray-50 rounded p-1.5 border border-gray-100 flex justify-between items-center relative mt-1.5">
                                <div class="absolute -top-1.5 left-2 bg-dark text-brand text-[8px] font-bold px-1 py-0.5 rounded uppercase tracking-wider shadow-sm leading-none">One Way</div>
                                <div class="mt-0.5">
                                    <span class="text-lg font-bold text-dark leading-none">₹{one_way}</span><span class="text-gray-500 text-[9px]">/km</span>
                                </div>
                                <div class="text-right">
                                    <p class="text-[9px] font-bold text-dark uppercase leading-none">{return_kms_text}</p>
                                </div>
                            </div>
                            <!-- Round Trip -->
                            <div class="bg-gray-50 rounded p-1.5 border border-gray-100 flex justify-between items-center relative mt-2.5">
                                <div class="absolute -top-1.5 left-2 bg-brand text-white text-[8px] font-bold px-1 py-0.5 rounded uppercase tracking-wider shadow-sm leading-none">Round Trip</div>
                                <div class="mt-0.5">
                                    <span class="text-lg font-bold text-dark leading-none">₹{round_trip}</span><span class="text-gray-500 text-[9px]">/km</span>
                                </div>
                                <div class="text-right">
                                    <p class="text-[9px] font-bold text-dark leading-none">{avg} km/day avg</p>
                                </div>
                            </div>
                            <!-- Driver Allowance -->
                            <div class="flex justify-between items-center text-xs border-b border-dashed border-gray-200 pb-1.5 pt-1">
                                <span class="text-gray-600 font-medium text-[11px]"><i class="fas fa-id-card text-brand mr-1"></i>Driver Allowance</span>
                                <span class="font-bold text-dark text-[11px]">₹{driver}/day</span>
                            </div>
                            <!-- Note -->
                            <div class="text-[9px] text-gray-500 leading-tight">
                                * Night allowance extra for round trips (10PM-6AM).<br>
                                * Toll, permit & parking charges extra.
                            </div>
                        </div>
                        
                        <div class="mt-auto flex gap-2">
                            <a href="tel:9666576797" class="flex-1 text-center border-2 border-dark text-dark py-1.5 rounded-lg text-sm font-bold hover:bg-dark hover:text-white transition">Call</a>
                            <a href="https://wa.me/919666576797" class="flex-1 text-center bg-brand text-white py-1.5 rounded-lg text-sm font-bold hover:bg-brand-dark transition shadow-md">Book Now</a>
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

pattern = r'(<div class="flex flex-wrap justify-center [^>]+>).*?(</div>\s*</div>\s*</section>)'
match = re.search(pattern, html, flags=re.DOTALL)

if match:
    grid_container = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">'
    new_html = html[:match.start(1)] + grid_container + '\\n' + cards_html + '\\n            ' + match.group(2) + html[match.end(2):]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully reverted layout back to CSS grid")
else:
    print("Could not find the flex container")
