# Poslední přepážka

Návrh a scénář týmové textové adventury pro 4IT107 Programování v Javě

## 1. Téma a zadání hry

Na orbitální stanici se utrhla z izolace fiktivní houbovitá nákaza. Prorůstá otevřenými průchody a vyřazuje systémy stanice. Hráč je službu konající technik. Začíná v Kajutě s prázdným batohem a musí obnovit napájení, spustit chlazení, získat povolení k odletu a odstartovat únikovým modulem. Vyhraje úspěšným příkazem `odstartuj`. Prohraje, jakmile je v nakaženém prostoru nebo nákaza dosáhne Hangáru.

### Prostory a počáteční stav

| ID | Prostor a popis | Sousedé | Počáteční vybavení |
| --- | --- | --- | --- |
| 0 | Kajuta - služební ubytovna | 1, 12 | servisní klika, rozvaděč |
| 1 | Chodba - obytný koridor | 0, 2 | - |
| 2 | Chladicí komora - rozvod tepla | 1, 3 | ventil |
| 3 | Velín - řízení evakuace | 2, 4 (A) | konzole |
| 4 | Sklad - náhradní díly | 3 (A), 5 (B) | pojistka |
| 5 | Dílna - odstavené ponky | 4 (B), 6 | - |
| 6 | Ošetřovna - prázdná ambulance | 5, 7 | - |
| 7 | Servisní tunel - kabelový průchod | 6, 8 | - |
| 8 | Strojovna - záložní zásoby | 7, 9 (C) | patrona |
| 9 | Předsíň - vstup k rampě | 8 (C), 10 | - |
| 10 | Hangár - odpalovací rampa | 9, 11 (D) | panel rampy, karta |
| 11 | Únikový modul - kabina kapsle | 10 (D) | startovací pult |
| 12 | Zadní strojovna - ohnisko nákazy | 0 | - |

### Předměty a prvky

Batoh unese jeden přenosný předmět. Klika otevře přepážku A a zůstane v batohu, dokud ji hráč nepoloží. Pojistku spotřebuje rozvaděč, patronu ventil a kartu konzole. Položená věc zůstane v místnosti a lze ji znovu sebrat. Rozvaděč, ventil, konzole, panel rampy a startovací pult jsou nepřenosné. Rozvaděč, ventil a konzole jsou tři rozšiřující prvky a mění stav herního světa podle tabulky příkazů.

<!-- page -->

## 1. Pravidla a příkazy

A, B, C a D jsou na začátku zavřené. Odemykání současně otevře průchod oběma směry. Otevřené A, B a C tak zůstanou. D lze jednou uzavřít zevnitř modulu a pak je uzavřená trvale. Napájení, chlazení, autorizace a připravenost rampy se po aktivaci zachovají. Přepážky ovlivňují pohyb hráče i nákazy.

Každý úspěšný pohyb, manipulace s předmětem a nový herní příkaz přičte jeden tah. Změna stavu se provede před posunem nákazy. Po každém 24. tahu nákaza současně přejde do všech prostorů sousedících otevřeným průchodem s množinou místností nakažených před daným šířením. Nákaza zůstane v již nakažených prostorách. Po tahu se zkontroluje infekce hráče, pak infekce Hangáru a nakonec případná výhra. Při souběhu má prohra hráče přednost. Po konci hry se další příkazy nepřijímají.

### Osm nových příkazů

| Příkaz | Místo a podmínka | Účinek |
| --- | --- | --- |
| odjisti a | Velín, klika v batohu, A zavřená | Otevře A. Klika zůstane hráči. |
| vymen pojistku | Kajuta, pojistka v batohu, rozvaděč bez pojistky | Spotřebuje pojistku a osadí ji do rozvaděče. |
| zapni rozvadec | Kajuta, osazená pojistka, proud vypnutý | Zapne napájení a otevře B. |
| otevri ventil | Chladicí komora, patrona v batohu, proud je zapnutý, chlazení neaktivní | Spotřebuje patronu, spustí chlazení a otevře C. |
| autorizuj odlet | Velín, karta v batohu, aktivní chlazení, odlet dosud nepovolený | Spotřebuje kartu, autorizuje odlet a otevře D. |
| priprav rampu | Hangár, autorizovaný odlet, rampa nepřipravená | Připraví rampu. |
| uzavri d | Únikový modul, D otevřená | Zavře D a izoluje modul. |
| odstartuj | Únikový modul, rampa připravená a D zavřená | Spustí modul. Pokud nenastane prohra, hráč vítězí. |

