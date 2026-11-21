# Poslední přepážka

Návrh a scénář týmové textové adventury pro 4IT107 Programování v Javě

## 1. Téma a zadání hry

Na orbitální stanici Orfeus unikla z izolace houbovitá nákaza. Prorůstá otevřenými průchody a vyřazuje systémy stanice. Hráč je službu konající technik. Začíná v Kajutě s prázdným batohem a musí obnovit napájení, spustit chlazení, získat povolení k odletu a odstartovat únikovým modulem. Vyhraje úspěšným příkazem `odstartuj`. Prohra nastane, když je hráč v nakaženém prostoru nebo když na konci 72. tahu zkolabuje stanice před odletem.

### Prostory a počáteční stav

| ID | Prostor a popis | Sousedé | Počáteční vybavení |
| --- | --- | --- | --- |
| 0 | Kajuta - služební ubytovna | 1, 12 (E) | servisní klika, rozvaděč |
| 1 | Chodba - obytný koridor | 0, 2 | - |
| 2 | Chladicí komora - rozvod tepla | 1, 3 | ventil |
| 3 | Velín - řízení evakuace | 2, 4 (A) | konzole |
| 4 | Sklad - náhradní díly | 3 (A), 5 (B) | skříň (pojistka) |
| 5 | Dílna - servisní stojany pro palubní moduly | 4 (B), 6 | servisní stojany (pevné) |
| 6 | Ošetřovna - prázdná ambulance | 5, 7 | - |
| 7 | Servisní tunel - kabelový průchod | 6, 8, 13 (F) | - |
| 8 | Strojovna - záložní zásoby | 7, 9 (C) | přepravka (patrona) |
| 9 | Předsíň - vstup k rampě | 8 (C), 10 | - |
| 10 | Hangár - odpalovací rampa | 9, 11 (D) | panel rampy, schránka (karta) |
| 11 | Únikový modul - kabina kapsle | 10 (D) | startovací pult |
| 12 | Zadní strojovna - ohnisko nákazy | 0 (E) | - |
| 13 | Servisní šachta - druhé ohnisko nákazy | 7 (F) | - |

### Předměty a prvky

Batoh unese jeden přenosný předmět. Klika otevře přepážku A a zůstane v batohu, dokud ji hráč nepoloží. Pojistku spotřebuje rozvaděč, patronu ventil a kartu konzole. Položená věc zůstane v místnosti a lze ji znovu sebrat. Rozvaděč, ventil, konzole, servisní stojany, panel rampy, startovací pult a tři kontejnery jsou nepřenosné. Tři rozšiřující prvky jsou zavřená skříň ve Skladu, zavřená přepravka ve Strojovně a zavřená schránka v Hangáru. Každá má vlastní obsah uvedený v mapě. Příkaz pro otevření přesune obsah kontejneru mezi volné věci v místnosti. Kontejner zůstane otevřený a prázdný. Před otevřením nelze jeho obsah vidět ve výpisu ani sebrat.

<!-- page -->

## 1. Pravidla a příkazy

A, B, C a D jsou na začátku zavřené. Odemykání současně otevře průchod oběma směry. Otevřené A, B a C tak zůstanou. D lze po autorizaci uzavřít zevnitř modulu. E a F jsou zprvu otevřené. Po obnově napájení lze E zavřít z Kajuty a F ze Servisního tunelu. Zavřené D, E a F už znovu otevřít nelze. Všechny neoznačené průchody jsou trvale otevřené. Na začátku jsou nakažené pouze prostory 12 a 13. Pojistka není osazená a napájení, chlazení, autorizace i rampa jsou neaktivní. Napájení, chlazení, autorizace a připravenost rampy se po aktivaci zachovají. Přepážky ovlivňují pohyb hráče i nákazy.

