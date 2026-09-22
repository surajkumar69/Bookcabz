import re

html_content = """    <!-- Premium Tariff Section -->
    <style>
        .tariff-scroll::-webkit-scrollbar { display: none; }
        .tariff-scroll { -ms-overflow-style: none; scrollbar-width: none; }
    </style>
    <section id="premium-tariff" class="py-20 bg-gray-50 overflow-hidden relative border-t border-gray-100">
        <div class="container mx-auto px-4">
            <div class="text-center max-w-3xl mx-auto mb-12">
                <h2 class="text-brand font-bold uppercase tracking-wider text-sm mb-2">Pricing Plans</h2>
                <h3 class="text-3xl md:text-4xl font-bold text-dark">Premium Vehicle Tariffs</h3>
                <div class="w-20 h-1 bg-brand mx-auto mt-4 rounded"></div>
            </div>

            <div class="relative">
                <!-- Navigation Arrows -->
                <button onclick="document.getElementById('tariff-carousel').scrollBy({left:-320, behavior:'smooth'})" class="absolute left-0 top-1/2 -translate-y-1/2 -ml-2 lg:-ml-6 z-10 w-12 h-12 bg-white rounded-full shadow-lg flex items-center justify-center text-dark hover:text-brand hover:scale-110 transition border border-gray-100 hidden md:flex">
                    <i class="fas fa-chevron-left"></i>
                </button>
                <button onclick="document.getElementById('tariff-carousel').scrollBy({left:320, behavior:'smooth'})" class="absolute right-0 top-1/2 -translate-y-1/2 -mr-2 lg:-mr-6 z-10 w-12 h-12 bg-white rounded-full shadow-lg flex items-center justify-center text-dark hover:text-brand hover:scale-110 transition border border-gray-100 hidden md:flex">
                    <i class="fas fa-chevron-right"></i>
                </button>

                <!-- Cards Container -->
                <div id="tariff-carousel" class="flex overflow-x-auto snap-x snap-mandatory gap-6 pb-8 pt-4 px-4 -mx-4 scroll-smooth tariff-scroll">
                    
                    <!-- Sedan AC -->
                    <div class="w-[85vw] md:w-[350px] bg-white rounded-2xl shadow-lg border border-gray-100 overflow-hidden snap-center flex-shrink-0 relative group flex flex-col">
                        <div class="h-48 bg-gray-200 relative overflow-hidden">
                            <img src="assets/images/fleet_sedan.jpg" alt="Sedan AC" class="w-full h-full object-cover transition duration-500 group-hover:scale-110">
                        </div>
                        <div class="p-6 flex-grow flex flex-col">
                            <h4 class="text-2xl font-bold text-dark text-center">Sedan AC</h4>
                            <div class="w-12 h-1 bg-brand mx-auto mt-2 mb-6 rounded"></div>

                            <div class="space-y-4 flex-grow">
                                <div class="bg-gray-50 rounded-lg p-4 border border-gray-100 relative">
                                    <div class="absolute -top-3 left-4 bg-dark text-brand text-[10px] font-bold px-2 py-1 rounded">ONE WAY</div>
                                    <div class="flex justify-between items-end mt-1">
                                        <div>
                                            <span class="text-2xl font-extrabold text-dark">₹15</span><span class="text-gray-500 text-sm">/km</span>
                                        </div>
                                        <div class="text-right">
                                            <p class="text-[10px] text-gray-500 font-semibold uppercase">Return KMS</p>
                                            <p class="text-xs font-bold text-dark">Chargeable</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="bg-gray-50 rounded-lg p-4 border border-gray-100 relative">
                                    <div class="absolute -top-3 left-4 bg-brand text-white text-[10px] font-bold px-2 py-1 rounded">ROUND TRIP</div>
                                    <div class="flex justify-between items-end mt-1">
                                        <div>
                                            <span class="text-2xl font-extrabold text-dark">₹13</span><span class="text-gray-500 text-sm">/km</span>
                                        </div>
                                        <div class="text-right">
                                            <p class="text-[10px] text-gray-500 font-semibold uppercase">Avg limit</p>
                                            <p class="text-xs font-bold text-dark">250 km/day</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex justify-between items-center py-2 border-b border-dashed border-gray-200">
                                    <span class="text-sm text-gray-600 font-medium"><i class="fas fa-id-card text-brand mr-2"></i>Driver Allowance</span>
                                    <span class="font-bold text-dark">₹400/day</span>
                                </div>
                            </div>
                            
                            <div class="mt-6">
                                <a href="https://wa.me/919825744216?text=I%20want%20to%20book%20a%20Sedan%20AC" target="_blank" class="block w-full text-center bg-dark text-white py-3 rounded-lg font-bold hover:bg-black transition shadow-md">
                                    BOOK NOW
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Ertiga -->
                    <div class="w-[85vw] md:w-[350px] bg-white rounded-2xl shadow-lg border border-gray-100 overflow-hidden snap-center flex-shrink-0 relative group flex flex-col">
                        <div class="h-48 bg-gray-200 relative overflow-hidden">
                            <img src="assets/images/fleet_ertiga.jpg" alt="Ertiga" class="w-full h-full object-cover transition duration-500 group-hover:scale-110">
                        </div>
                        <div class="p-6 flex-grow flex flex-col">
                            <h4 class="text-2xl font-bold text-dark text-center">Ertiga</h4>
                            <div class="w-12 h-1 bg-brand mx-auto mt-2 mb-6 rounded"></div>

                            <div class="space-y-4 flex-grow">
                                <div class="bg-gray-50 rounded-lg p-4 border border-gray-100 relative">
                                    <div class="absolute -top-3 left-4 bg-dark text-brand text-[10px] font-bold px-2 py-1 rounded">ONE WAY</div>
                                    <div class="flex justify-between items-end mt-1">
                                        <div>
                                            <span class="text-2xl font-extrabold text-dark">₹19</span><span class="text-gray-500 text-sm">/km</span>
                                        </div>
                                        <div class="text-right">
                                            <p class="text-[10px] text-gray-500 font-semibold uppercase">Return KMS</p>
                                            <p class="text-xs font-bold text-dark">Chargeable</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="bg-gray-50 rounded-lg p-4 border border-gray-100 relative">
                                    <div class="absolute -top-3 left-4 bg-brand text-white text-[10px] font-bold px-2 py-1 rounded">ROUND TRIP</div>
                                    <div class="flex justify-between items-end mt-1">
                                        <div>
                                            <span class="text-2xl font-extrabold text-dark">₹16</span><span class="text-gray-500 text-sm">/km</span>
                                        </div>
                                        <div class="text-right">
                                            <p class="text-[10px] text-gray-500 font-semibold uppercase">Avg limit</p>
                                            <p class="text-xs font-bold text-dark">250 km/day</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex justify-between items-center py-2 border-b border-dashed border-gray-200">
                                    <span class="text-sm text-gray-600 font-medium"><i class="fas fa-id-card text-brand mr-2"></i>Driver Allowance</span>
                                    <span class="font-bold text-dark">₹400/day</span>
                                </div>
                            </div>
                            
                            <div class="mt-6">
                                <a href="https://wa.me/919825744216?text=I%20want%20to%20book%20an%20Ertiga" target="_blank" class="block w-full text-center bg-dark text-white py-3 rounded-lg font-bold hover:bg-black transition shadow-md">
                                    BOOK NOW
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Kia Carens -->
                    <div class="w-[85vw] md:w-[350px] bg-white rounded-2xl shadow-lg border border-gray-100 overflow-hidden snap-center flex-shrink-0 relative group flex flex-col">
                        <div class="h-48 bg-gray-200 relative overflow-hidden">
                            <img src="assets/images/fleet_carens.jpg" alt="Kia Carens" class="w-full h-full object-cover transition duration-500 group-hover:scale-110">
                        </div>
                        <div class="p-6 flex-grow flex flex-col">
                            <h4 class="text-2xl font-bold text-dark text-center">Kia Carens</h4>
                            <div class="w-12 h-1 bg-brand mx-auto mt-2 mb-6 rounded"></div>

                            <div class="space-y-4 flex-grow">
                                <div class="bg-gray-50 rounded-lg p-4 border border-gray-100 relative">
                                    <div class="absolute -top-3 left-4 bg-dark text-brand text-[10px] font-bold px-2 py-1 rounded">ONE WAY</div>
                                    <div class="flex justify-between items-end mt-1">
                                        <div>
                                            <span class="text-2xl font-extrabold text-dark">₹20</span><span class="text-gray-500 text-sm">/km</span>
                                        </div>
                                        <div class="text-right">
                                            <p class="text-[10px] text-gray-500 font-semibold uppercase">Return KMS</p>
                                            <p class="text-xs font-bold text-dark">Chargeable</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="bg-gray-50 rounded-lg p-4 border border-gray-100 relative">
                                    <div class="absolute -top-3 left-4 bg-brand text-white text-[10px] font-bold px-2 py-1 rounded">ROUND TRIP</div>
                                    <div class="flex justify-between items-end mt-1">
                                        <div>
                                            <span class="text-2xl font-extrabold text-dark">₹17</span><span class="text-gray-500 text-sm">/km</span>
                                        </div>
                                        <div class="text-right">
                                            <p class="text-[10px] text-gray-500 font-semibold uppercase">Avg limit</p>
                                            <p class="text-xs font-bold text-dark">300 km/day</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex justify-between items-center py-2 border-b border-dashed border-gray-200">
                                    <span class="text-sm text-gray-600 font-medium"><i class="fas fa-id-card text-brand mr-2"></i>Driver Allowance</span>
                                    <span class="font-bold text-dark">₹400/day</span>
                                </div>
                            </div>
                            
                            <div class="mt-6">
                                <a href="https://wa.me/919825744216?text=I%20want%20to%20book%20a%20Kia%20Carens" target="_blank" class="block w-full text-center bg-dark text-white py-3 rounded-lg font-bold hover:bg-black transition shadow-md">
                                    BOOK NOW
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Innova -->
                    <div class="w-[85vw] md:w-[350px] bg-white rounded-2xl shadow-lg border border-gray-100 overflow-hidden snap-center flex-shrink-0 relative group flex flex-col">
                        <div class="h-48 bg-gray-200 relative overflow-hidden">
                            <img src="assets/images/fleet_innova.jpg" alt="Innova" class="w-full h-full object-cover transition duration-500 group-hover:scale-110">
                        </div>
                        <div class="p-6 flex-grow flex flex-col">
                            <h4 class="text-2xl font-bold text-dark text-center">Innova</h4>
                            <div class="w-12 h-1 bg-brand mx-auto mt-2 mb-6 rounded"></div>

                            <div class="space-y-4 flex-grow">
                                <div class="bg-gray-50 rounded-lg p-4 border border-gray-100 relative">
                                    <div class="absolute -top-3 left-4 bg-dark text-brand text-[10px] font-bold px-2 py-1 rounded">ONE WAY</div>
                                    <div class="flex justify-between items-end mt-1">
                                        <div>
                                            <span class="text-2xl font-extrabold text-dark">₹20</span><span class="text-gray-500 text-sm">/km</span>
                                        </div>
                                        <div class="text-right">
                                            <p class="text-[10px] text-gray-500 font-semibold uppercase">Return KMS</p>
                                            <p class="text-xs font-bold text-dark">Chargeable</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="bg-gray-50 rounded-lg p-4 border border-gray-100 relative">
                                    <div class="absolute -top-3 left-4 bg-brand text-white text-[10px] font-bold px-2 py-1 rounded">ROUND TRIP</div>
                                    <div class="flex justify-between items-end mt-1">
                                        <div>
                                            <span class="text-2xl font-extrabold text-dark">₹17</span><span class="text-gray-500 text-sm">/km</span>
                                        </div>
                                        <div class="text-right">
                                            <p class="text-[10px] text-gray-500 font-semibold uppercase">Avg limit</p>
                                            <p class="text-xs font-bold text-dark">300 km/day</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex justify-between items-center py-2 border-b border-dashed border-gray-200">
                                    <span class="text-sm text-gray-600 font-medium"><i class="fas fa-id-card text-brand mr-2"></i>Driver Allowance</span>
                                    <span class="font-bold text-dark">₹400/day</span>
                                </div>
                            </div>
                            
                            <div class="mt-6">
                                <a href="https://wa.me/919825744216?text=I%20want%20to%20book%20an%20Innova" target="_blank" class="block w-full text-center bg-dark text-white py-3 rounded-lg font-bold hover:bg-black transition shadow-md">
                                    BOOK NOW
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Innova Crysta -->
                    <div class="w-[85vw] md:w-[350px] bg-white rounded-2xl shadow-lg border border-gray-100 overflow-hidden snap-center flex-shrink-0 relative group flex flex-col">
                        <div class="h-48 bg-gray-200 relative overflow-hidden">
                            <img src="assets/images/fleet_crysta.jpg" alt="Innova Crysta" class="w-full h-full object-cover transition duration-500 group-hover:scale-110">
                        </div>
                        <div class="p-6 flex-grow flex flex-col">
                            <h4 class="text-2xl font-bold text-dark text-center">Innova Crysta</h4>
                            <div class="w-12 h-1 bg-brand mx-auto mt-2 mb-6 rounded"></div>

                            <div class="space-y-4 flex-grow">
                                <div class="bg-gray-50 rounded-lg p-4 border border-gray-100 relative">
                                    <div class="absolute -top-3 left-4 bg-dark text-brand text-[10px] font-bold px-2 py-1 rounded">ONE WAY</div>
                                    <div class="flex justify-between items-end mt-1">
                                        <div>
                                            <span class="text-2xl font-extrabold text-dark">₹25</span><span class="text-gray-500 text-sm">/km</span>
                                        </div>
                                        <div class="text-right">
                                            <p class="text-[10px] text-gray-500 font-semibold uppercase">Return KMS</p>
                                            <p class="text-xs font-bold text-dark">Chargeable</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="bg-gray-50 rounded-lg p-4 border border-gray-100 relative">
                                    <div class="absolute -top-3 left-4 bg-brand text-white text-[10px] font-bold px-2 py-1 rounded">ROUND TRIP</div>
                                    <div class="flex justify-between items-end mt-1">
                                        <div>
                                            <span class="text-2xl font-extrabold text-dark">₹19</span><span class="text-gray-500 text-sm">/km</span>
                                        </div>
                                        <div class="text-right">
                                            <p class="text-[10px] text-gray-500 font-semibold uppercase">Avg limit</p>
                                            <p class="text-xs font-bold text-dark">300 km/day</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex justify-between items-center py-2 border-b border-dashed border-gray-200">
                                    <span class="text-sm text-gray-600 font-medium"><i class="fas fa-id-card text-brand mr-2"></i>Driver Allowance</span>
                                    <span class="font-bold text-dark">₹400/day</span>
                                </div>
                            </div>
                            
                            <div class="mt-6">
                                <a href="https://wa.me/919825744216?text=I%20want%20to%20book%20an%20Innova%20Crysta" target="_blank" class="block w-full text-center bg-dark text-white py-3 rounded-lg font-bold hover:bg-black transition shadow-md">
                                    BOOK NOW
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Tempo Traveller -->
                    <div class="w-[85vw] md:w-[350px] bg-white rounded-2xl shadow-lg border border-gray-100 overflow-hidden snap-center flex-shrink-0 relative group flex flex-col">
                        <div class="h-48 bg-gray-200 relative overflow-hidden">
                            <img src="assets/images/fleet_tempo.jpg" alt="Tempo Traveller" class="w-full h-full object-cover transition duration-500 group-hover:scale-110">
                        </div>
                        <div class="p-6 flex-grow flex flex-col">
                            <h4 class="text-2xl font-bold text-dark text-center">Tempo Traveller</h4>
                            <div class="w-12 h-1 bg-brand mx-auto mt-2 mb-6 rounded"></div>

                            <div class="space-y-4 flex-grow">
                                <div class="bg-gray-50 rounded-lg p-4 border border-gray-100 relative">
                                    <div class="absolute -top-3 left-4 bg-dark text-brand text-[10px] font-bold px-2 py-1 rounded">ONE WAY</div>
                                    <div class="flex justify-between items-end mt-1">
                                        <div>
                                            <span class="text-2xl font-extrabold text-dark">₹23</span><span class="text-gray-500 text-sm">/km</span>
                                        </div>
                                        <div class="text-right">
                                            <p class="text-[10px] text-gray-500 font-semibold uppercase">Return KMS</p>
                                            <p class="text-xs font-bold text-dark">Chargeable</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="bg-gray-50 rounded-lg p-4 border border-gray-100 relative">
                                    <div class="absolute -top-3 left-4 bg-brand text-white text-[10px] font-bold px-2 py-1 rounded">ROUND TRIP</div>
                                    <div class="flex justify-between items-end mt-1">
                                        <div>
                                            <span class="text-2xl font-extrabold text-dark">₹23</span><span class="text-gray-500 text-sm">/km</span>
                                        </div>
                                        <div class="text-right">
                                            <p class="text-[10px] text-gray-500 font-semibold uppercase">Avg limit</p>
                                            <p class="text-xs font-bold text-dark">300 km/day</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex justify-between items-center py-2 border-b border-dashed border-gray-200">
                                    <span class="text-sm text-gray-600 font-medium"><i class="fas fa-id-card text-brand mr-2"></i>Driver Allowance</span>
                                    <span class="font-bold text-dark">₹500/day</span>
                                </div>
                            </div>
                            
                            <div class="mt-6">
                                <a href="https://wa.me/919825744216?text=I%20want%20to%20book%20a%20Tempo%20Traveller" target="_blank" class="block w-full text-center bg-dark text-white py-3 rounded-lg font-bold hover:bg-black transition shadow-md">
                                    BOOK NOW
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Urbania -->
                    <div class="w-[85vw] md:w-[350px] bg-white rounded-2xl shadow-lg border border-gray-100 overflow-hidden snap-center flex-shrink-0 relative group flex flex-col">
                        <div class="h-48 bg-gray-200 relative overflow-hidden">
                            <img src="assets/images/fleet_urbania.jpg" alt="Urbania" class="w-full h-full object-cover transition duration-500 group-hover:scale-110">
                        </div>
                        <div class="p-6 flex-grow flex flex-col">
                            <h4 class="text-2xl font-bold text-dark text-center">Urbania</h4>
                            <div class="w-12 h-1 bg-brand mx-auto mt-2 mb-6 rounded"></div>

                            <div class="space-y-4 flex-grow">
                                <div class="bg-gray-50 rounded-lg p-4 border border-gray-100 relative">
                                    <div class="absolute -top-3 left-4 bg-dark text-brand text-[10px] font-bold px-2 py-1 rounded">ONE WAY</div>
                                    <div class="flex justify-between items-end mt-1">
                                        <div>
                                            <span class="text-2xl font-extrabold text-dark">₹40</span><span class="text-gray-500 text-sm">/km</span>
                                        </div>
                                        <div class="text-right">
                                            <p class="text-[10px] text-gray-500 font-semibold uppercase">Return KMS</p>
                                            <p class="text-xs font-bold text-dark">Chargeable</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="bg-gray-50 rounded-lg p-4 border border-gray-100 relative">
                                    <div class="absolute -top-3 left-4 bg-brand text-white text-[10px] font-bold px-2 py-1 rounded">ROUND TRIP</div>
                                    <div class="flex justify-between items-end mt-1">
                                        <div>
                                            <span class="text-2xl font-extrabold text-dark">₹40</span><span class="text-gray-500 text-sm">/km</span>
                                        </div>
                                        <div class="text-right">
                                            <p class="text-[10px] text-gray-500 font-semibold uppercase">Avg limit</p>
                                            <p class="text-xs font-bold text-dark">300 km/day</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex justify-between items-center py-2 border-b border-dashed border-gray-200">
                                    <span class="text-sm text-gray-600 font-medium"><i class="fas fa-id-card text-brand mr-2"></i>Driver Allowance</span>
                                    <span class="font-bold text-dark">₹700/day</span>
                                </div>
                            </div>
                            
                            <div class="mt-6">
                                <a href="https://wa.me/919825744216?text=I%20want%20to%20book%20an%20Urbania" target="_blank" class="block w-full text-center bg-dark text-white py-3 rounded-lg font-bold hover:bg-black transition shadow-md">
                                    BOOK NOW
                                </a>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

            <!-- Notes Section -->
            <div class="max-w-4xl mx-auto mt-8 bg-white p-6 rounded-2xl shadow-md border border-gray-100 relative overflow-hidden">
                <div class="absolute left-0 top-0 bottom-0 w-2 bg-brand"></div>
                <h4 class="font-bold text-dark mb-4 flex items-center text-lg pl-2"><i class="fas fa-info-circle text-brand mr-3 text-xl"></i> Additional Charges & Information</h4>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-gray-600 font-medium pl-2">
                    <div class="flex items-start">
                        <i class="fas fa-moon text-gray-400 mt-1 mr-3"></i>
                        <p>Night allowance is extra for round trips travelling between <strong class="text-dark">10:00 PM and 06:00 AM</strong>.</p>
                    </div>
                    <div class="flex items-start">
                        <i class="fas fa-road text-gray-400 mt-1 mr-3"></i>
                        <p><strong class="text-dark">Toll, permit and parking charges</strong> are extra on all trips.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to insert this right after </section> of the fleet section.
fleet_end_marker = '<!-- Bengaluru Cab Service Section -->'
if fleet_end_marker in html:
    html = html.replace(fleet_end_marker, html_content + '\\n    ' + fleet_end_marker)
else:
    print("Could not find the marker to insert")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Successfully injected the new premium tariff section.")
