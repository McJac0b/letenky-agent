# Sledovanie leteniek — kritériá a stav

**Vyhľadávať vždy pre 4 dospelých** (reálna dostupnosť miest), ale **všetky ceny v reportoch a logu uvádzať NA 1 OSOBU** (= celková cena z Google Flights ÷ 4, zaokrúhliť na celé doláre). Google Flights pri 4 pasažieroch zobrazuje TOTAL za všetkých — nezabudnúť deliť štyrmi.

## Cestujúci a batožina
- 4 dospelí
- **Sledovať VŠETKY aerolinky rovnocenne — rozhoduje najnižšia cena.** Batožina NIE je kritérium.
- V reporte pri každom lete len informačne uviesť, či je príručná batožina v cene (Delta, JetBlue, American, Southwest, Alaska = áno; United/Spirit/Frontier Basic Economy = nie), nech je jasné, čo cena zahŕňa.

## Let 1: New York → Miami
- Dátum: **nedeľa 30. 8. 2026**
- Odlet: **po 19:00** (večer)
- Letiská odlet: JFK / LGA / EWR (jedno)
- Letiská prílet: MIA preferované; FLL (Fort Lauderdale, ~40 min od Miami) akceptovateľné ako lacnejšia alternatíva — vždy sledovať oboje
- URL: https://www.google.com/travel/flights?q=one%20way%20flights%20from%20New%20York%20to%20Miami%20on%202026-08-30%20for%204%20passengers

## Let 2: Miami → Las Vegas
- Dátum: **sobota 5. 9. 2026**
- Odlet: **po 13:00** (cca)
- Letiská odlet: **MIA aj FLL** (Fort Lauderdale) — lacné lety do Vegas idú často z FLL; keďže na leg 1 sa často prilieta na FLL, je to prirodzené. Vždy sledovať oboje.
- Letiská prílet: LAS
- URL (Miami metro = MIA aj FLL): https://www.google.com/travel/flights?q=one%20way%20flights%20from%20Miami%20to%20Las%20Vegas%20on%202026-09-05%20for%204%20passengers

## Doterajšie minimá — ceny na 1 osobu (aktualizovať pri každom novom minime)
| Metrika | Cena/os. | Detail | Zistené |
|---|---|---|---|
| Let 1 → FLL po 19:00 (najlacnejší celkovo) | $109 | United 20:37 EWR–FLL nonstop | 2026-07-18 |
| Let 1 → MIA po 19:00 (najlacnejší celkovo) | $178 | American 19:29 LGA–MIA nonstop (aj 20:30 JFK–MIA, aj United 20:29 EWR–MIA) | 2026-07-19 |
| Let 2 → LAS po 13:00 (najlacnejší celkovo) | $136 | Frontier 15:00 FLL–LAS, 1 prestup cez ATL 4h34 (Basic, bez batožiny) | 2026-07-21 |
| Let 2 → LAS po 13:00 (najlacnejší nonstop) | $194 | American 20:20 MIA–LAS; JetBlue 16:15 FLL–LAS | 2026-07-19 |

Poznámky z 18. 7. 2026:
- Let 1: Google price insights: „ceny sú typické, najlacnejšie býva rezervovať do 16. 8."
- Let 2: Google price insights: „ceny sú momentálne vysoké" — tu sa oplatí čakať na pokles.

Poznámky z 18. 7. 2026 (cloud scan, večer):
- Let 1 MIA aj FLL: ceny stabilné, žiadna zmena voči doterajším minimám ($179 MIA nonstop na LGA/JFK/EWR, $124 JFK-FLL JetBlue večer). Predošlé minimum $109 (EWR-FLL United 20:37) sa dnes medzi top výsledkami nezobrazilo — Google Flights vracia len obmedzený výber, nemusí to znamenať skutočný nárast ceny danej konkrétnej letenky.
- Let 2: NOVÉ MINIMUM $170 (Southwest 17:10 MIA–LAS, 2 prestupy) — pod nákupným prahom $175!

Poznámky z 19. 7. 2026 (cloud scan, ráno, fast-flights cez priamy HTTP fetch — primp/proxy TLS zlyhával):
- Let 1: bez zmeny, ceny zodpovedajú doterajším minimám ($179 MIA nonstop, $124 JFK-FLL JetBlue večer). $109 EWR-FLL stále mimo top výsledkov.
- Let 2: potvrdené $170 Southwest 17:10 (2 prestupy), stále pod prahom $175 — bez nového minima.