Každý úspěšný pohyb, manipulace s předmětem a nový herní příkaz přičte jeden tah. Změna stavu se provede před posunem nákazy. Po každém 24. tahu nákaza současně přejde do všech prostorů sousedících otevřeným průchodem s množinou místností nakažených před daným šířením. Nákaza zůstane v již nakažených prostorách. Po tahu se zkontroluje nákaza hráče (i v právě zasažené místnosti), pak výhra a nakonec limit 72 tahů. Vyhodnotí se pouze první splněná podmínka. Infekce je pro hráče okamžitě smrtelná, oblek nemá vlastní počítadlo. Po konci hry se relace ukončí. Konec vstupního proudu ukončí relaci se stejným hlášením jako konec.

### Devět nových příkazů

| Příkaz | Místo a podmínka | Účinek |
| --- | --- | --- |
| odjisti a | Velín, klika v batohu, A zavřená | Otevře A. Klika zůstane hráči. |
| vymen pojistku | Kajuta, pojistka v batohu, rozvaděč bez pojistky | Spotřebuje pojistku a osadí ji do rozvaděče. |
| zapni rozvadec | Kajuta, osazená pojistka, proud vypnutý | Zapne napájení a otevře B. |
| otevri ventil | Chladicí komora, patrona v batohu, proud je zapnutý, chlazení neaktivní | Spotřebuje patronu, spustí chlazení a otevře C. |
| autorizuj odlet | Velín, karta v batohu, aktivní chlazení, odlet dosud nepovolený | Spotřebuje kartu, autorizuje odlet a otevře D. |
| odklop <kontejner> | Sklad: skrin, Strojovna: prepravka, Hangár: schranka. Kontejner je zavřený. | Otevře kontejner a uvolní jeho obsah do místnosti. |
| priprav rampu | Hangár, autorizovaný odlet, E a F uzavřené, rampa nepřipravená | Připraví rampu. |
| uzavri <d/e/f> | D: Únikový modul. E: Kajuta. F: Servisní tunel. Přepážka otevřená, napájení zapnuté. | Trvale zavře zvolenou přepážku. |
| odstartuj | Únikový modul, rampa připravená a D zavřená | Spustí modul. Pokud nenastane prohra, hráč vítězí. |

### Základní a systémové příkazy

`jdi <prostor>` přesune hráče do sousedního prostoru otevřeným průchodem. `seber <vec>` vloží přenosnou věc z místnosti do prázdného batohu. `poloz <vec>` položí drženou věc v aktuálním prostoru. `pomoc` vypíše syntax, `napoveda` aktuální okolí a batoh, `konec` ukončí relaci bez výsledku hry. `uloz` a `nacti` pracují s pevným souborem save.json v pracovním adresáři.

Vstup se ořízne, převede na malá písmena, odstraní se diakritika a mezi slovy se tolerují násobné mezery. První slovo je příkaz, celý zbytek jeden parametr. Systémové a odmítnuté příkazy neposouvají tah.

<!-- page -->

## 2. Mapa stanice

<!-- map -->

Čára vyznačuje obousměrný průchod. A až D jsou zprvu zavřené, E a F otevřené. Značky A až F odpovídají tabulce pod mapou.

| Přepážka | Co ji otevře |
| --- | --- |
| A - Velín / Sklad | Odjištění klikou z Velína. |
| B - Sklad / Dílna | Obnovení napájení v Kajutě. |
| C - Strojovna / Předsíň | Spuštění chlazení v Chladicí komoře. |
| D - Hangár / Únikový modul | Autorizace odletu ve Velínu. Zevnitř modulu se po průchodu uzavře. |
| E - Kajuta / Zadní strojovna | Zprvu otevřená. Z Kajuty ji lze uzavřít po obnově proudu. |
| F - Servisní tunel / Servisní šachta | Zprvu otevřená. Z tunelu ji lze uzavřít po obnově proudu. |

<!-- page -->

## 3. Vítězný scénář

Jediná trasa k odletu vede hlavní chodbou. Cesta pro pojistku a zpět (0-4-0) zabere 8 pohybů, cesta pro patronu (0-8-2) 14, pro kartu (2-10-3) 15 a cesta k modulu (3-11) 8. Celkem nejméně 45 pohybů. K nim přibývají čtyři sebrání, jedno položení kliky a 13 povinných obslužných akcí (devět různých příkazů, odklop a uzavri každý třikrát). Dolní mez je 63 tahů a scénář jí dosahuje.

