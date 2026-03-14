import json

raw_data = """H|george washington,washington|He commanded the disastrous Fort Necessity.|He put down the Whiskey Rebellion.|He crossed the Delaware River.|He is on the one-dollar bill.|name this first US President.
H|abraham lincoln,lincoln|He gave the Cooper Union speech.|He participated in a series of debates with Stephen Douglas.|He delivered the Gettysburg Address.|He was assassinated by John Wilkes Booth.|name this 16th US President.
H|julius caesar,caesar|He won the Battle of Alesia against Vercingetorix.|He famously crossed the Rubicon river.|He was assassinated on the Ides of March.|He was a Roman dictator who dated Cleopatra.|name this Roman leader.
H|alexander the great,alexander|He won the Battle of Gaugamela.|He tamed the horse Bucephalus.|He conquered the Persian Empire.|He was a king of Macedon who never lost a battle.|name this great conqueror.
H|napoleon bonaparte,napoleon|He won the Battle of Austerlitz.|He was exiled to the island of Elba.|He was defeated at the Battle of Waterloo.|He was a French emperor who crowned himself.|name this French military leader.
H|winston churchill,churchill|He served as First Lord of the Admiralty during Gallipoli.|He promised "blood, toil, tears, and sweat."|He led his country during the Blitz.|He was the UK Prime Minister during World War II.|name this British leader.
H|cleopatra,cleopatra vii|She was the last active ruler of the Ptolemaic Kingdom.|She fought alongside Mark Antony at Actium.|She supposedly committed suicide with an asp.|She was a famous queen of Egypt.|name this Egyptian queen.
H|franklin d roosevelt,fdr,roosevelt|He attempted to pack the Supreme Court.|He gave "fireside chats" to the nation.|He led the US through most of World War II.|He was the only US President elected four times.|name this man who proposed the New Deal.
H|genghis khan,temujin|He was born with the name Temujin.|He established the Yassa code of law.|He united the nomadic tribes of the steppes.|He founded the Mongol Empire.|name this Asian conqueror.
H|joan of arc,joan|She lifted the siege of Orleans.|She was captured by the Burgundians and sold to the English.|She was burned at the stake in Rouen.|She was a French peasant girl who claimed divine guidance.|name this heroine of France.
H|gandhi,mahatma gandhi|He organized the Salt March to Dandi.|He advocated for nonviolent resistance called Satyagraha.|He was assassinated by Nathuram Godse.|He led India to independence from British rule.|name this Indian leader.
H|nelson mandela,mandela|He was imprisoned on Robben Island for 27 years.|He was a leader of the African National Congress.|He worked with F.W. de Klerk to end apartheid.|He became the first black president of his country.|name this South African leader.
H|thomas jefferson,jefferson|He authorized the Lewis and Clark expedition.|He served as the first US Secretary of State.|He purchased the Louisiana Territory from France.|He was the primary author of the Declaration of Independence.|name this third US President.
H|theodore roosevelt,teddy roosevelt|He led the Rough Riders at San Juan Hill.|He was associated with the "Bull Moose" Party.|He promised a "Square Deal" for Americans.|He famously said "speak softly and carry a big stick."|name this 26th US President.
H|martin luther king jr,mlk,king|He wrote the "Letter from Birmingham Jail."|He led the Montgomery bus boycott.|He was assassinated at the Lorraine Motel in Memphis.|He delivered the "I Have a Dream" speech.|name this American civil rights leader.
H|john f kennedy,jfk,kennedy|He dealt with the Bay of Pigs invasion.|He diffused the Cuban Missile Crisis.|He was assassinated by Lee Harvey Oswald in Dallas.|He was the 35th US President.|name this President of the 1960s.
H|christopher columbus,columbus|He initially landed in the Bahamas at San Salvador.|He governed Hispaniola poorly and was arrested.|He sailed the Nina, Pinta, and Santa Maria.|He completed four voyages across the Atlantic Ocean.|name this Italian explorer who "discovered" the New World.
H|richard nixon,nixon|He traveled to China to normalize relations.|He ordered the "Saturday Night Massacre."|He ended US involvement in the Vietnam War.|He resigned due to the Watergate scandal.|name this 37th US President.
H|marie antoinette,antoinette|She was born an Archduchess of Austria.|She was married to King Louis XVI.|She is apocryphally quoted as saying "Let them eat cake."|She was a queen who was executed by guillotine.|name this French queen.
H|queen elizabeth i,elizabeth i|She was the daughter of Anne Boleyn.|She defeated the Spanish Armada in 1588.|She was known as the "Virgin Queen."|She was a powerful Tudor monarch of England.|name this English queen.
H|thomas edison,edison|He established a laboratory in Menlo Park.|He engaged in the "War of the Currents" with Nikola Tesla.|He invented the phonograph.|He developed a practical incandescent light bulb.|name this American inventor.
H|henry viii,henry 8|He was awarded the title "Defender of the Faith."|He separated the Church of England from papal authority.|He fathered Edward VI, Mary I, and Elizabeth I.|He notoriously had six wives.|name this Tudor king of England.
H|mao zedong,mao|He launched the Let a Hundred Flowers Bloom campaign.|He initiated the Great Leap Forward.|He led the Long March.|He founded the People's Republic of China.|name this communist leader.
H|vladimir lenin,lenin|He led the Bolshevik faction of the Russian Social Democratic Labour Party.|He signed the Treaty of Brest-Litovsk.|He orchestrated the October Revolution of 1917.|He was the first head of Soviet Russia.|name this Russian communist revolutionary.
H|joseph stalin,stalin|He implemented a series of Five-Year Plans.|He led the Great Purge to eliminate his enemies.|He was a member of the "Big Three" alongside FDR and Churchill.|He was a dictator of the Soviet Union after Lenin.|name this Soviet leader.
H|charlemagne,charles the great|His biographer was Einhard.|He became King of the Franks in 768.|He was crowned Emperor of the Romans by Pope Leo III on Christmas Day 800.|He united much of Western Europe during the early Middle Ages.|name this Carolingian ruler.
H|simon bolivar,bolivar|He wrote the Jamaica Letter.|He served as president of Gran Colombia.|He is known as "El Libertador."|He led the independence movements in South America.|name this Venezuelan military and political leader.
H|fidel castro,castro|He delivered the "History Will Absolve Me" speech.|He overthrew the regime of Fulgencio Batista.|He led his country during the Bay of Pigs invasion.|He established a communist state in Cuba.|name this Cuban revolutionary.
H|isaac newton,newton|He had a bitter dispute with Gottfried Leibniz over calculus.|He wrote the Principia Mathematica.|He formulated the laws of motion and universal gravitation.|He supposedly discovered gravity when a apple hit his head.|name this English scientist.
H|albert einstein,einstein|He published four groundbreaking papers in the "Annus Mirabilis" of 1905.|He won a Nobel Prize for his explanation of the photoelectric effect.|He developed the theory of special relativity.|He formulated the equation E = mc^2.|name this theoretical physicist.
H|rosa parks,parks|She attended the Highlander Folk School.|She refused to give up her seat in the "colored" section to a white passenger.|Her arrest sparked the Montgomery bus boycott.|She is known as the "mother of the civil rights movement."|name this American activist.
H|harriet tubman,tubman|She served as a scout and spy for the Union Army during the American Civil War.|She famously carried a revolver and threatened to shoot any passenger who wanted to turn back.|She made 13 missions to rescue enslaved family and friends.|She was a famous "conductor" on the Underground Railroad.|name this abolitionist.
G|france|It contains the Massif Central and the region of Brittany.|It is separated from its southern neighbor by the Pyrenees.|It is home to the Louvre and the Eiffel Tower.|It is a European nation with capital Paris.|name this country.
G|japan|It contains the island of Hokkaido in its north.|It contains Mount Fuji on its island of Honshu.|It was struck by a devastating earthquake and tsunami in 2011.|It is an Asian nation known as the Land of the Rising Sun.|name this Asian country with capital Tokyo.
G|brazil|It contains the Pantanal, the world's largest tropical wetland area.|It shares the Itaipu Dam with Paraguay.|It is home to the majority of the Amazon Rainforest.|It is the largest country in South America.|name this Portuguese-speaking nation.
G|egypt|It contains the Sinai Peninsula, which borders the Red Sea.|It controls the Suez Canal.|It is home to the ancient pyramids of Giza.|It is an African country centered on the Nile River.|name this nation with capital Cairo.
G|australia|It contains the MacDonnell Ranges and the city of Alice Springs.|It is home to the Great Barrier Reef.|It is the world's smallest continent.|It is a country known for kangaroos and koalas.|name this Oceanian nation with capital Canberra.
G|russia|It contains Lake Baikal, the world's deepest lake.|It is separated from Alaska by the Bering Strait.|It contains the Ural Mountains, dividing Europe and Asia.|It is the largest country in the world by land area.|name this country with capital Moscow.
G|china|It contains the Taklamakan Desert and shares the Gobi Desert with Mongolia.|It is home to the Three Gorges Dam on the Yangtze River.|It built a massive wall to protect against nomadic invasions.|It is the most populous country in the world.|name this Asian nation with capital Beijing.
G|india|It contains the Deccan Plateau and the Western Ghats.|It shares the Thar Desert with its western neighbor, Pakistan.|It is home to the Taj Mahal in Agra.|It is a South Asian country with capital New Delhi.|name this nation.
G|italy|It contains the Apennine Mountains, which run down its center.|It completely surrounds the independent enclaves of San Marino and Vatican City.|It is shaped like a boot kicking the island of Sicily.|It is a European country with capital Rome.|name this nation.
G|canada|It contains Baffin Island and the territory of Nunavut.|It shares the Great Lakes with its southern neighbor.|It features the prominent CN Tower in Toronto.|It is the second-largest country in the world and uses a maple leaf on its flag.|name this North American country.
G|mexico|It contains the Yucatan Peninsula and the Baja California Peninsula.|It borders the Gulf of Mexico to its east.|It is located immediately south of the United States.|It is a Spanish-speaking country with capital Mexico City.|name this nation.
G|united kingdom,uk,great britain|It contains the region of Wales and the city of Cardiff.|It is separated from mainland Europe by the English Channel.|It is comprised of England, Scotland, Wales, and Northern Ireland.|It is an island nation with capital London.|name this country.
G|germany|It contains the Black Forest and the region of Bavaria.|It was divided by a famous wall during the Cold War.|It is a major European power known for its autobahns and Oktoberfest.|It is a country with capital Berlin.|name this nation.
G|spain|It contains the autonomous communities of Catalonia and Andalusia.|It shares the Iberian Peninsula with Portugal.|It is known for the running of the bulls in Pamplona.|It is a European country with capital Madrid.|name this nation.
G|south africa|It completely surrounds the independent nation of Lesotho.|It has three capital cities: Pretoria, Bloemfontein, and Cape Town.|It officially ended its policy of apartheid in the 1990s.|It is located at the southern tip of the African continent.|name this country.
G|argentina|It contains the region of Patagonia and the Pampas.|It disputes sovereignty over the Falkland Islands with the UK.|It is the birthplace of the tango and Lionel Messi.|It is a South American country with capital Buenos Aires.|name this nation.
G|amazon river,amazon|It originates in the Mantaro River in Peru.|It contains the meeting of waters where the dark Rio Negro joins the sandy Solimoes.|It flows through the largest rainforest in the world.|It is the longest river in South America.|name this massive river.
G|nile river,nile|It has two major tributaries that meet in Khartoum, Sudan.|It flows through Lake Victoria in its upper reaches.|It floods annually, which allowed ancient Egyptian agriculture to thrive.|It is generally considered the longest river in the world.|name this river in Africa.
G|sahara desert,sahara|Its central part contains the Ahaggar Mountains.|It experiences hot, dry winds known as the sirocco.|It covers much of North Africa, including parts of Egypt and Libya.|It is the largest hot desert in the world.|name this vast African desert.
G|mount everest,everest|Its native names include Chomolungma and Sagarmatha.|It was first successfully summited by Tenzing Norgay and Edmund Hillary.|It is located in the Himalayas on the border of Nepal and China.|It is the highest mountain above sea level on Earth.|name this peak.
G|pacific ocean,pacific|It is home to the Mariana Trench, the deepest part of the world's oceans.|It is surrounded by a "Ring of Fire" known for volcanic activity.|It separates Asia and the Americas.|It is the largest and deepest ocean on Earth.|name this body of water.
G|atlantic ocean,atlantic|It contains the Sargasso Sea, a region with no land boundaries.|It features the Mid-Atlantic Ridge, a divergent tectonic plate boundary.|It separates the Americas from Europe and Africa.|It is the second-largest ocean in the world.|name this ocean.
G|california|It contains the Salton Sea and the lowest point in North America at Death Valley.|It is the location of the San Andreas Fault.|It is home to Silicon Valley and Hollywood.|It is the most populous US state.|name this state with capital Sacramento.
G|texas|It contains the Llano Estacado and the Edwards Plateau.|It fought as an independent republic against Mexico at the Alamo.|It is known for its oil industry and the city of Houston.|It is the largest US state in the contiguous 48 and uses a "Lone Star" on its flag.|name this state.
G|new york|It contains the Adirondack Mountains and Lake George.|It shares Niagara Falls with Canada.|It is home to the Statue of Liberty and the Empire State Building.|It is a northeastern US state known as the "Empire State."|name this state with capital Albany.
G|florida|It contains the Everglades, a massive tropical wetland.|It features a chain of islands in the south known as the "Keys."|It is home to the Kennedy Space Center and Walt Disney World.|It is a southeastern US peninsula state.|name this "Sunshine State."
G|hawaii|It contains the active volcano Kilauea and the Mauna Loa observatory.|It was the site of the attack on Pearl Harbor.|It is the only US state located outside North America.|It is an archipelago in the Pacific Ocean.|name this state with capital Honolulu.
G|alaska|It contains the Brooks Range and the Aleutian Islands.|It was purchased from Russia in 1867 in what was called "Seward's Folly."|It contains Denali, the highest mountain peak in North America.|It is the largest US state by land area.|name this state with capital Juneau.
G|antarctica|It contains the subglacial Lake Vostok.|It is governed by a treaty system established in 1959.|It is the coldest, driest, and windiest continent.|It is a landmass situated at the South Pole.|name this ice-covered continent.
G|grand canyon|It was carved over millions of years by the Colorado River.|It is located in a namesake National Park in Arizona.|It is a massive gorge characterized by colorful rock layers.|It is a famous American natural landmark.|name this large canyon.
G|himalayas|They contain the Siachen Glacier and the Karakoram range.|They were formed by the collision of the Indian and Eurasian tectonic plates.|They are home to peaks like K2 and Mount Everest.|They are a massive mountain range in Asia.|name this mountain range.
G|mediterranean sea,mediterranean|It is connected to the Atlantic Ocean via the Strait of Gibraltar.|It separates Europe and Africa.|It washes the shores of countries like Italy, Greece, and Egypt.|It is an important sea in classical antiquity.|name this body of water.
S|hydrogen,h|It is the only element that can exist with zero neutrons in its nucleus.|Its isotopes are deuterium and tritium.|It fuses into helium in the center of the Sun.|It is the lightest and most abundant element in the universe.|name this element with atomic number 1.
S|oxygen,o|It forms a pale blue liquid at very low temperatures and is strongly paramagnetic.|It exists as an ozone allotrope with three atoms.|It is required for human respiration and typical combustion.|It is an element that makes up about 21% of the Earth's atmosphere.|name this element with atomic number 8.
S|carbon,c|It forms buckminsterfullerenes, consisting of 60 atoms forming a sphere.|It can exist as allotropes such as graphite and diamond.|It forms the basis of all known life on Earth.|It is the element studied in organic chemistry.|name this element with atomic number 6.
S|gold,au|It can be dissolved by a mixture of nitric acid and hydrochloric acid called aqua regia.|It has the symbol Au on the periodic table.|It is a highly malleable, yellow transition metal.|It is often used in jewelry and coins and was sought after by alchemists.|name this precious metal.
S|iron,fe|It is the heaviest element produced by fusion in the cores of massive stars before a supernova.|It is the main component of Earth's core and meteorites.|It oxidizes to form rust when exposed to oxygen and moisture.|It is a magnetic metal derived from ores like hematite.|name this element with symbol Fe.
S|calcium,ca|It is found in the mineral calcite, which makes up limestone and marble.|It is stored in the sarcoplasmic reticulum in muscle cells.|It is essential for bone formation and strength.|It is found in dairy products like milk and cheese.|name this alkaline earth metal.
S|sodium,na|It emits a bright yellow light in a flame test.|It strongly reacts violently with water to produce hydrogen gas.|It forms a basic salt when bonded with chlorine.|It is an alkali metal with the symbol Na.|name this element.
S|mitochondria,mitochondrion|It contains a folded inner membrane structure called cristae.|It is inherited exclusively from the mother via the egg cell.|It produces ATP through cellular respiration.|It is famously known as the "powerhouse of the cell."|name this organelle.
S|nucleus|It contains the nucleolus, where ribosomes are synthesized.|It is surrounded by a double membrane known as the nuclear envelope.|It houses the cell's genetic material, or DNA.|It is the central control center of a eukaryotic cell.|name this organelle.
S|chloroplast|It contains flat disc-like structures called thylakoids stacked in grana.|It contains the green pigment chlorophyll.|It is the site of photosynthesis in plant cells.|It is an organelle that converts light energy into sugars.|name this plant cell organelle.
S|photosynthesis|It utilizes the Calvin cycle to produce glucose.|It requires carbon dioxide, water, and sunlight as primary inputs.|It is the process by which plants make their own food.|It produces oxygen as a byproduct.|name this biological process.
S|dna,deoxyribonucleic acid|Its structure was discovered using X-ray diffraction by Rosalind Franklin.|It forms a double helix structure held together by hydrogen bonds.|It consists of four bases: adenine, thymine, cytosine, and guanine.|It carries the genetic instructions used in growth and reproduction.|name this molecule.
S|gravity|It was formulated into a law by Isaac Newton in his Principia.|It is described as a curvature of spacetime in Einstein's general relativity.|It causes objects equipped with mass to attract one another.|It keeps planets in orbit around the sun.|name this fundamental force.
S|electron|It was discovered by J.J. Thomson using cathode ray tubes.|It is a fundamental lepton that orbits the atomic nucleus.|It carries a negative charge and determines chemical bonding.|It flows to create electricity.|name this subatomic particle.
S|proton|It is composed of two up quarks and one down quark.|It was discovered by Ernest Rutherford and determines the atomic number of an element.|It resides in the atomic nucleus alongside neutrons.|It is a positively charged subatomic particle.|name this particle.
S|neutron|It decays into a proton, an electron, and an antineutrino in beta decay.|It was discovered by James Chadwick in 1932.|It has a mass slightly larger than a proton but carries no electric charge.|It is a neutral subatomic particle found in the nucleus.|name this particle.
S|jupiter|It contains the Galilean moons Ganymede, Callisto, Io, and Europa.|Its massive atmosphere features the raging Great Red Spot.|It is the largest planet in our solar system.|It is the fifth planet from the Sun.|name this gas giant.
S|mars|It is home to Olympus Mons, the largest volcano in the solar system.|It features the Valles Marineris canyon system.|It is explored by rovers like Curiosity and Perseverance.|It is the fourth planet from the Sun, known as the "Red Planet."|name this planet.
S|saturn|It features a hexagonal storm pattern at its north pole.|Its largest moon is Titan, which has a thick atmosphere and hydrocarbon lakes.|It is famous for its extensive ring system made of ice and rock.|It is the sixth planet from the Sun.|name this gas giant.
S|venus|It has an incredibly dense atmosphere consisting mainly of carbon dioxide.|It exhibits a runaway greenhouse effect, making it the hottest planet.|It is the second planet from the Sun and similar in size to Earth.|It is Earth's "sister planet."|name this planet.
S|earth|It has a solid inner core and a liquid outer core that generates its magnetic field.|It is the only planet known to harbor liquid water on its surface.|It is the third planet from the Sun.|It is the planet we live on.|name this home planet.
S|sun,sol|It exhibits a roughly 11-year cycle of surface activity and sunspots.|It converts hydrogen into helium via nuclear fusion in its core.|It is a G-type main-sequence star located at the center of our solar system.|It is the star that provides our daylight.|name this celestial body.
S|black hole|Its outer boundary is known as the event horizon.|Its center is thought to contain a singularity of infinite density.|It has a gravitational pull so strong that not even light can escape.|It is often formed from the collapse of a massive star.|name this astronomical object.
S|water,h2o|It has a highly unusual property of expanding when it freezes into a solid.|It exhibits hydrogen bonding, giving it high surface tension and boiling point.|It consists of two hydrogen atoms covalently bonded to one oxygen atom.|It is the universal solvent essential for all life.|name this liquid.
S|pi|It is proven to be a transcendental number, meaning it is not the root of any non-zero integer polynomial.|Its value can be approximated by the fraction 22/7.|It represents the ratio of a circle's circumference to its diameter.|It begins with 3.14159.|name this mathematical constant.
S|fibonacci sequence|It was originally used to model the growth of a rabbit population.|The ratio between its consecutive terms approaches the golden ratio.|It is a sequence where each number is the sum of the two preceding ones.|It begins with 0, 1, 1, 2, 3, 5.|name this mathematical sequence.
S|prime numbers,primes|They are the building blocks of the integers according to the fundamental theorem of arithmetic.|They are the subject of the Riemann hypothesis and the Goldbach conjecture.|They are natural numbers greater than 1 that cannot be formed by multiplying two smaller numbers.|They include 2, 3, 5, 7, and 11.|name these numbers.
S|speed of light,c|It was proposed to be constant in all inertial reference frames by Albert Einstein.|It represents the letter 'c' in the equation E = mc^2.|It is approximately 300,000 kilometers per second in a vacuum.|It is the fastest speed at which information can travel.|name this value.
S|charles darwin,darwin|He observed variations in finch beaks during his voyage on the HMS Beagle.|He introduced the concept of natural selection.|He authored the influential book "On the Origin of Species."|He developed the modern theory of evolution.|name this British naturalist.
S|albert einstein,einstein|He explained Brownian motion and the photoelectric effect in 1905.|He showed that gravity bends light in his theory of general relativity.|He developed the prominent mass-energy equivalence formula E = mc^2.|He is arguably the most famous theoretical physicist of the 20th century.|name this scientist.
S|marie curie,curie|She is the only person to win a Nobel Prize in two different scientific fields.|She discovered the elements polonium and radium.|She conducted pioneering research on radioactivity.|She was a famous female scientist.|name this Polish-French physicist.
S|isaac newton,newton|He was credited with co-inventing calculus alongside Leibniz.|He studied white light using prisms and wrote the book "Opticks."|He formulated three foundational laws of motion.|He supposedly discovered gravity when an apple fell on him.|name this English physicist.
A|william shakespeare,shakespeare|He wrote the narrative poems "Venus and Adonis" and "The Rape of Lucrece."|He authored tragedies such as "Macbeth" and "Hamlet."|His plays were performed at the Globe Theatre.|He is often called the "Bard of Avon."|name this English playwright.
A|homer|His work was famously translated by Alexander Pope and Robert Fagles.|He supposedly lived in Ionia and was a blind bard.|He wrote an epic poem about the Greek hero Odysseus' journey home.|He is the traditional author of the "Iliad" and the "Odyssey."|name this ancient Greek poet.
A|mark twain,twain|He was born Samuel Langhorne Clemens and saw Halley's Comet twice.|He wrote a novel about a boy traveling down the Mississippi River with the escaped slave Jim.|He wrote "The Adventures of Tom Sawyer."|He is a famous American author known for his wit.|name this writer.
A|jane austen,austen|She wrote the novels "Northanger Abbey" and "Mansfield Park."|She chronicled the romantic pursuits of the Dashwood sisters in "Sense and Sensibility."|She created the characters of Elizabeth Bennet and Mr. Darcy.|She wrote "Pride and Prejudice."|name this English author.
A|charles dickens,dickens|He created the characters Miss Havisham and Pip in "Great Expectations."|He wrote a novel opening with "It was the best of times, it was the worst of times."|He wrote about an orphan who asks for "some more" gruel in "Oliver Twist."|He authored "A Christmas Carol" featuring Ebenezer Scrooge.|name this Victorian novelist.
A|f scott fitzgerald,fitzgerald|He coined the term "Jazz Age."|He wrote the novels "Tender Is the Night" and "The Beautiful and Damned."|He wrote a novel narrated by Nick Carraway about a wealthy man living in West Egg.|He authored "The Great Gatsby."|name this American author.
A|leonardo da vinci,da vinci|He created the "Vitruvian Man" drawing based on ideal human proportions.|He painted a mural depicting Jesus and his apostles at "The Last Supper."|He painted a portrait of Lisa del Giocondo, famously known for her enigmatic smile.|He was an Italian Renaissance polymath who painted the "Mona Lisa."|name this artist.
A|vincent van gogh,van gogh|He painted a series of vibrant "Sunflowers" while living in Arles.|He famously cut off part of his own ear after an argument with Paul Gauguin.|He painted a swirling night sky over a village in "The Starry Night."|He was a Dutch Post-Impressionist painter.|name this artist.
A|pablo picasso,picasso|He co-founded the Cubist movement alongside Georges Braque.|He went through distinctive Blue and Rose painting periods.|He painted a massive anti-war mural titled "Guernica".|He was a famous Spanish painter and sculptor.|name this artist.
A|michelangelo|He sculpted a renowned marble statue of David holding a slingshot.|He painted the "Creation of Adam" featuring God extending his finger to man.|He famously painted the ceiling of the Sistine Chapel.|He was a renowned Italian Renaissance sculptor and painter.|name this artist.
A|ludwig van beethoven,beethoven|He composed the "Eroica" Symphony, initially dedicated to Napoleon.|He wrote the piano piece "Fur Elise."|He composed his renowned Ninth Symphony, featuring the "Ode to Joy," while completely deaf.|He was a crucial figure in the transition between the Classical and Romantic eras.|name this German composer.
A|wolfgang amadeus mozart,mozart|He composed the operas "The Marriage of Figaro" and "The Magic Flute."|He was a prolific child prodigy who toured Europe with his sister Nannerl.|He composed "Eine kleine Nachtmusik."|He was an influential Austrian composer of the Classical period.|name this composer.
A|johann sebastian bach,bach|He composed the "Brandenburg Concertos" for the Margrave of Brandenburg.|He compiled the "Well-Tempered Clavier."|He was a highly skilled organist and a key figure of the Baroque period.|His massive musical family included sons like C.P.E. and J.C.|name this German composer.
A|zeus|He overthrew his father Cronus to become the ruler of the gods.|His symbols include the eagle and the aegis shield.|He was notorious for his many affairs with mortals like Alcmene and Danae, often changing form.|He was the Greek god of sky and thunder, and king of Mount Olympus.|name this deity.
A|hera|She sent two serpents to kill the infant Heracles in his crib.|She was the mother of Ares, Hephaestus, and Hebe.|She was often depicted with a peacock and was known to be deeply jealous of her husband's affairs.|She was the Greek goddess of women, marriage, and childbirth.|name this queen of the gods.
A|poseidon|He competed with Athena for the patronage of Athens and created the first horse.|He fathered the Cyclops Polyphemus, who was blinded by Odysseus.|He carried a powerful three-pronged spear known as a trident.|He was the Greek god of the sea and earthquakes.|name this deity.
A|athena|She was born fully grown and armored from the forehead of Zeus.|She transformed the weaver Arachne into a spider.|She is associated with owls, olive trees, and wisdom.|She was the Greek goddess of wisdom and warfare.|name this deity.
A|apollo|He pursued the nymph Daphne, who turned into a laurel tree to escape him.|He famously slew the giant serpent Python at Delphi.|He drove the sun chariot across the sky and played the lyre.|He was the Greek god of music, light, and prophecy.|name this deity.
A|hades|He kidnapped Persephone to be his bride and queen.|He ruled a domain guarded by the three-headed dog Cerberus.|His Roman equivalent was Pluto.|He was the Greek god of the underworld and the dead.|name this deity.
A|hercules,heracles|He accidentally killed his music tutor Linus with a lyre.|He was ordered by King Eurystheus to complete twelve difficult labors.|He slew the Nemean Lion and the multi-headed Hydra.|He was a Greek hero known for his immense physical strength.|name this mythic figure.
A|the bible|It was translated into English under King James I in 1611.|It contains numerous books including Psalms, Proverbs, and Revelation.|It is divided into the Old Testament and the New Testament.|It is the central religious text of Christianity.|name this holy book.
A|the quran,quran|It is divided into 114 chapters known as surahs.|It was revealed to its central prophet in the cave of Hira beginning in 610 CE.|It is believed to be the verbatim word of God as dictated to Muhammad.|It is the central religious text of Islam.|name this holy book.
A|the torah,torah|It forms the first section of the Hebrew Bible, known as the Tanakh.|It contains the laws given to Moses on Mount Sinai.|It consists of Genesis, Exodus, Leviticus, Numbers, and Deuteronomy.|It is the primary holy text of Judaism.|name this book.
A|buddhism|It teaches the Eightfold Path as a way to end suffering.|It centers on the Four Noble Truths.|It was founded by a prince named Siddhartha Gautama who achieved enlightenment under a Bodhi tree.|It is a major Eastern religion aiming for Nirvana.|name this religion.
A|hinduism|It features the central trinity of Brahma, Vishnu, and Shiva, known as the Trimurti.|It reveres texts such as the Vedas and the Upanishads.|It involves the concepts of karma and reincarnation.|It is the primary religion of India.|name this religion.
A|george orwell,orwell|He wrote a nonfiction account of his time in the Spanish Civil War titled "Homage to Catalonia."|He wrote an allegorical novella featuring the pigs Snowball and Napoleon.|He wrote "Animal Farm."|He wrote a dystopian novel about the surveillance state of Big Brother, titled "1984."|name this British author.
A|j r r tolkien,tolkien|He created the languages Quenya and Sindarin for his fictional world of Arda.|He wrote a novel about Bilbo Baggins' quest to the Lonely Mountain.|He authored the "Lord of the Rings" trilogy.|He was a close friend of C.S. Lewis and created Middle-earth.|name this English author.
A|c s lewis,lewis|He wrote a Christian apologetic book titled "Mere Christianity."|He wrote a novel where the Pevensie children enter a magical wardrobe.|He authored "The Lion, the Witch and the Wardrobe."|He created the fictional realm of Narnia.|name this British author.
A|j k rowling,rowling|She wrote under the pseudonym Robert Galbraith for her Cormoran Strike series.|She authored a major fantasy series centered around Hogwarts School of Witchcraft and Wizardry.|She created the characters Hermione Granger and Ron Weasley.|She wrote the "Harry Potter" series.|name this British author.
A|agatha christie,christie|She wrote "And Then There Were None," which became the best-selling mystery novel ever.|She created the sharp-witted spinster detective Miss Marple.|She created the eccentric Belgian detective Hercule Poirot.|She is one of the most famous British mystery writers of all time.|name this author.
A|arthur conan doyle,doyle|He featured the spectral dog in his novel "The Hound of the Baskervilles."|He wrote "A Study in Scarlet," introducing a brilliant, violin-playing detective and Dr. Watson.|He created the brilliant detective Sherlock Holmes.|He was a British writer and physician.|name this author.
A|mary shelley,shelley|She wrote "The Last Man," an early apocalyptic science fiction novel.|She famously conceived her masterpiece during a rainy summer at Lake Geneva with Lord Byron.|She wrote a novel subtitled "The Modern Prometheus."|She authored the classic novel "Frankenstein."|name this English writer."""

