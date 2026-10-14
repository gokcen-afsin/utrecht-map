"""Select the 3D BAG tiles that overlap the gemeente Utrecht."""
import geopandas as gpd
import matplotlib.pyplot as plt

BOUNDARY = "data/raw/GIS_DSG_GEM_GRENS.gpkg"
TILE_INDEX = "data/raw/tile_index.fgb"
OUT = "data/processed/utrecht_tiles.gpkg"

b = gpd.read_file(BOUNDARY)
print("boundary CRS:", b.crs)

# Option 1: keep tiles overlapping Utrecht's bounding box (xmin, ymin, xmax, ymax).
tiles_bbox = gpd.read_file(TILE_INDEX, bbox=tuple(b.total_bounds))

# Option 2: keep tiles overlapping the actual boundary polygon.
tiles_mask = gpd.read_file(TILE_INDEX, mask=b.geometry.iloc[0])

print("tile index CRS:", tiles_mask.crs)  # must match the boundary, or the filter is meaningless
print("tiles via bbox:", len(tiles_bbox))
print("tiles via mask:", len(tiles_mask))
print(tiles_mask.columns.tolist())
print(tiles_mask.head())

# Save the selection; the download step reads the gpkg_download links from it.
tiles_mask.to_file(OUT)

# Grey: tiles dropped by the mask. Black: tiles kept. Blue: Utrecht.
ax = tiles_bbox.boundary.plot(color="lightgrey", figsize=(8, 8))
tiles_mask.boundary.plot(ax=ax, color="black", linewidth=0.5)
b.plot(ax=ax, alpha=0.4)
ax.set_title(f"3D BAG tiles: {len(tiles_mask)} overlap Utrecht ({len(tiles_bbox)} in bbox)")
plt.show()