Sloupec Přesný výstup je součást sekce 4. Pomlčka ve sloupci Změna znamená, že se nic dalšího kromě polohy nebo batohu nezměnilo.

| Tah | Příkaz | Prostor | Batoh | Změna | Přesný výstup |
| --- | --- | --- | --- | --- | --- |
| 1 | seber servisni klika | Kajuta | servisní klika | - | Sebráno: servisní klika. |
| 2 | jdi chodba | Chodba | servisní klika | - | Přesun: Chodba. |
| 3 | jdi chladici komora | Chladicí komora | servisní klika | - | Přesun: Chladicí komora. |
| 4 | jdi velin | Velín | servisní klika | - | Přesun: Velín. |
| 5 | odjisti a | Velín | servisní klika | Otevřena A | Přepážka A je otevřená. |
| 6 | poloz servisni klika | Velín | - | - | Položeno: servisní klika. |
| 7 | jdi sklad | Sklad | - | - | Přesun: Sklad. |
| 8 | odklop skrin | Sklad | - | Skříň otevřena, pojistka ve Skladu. | Otevřeno: skříň. Obsah: pojistka. |
| 9 | seber pojistka | Sklad | pojistka | - | Sebráno: pojistka. |
| 10 | jdi velin | Velín | pojistka | - | Přesun: Velín. |

<!-- page -->

## 3. Vítězný scénář · tahy 11 až 24

| Tah | Příkaz | Prostor | Batoh | Změna | Přesný výstup |
| --- | --- | --- | --- | --- | --- |
| 11 | jdi chladici komora | Chladicí komora | pojistka | - | Přesun: Chladicí komora. |
| 12 | jdi chodba | Chodba | pojistka | - | Přesun: Chodba. |
| 13 | jdi kajuta | Kajuta | pojistka | - | Přesun: Kajuta. |
| 14 | vymen pojistku | Kajuta | - | Osazena pojistka | Pojistka je osazená. |
| 15 | zapni rozvadec | Kajuta | - | Proud, otevřena B | Napájení obnoveno. Přepážka B je otevřená. |
| 16 | uzavri e | Kajuta | - | Ohnisko v Zadní strojovně izolováno. | Přepážka E je uzavřená. |
| 17 | jdi chodba | Chodba | - | - | Přesun: Chodba. |
| 18 | jdi chladici komora | Chladicí komora | - | - | Přesun: Chladicí komora. |
| 19 | jdi velin | Velín | - | - | Přesun: Velín. |
| 20 | jdi sklad | Sklad | - | - | Přesun: Sklad. |
| 21 | jdi dilna | Dílna | - | - | Přesun: Dílna. |
| 22 | jdi osetrovna | Ošetřovna | - | - | Přesun: Ošetřovna. |
| 23 | jdi servisni tunel | Servisní tunel | - | - | Přesun: Servisní tunel. |
| 24 | uzavri f | Servisní tunel | - | Ohnisko v Servisní šachtě izolováno. | Přepážka F je uzavřená. |

<!-- page -->

## 3. Vítězný scénář · tahy 25 až 38

| Tah | Příkaz | Prostor | Batoh | Změna | Přesný výstup |
| --- | --- | --- | --- | --- | --- |
| 25 | jdi strojovna | Strojovna | - | - | Přesun: Strojovna. |
| 26 | odklop prepravka | Strojovna | - | Přepravka otevřena, patrona ve Strojovně. | Otevřeno: přepravka. Obsah: patrona. |
| 27 | seber patrona | Strojovna | patrona | - | Sebráno: patrona. |
| 28 | jdi servisni tunel | Servisní tunel | patrona | - | Přesun: Servisní tunel. |
| 29 | jdi osetrovna | Ošetřovna | patrona | - | Přesun: Ošetřovna. |
| 30 | jdi dilna | Dílna | patrona | - | Přesun: Dílna. |
| 31 | jdi sklad | Sklad | patrona | - | Přesun: Sklad. |
| 32 | jdi velin | Velín | patrona | - | Přesun: Velín. |
| 33 | jdi chladici komora | Chladicí komora | patrona | - | Přesun: Chladicí komora. |
| 34 | otevri ventil | Chladicí komora | - | Chlazení, otevřena C | Chlazení běží. Přepážka C je otevřená. |
| 35 | jdi velin | Velín | - | - | Přesun: Velín. |
| 36 | jdi sklad | Sklad | - | - | Přesun: Sklad. |
| 37 | jdi dilna | Dílna | - | - | Přesun: Dílna. |
| 38 | jdi osetrovna | Ošetřovna | - | - | Přesun: Ošetřovna. |