lines = raw_data.strip().split('\n')
questions = []

cat_map = {
    'H': 'History',
    'G': 'Geography',
    'S': 'Science',
    'A': 'Academics'
}

for line in lines:
    if not line: continue
    parts = line.split('|')
    cat = cat_map[parts[0]]
    ans = parts[1].split(',')
    c_varsity = parts[2]
    c_jv = parts[3]
    c_mid = parts[4]
    c_elem = parts[5]
    c_common = parts[6]
    
    # 1. Varsity
    questions.append({
        "level": "Varsity",
        "topic": cat,
        "text": f"{c_varsity} (*) {c_jv} (+) For 10 points, {c_common}",
        "answers": ans
    })
    
    # 2. JV
    questions.append({
        "level": "JV",
        "topic": cat,
        "text": f"{c_jv} (*) {c_mid} (+) For 10 points, {c_common}",
        "answers": ans
    })
    
    # 3. Middle
    questions.append({
        "level": "Middle",
        "topic": cat,
        "text": f"{c_mid} (*) {c_elem} (+) For 10 points, {c_common}",
        "answers": ans
    })
    
    # 4. Elementary
    questions.append({
        "level": "Elementary",
        "topic": cat,
        "text": f"{c_elem} (*) For 10 points, {c_common}",
        "answers": ans
    })

# Shuffle briefly to mix the order a bit so it's not totally sequential but maintain some order if wanted
# But for now let's leave it sequential, people usually like it grouped or we shuffle it so game is random
import random
random.seed(42)
random.shuffle(questions)

js_content = "const questionsDB = " + json.dumps(questions, indent=2) + ";\n\nwindow.questionsDB = questionsDB;\n"

with open("c:\\Users\\chayn\\.gemini\\antigravity\\scratch\\iac-quizbowl-trainer\\questions.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated {len(questions)} questions!")
