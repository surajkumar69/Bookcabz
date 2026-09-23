import re

def generate_card(title, desc, img, one_way, round_trip, avg, driver, pax, bags):
    if "Tempo" in title or "Urbania" in title:
        return_kms_text = "Chargeable"
    else:
        return_kms_text = "Not Chargeable"

    # Some basic extraction for the badge text based on pax
    # e.g., "7 Passengers" -> "7+1"
    seats = ""
    if "Passengers" in pax:
        num = pax.split()[0]
        if num.isdigit():
            seats = f" SEATS- ({num}+1)"
    elif "Pax" in pax:
        num = pax.split()[0]
        seats = f" SEATS- ({num}+1)"

    badge_text = f"{title}{seats}".upper()

    return f'''
                <!-- {title} -->
                <div class="bg-white border border-gray-200 rounded-lg p-5 relative flex flex-col hover:shadow-xl transition-shadow duration-300">
                    <div class="absolute top-0 left-0 bg-dark text-white text-[9px] font-bold px-3 py-1.5 uppercase tracking-wider rounded-br-lg z-10">
                        {badge_text}
                    </div>
                    
                    <div class="h-32 mt-6 mb-4 flex items-center justify-center">
                        <img src="assets/images/{img}?v=3" alt="{title}" class="h-full object-contain transition duration-500 hover:scale-105">
                    </div>
                    
                    <h3 class="text-lg font-bold text-dark uppercase mb-0.5">{title}</h3>
                    <p class="text-[11px] text-gray-500 mb-5">{desc} • {pax} • AC • {bags}</p>
                    
                    <div class="flex-grow flex flex-col space-y-4">
                        <!-- One Way -->
                        <div>
                            <div class="text-[11px] text-gray-500 mb-1.5 uppercase tracking-wide">One-Way Trip</div>
                            <div class="flex justify-between text-sm text-dark mb-1">
                                <span>Base Charge</span>
                                <span class="font-bold">₹{one_way}/Km</span>
                            </div>
                            <div class="flex justify-between text-sm text-dark">
                                <span>Return Kms</span>
                                <span class="font-bold text-xs">{return_kms_text}</span>
                            </div>
                        </div>
                        
                        <hr class="border-gray-100">
                        
                        <!-- Round Trip -->
                        <div>
                            <div class="text-[11px] text-gray-500 mb-1.5 uppercase tracking-wide">Round Trip</div>
                            <div class="flex justify-between text-sm text-dark mb-1">
                                <span>Base Charge</span>
                                <span class="font-bold">₹{round_trip}/Km</span>
                            </div>
                            <div class="flex justify-between text-sm text-dark">
                                <span>Coverage Distance</span>
                                <span class="font-bold text-xs">{avg} Km/Day</span>
                            </div>
                        </div>
                        
                        <hr class="border-gray-100">
                        
                        <!-- Driver -->
                        <div>
                            <div class="flex justify-between text-sm text-dark mb-1">
                                <span>Driver Allowance</span>
                                <span class="font-bold">₹{driver}/Day</span>
                            </div>
                            <div class="text-[10px] text-gray-400 mt-1 leading-tight">
                                Toll, State Tax, Parking - Extra<br>
                                Night allowance extra (10PM-6AM)
                            </div>
                        </div>
                    </div>
                    
                    <div class="mt-6">
                        <a href="https://wa.me/919666576797" class="block w-full text-center border border-brand text-dark py-2.5 rounded text-sm font-bold hover:bg-brand hover:text-dark transition uppercase flex items-center justify-center gap-2">
                            <i class="fas fa-car"></i> BOOK NOW
                        </a>
                    </div>
                </div>'''

vehicles = [
    ("Sedan AC", "Etios or Dzire", "fleet_sedan.jpg", "15", "13", "250", "400", "4 Passengers", "2 Bags"),
    ("Ertiga", "Standard MPV", "fleet_ertiga.jpg", "19", "16", "250", "400", "6 Passengers", "3 Bags"),
    ("Kia Carens", "Comfort MPV", "fleet_carens.jpg", "20", "17", "300", "400", "6 Passengers", "3 Bags"),
    ("Innova", "Premium SUV", "fleet_innova.jpg", "20", "17", "300", "400", "7 Passengers", "4 Bags"),
    ("Innova Crysta", "Luxury SUV", "fleet_crysta.jpg", "25", "19", "300", "400", "7 Passengers", "4 Bags"),
    ("Tempo Traveller", "Group Travel", "fleet_tempo.jpg", "23", "23", "300", "500", "12-14 Pax", "Ample Space"),
    ("Urbania", "Luxury Group Travel", "fleet_urbania.jpg", "40", "40", "300", "700", "10-17 Pax", "Recliners")
]

cards_html = "\\n".join([generate_card(*v) for v in vehicles])

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
# We know the fleet section is a grid container
pattern = r'(<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">).*?(</div>\s*</div>\s*</section>)'
match = re.search(pattern, html, flags=re.DOTALL)

if match:
    # Use gap-6 to match the airy feel of the reference
    grid_container = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">'
    new_html = html[:match.start(1)] + grid_container + '\\n' + cards_html + '\\n            ' + match.group(2) + html[match.end(2):]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully updated to reference layout")
else:
    print("Could not find fleet container")