<!-- page -->

## 3. Vítězný scénář · tahy 39 až 52

| Tah | Příkaz | Prostor | Batoh | Změna | Přesný výstup |
| --- | --- | --- | --- | --- | --- |
| 39 | jdi servisni tunel | Servisní tunel | - | - | Přesun: Servisní tunel. |
| 40 | jdi strojovna | Strojovna | - | - | Přesun: Strojovna. |
| 41 | jdi predsin | Předsíň | - | - | Přesun: Předsíň. |
| 42 | jdi hangar | Hangár | - | - | Přesun: Hangár. |
| 43 | odklop schranka | Hangár | - | Schránka otevřena, karta v Hangáru. | Otevřeno: schránka. Obsah: karta. |
| 44 | seber karta | Hangár | karta | - | Sebráno: karta. |
| 45 | jdi predsin | Předsíň | karta | - | Přesun: Předsíň. |
| 46 | jdi strojovna | Strojovna | karta | - | Přesun: Strojovna. |
| 47 | jdi servisni tunel | Servisní tunel | karta | - | Přesun: Servisní tunel. |
| 48 | jdi osetrovna | Ošetřovna | karta | - | Přesun: Ošetřovna. |
| 49 | jdi dilna | Dílna | karta | - | Přesun: Dílna. |
| 50 | jdi sklad | Sklad | karta | - | Přesun: Sklad. |
| 51 | jdi velin | Velín | karta | - | Přesun: Velín. |
| 52 | autorizuj odlet | Velín | - | Povolení, otevřena D | Odlet povolen. Přepážka D je otevřená. |

<!-- page -->

## 3. Vítězný scénář · tahy 53 až 63

| Tah | Příkaz | Prostor | Batoh | Změna | Přesný výstup |
| --- | --- | --- | --- | --- | --- |
| 53 | jdi sklad | Sklad | - | - | Přesun: Sklad. |
| 54 | jdi dilna | Dílna | - | - | Přesun: Dílna. |
| 55 | jdi osetrovna | Ošetřovna | - | - | Přesun: Ošetřovna. |
| 56 | jdi servisni tunel | Servisní tunel | - | - | Přesun: Servisní tunel. |
| 57 | jdi strojovna | Strojovna | - | - | Přesun: Strojovna. |
| 58 | jdi predsin | Předsíň | - | - | Přesun: Předsíň. |
| 59 | jdi hangar | Hangár | - | - | Přesun: Hangár. |
| 60 | priprav rampu | Hangár | - | Rampa připravena (E a F uzavřené) | Rampa je připravená. |
| 61 | jdi unikovy modul | Únikový modul | - | - | Přesun: Únikový modul. |
| 62 | uzavri d | Únikový modul | - | Uzavřena D | Přepážka D je uzavřená. |
| 63 | odstartuj | Únikový modul | - | Výhra | Únikový modul odstartoval. Vyhráváš. |

<!-- page -->

## 3. Kontrola scénáře a prohra