Poznámky z 19. 7. 2026 (cloud scan, dopoludnie, fast-flights cez requests+proxy — primp priamo dostával "connection reset"):
- Let 1: bez zmeny. Najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop), najlacnejší MIA $179 (American/United, viacero letov). $109 EWR-FLL sa opäť nezobrazilo.
- Let 2: dnešný najlacnejší $175 (American MIA 22:14, 2 prestupy) — nad doterajším minimom $170, Southwest 17:10 dnes len $243 (iná trasa cez HOU, 1 prestup). Bez nového minima, stále nad prahom $175 (presne na hranici).

Poznámky z 19. 7. 2026 (cloud scan, doobeda, fast-flights get_flights zlyhával na TLS cez proxy — obídené priamym `requests` fetchom s CA bundle a fast_flights.parser.parse()):
- Let 1: bez zmeny. Najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop), najlacnejší MIA $179 (American JFK/LGA, United EWR, všetky zhodne). $109 EWR-FLL sa opäť nezobrazilo.
- Let 2: najlacnejší $175 (American MIA 22:14, 2 prestupy) — na hranici prahu $175, bez nového minima.

Poznámky z 19. 7. 2026 (cloud scan, poludnie, rovnaký obchádzací spôsob):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $179 (American JFK 20:30, American LGA 19:29, United EWR 20:29), najlacnejší FLL $139 (Delta LGA 19:29 nonstop). JFK-FLL večerný let sa dnes v top výsledkoch vôbec nezobrazil.
- Let 2: bez zmeny, najlacnejší $175 (American MIA 22:14, 2 prestupy) — stále nad prahom $175.

Poznámky z 19. 7. 2026 (cloud scan, popoludnie, fast-flights get_flights zlyhával cez primp/proxy — použitý workaround: `requests` s REQUESTS_CA_BUNDLE + `fast_flights.parser.parse()` na base URL `/travel/flights`, nie `/search`):
- Let 1: NOVÉ MINIMUM $178 na MIA nonstop (American JFK 20:30, American LGA 19:29, United EWR 20:29) — o $1 nižšie ako doterajšie $179. Najlacnejší FLL večerný $138 (Delta LGA 19:29 nonstop), pod doterajším minimom $109 (EWR-FLL) sa dnes nedostal. JFK-FLL trasa dnes opakovane vracala chybu "unsupported" z Google Flights, vynechaná (pokrytie zvyšnými 5 kombináciami dostatočné).
- Let 2: bez zmeny, najlacnejší $175 (American MIA 22:14, 2 prestupy) — presne na hranici prahu $175, bez nového minima.

Poznámky z 19. 7. 2026 (cloud scan, popoludnie, requests+CA bundle + fast_flights.parser.parse(), fungovalo priamo bez chýb):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK 20:30, American LGA 19:29, United EWR 20:29 — všetky zhodne), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes v top výsledkoch opäť nezobrazilo.
- Let 2: bez zmeny, najlacnejší $175 (American MIA 22:14, 2 prestupy) — presne na hranici prahu $175, bez nového minima.

Poznámky z 20. 7. 2026 (cloud scan, requests+CA bundle + fast_flights.parser.parse(), fungovalo priamo bez chýb):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK/LGA, United EWR), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes v top výsledkoch opäť nezobrazilo.
- Let 2: bez zmeny na celkovom minime $140 (Frontier FLL 15:00, 1 prestup). Nové: FLL-LAS aj cez United/American/Southwest/Delta (1 prestup) za $169/os — pod prahom $175, ale nad doterajším minimom $140. Najlacnejší nonstop stále $194.

Poznámky z 20. 7. 2026 (cloud scan, noc, requests+CA bundle + fast_flights.parser.parse(), fungovalo priamo bez chýb):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK 20:30, American LGA 19:29, United EWR 20:29 — všetky zhodne), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes v top výsledkoch opäť nezobrazilo.
- Let 2: bez zmeny. Najlacnejší celkovo $140 (Frontier FLL 15:00, 1 prestup cez ATL). FLL-LAS cez United/American/Southwest/Delta (1 prestup) opäť $169/os — pod prahom $175. Najlacnejší nonstop $194 (JetBlue FLL, American MIA). Zapísaných 19 letov (7× let1, 12× let2).

Poznámky z 20. 7. 2026 (cloud scan, ráno, priama Google Flights fetch cez requests s CONSENT cookie — dovtedy chýbajúca CONSENT cookie spôsobovala presmerovanie na "unsupported" stránku; s ňou funguje aj bez fast_flights get_flights/primp, priamo cez /travel/flights/search + fast_flights.parser.parse()):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK 20:30, American LGA 19:29, United EWR 20:29 — všetky zhodne), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes v top výsledkoch opäť nezobrazilo.
- Let 2: bez zmeny. Najlacnejší celkovo $140 (Frontier FLL 15:00, 1 prestup cez ATL). Najlacnejší nonstop $194 (American MIA 20:20, JetBlue FLL 20:44). Zapísaných 18 letov (7× let1, 11× let2).

