--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3 (Ubuntu 12.3-1.pgdg20.04+1)
-- Dumped by pg_dump version 12.3 (Ubuntu 12.3-1.pgdg20.04+1)

-- Started on 2020-07-02 15:14:09 +07

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 202 (class 1259 OID 16400)
-- Name: travel-recomm; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."travel-recomm" (
    id integer NOT NULL,
    section character varying(128),
    subsection character varying(256),
    "Info" character varying(10485760)
);


ALTER TABLE public."travel-recomm" OWNER TO postgres;

--
-- TOC entry 2958 (class 0 OID 16400)
-- Dependencies: 202
-- Data for Name: travel-recomm; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."travel-recomm" (id, section, subsection, "Info") FROM stdin;
0	Tag	\N	place to go, itinerary, where to stay, how to travel
1	Have You Heard Vietnam is Difficult or the Vietnamese Unpleasant?	\N	some of the nicest, friendliest, kindest and happiest people you could meet; bad stories involve taxi driver scams; haggling over prices is just the normal way to do things
2	Traffic and Roads in Vietnam	\N	Feel safer on the roads in Vietnam than in any Asian country because of low speed limits and largely populated by push bikes and scooters roads; cities are busy; crossing the road is an adventure; watch out for taxis and buses, they can be unpredictable; road death rates are high in Vietnam; do not hire scooters unless you have a suitable international motorbike license and adequate insurance.
3	Highlights of Vietnam	\N	8 UNESCO listed sites; including Ha Long Bay, Hue’s historic sites, the old town of Hoi An and the Champa complex at My Son sanctuary
4	Destinations in Vietnam	\N	lots of places to visit in Vietnam; new addition and one that we highly recommend is Phong Nha National Park and caves in Central Vietnam.
5	Destinations in Vietnam	Saigon  ( Ho Chi Minh)	Saigon refers to the inner city area of Ho Chi Minh City. Renamed after the war in honor of the North Vietnamese leader. Most people end up in is District 1 where you will find backpacker accommodation and agencies selling tours and transportation to just about anywhere in Vietnam. The Cu Chi tunnels are located about 50 km west. You can visit Cao Dai temple, its religion is unique to Vietnam and was founded in 1912.The biggest draw card in Saigon is the War Remnants Museum and the Old Palace (now called Independence Palace) from the colonial era but not used since 1975. Saigon also boasts French Period architecture, abundant great food and fascinating markets.
6	Destinations in Vietnam	Hoi An	This incredibly picturesque riverside city is something of a tourist hot spot these days, combing the charms of the Old Town with its ancient buildings, tailor’s shops and Hoi An central market with nearby rice paddies and beaches.Hoi An food is world-famous and central Vietnam is a big producer of quality sea food.Around town there are various places of interest to keep you busy, throw a pot at the pottery village. My Son Sanctuary and Marble Mountain are a short day trip from Hoi An and Hue is accessible by tour, bus or train.The nearest large city, Danang, is about 45 minutes away and is another beach-side tourist draw, popular with family holiday-makers
7	Destinations in Vietnam	Hanoi	noisy, vibrant capital city Hanoi with its traffic-choked streets of the Old Quarter, crumbling colonial buildings, street vendors and traditional tubular shops. Hanoi is filled with historic buildings: the ornate Temple of Literature, St Joseph’s Cathedral (nha tho lon) and the Imperial Citadel of Thang Long. Learn about the country’s revolutionary leader at the Ho Chi Minh mausoleum and palace complex. Take a stroll around Hoan Kiem Lake where locals come to exercise and relax. Sampling its famous food delights such as a Banh Mi sandwich or Bun Cha. Stop in at Café Giang for a Ca Phe Trung (egg coffee)
8	Destinations in Vietnam	Ha Long Bay	magical location in Vietnam with emerald-green waters, limestone islands and mystical caves, all while touring on Junk Boats. From day tours through to tours that keep you entertained for 2 days 3 nights, we highly recommend the latter. Sleeping on a Junk Boat, while doing day visits to floating villages, taking rowing tours, and getting to jump off the boat into the cool refreshing water, is so relaxing and fun plus gives you a great insight to local living and seeing nature’s beauty up close. Highly recommend you choose your junk boat tour wisely and spend a few extra dollars to get a better experience and higher quality boat. We have done three tours since 2008 and loved Signature Cruises.
9	Destinations in Vietnam	Sapa	Sapa is a must-see destination for nature lovers. Sapa is within easy reach of Hanoi, by overnight bus or train. In Sapa, the magnificent purple mountains sink away into deep valleys, where terraced rice paddies feed the imagination. Its has many ethnic minorities, including the H’Mong, the Dao and the Dai. The big draw is the chance to trek along Sapa’s stunning valleys and mountains. Taking a multi-day trek between village homestays will give you the chance to immerse yourself in a slower pace of life, stretch your legs, and indulge in shots of the locally-made rice wine which burns a little as it goes down but is perfect way to loosen your muscles after a long day of walking!
10	Tours in Vietnam	\N	How do you want to visit Vietnam? There are heaps of options.
11	Vietnam with Kids and for Families	\N	There are loads of interesting things for the kids to do like the pottery classes, the Cu Chi tunnels tour or coconut boat rides and crab catching. There is much to learn about culture and history. Vietnamese food is generally lacking in spice or chili except the Central Vietnam. You can also get just about any western food here. Not likely to have any sort of tummy trouble or diarrhoea in Vietnam. Lots of tropical bugs like mosquitoes. There are plenty of accommodation options at all price points and likewise plenty of transportation options. There are beaches if that is your want. Be mindful of the weather and if you plan to use bikes bring your own helmets. Hoi An is a massively popular family holiday hot spot particularly for Australians
12	Vietnam with Kids and for Families	Small Group Tours of Vietnam	All of the big adventure travel companies offer small group tours of Vietnam for big fans of Explore Worldwide
13	Vietnam with Kids and for Families	Tours and Transportation Within Vietnam. Booking Trains, Buses and Planes	Every town visited by tourists and backpackers has plenty of small travel agents’ shops selling tours and onward transportation. Everything is very easy to arrange on the ground but need time and your best haggling skills. Can easily book train or bus tickets online ( or even flights)in advance,  you can use 12GoAsia or local agent.If you’re short of time or need to book a tour in advance for a particular day, we recommend booking online.
14	Classes and Courses to Take	\N	Cooking classes, pottery classes, Vietnamese lessons, yoga, painting and more
15	Theatre, Dance & Music from Lune and Traditional Vietnamese Water Puppets.	\N	The Lune Theatre productions that you can catch in Saigon, Hanoi and in a purpose-built performance space in Hoi An. These shows are magical and beautiful, featuring traditional music and instruments, dance, drama and more. For example, “The Mist” beautifully illustrates the life of rice farmers in the Mekong Delta. You can book Lune tickets in advance for Hoi An. There are 4 different shows that rotate through Lune’s current 3 theatres in Vietnam. Vietnamese water puppet shows is great for kids and a lot of fun. These short performances are traditional and well worth seeing.
16	Visas for Vietnam	Overview	Vietnam isn’t as easy as other countries in South East Asia when it comes to visas plus one of the more expensive countries to enter. Visa on arrival only for a two-week holiday and for a certain nationalities. Vietnam requires a little forward planning for long-term travellers.
17	Visas for Vietnam	Types	2 Week, E-Visa, 3 Month, Multiple Entry and More
18	Visas for Vietnam	Warning	Please read the information below and do your own research for your country. We’re as current as we can be, but lots of regulations changes. Visa requirement change constantly, please double-check information with Sherpa or another reputable visa company.
19	Visas for Vietnam	Visas	Visitors to Vietnam can visit a Vietnamese embassy to buy their Visa, or arrange an e-visa approval online which they must then produce on arrival. The embassy in London would charge $100 US for each 3 month visa. That was significantly more expensive than using the agency.
20	Visas for Vietnam	Travel Agency	The agencies don’t actually issue the visas but give you an authorization letter from the Vietnamese immigration department which allows you to receive a visa on arrival. Airlines are strict and won’t let you on the plane without either a full visa or authorization letter. You pay a small fee to the agency to get the letter emailed to you but risk of getting wrong mail contains other people’s details such as name, date of birth and passport number as agency will apply for multiple travellers. The costs are normally between $20 and $25 US for the authorization letter. You then need to pay the stamping fee (from $20 for a single month to $25 for a three-month single entry visa) on arrival in Vietnam where the actual visa is stuck into your passport. The multiple entry visas attract a higher stamping fee approximately $50 US. All the stamping fees need to be paid in cash in US $.The authorization letter only works if you are flying into an international airport. It will not work at land crossings. For that you’ll need to have a visa in your passport from an embassy or you will only be entitled to the free 15 day visa on arrival (certain counties only).
21	Food in Vietnam	\N	Specialties included pho, mi quang, banh xeo and bun bo Hue. The best food in Vietnam comes from street stalls, it’s what the locals eat and inexpensive. Do not expect a menu, these stalls specialise in one perfectly executed dish only. Vietnamese food is light and fresh with few spices. If you like your food hot you’ll find fresh and dried chilies on the table to add to taste. There are restaurants catering to tourists at every price point. Fresh, steamed and fried spring rolls are a favourite. You’ll find incredible fresh seafood in Central Vietnam with prawns costing little. Vegetarians, even vegans, are pretty well catered for in Vietnam too.
22	Vaccinations for Vietnam and Health	\N	I’m happy to say that Vietnam is in the group that gave us zero ilnesses or tummy trouble. None of us have had any travellers diarrhoea or sickness in over 6 months in Vietnam. We’ve eaten everything, at every street food stall and had no trouble at all. We’re hugely impressed with how clean things are here compared to some other parts of the world. There are few flies, and few mosquitos, there are plenty of rats. If you get sick in Vietnam it’s easy to pop along to a pharmacy, there’s one on almost every street and the pharmacists are very helpful and know their stuff. We’ve had to buy treatment for ringworm ( picked up by one of the kids in London), mouth ulcers and dressings for bike-related scrapes, it’s been no trouble at all. I would suggest carrying a basic first aid kit with you. Beware of malaria in the rainy season.
23	Hotels, Hostels, Guest Houses, Resorts and Apartments. Finding Them	\N	The first time we visited Vietnam it was very much a backpacker destination, these days there are plenty of up-market hotels and resorts on offer too and the tourists are flooding to Vietnam. People like us, the digital nomads and long term travellers are also here and there are amazing bargains to be had in long-term, quality accommodation.
24	Hotels, Hostels, Guest Houses, Resorts and Apartments. Finding Them	Finding the Best Prices and Deals on Hotels and Resorts in Vietnam	We highly recommend checking booking engine if you’re serious about finding the best price for your stay. If you’re the sort to book a long time in advance, maybe reserving multiple hotels on a fully refundable basis, Booking.com is your friend. The Sunrise Resort is one of the luxury hotels we’ve tested on behalf of Luxury Escapes, an Australian company specialising on incredibly good offers on top end hotel packages. Their special offer prices are way below what we paid for these hotels and the quality was superb.
25	Hotels, Hostels, Guest Houses, Resorts and Apartments. Finding Them	Hostels	You will find a big selection of hostels, some have private family rooms, on all of the booking engine.
26	Hotels, Hostels, Guest Houses, Resorts and Apartments. Finding Them	Long Term Stays, House and Apartments	We’ve booked hotels in Hoi An and Hue through Airbnb, both were good, small boutique style hotels or homestays. A homestay can be a hotel, hostel or actual homestay in Vietnam. We found our beautiful house for 2 months in Hoi An through a local expats Facebook group. We booked a cheap hotel for arrival and within half a day of posting in the expat group we’d found the perfect house for us at a great price.
\.


--
-- TOC entry 2831 (class 2606 OID 16407)
-- Name: travel-recomm travel-recomm_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."travel-recomm"
    ADD CONSTRAINT "travel-recomm_pkey" PRIMARY KEY (id);


-- Completed on 2020-07-02 15:14:10 +07

--
-- PostgreSQL database dump complete
--