| První použití | Příkaz | Proč je nový příkaz nutný |
| --- | --- | --- |
| 1 | seber | - |
| 2 | jdi | - |
| 5 | odjisti | Otevře cestu k pojistce. |
| 6 | poloz | - |
| 8 | odklop | Zpřístupní pojistku, patronu a kartu. |
| 14 | vymen | Bez pojistky nelze zapnout proud. |
| 15 | zapni | Otevře B a povolí uzavírání i chlazení. |
| 16 | uzavri | Rampa vyžaduje uzavřené E a F, start uzavřenou D. |
| 34 | otevri | Bez chlazení nelze projít C ani autorizovat odlet. |
| 52 | autorizuj | Bez povolení se D neotevře a rampa se nepřipraví. |
| 60 | priprav | Bez připravené rampy modul nestartuje. |
| 63 | odstartuj | Jako jediný vyhodnotí výhru. |

### Krátký prohrávající scénář

Z nové hry zadej `jdi zadni strojovna`. Tah 1 přesune hráče s prázdným batohem do Zadní strojovny a skončí prohrou. Výstup: Přesun: Zadní strojovna. [NL] Nákaza tě dostihla. Prohráváš.

### Kontrola uložení a načtení

Po 27. tahu dej `uloz`, pak `konec`. Spusť novou relaci a zadej `nacti`. Obnoví se Strojovna s patronou v batohu, klika ve Velínu, osazená pojistka, zapnutý proud, otevřené A a B, zavřené C až F a otevřená skříň i přepravka. Schránka je zavřená. Nákaza je stále ve dvou původních ohniscích. Další tah má číslo 28.

<!-- page -->

## 4. Přesné výstupy hry

Ve scénáři značí symbol [NL] nový řádek. Výstupy v této části ani ve scénáři neobsahují uvozovky. Úvod se vytiskne po startu nové relace. Jediný výstup výhry je uveden u tahu 63.

### Úvod, konec a systémové příkazy

| Událost | Přesný výstup |
| --- | --- |
| Úvod | Poslední přepážka. Stanice Orfeus je napadena. Ohniska: Zadní strojovna, Servisní šachta. Do kolapsu zbývá 72 tahů. Dostaň se do únikového modulu a odstartuj. Začínáš v prostoru Kajuta. Napiš pomoc pro seznam příkazů. |
| pomoc | Příkazy: jdi <prostor>, seber <vec>, poloz <vec>, odjisti a, vymen pojistku, zapni rozvadec, otevri ventil, autorizuj odlet, odklop <kontejner>, priprav rampu, uzavri <d/e/f>, odstartuj, pomoc, napoveda, uloz, nacti, konec. |
| napoveda | Prostor: {prostor}. Sousední prostory: {sousedé}. Věci tady: {věci}. Batoh: {batoh}. Do kolapsu zbývá {72 minus počet tahů}. Zavřená přepážka brání nákaze v postupu. |
| uloz / nacti | Hra uložena. / Hra načtena. |
| konec | Hra ukončena. |
| Prohra při kolapsu | Stanice zkolabovala. Prohráváš. |
| Nákaza postoupila | Nákaza postoupila: {prostory}. |
| Prohra v nakažené místnosti | Nákaza tě dostihla. Prohráváš. |

V nápovědě vypiš sousedy podle ID a u označené přepážky připiš „ ({písmeno}: otevřeno)“ nebo „ ({písmeno}: zavřeno)“. Věci seřaď podle normalizovaných názvů včetně pevných prvků. Sousední prostory a věci odděluj čárkou a mezerou. Prázdný seznam nebo batoh označ „nic“. Pro vstup použij názvy z výpisu bez poznámky o přepážce.

Použij názvy prostorů z mapy, při více nově zasažených prostorech je vypiš podle ID a odděl čárkou a mezerou. Po úspěšném tahu nejdřív vytiskni běžné hlášení akce, potom případné šíření a případný konečný výsledek. `odstartuj` nemá samostatné běžné hlášení. U pohybu použij „Přesun: {prostor}.“, u běžného sebrání a položení použij „Sebráno: {věc}.“ a „Položeno: {věc}.“ s názvem věci v prvním pádě a malými písmeny.

<!-- page -->

## 4. Chyby vstupu a souborů

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