### Základní a systémové příkazy

`jdi <prostor>` přesune hráče do sousedního prostoru otevřeným průchodem. `seber <vec>` vloží přenosnou věc z místnosti do prázdného batohu. `poloz <vec>` položí drženou věc v aktuálním prostoru. `pomoc` vypíše syntax, `napoveda` aktuální okolí a batoh, `konec` ukončí relaci bez výsledku hry. `uloz` a `nacti` pracují s pevným souborem save.json v pracovním adresáři.

Vstup se ořízne, převede na malá písmena, odstraní se diakritika a mezi slovy se tolerují násobné mezery. První slovo je příkaz, celý zbytek jeden parametr. Systémové a odmítnuté příkazy neposouvají tah.

<!-- page -->

## 2. Mapa stanice

<!-- map -->

Čára vyznačuje obousměrný průchod. Přepážky jsou na začátku zavřené. Značky A až D odpovídají tabulce pod mapou.

| Přepážka | Co ji otevře |
| --- | --- |
| A - Velín / Sklad | Odjištění klikou z Velína. |
| B - Sklad / Dílna | Obnovení napájení v Kajutě. |
| C - Strojovna / Předsíň | Spuštění chlazení v Chladicí komoře. |
| D - Hangár / Únikový modul | Autorizace odletu ve Velínu. Zevnitř modulu se po průchodu uzavře. |

<!-- page -->

## 3. Vítězný scénář

### Proč výhra vyžaduje 58 tahů

Jediná trasa ke každému potřebnému předmětu vede hlavní chodbou. Pojistka nutí projít 0 - 4 - 0 (8 pohybů). Patrona je dostupná až po zapnutí napájení a nutí projít 0 - 8 - 2 (14 pohybů). Karta je dostupná až po spuštění chlazení a nutí projít 2 - 10 - 3 (15 pohybů). Po autorizaci zbývá 3 - 11 (8 pohybů). Celkem je to nejméně 45 pohybů.

K pohybům přibývají čtyři povinná sebrání, jedno položení kliky kvůli kapacitě batohu a osm nezbytných nových příkazů. Dolní mez je tedy 58 tahů. Následující scénář ji dosahuje. Načtení obnoví celý uložený stav včetně počítadla a neposkytuje zkratku z počátečního stavu.

Sloupec „Přesný výstup“ tvoří první část sekce 4. U změn se vždy uvádí přesun hráče ve sloupci „Prostor“ a změna inventáře ve sloupci „Batoh“. Pomlčka ve sloupci „Změna“ značí, že žádný další stav se nezměnil.

| Tah | Příkaz | Prostor | Batoh | Změna | Přesný výstup |
| --- | --- | --- | --- | --- | --- |
| 1 | seber servisni klika | Kajuta | servisní klika | - | Sebráno: servisní klika. |
| 2 | jdi chodba | Chodba | servisní klika | - | Přesun: Chodba. |
| 3 | jdi chladici komora | Chladicí komora | servisní klika | - | Přesun: Chladicí komora. |
| 4 | jdi velin | Velín | servisní klika | - | Přesun: Velín. |
| 5 | odjisti a | Velín | servisní klika | Otevřena A | Přepážka A je otevřená. |
| 6 | poloz servisni klika | Velín | - | - | Položeno: servisní klika. |
| 7 | jdi sklad | Sklad | - | - | Přesun: Sklad. |
| 8 | seber pojistka | Sklad | pojistka | - | Sebráno: pojistka. |
| 9 | jdi velin | Velín | pojistka | - | Přesun: Velín. |
| 10 | jdi chladici komora | Chladicí komora | pojistka | - | Přesun: Chladicí komora. |
| 11 | jdi chodba | Chodba | pojistka | - | Přesun: Chodba. |
| 12 | jdi kajuta | Kajuta | pojistka | - | Přesun: Kajuta. |

<!-- page -->

## 3. Vítězný scénář · tahy 13 až 28

