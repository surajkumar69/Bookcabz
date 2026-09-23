import re

def generate_card(title, desc, img, one_way, round_trip, avg, driver, pax, bags):
    if "Tempo" in title or "Urbania" in title:
        return_kms_text = "Chargeable"
    else:
        return_kms_text = "Not Chargeable"

    seats = ""
    if "Passengers" in pax:
        num = pax.split()[0]
        if num.isdigit():
            seats = f" - ({num}+1)"
    elif "Pax" in pax:
        num = pax.split()[0]
        seats = f" - ({num}+1)"

    badge_text = f"{title}{seats}".upper()

    return f'''
                <!-- {title} -->
                <div class="bg-white border border-gray-200 rounded-lg p-5 relative flex flex-col hover:shadow-md transition-shadow duration-300">
                    <!-- Badge -->
                    <div class="absolute top-0 left-0 bg-dark text-white text-[10px] font-bold px-3 py-1.5 uppercase tracking-wider rounded-br-lg z-10">
                        {badge_text}
                    </div>
                    
                    <!-- Image -->
                    <div class="h-36 mt-5 mb-3 flex items-center justify-center">
                        <img src="assets/images/{img}?v=3" alt="{title}" class="h-full object-contain transition duration-500 hover:scale-105">
                    </div>
                    
                    <!-- Title & Desc -->
                    <h3 class="text-lg font-bold text-dark uppercase mb-0.5">{title}</h3>
                    <p class="text-[11px] text-gray-500 mb-4">{desc} • {pax} • AC • {bags}</p>
                    
                    <!-- Details -->
                    <div class="flex-grow flex flex-col space-y-3">
                        <!-- One Way -->
                        <div>
                            <div class="text-[11px] text-brand font-bold mb-1 uppercase tracking-wide">One-Way Trip</div>
                            <div class="flex justify-between text-sm text-dark mb-0.5">
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
                            <div class="text-[11px] text-brand font-bold mb-1 uppercase tracking-wide">Round Trip</div>
                            <div class="flex justify-between text-sm text-dark mb-0.5">
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
                            <div class="flex justify-between text-sm text-dark mb-1 mt-1">
                                <span>Driver Batta</span>
                                <span class="font-bold">₹{driver}/Day</span>
                            </div>
                            <div class="text-[10px] text-gray-400 mt-0.5 leading-tight">
                                Toll, State Tax, Parking - Extra
                            </div>
                        </div>
                    </div>
                    
                    <!-- Button -->
                    <div class="mt-5 mt-auto">
                        <a href="https://wa.me/919666576797" class="block w-full text-center border-2 border-brand text-dark py-2 rounded font-bold text-sm hover:bg-brand hover:text-dark transition uppercase flex items-center justify-center gap-2">
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

cards_html = "\n".join([generate_card(*v) for v in vehicles])

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure we only touch the fleet section!
fleet_pattern = r'(<section id="fleet"[^>]*>.*?</section>)'
fleet_match = re.search(fleet_pattern, html, flags=re.DOTALL)

if fleet_match:
    fleet_html = fleet_match.group(1)
    
    # 1. Update the container width in the fleet section
    container_pattern = r'(<section id="fleet"[^>]*>\s*)<div class="(?:container )?mx-auto px-4[^"]*">'
    fleet_html = re.sub(container_pattern, r'\1<div class="max-w-[1450px] mx-auto px-4">', fleet_html)
    
    # 2. Replace the cards grid in the fleet section
    grid_pattern = r'(<div class="grid [^>]+>).*?(</div>\s*</div>\s*</section>)'
    # We find the FIRST grid in the fleet section (which is the outer cards container)
    grid_match = re.search(grid_pattern, fleet_html, flags=re.DOTALL)
    
    if grid_match:
        grid_container = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">'
        new_fleet_html = fleet_html[:grid_match.start(1)] + grid_container + '\n' + cards_html + '\n            ' + grid_match.group(2) + fleet_html[grid_match.end(2):]
        
        # 3. Replace the old fleet section with the new one in the main html
        new_html = html[:fleet_match.start(1)] + new_fleet_html + html[fleet_match.end(1):]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Successfully updated only the fleet layout without touching the home section.")
    else:
        print("Could not find grid container inside fleet section.")
else:
    print("Could not find fleet section.")
