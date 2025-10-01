# stdlib imports
import pathlib
from collections.abc import Sequence
from typing import Literal

# third party imports
import geopandas as gpd
import pandas as pd
from pyproj import CRS, Transformer
from shapely.geometry import box

# local imports
from esi_utils_geo.city import Cities
from esi_utils_geo.font_calculator import FontCalculator

DEFAULT_BUFFER_RATIO = (
    0.01  # fraction of total width of map that should be the buffer around a city bbox
)
JUSTIFICATIONS = Literal["TL", "TC", "TR", "ML", "MC", "MR", "BL", "BC", "BR"]


def get_mercator_cities(
    cities: Cities,
    bounds: Sequence[float],
    fontname: str,
    fontsize: int,
    figure_width: float,
    nrows: int = 2,
    ncols: int = 2,
    cities_per_grid: int = 20,
    buffer_ratio: int = DEFAULT_BUFFER_RATIO,
    justify_string: JUSTIFICATIONS = "BL",
    debug: bool = False,
) -> pd.DataFrame:
    """Retrieve a dataframe of cities inside GMT Mercator map that do not collide.

    Notes:
     - This will only work with ASCII city names.
     - nrow/ncols/cities_per_grid options are used to divide the map into a grid
       and limit each grid cell to the largest cities_per_grid cities.

    Args:
        cities - esi-utils-geo Cities instance.
        bounds - sequence of (lonmin,lonmax,latmin,latmax)
        fontname - Font name (one of the 35 Postscript fonts)
        fontsize - Size in points
        figure_width - Width of GMT figure in inches.
        nrows - Number of rows to make in grid
        ncols - Number of columns to make in grid
        cities_per_grid - Maxmimum number of cities to allow in each grid cell.
        buffer_ratio - Amount of whitespace to add around city names,
                       as a percentage of figure width.
    Returns:
        dataframe Pandas dataframe containing cities that will not collide, with at least these columns.
                  - name ASCII City name
                  - lat Latitude of city
                  - lon Longitude of city
                  - pop Population of city
    """
    xmin, xmax, ymin, ymax = bounds
    fontsfile = pathlib.Path(__file__).parent / "data" / "postscript_fonts.json"
    calculator = FontCalculator(fontsfile)
    mapcities = (
        cities.limitByBounds(bounds)
        .limitByGrid(nx=ncols, ny=nrows, cities_per_grid=cities_per_grid)
        .getDataFrame()
    )
    mapcities.sort_values(by="pop", ascending=False, inplace=True)
    mapcities = mapcities.loc[mapcities["pop"] >= 1000]
    mapcities.reset_index(inplace=True)

    # handle 180 meridian crossing
    if xmin > xmax:
        xmax += 360
    clon = xmin + (xmax - xmin) / 2
    if clon > 180:
        clon -= 360

    clat = ymin + (ymax - ymin) / 2
    proj_str = f"+proj=merc +lon_0={clon} +ellps=WGS84 +units=m +no_defs +lat_ts={clat}"
    map_crs = CRS(proj_str)
    wgs84_crs = CRS("EPSG:4326")
    transformer = Transformer.from_crs(wgs84_crs, map_crs, always_xy=True)
    ulx, uly = transformer.transform(xmin, ymax)
    lrx, lry = transformer.transform(xmax, ymin)
    fig_projected_width = lrx - ulx
    fig_projected_height = uly - lry
    aspect = fig_projected_width / fig_projected_height
    figure_height = figure_width / aspect

    buffer = fig_projected_width * buffer_ratio

    rectangle_coords = []

    lefts = []
    rights = []
    bottoms = []
    tops = []
    map_xcolumn = []
    map_ycolumn = []

    for _, city in mapcities.iterrows():
        lat = city["lat"]
        lon = city["lon"]
        name = city["name"]
        map_x, map_y = transformer.transform(lon, lat)
        width_string_inches, height_string_inches = calculator.get_string_size_inches(
            name, fontname, fontsize
        )
        width_string_map = (width_string_inches / figure_height) * fig_projected_width
        height_string_map = (
            height_string_inches / figure_height
        ) * fig_projected_height
        x_adj = 0
        y_adj = 0
        if "C" in justify_string:
            x_adj = width_string_map * 0.5
        elif "R" in justify_string:
            x_adj = width_string_map * 1.0
        if "M" in justify_string:
            y_adj = height_string_map * 0.5
        elif "T" in justify_string:
            y_adj = height_string_map * 1.0

        # take the desired justification into account when setting the
        # left/right/bottom/top edge coordinates.
        left = map_x - x_adj - buffer
        right = map_x + width_string_map - x_adj + buffer
        bottom = map_y - y_adj - buffer
        top = map_y + height_string_map - y_adj + buffer

        map_xcolumn.append(map_x)
        map_ycolumn.append(map_y)

        lefts.append(left)
        rights.append(right)
        bottoms.append(bottom)
        tops.append(top)

        rectangle_coords.append((left, bottom, right, top))

    rectangles = [
        box(minx, miny, maxx, maxy) for minx, miny, maxx, maxy in rectangle_coords
    ]
    gdf = gpd.GeoDataFrame(geometry=rectangles, crs=map_crs.to_wkt())
    for column in mapcities.columns:
        gdf[column] = mapcities[column].values

    # filter out cities that draw off the map
    gdf["left"] = lefts
    gdf["right"] = rights
    gdf["bottom"] = bottoms
    gdf["top"] = tops
    gdf["map_x"] = map_xcolumn
    gdf["map_y"] = map_ycolumn
    inside_idx = (
        (gdf["left"] >= ulx)
        & (gdf["right"] <= lrx)
        & (gdf["bottom"] >= lry)
        & (gdf["top"] <= uly)
    )
    gdf = gdf.loc[inside_idx].copy()
    drop_labels = ["index"]
    if not debug:
        drop_labels += ["left", "right", "bottom", "top", "map_x", "map_y"]
    gdf.drop(labels=drop_labels, axis="columns", inplace=True)

    loser_idx = []
    for idx1, city1 in gdf.iterrows():
        if idx1 in loser_idx:
            continue
        for idx2, city2 in gdf.iterrows():
            if idx1 == idx2:
                continue
            if idx2 in loser_idx:
                continue
            if city1["geometry"].intersects(city2["geometry"]):
                loser_idx.append(idx2)

    mapcities = gdf[~gdf.index.isin(loser_idx)]
    map_frame = pd.DataFrame(mapcities.drop(columns=["geometry"]))
    return map_frame