| Tah | Příkaz | Prostor | Batoh | Změna | Přesný výstup |
| --- | --- | --- | --- | --- | --- |
| 13 | vymen pojistku | Kajuta | - | Osazena pojistka | Pojistka je osazená. |
| 14 | zapni rozvadec | Kajuta | - | Proud, otevřena B | Napájení obnoveno. Přepážka B je otevřená. |
| 15 | jdi chodba | Chodba | - | - | Přesun: Chodba. |
| 16 | jdi chladici komora | Chladicí komora | - | - | Přesun: Chladicí komora. |
| 17 | jdi velin | Velín | - | - | Přesun: Velín. |
| 18 | jdi sklad | Sklad | - | - | Přesun: Sklad. |
| 19 | jdi dilna | Dílna | - | - | Přesun: Dílna. |
| 20 | jdi osetrovna | Ošetřovna | - | - | Přesun: Ošetřovna. |
| 21 | jdi servisni tunel | Servisní tunel | - | - | Přesun: Servisní tunel. |
| 22 | jdi strojovna | Strojovna | - | - | Přesun: Strojovna. |
| 23 | seber patrona | Strojovna | patrona | - | Sebráno: patrona. |
| 24 | jdi servisni tunel | Servisní tunel | patrona | Nákaza: Kajuta | Přesun: Servisní tunel. [NL] Nákaza postoupila: Kajuta. |
| 25 | jdi osetrovna | Ošetřovna | patrona | - | Přesun: Ošetřovna. |
| 26 | jdi dilna | Dílna | patrona | - | Přesun: Dílna. |
| 27 | jdi sklad | Sklad | patrona | - | Přesun: Sklad. |
| 28 | jdi velin | Velín | patrona | - | Přesun: Velín. |

<!-- page -->

## 3. Vítězný scénář · tahy 29 až 44

| Tah | Příkaz | Prostor | Batoh | Změna | Přesný výstup |
| --- | --- | --- | --- | --- | --- |
| 29 | jdi chladici komora | Chladicí komora | patrona | - | Přesun: Chladicí komora. |
| 30 | otevri ventil | Chladicí komora | - | Chlazení, otevřena C | Chlazení běží. Přepážka C je otevřená. |
| 31 | jdi velin | Velín | - | - | Přesun: Velín. |
| 32 | jdi sklad | Sklad | - | - | Přesun: Sklad. |
| 33 | jdi dilna | Dílna | - | - | Přesun: Dílna. |
| 34 | jdi osetrovna | Ošetřovna | - | - | Přesun: Ošetřovna. |
| 35 | jdi servisni tunel | Servisní tunel | - | - | Přesun: Servisní tunel. |
| 36 | jdi strojovna | Strojovna | - | - | Přesun: Strojovna. |
| 37 | jdi predsin | Předsíň | - | - | Přesun: Předsíň. |
| 38 | jdi hangar | Hangár | - | - | Přesun: Hangár. |
| 39 | seber karta | Hangár | karta | - | Sebráno: karta. |
| 40 | jdi predsin | Předsíň | karta | - | Přesun: Předsíň. |
| 41 | jdi strojovna | Strojovna | karta | - | Přesun: Strojovna. |
| 42 | jdi servisni tunel | Servisní tunel | karta | - | Přesun: Servisní tunel. |
| 43 | jdi osetrovna | Ošetřovna | karta | - | Přesun: Ošetřovna. |
| 44 | jdi dilna | Dílna | karta | - | Přesun: Dílna. |

<!-- page -->

## 3. Vítězný scénář · tahy 45 až 58

| Tah | Příkaz | Prostor | Batoh | Změna | Přesný výstup |
| --- | --- | --- | --- | --- | --- |
| 45 | jdi sklad | Sklad | karta | - | Přesun: Sklad. |
| 46 | jdi velin | Velín | karta | - | Přesun: Velín. |
| 47 | autorizuj odlet | Velín | - | Povolení, otevřena D | Odlet povolen. Přepážka D je otevřená. |
| 48 | jdi sklad | Sklad | - | Nákaza: Chodba | Přesun: Sklad. [NL] Nákaza postoupila: Chodba. |
| 49 | jdi dilna | Dílna | - | - | Přesun: Dílna. |
| 50 | jdi osetrovna | Ošetřovna | - | - | Přesun: Ošetřovna. |
| 51 | jdi servisni tunel | Servisní tunel | - | - | Přesun: Servisní tunel. |
| 52 | jdi strojovna | Strojovna | - | - | Přesun: Strojovna. |
| 53 | jdi predsin | Předsíň | - | - | Přesun: Předsíň. |
| 54 | jdi hangar | Hangár | - | - | Přesun: Hangár. |
| 55 | priprav rampu | Hangár | - | Rampa připravena | Rampa je připravená. |
| 56 | jdi unikovy modul | Únikový modul | - | - | Přesun: Únikový modul. |
| 57 | uzavri d | Únikový modul | - | Uzavřena D | Přepážka D je uzavřená. |
| 58 | odstartuj | Únikový modul | - | Výhra | Únikový modul odstartoval. Vyhráváš. |