Poznámky z 20. 7. 2026 (cloud scan, dopoludnie, rovnaký spôsob — requests + CONSENT cookie + fast_flights.parser.parse()):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK 20:30, American LGA 19:29, United EWR 20:29 — všetky zhodne), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes opäť nezobrazilo.
- Let 2: bez zmeny. Najlacnejší celkovo $140 (Frontier FLL 15:00, 1 prestup cez ATL, stále pod prahom $175). Najlacnejší nonstop $194 (American MIA 20:20, JetBlue FLL 20:44). Zapísaných 18 letov (7× let1, 11× let2).

Poznámky z 20. 7. 2026 (cloud scan, dopoludnie, requests+CA bundle+CONSENT cookie + fast-flights 3.0.2 create_query/parser.parse()):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK/LGA, United EWR), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes v top výsledkoch opäť nezobrazilo.
- Let 2: bez zmeny na celkovom minime $140 (Frontier FLL 15:00, 1 prestup cez ATL, stále pod prahom $175). Najlacnejší nonstop $194 (American MIA 20:20, JetBlue FLL 20:44). Zapísaných 18 letov (7× let1, 11× let2).

Poznámky z 20. 7. 2026 (cloud scan, obed, requests+CA bundle+CONSENT cookie + fast-flights 3.0.2 create_query/parser.parse()):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK/LGA, United EWR), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes opäť nezobrazilo.
- Let 2: bez zmeny na celkovom minime $140 (Frontier FLL 15:00, 1 prestup cez ATL, stále pod prahom $175). Najlacnejší nonstop $194 (American MIA 20:20). Najlacnejší MIA-LAS $175 (American, 2 prestupy, presne na hranici prahu). Zapísaných 17 letov (7× let1, 10× let2).

Poznámky z 20. 7. 2026 (cloud scan, popoludnie, requests+CA bundle+CONSENT cookie + fast-flights 3.0.2 create_query/parser.parse()):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK 20:30, American LGA 19:29, United EWR 20:29), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes opäť nezobrazilo.
- Let 2: bez zmeny na celkovom minime $140 (Frontier FLL 15:00, 1 prestup cez ATL, stále pod prahom $175). Najlacnejší nonstop $194 (American MIA 20:20). Najlacnejší MIA-LAS $175 (American, 2 prestupy). Zapísaných 18 letov (7× let1, 11× let2).

Poznámky z 20. 7. 2026 (cloud scan, popoludnie, requests+CA bundle+CONSENT cookie + fast-flights 3.0.2 create_query/parser.parse()):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK 20:30, American LGA 19:29, United EWR 20:29), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes opäť nezobrazilo.
- Let 2: bez zmeny na celkovom minime $140 (Frontier FLL 15:00, 1 prestup cez ATL, stále pod prahom $175). Najlacnejší nonstop $194 (American MIA 20:20). Najlacnejší MIA-LAS $175 (American, 2 prestupy cez IAH a DFW). Zapísaných 18 letov (7× let1, 11× let2).

Poznámky z 20. 7. 2026 (cloud scan, večer, requests+CA bundle+CONSENT cookie + fast-flights 3.0.2 create_query/parser.parse()):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK 20:30, American LGA 19:29, United EWR 20:29), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes opäť nezobrazilo.
- Let 2: bez zmeny na celkovom minime $140 (Frontier FLL 15:00, 1 prestup cez ATL, stále pod prahom $175). Najlacnejší nonstop $194 (American MIA 20:20). Najlacnejší MIA-LAS $175 (American, 2 prestupy cez IAH a DFW). Zapísaných 18 letov (7× let1, 11× let2).

Poznámky z 20. 7. 2026 (cloud scan, večer, requests+CA bundle+CONSENT cookie + fast-flights 3.0.2 create_query/parser.parse()):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK 20:30, American LGA 19:29, United EWR 20:29), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes opäť nezobrazilo.
- Let 2: bez zmeny na celkovom minime $140 (Frontier FLL 15:00, 1 prestup cez ATL, stále pod prahom $175). Najlacnejší nonstop $194 (American MIA 20:20). Najlacnejší MIA-LAS $175 (American, 2 prestupy cez IAH a DFW). Zapísaných 18 letov (7× let1, 11× let2).

Poznámky z 20. 7. 2026 (cloud scan, neskorý večer, requests+CA bundle+CONSENT cookie + fast-flights 3.0.2 create_query/parser.parse()):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK 20:30, American LGA 19:29, United EWR 20:29), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes opäť nezobrazilo.
- Let 2: bez zmeny na celkovom minime $140 (Frontier FLL 15:00, 1 prestup cez ATL, stále pod prahom $175). Najlacnejší nonstop $194 (American MIA 20:20). Najlacnejší MIA-LAS $175 (American, 2 prestupy cez IAH a DFW). Zapísaných 18 letov (7× let1, 11× let2).

