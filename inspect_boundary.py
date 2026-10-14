import geopandas as gpd
import pyogrio
import matplotlib.pyplot as plt

path = "data/raw/GIS_DSG_GEM_GRENS.gpkg"
print(pyogrio.list_layers(path))   # a GeoPackage can hold several layers
b = gpd.read_file(path)
print(b.crs)
print(len(b), b.geom_type.tolist())
print(b.area / 1e6, "km²")         # area is in m² because RD New is in metres
b.plot()
plt.show()