<!-- page -->

## 3. Kontrola scénáře a prohra

| První použití | Příkaz | Proč je nový příkaz nutný |
| --- | --- | --- |
| 1 | seber | - |
| 2 | jdi | - |
| 5 | odjisti | Bez A není dostupná pojistka. |
| 6 | poloz | - |
| 13 | vymen | Bez pojistky rozvaděč nezapne proud. |
| 14 | zapni | Bez proudu je B zavřená a ventil nelze spustit. |
| 30 | otevri | Bez chlazení je C zavřená a odlet nelze autorizovat. |
| 47 | autorizuj | Bez povolení se D neotevře a rampu nelze připravit. |
| 55 | priprav | Bez připravené rampy modul neodstartuje. |
| 57 | uzavri | Start je podmíněný izolací modulu. |
| 58 | odstartuj | Příkaz jako jediný vyhodnotí výhru. |

### Krátký prohrávající scénář

Z čerstvé hry zadej `jdi zadni strojovna`. Tah 1 přesune hráče do Zadní strojovny, batoh zůstane prázdný a hra skončí. Přesný výstup na dvou řádcích je „Přesun: Zadní strojovna.“ a „Nákaza tě dostihla. Prohráváš.“

### Zkouška uložení a načtení

Po 24. tahu vítězného scénáře ulož hru. Ukonči běh a po dalším spuštění načti uloženou pozici. Obnoví se Servisní tunel, patrona v batohu, klika ve Velínu, osazená pojistka, zapnutý proud, otevřené A a B, zavřené C a D, vypnuté chlazení, nepovolený odlet a nepřipravená rampa. Nakažené jsou Zadní strojovna a Kajuta. Další tah má číslo 25 a zbytek scénáře má stejné výstupy.

<!-- page -->

## 4. Přesné výstupy hry

Ve scénáři značí symbol [NL] nový řádek. Výstupy v této části ani ve scénáři neobsahují uvozovky. Úvod se vytiskne po startu nové relace. Jediný výstup výhry je uveden u tahu 58.

### Úvod, konec a systémové příkazy

| Událost | Přesný výstup |
| --- | --- |
| Úvod | Poslední přepážka. Stanice je napadena. Dostaň se do únikového modulu a odstartuj. Začínáš v prostoru Kajuta. Napiš pomoc pro seznam příkazů. |
| pomoc | Příkazy: jdi <prostor>, seber <vec>, poloz <vec>, odjisti a, vymen pojistku, zapni rozvadec, otevri ventil, autorizuj odlet, priprav rampu, uzavri d, odstartuj, pomoc, napoveda, uloz, nacti, konec. |
| napoveda | Prostor: {prostor}. Sousední prostory: {sousedé}. Věci tady: {věci}. Batoh: {batoh}. Zavřená přepážka brání nákaze v postupu. |
| uloz / nacti | Hra uložena. / Hra načtena. |
| konec | Hra ukončena. |
| Nákaza postoupila | Nákaza postoupila: {prostory}. |
| Prohra hráče / prohra ztrátou rampy | Nákaza tě dostihla. Prohráváš. / Nákaza vyřadila rampu. Prohráváš. |

V nápovědě vypiš sousedy podle ID a k zavřeným připiš „ (zavřeno)“. Věci seřaď podle normalizovaných názvů včetně pevných prvků. Sousední prostory a věci odděluj čárkou a mezerou. Prázdný seznam nebo batoh označ „nic“. Pro vstup použij názvy z výpisu bez poznámky o přepážce.

Použij názvy prostorů z mapy, při více nově zasažených prostorech je vypiš podle ID a odděl čárkou a mezerou. Po úspěšném tahu nejdřív vytiskni běžné hlášení akce, potom případné šíření a případný konečný výsledek. `odstartuj` nemá samostatné běžné hlášení. U pohybu použij „Přesun: {prostor}.“, u běžného sebrání a položení použij „Sebráno: {věc}.“ a „Položeno: {věc}.“ s názvem věci v prvním pádě a malými písmeny.

### Chyby vstupu a souborů

