import re

def generate_card(title, desc, img, one_way, round_trip, avg, driver, pax, bags):
    is_premium = "PREMIUM" if "Crysta" in title else ""
    is_popular = "POPULAR" if "Sedan" in title else ""
    is_luxury = "ULTRA LUXURY" if "Urbania" in title else ""
    
    badge = ""
    if is_popular:
        badge = f'<div class="absolute top-3 right-3 bg-dark text-white text-[10px] font-bold px-2.5 py-1 rounded-full shadow-sm">{is_popular}</div>'
    elif is_premium:
        badge = f'<div class="absolute top-3 right-3 bg-brand text-dark text-[10px] font-bold px-2.5 py-1 rounded-full shadow-sm">{is_premium}</div>'
    elif is_luxury:
        badge = f'<div class="absolute top-3 right-3 bg-white text-dark font-bold text-[10px] px-2.5 py-1 rounded-full shadow-sm border border-gray-100">{is_luxury}</div>'

    icon_class = "fa-suitcase"
    if "Urbania" in title:
        icon_class = "fa-couch"

    if "Tempo" in title or "Urbania" in title:
        return_kms_text = "Return kms chargeable"
    else:
        return_kms_text = "Return kms not chargeable"

    return f'''
                <!-- {title} -->
                <div class="w-full md:w-[calc(50%-12px)] lg:w-[calc(33.333%-16px)] flex flex-col bg-white rounded-2xl overflow-hidden card-hover shadow-[0_4px_20px_rgba(0,0,0,0.05)] border border-gray-100">
                    <div class="h-44 bg-gray-50/50 relative overflow-hidden flex items-center justify-center p-4">
                        <img src="assets/images/{img}?v=3" alt="{title}" class="w-full h-full object-contain object-center transition duration-500 hover:scale-110 drop-shadow-md">
                        {badge}
                    </div>
                    <div class="p-5 flex-grow flex flex-col bg-white">
                        <div class="mb-4">
                            <h4 class="text-xl font-extrabold text-dark mb-1 leading-tight">{title}</h4>
                            <p class="text-gray-500 text-xs">{desc}</p>
                        </div>
                        
                        <div class="grid grid-cols-2 gap-x-2 gap-y-2 mb-4 border-b border-gray-100 pb-4">
                            <div class="flex items-center text-xs text-gray-700 font-medium">
                                <i class="fas fa-users w-5 text-brand opacity-80"></i> {pax}
                            </div>
                            <div class="flex items-center text-xs text-gray-700 font-medium">
                                <i class="fas fa-snowflake w-5 text-blue-400 opacity-80"></i> AC
                            </div>
                            <div class="flex items-center text-xs text-gray-700 font-medium col-span-2">
                                <i class="fas {icon_class} w-5 text-gray-400 opacity-80"></i> {bags}
                            </div>
                        </div>
                        
                        <div class="space-y-2 mb-4 mt-auto">
                            <!-- One Way -->
                            <div class="bg-white rounded-lg p-2.5 border border-gray-100 shadow-sm flex justify-between items-center relative mt-2 group hover:border-brand/30 transition">
                                <div class="absolute -top-2 left-2 bg-dark text-white text-[8px] font-bold px-1.5 py-0.5 rounded shadow-sm uppercase tracking-wider">One Way</div>
                                <div class="mt-1">
                                    <span class="text-lg font-extrabold text-dark">₹{one_way}</span><span class="text-gray-500 text-[10px] font-medium">/km</span>
                                </div>
                                <div class="text-right">
                                    <p class="text-[9px] font-bold text-gray-700 uppercase">{return_kms_text}</p>
                                </div>
                            </div>
                            <!-- Round Trip -->
                            <div class="bg-gray-50 rounded-lg p-2.5 border border-gray-100 shadow-sm flex justify-between items-center relative mt-3 group hover:border-brand/30 transition">
                                <div class="absolute -top-2 left-2 bg-brand text-dark text-[8px] font-bold px-1.5 py-0.5 rounded shadow-sm uppercase tracking-wider">Round Trip</div>
                                <div class="mt-1">
                                    <span class="text-lg font-extrabold text-dark">₹{round_trip}</span><span class="text-gray-500 text-[10px] font-medium">/km</span>
                                </div>
                                <div class="text-right">
                                    <p class="text-[9px] font-bold text-gray-700">{avg} km/day avg</p>
                                </div>
                            </div>
                            <!-- Driver Allowance -->
                            <div class="flex justify-between items-center text-xs border-b border-dashed border-gray-200 pb-2 pt-1.5">
                                <span class="text-gray-600 font-semibold text-xs"><i class="fas fa-id-card text-brand mr-1.5"></i>Driver Allowance</span>
                                <span class="font-extrabold text-dark text-xs">₹{driver}/day</span>
                            </div>
                            <!-- Note -->
                            <div class="text-[9px] text-gray-400 font-medium leading-tight pt-1">
                                * Night allowance extra for round trips (10PM-6AM).<br>
                                * Toll, permit & parking charges extra.
                            </div>
                        </div>
                        
                        <div class="mt-2 flex gap-2">
                            <a href="tel:+919825744216" class="flex-1 text-center border-2 border-dark text-dark py-2 rounded-lg text-sm font-bold hover:bg-dark hover:text-white transition flex items-center justify-center gap-1.5"><i class="fas fa-phone text-xs"></i> Call</a>
                            <a href="https://wa.me/919666576797" class="flex-1 text-center bg-brand text-white py-2 rounded-lg text-sm font-bold hover:bg-brand-dark transition shadow-md flex items-center justify-center gap-1.5"><i class="fab fa-whatsapp text-sm"></i> Book</a>
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

import re
pattern = r'(<div class="grid [^>]+>).*?(</div>\s*</div>\s*</section>)'
match = re.search(pattern, html, flags=re.DOTALL)

if match:
    flex_container = '<div class="flex flex-wrap justify-center gap-6 max-w-7xl mx-auto">'
    new_html = html[:match.start(1)] + flex_container + '\\n' + cards_html + '\\n            ' + match.group(2) + html[match.end(2):]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully updated layout to flexbox")
else:
    # Try alternate if it's already flex
    pattern = r'(<div class="flex flex-wrap justify-center [^>]+>).*?(</div>\s*</div>\s*</section>)'
    match = re.search(pattern, html, flags=re.DOTALL)
    if match:
        flex_container = '<div class="flex flex-wrap justify-center gap-6 max-w-7xl mx-auto">'
        new_html = html[:match.start(1)] + flex_container + '\\n' + cards_html + '\\n            ' + match.group(2) + html[match.end(2):]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Successfully updated layout to flexbox")
    else:
        print("Could not find container")
