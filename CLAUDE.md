# Utrecht, building by building

A 3D map of every building in Utrecht, coloured by construction year. First portfolio project on the way to spatial analytics / location optimization consultancy work. Made for fun and learning.

## About me
- Gökçen. MSc Econometrics & Management Science (operations research). Comfortable with Python and mathematical modelling.
- New to geospatial tooling: coordinate systems, GeoPandas, QGIS, web maps are all still being learned.
- Working on this alongside a full-time job, at my own pace. Don't plan my time or propose schedules.

## How to work with me
- This is a learning project. Explain concepts and think through decisions together; don't just hand over finished code.
- When there is a modelling choice, lay out the options plainly and let me decide. Explain jargon when you first use it.
- Be concise and direct. No unnecessary affirmations.
- Prefer open-source tools.

## Inspiration / reference
- LAYRS Delft and Amsterdam maps by Alex Barakov: https://stop-token.com/lab/amsterdam/
- Code: https://github.com/alexbarakov/amsterdam-by-building (MIT licence). Use it as a reference to compare against after I've tried something myself, not as a template to copy. Credit it.
  - `pipeline/s01_load.py`: loads 3D BAG tiles, clips to city boundary.
  - `pipeline/s02_attributes.py`: repairs BAG construction years (placeholder 1005, spikes at round years like 1905, monument register overrides, estimates from dated neighbours) and computes heights.

## Decisions so far
- **Data source:** 3D BAG (TU Delft) tiles, as Barakov does. CC BY 4.0, credit it.
- **Status:** keep only existing buildings; rely on 3D BAG for this (it covers existing buildings). Worth verifying the status column once Utrecht is loaded.
- **Which buildings:** keep everything, including sheds and small structures.
- **Height:** 70th-percentile roof height (`b3_h_dak_70p`) of the tallest LoD1.3 part, minus ground height (`b3_h_maaiveld`), minimum 2.5 m. Same as Barakov.
- **Construction years:** use Barakov's approach to cleaning bad BAG years (concept, not copy-paste).
- **Clipping to Utrecht:** keep a building if its representative point (`representative_point()`, guaranteed inside the polygon, unlike the centroid) falls inside the gemeente boundary.
- **3D is a must.** Render with MapLibre GL `fill-extrusion` (not three.js). Serve data as PMTiles built with `tippecanoe`.
- **Not in scope for now:** photos, Wikipedia stories, residents, quests.

## Steps
1. Download Utrecht's 3D BAG tiles (via the 3D BAG tile index) and the gemeente boundary (CBS gemeentegrenzen via PDOK). ← next
2. Build one clean building table in Python: ID, geometry, year, height, function, buurt. Fix bad years.
3. Convert to PMTiles with tippecanoe.
4. Render in MapLibre with fill-extrusion, coloured by year.
5. Later: add layers on the same building table (energy labels, walking time to amenities, facility location optimization, e.g. "where should the next X go").

## Geo notes
- Dutch data is in EPSG:28992 (RD New, metres). Web maps need EPSG:4326 (WGS84 lon/lat). Reproject at export time.
- Data credits: 3D BAG CC BY 4.0; BAG/BGT via PDOK CC0; CBS CC BY 4.0; OSM ODbL.
