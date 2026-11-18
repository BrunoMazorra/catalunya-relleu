# Catalunya en relleu

Mapa 3D de la població dels municipis de Catalunya, de 1981 a 2026, centrat en el voltant de Barcelona.

**Pàgina web: https://brunomazorra.github.io/catalunya-relleu/**

Cada municipi és un prisma: l'alçada és la densitat de població i el color, el canvi de població des de 1981. La barra de temps va de 1981 a 2026, i els cercles marquen la distància a la plaça de Catalunya cada 10 km. A sota del mapa hi ha les gràfiques per anells de distància i una taula amb les dades.

## Què mostra

Barcelona i els municipis a menys de 10 km tenen gairebé la mateixa gent que el 1981. Tot el creixement s'ha fet entre 10 i 60 km de Barcelona.

![Població acumulada fins a 10, 20, 30, 40, 50 i 60 km de la plaça de Catalunya, 1981–2026](img/poblacio-fins-60km.svg)

![Canvi de població des de 1981, anell per anell](img/canvi-per-anells.svg)

| Anell (distància a la plaça de Catalunya) | 1981 | 2026 (provisional) | Canvi |
|---|---:|---:|---:|
| Barcelona ciutat | 1.752.000 | 1.744.000 | 0 % |
| 0–10 km | 908.000 | 935.000 | +3 % |
| 10–20 km | 824.000 | 1.279.000 | +55 % |
| 20–30 km | 475.000 | 900.000 | +89 % |
| 30–40 km | 153.000 | 376.000 | +146 % |
| 40–50 km | 237.000 | 430.000 | +81 % |
| 50–60 km | 185.000 | 366.000 | +98 % |
| **Fins a 60 km** | **4.534.000** | **6.029.000** | **+33 %** |
| Més de 60 km | 1.416.000 | 2.182.000 | +54 % |
| **Catalunya** | **5.950.000** | **8.211.000** | **+38 %** |

Xifres arrodonides al miler. Cada municipi compta a l'anell on cau el seu centre; Barcelona es compta a part.

## Dades i mètode

- Població: Idescat, [padró municipal](https://www.idescat.cat/pub/?id=pmh&n=446&lang=ca) 1998–2025 i [sèries històriques](https://www.idescat.cat/pub/?id=shd&n=1341&lang=ca) de 1981, 1986 i 1991. Entre aquests anys la població de cada municipi s'interpola i cada any s'ajusta al total de Catalunya. 2026 és l'avanç provisional per províncies aplicat a 2025.
- Contorns municipals: INE, via [es-atlas](https://github.com/martgnz/es-atlas), simplificats.
- Distàncies: des de la plaça de Catalunya fins al centre de cada municipi, en una projecció plana local.

## Estructura

```
index.html              pàgina completa (es genera, no s'edita a mà)
src/template.html       pàgina: estils, mapa 3D (three.js) i gràfiques
src/charts.js           dibuix de les gràfiques, compartit amb el script de les imatges
src/build.py            junta plantilla + gràfiques + dades → index.html
src/readme-charts.mjs   genera les imatges de img/ amb el mateix codi
data/municipis.json     població per any i contorn de cada municipi
```

Per regenerar-ho:

```bash
python3 src/build.py
node src/readme-charts.mjs
```