Při více chybách vyber první v tomto pořadí: příkaz, parametr, místo, již provedený úkon, další podmínky. U odklop jsou platné parametry skrin, prepravka, schranka. U uzavri jsou platné d, e, f. Uzavření dosud neodemčené D je nesplněná podmínka, uzavření již utěsněné D je opakovaný úkon. U sebrání nejprve ověř dostupnost, potom přenosnost a kapacitu. Opakované odjištění, výměna, zapnutí, chlazení, autorizace, otevření kontejneru, příprava nebo uzavření se pozná podle příslušného příznaku stavu.

<!-- page -->

## 4. Hlášení přepážek a uložení

Za výpis napoveda přidej v následujících místnostech jeden samostatný řádek. Text se nemění se stavem hry.

| Prostor | Přesný doplňující řádek nápovědy |
| --- | --- |
| Kajuta | Rozvaděč potřebuje pojistku. Přepážka E má elektrický pohon. |
| Chladicí komora | Ventil potřebuje napájení a chladicí patronu. |
| Velín | Přepážku A odjistí servisní klika. Konzole potřebuje chlazení a kartu. |
| Servisní tunel | Přepážka F má elektrický pohon. |
| Hangár | Rampa vyžaduje autorizaci a uzavřené přepážky E a F. |
| Únikový modul | Start vyžaduje připravenou rampu a uzavřenou přepážku D. |

Soubor save.json obsahuje verzi formátu, ID prostoru hráče, pozici každé přenosné věci (místnost, kontejner, batoh nebo spotřebováno), celkový počet tahů, nakažené prostory, stav šesti přepážek (u D rozlišit zamčeno a trvale uzavřeno), stav otevření každého kontejneru a příznaky osazené pojistky, zapnutého proudu, chlazení, povolení odletu a připravené rampy. Po načtení se obnoví všechny uložené hodnoty. Neznámou verzi, chybějící údaje a neplatné nebo rozporné hodnoty hra odmítne; současná rozehraná hra zůstane zachovaná. Při ukládání se hotový dočasný soubor přesune na cílovou cestu až po úspěšném zápisu. Hra ošetří chyby vstupu a souborů bez pádu.

## 5. Uživatelská příručka

Po sestavení hotové hry spusť v terminálu `java -jar target/posledni-prepazka.jar`. Cílem je opustit napadenou stanici v únikovém modulu. Každou akci napiš na samostatný řádek a potvrď Enterem. Používej názvy prostorů a předmětů tak, jak je uvádí hra. Příkazy fungují i bez české diakritiky.

- `jdi <prostor>`, `seber <vec>` a `poloz <vec>` slouží k pohybu a manipulaci s předměty. Batoh má jedno místo.
- `odjisti a`, `vymen pojistku`, `zapni rozvadec`, `otevri ventil`, `autorizuj odlet`, `odklop <kontejner>`, `priprav rampu`, `uzavri <d/e/f>` a `odstartuj` slouží k obsluze stanice a modulu.
- `pomoc` zobrazí příkazy, `napoveda` prostor, sousedy, věci a batoh. `konec` ukončí relaci.
- `uloz` přepíše uloženou pozici v souboru save.json ve složce, ze které je hra spuštěná. Po spuštění hry můžeš příkazem `nacti` pokračovat z tohoto souboru.
- Nákaza postupuje s tahy. Čtení, chybné vstupy a systémové příkazy čas neposunou.

## 6. Členové týmu

Před odevzdáním doplňte skutečná jména a xname a potvrďte pracovní rozdělení. Každý nový příkaz a každý rozšiřující prvek má právě jednoho odpovědného člena.

| Jméno a příjmení | xname | Nové příkazy | Prvek | Další podíl |
| --- | --- | --- | --- | --- |
| Člen 1 | Doplnit | odjisti, vymen, odklop | skříň | Mapa, společná pravidla kontejnerů a inventář |
| Člen 2 | Doplnit | zapni, otevri | přepravka | Tahy, šíření nákazy a vyhodnocení prohry |
| Člen 3 | Doplnit | autorizuj, priprav | schránka | Přesné herní texty, uložení a načtení |
| Člen 4 | Doplnit | uzavri, odstartuj | - | Přepážky, scénáře a uživatelská příručka |