Poznámky z 20. 7. 2026 (cloud scan, noc, requests+CA bundle+CONSENT cookie + fast-flights 3.0.2 create_query/parser.parse()):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK 20:30, American LGA 19:29, United EWR 20:29), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes opäť nezobrazilo.
- Let 2: bez zmeny na celkovom minime $140 (Frontier FLL 15:00, 1 prestup cez ATL, stále pod prahom $175). Najlacnejší nonstop $194 (American MIA 20:20). Najlacnejší MIA-LAS $175 (American, 2 prestupy cez IAH a DFW). Zapísaných 18 letov (7× let1, 11× let2).

Poznámky z 21. 7. 2026 (cloud scan, noc, requests+CA bundle+CONSENT cookie + fast-flights 3.0.2 create_query/parser.parse()):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK 20:30, American LGA 19:29, United EWR 20:29), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes opäť nezobrazilo.
- Let 2: bez zmeny na celkovom minime $140 (Frontier FLL 15:00, 1 prestup cez ATL, stále pod prahom $175). Najlacnejší nonstop $194 (American MIA 20:20). Najlacnejší MIA-LAS $175 (American, 2 prestupy cez IAH a DFW). Zapísaných 18 letov (7× let1, 11× let2).

Poznámky z 21. 7. 2026 (cloud scan, skoro ráno, requests+CA bundle+CONSENT cookie + fast-flights 3.0.2 create_query/parser.parse()):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK 20:30, American LGA 19:29), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes opäť nezobrazilo.
- Let 2: NOVÉ MINIMUM $136 (Frontier FLL 15:00, 1 prestup cez ATL 4h34) — pod doterajším minimom $140 aj pod prahom $175. Ostatné MIA/FLL-LAS 1-prestupové lety $169–$203 (American, Southwest, Delta, United), Southwest MIA 17:10 2 prestupy $170. Zapísaných 17 letov (7× let1, 10× let2).

Poznámky z 21. 7. 2026 (cloud scan, ráno, requests+CA bundle + fast-flights 3.0.2, jednotlivé páry letísk):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK 20:30, American LGA 19:29), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes opäť nezobrazilo.
- Let 2: bez zmeny na celkovom minime $136 (Frontier FLL 15:00, 1 prestup cez ATL 4h34) — stále pod prahom $175. Southwest MIA 17:10 2 prestupy $170. Zapísaných 17 letov (7× let1, 10× let2).

Poznámky z 21. 7. 2026 (cloud scan, dopoludnie, requests+CA bundle+CONSENT cookie + fast-flights 3.0.2 create_query/parser.parse()):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK 20:30, American LGA 19:29, United EWR 20:29), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes opäť nezobrazilo.
- Let 2: bez zmeny na celkovom minime $136 (Frontier FLL 15:00, 1 prestup cez ATL 4h34) — stále pod prahom $175. Najlacnejší nonstop $194 (American MIA 20:20). Najlacnejší MIA-LAS $175 (American, 2 prestupy cez IAH a DFW). Zapísaných 16 letov (8× let1, 8× let2).

Poznámky z 21. 7. 2026 (cloud scan, dopoludnie #2, requests+CA bundle+CONSENT cookie + fast-flights 3.0.2 create_query/parser.parse()):
- Let 1: bez zmeny. Najlacnejší MIA nonstop $178 (American JFK 20:30, American LGA 19:29, United EWR 20:29), najlacnejší FLL $124 (JetBlue JFK 20:00 nonstop). $109 EWR-FLL sa dnes opäť nezobrazilo.
- Let 2: bez zmeny na celkovom minime $136 (Frontier FLL 15:00, 1 prestup cez ATL 4h34) — stále pod prahom $175. Najlacnejší nonstop $194 (American MIA 20:20). Najlacnejší MIA-LAS $175 (American, 2 prestupy cez IAH a DFW). Zapísaných 16 letov (8× let1, 8× let2).

## Pravidlá upozornení
- Nové minimum v ktorejkoľvek metrike, alebo pokles ≥ 5 % oproti minimu → výrazné upozornenie v reporte + aktualizovať tabuľku miním.
- Nákupné prahy (cena/os., ktorákoľvek aerolinka): Let 1 pod **$100** (FLL) / pod **$150** (MIA), Let 2 pod **$175** → odporučiť okamžitý nákup.
- Nákup robí používateľ sám — agent nikdy nenakupuje, iba upozorňuje.