| Situace | Přesný výstup |
| --- | --- |
| Prázdný vstup nebo neznámé slovo příkazu | Neznámý příkaz. Napiš pomoc. |
| Chybí parametr / nadbytečný nebo neplatný pevný parametr | Chybí parametr. / Neplatný parametr. |
| Cíl pohybu neexistuje nebo není sousední | Tudy cesta nevede. |
| Cíl pohybu je za zavřenou přepážkou | Přepážka {písmeno} je zavřená. |
| Věc při sebrání v prostoru není / je pevná / batoh plný | Tato věc tu není. / Tuto věc nelze sebrat. / Batoh je plný. |
| Hráč pokládá věc, kterou nedrží | Tuto věc v batohu nemáš. |
| Nový příkaz mimo určený prostor | Tady tento příkaz nelze použít. |
| Nová akce už byla provedena | Tento úkon už byl proveden. |
| Nový příkaz bez potřebného vybavení či stavu | Chybí potřebný předmět nebo systém není připraven. |
| Uložení selhalo / soubor chybí / načtení selhalo | Hru se nepodařilo uložit. / Uložená hra neexistuje. / Uloženou hru nelze načíst. |

Při více chybách vyber první v tomto pořadí: příkaz, parametr, místo, již provedený úkon, další podmínky. U sebrání nejprve ověř dostupnost, potom přenosnost a kapacitu. Opakované odjištění, výměna, zapnutí, chlazení, autorizace, příprava nebo uzavření se pozná podle příslušného příznaku stavu.

<!-- page -->

## 4. Uložení a ověření implementace

Soubor save.json obsahuje verzi formátu, ID prostoru hráče, pozici každé přenosné věci (místnost, batoh nebo spotřebováno), celkový počet tahů, nakažené prostory, stav čtyř přepážek a příznaky osazené pojistky, zapnutého proudu, chlazení, povolení odletu a připravené rampy. Po načtení se obnoví všechny uložené hodnoty. Neznámou verzi, chybějící údaje a neplatné nebo rozporné hodnoty hra odmítne; současná rozehraná hra zůstane zachovaná. Při ukládání se hotový dočasný soubor přesune na cílovou cestu až po úspěšném zápisu. Hra ošetří chyby vstupu a souborů bez pádu.

Při implementaci se počítá se samostatnými třídami pro prostor, věc, batoh a typy rozšiřujících prvků, společným rozhraním příkazů a prvků, soukromými atributy a kolekcemi pro stav hry. Stream API s lambdami lze využít pro hledání věci, seřazení výpisu věcí a sestavení hlášení o nově napadených prostorech. Projekt se sestaví Mavenem pro Javu 25.

JUnit má přehrát celý vítězný scénář, ověřit prohru, plný batoh a nepřenosnou věc, interakce s prvky, uložení a načtení, neznámé příkazy, chybný vstup a chybějící či poškozenou uloženou hru.

## 5. Uživatelská příručka

Po sestavení hry spusť v terminálu `java -jar target/posledni-prepazka.jar`. Cílem je opustit napadenou stanici v únikovém modulu. Každou akci napiš na samostatný řádek a potvrď Enterem. Používej názvy prostorů a předmětů tak, jak je uvádí hra. Příkazy fungují i bez české diakritiky.

- `jdi <prostor>`, `seber <vec>` a `poloz <vec>` slouží k pohybu a manipulaci s předměty. Batoh má jedno místo.
- `odjisti a`, `vymen pojistku`, `zapni rozvadec`, `otevri ventil`, `autorizuj odlet`, `priprav rampu`, `uzavri d` a `odstartuj` slouží k obsluze stanice a modulu.
- `pomoc` zobrazí příkazy, `napoveda` prostor, sousedy, věci a batoh. `konec` ukončí relaci.
- `uloz` přepíše uloženou pozici v souboru save.json ve složce, ze které je hra spuštěná. Po spuštění hry můžeš příkazem `nacti` pokračovat z tohoto souboru.
- Nákaza postupuje s tahy. Čtení, chybné vstupy a systémové příkazy čas neposunou.

## 6. Členové týmu

Před odevzdáním doplňte skutečná jména a xname a potvrďte pracovní rozdělení. Každý nový příkaz a každý rozšiřující prvek má právě jednoho odpovědného člena.

| Jméno a příjmení | xname | Nové příkazy | Prvek | Další podíl |
| --- | --- | --- | --- | --- |
| Doplnit člena 1 | Doplnit | odjisti, vymen | rozvaděč | mapa |
| Doplnit člena 2 | Doplnit | zapni, otevri | ventil | pravidla tahů |
| Doplnit člena 3 | Doplnit | autorizuj, priprav | konzole | herní texty |
| Doplnit člena 4 | Doplnit | uzavri, odstartuj | - | scénář a příručka |
