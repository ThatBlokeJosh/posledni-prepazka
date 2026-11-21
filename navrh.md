# Návrh hry

## Příběh a cíl

Hráč je technik na vesmírné stanici, jejíž systémy narušuje fiktivní houbovitá nákaza. Začíná v kajutě, zatímco první napadený prostor je zadní strojovna. Musí obnovit proud, izolovat napadené sektory a zprovoznit únikový modul. Vyhraje úspěšným startem. Prohraje, jakmile nákaza pronikne do kterékoli místnosti s hráčem nebo do hangáru, kde vyřadí odpalovací rampu.

## Mapa stanice

Každé spojení je obousměrné, když je otevřené. Běžné průchody v sektoru jsou průchozí od začátku.

- **Obytný sektor:** Kajuta (start) ↔ Chodba ↔ Sklad. Chodba ↔ Ošetřovna.
- **Technický sektor:** Rozvodna ↔ Dílna ↔ Zadní strojovna (zdroj nákazy). Dílna ↔ Chladicí komora.
- **Evakuační sektor:** Předsíň ↔ Velín, Předsíň ↔ Hangár ↔ Únikový modul.
- **Přepážka A:** Chodba ↔ Rozvodna. Otevírá se mechanicky.
- **Přepážka B:** Rozvodna ↔ Předsíň. Otevírá se elektricky po obnovení proudu.
- **Poklop modulu:** Hangár ↔ Únikový modul. Odemkne se po autorizaci ve Velínu.

## Předměty a interakce

Sklad obsahuje přenosnou pojistku a servisní kliku, Ošetřovna přenosnou autorizační kartu. Batoh má pracovní kapacitu dva předměty. V Rozvodně je pevný rozvaděč, v Chladicí komoře pevný ventil, ve Velínu pevná konzole a v Hangáru pevný ovládací panel rampy. Rozvaděč, ventil a konzole jsou interaktivní prvky. Výměna pojistky ji odebere z batohu, takže uvolní místo pro kartu.

## Nákaza a tahy

Pracovní pravidlo je, že po každém dvacátém úspěšném herním tahu nákaza postoupí po každém otevřeném propojení z místností zasažených na začátku šíření. V jednom takovém tahu tedy postoupí nejvýš o jedno spojení. Zavřená přepážka šíření blokuje. Úspěšné akce jako pohyb, sebrání a položení předmětu posouvají čas. Chybný vstup a systémové příkazy ho neposouvají. Výhra příkazem startu skončí okamžitě. Interval šíření se doladí podle kompletního scénáře.

Aby bylo uzavření přepážky B nutné i při rychlé hře, bezpečnostní kontrola ve Velínu povolí start jen při uzavřené B. Před startem musí být zároveň obnovené napájení, aktivní chlazení, povolený poklop a připravená rampa.

## Osm nových příkazů

| Příkaz | Účinek a vazba na výhru |
| --- | --- |
| `odjisti A` | V Chodbě se servisní klikou otevře jedinou cestu do Rozvodny. |
| `vymen pojistku` | V Rozvodně vloží pojistku z batohu do rozvaděče. |
| `zapni rozvadec` | S novou pojistkou obnoví proud a otevře přepážku B. |
| `otevri ventil` | V Chladicí komoře spustí chlazení potřebné k přípravě rampy. |
| `uzavri B` | Z Předsíně uzavře přepážku kvůli šíření a podmínce autorizace. |
| `autorizuj odlet` | Ve Velínu s kartou a uzavřenou B udělí povolení a odemkne poklop modulu. |
| `priprav rampu` | Z Hangáru s napájením, chlazením a povolením připraví rampu ke startu. |
| `odstartuj` | Z modulu s připravenou rampou ukončí hru výhrou. |

Základní příkazy jsou `jdi`, `seber`, `poloz`, `konec`, `pomoc` a `napoveda`. `uloz` a `nacti` budou pracovat i s pozicí hráče, předměty, stavem techniky a dveří, počítadlem tahů a rozsahem nákazy.

## Ukázka prvního průchodu

Hráč ve Skladu sebere kliku a pojistku, vrátí se do Chodby, odjistí A a v Rozvodně vymění pojistku. Protože výměna uvolnila místo v batohu, může se ještě vrátit do Ošetřovny pro kartu. Před vstupem do evakuačního sektoru musí zapnout rozvaděč a otevřít ventil. Z Předsíně pak uzavře B, aby mohl odlet autorizovat.

## K dopracování před odevzdáním

- Rozpracovat trasu tak, aby **nejkratší vítězný postup** vyžadoval alespoň 40 herních kroků. Tato kostra zatím čtyřicet kroků nezajišťuje. Do vítězného scénáře zahrnout i smysluplné použití příkazu `poloz`.
- Ověřit, že vhodný interval šíření umožní vítěznou trasu a dává hráči čas odbočit do Chladicí komory. Sepsat krokový vítězný a krátký prohrávající scénář.
- Doplnit přesná hlášení, grafický plánek, příručku a týmové rozdělení (dva nové příkazy na člena a jeden odpovědný člen za každý příkaz a rozšiřující prvek).
