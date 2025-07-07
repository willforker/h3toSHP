import pandas as pd
import geopandas as gpd
from shapely.geometry import shape, Polygon
import h3
import argparse
import os

def h3_to_polygon(h3_index):
    """Convert an H3 index to a shapely Polygon."""
    boundary = h3.cells_to_h3shape([h3_index])
    polygon = shape(boundary.__geo_interface__)
    return polygon # returns GeoJSON string geom

def csv_to_geofile(csv_path, h3_column='h3', output_path='output.geojson'):
    # Load CSV
    df = pd.read_csv(csv_path)
    
    if h3_column not in df.columns:
        raise ValueError(f"Column '{h3_column}' not found in CSV.")

    # Generate geometries
    df['geometry'] = df[h3_column].apply(h3_to_polygon)

    # Convert to GeoDataFrame
    gdf = gpd.GeoDataFrame(df, geometry='geometry', crs='EPSG:4326')

    # Save to file
    _, ext = os.path.splitext(output_path.lower())
    if ext == '.shp':
        gdf.to_file(output_path)
    elif ext == '.geojson' or ext == '.json':
        gdf.to_file(output_path, driver='GeoJSON')
    else:
        raise ValueError("Unsupported output format. Use .shp or .geojson")

    print(f"Geo file saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert H3 CSV to GeoFile (GeoJSON or Shapefile).")
    parser.add_argument("csv_path", help="Path to input CSV file")
    parser.add_argument("--h3_column", default="h3", help="Column name containing H3 indices")
    parser.add_argument("--output", default="output.geojson", help="Path to output file (.geojson or .shp)")

    args = parser.parse_args()
    csv_to_geofile(args.csv_path, args.h3_column, args.output)
