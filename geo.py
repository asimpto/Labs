import h3


def get_hexagons(resolution):
    min_lat, max_lat = -90.0, 90.0
    min_lon, max_lon = -180.0, 180.0

    hexagons = set()

    lat_step = 1
    lon_step = 1

    lat = min_lat
    while lat < max_lat:
        lon = min_lon
        while lon < max_lon:
            hexagon = h3.geo_to_h3(lat, lon, resolution)
            hexagons.add(hexagon)
            lon += lon_step / 3
        lat += lat_step / 3

    return hexagons


resolution = 3
hexagons = get_hexagons(resolution)

with open('out.txt', 'w') as f:
    print(f"Total hexagons at resolution {resolution}: {len(hexagons)}", file=f)
    for hexagon in hexagons:
        vertices = h3.h3_to_geo_boundary(hexagon)
        print(f"Hexagon: {hexagon}", file=f)
        print("Vertices:", file=f)
        for vertex in vertices:
            print(vertex, file=f)
