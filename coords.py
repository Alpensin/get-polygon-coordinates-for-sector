from math import pi, cos, sin

def build_sector(azimuth, beam, lat, lon, length=150, parts=2):
    """Drawing sector displaying azimuth and horizontal beam of antenna"""
    border_h = beam/2
    step = border_h/parts
    azimuths = list(0 for i in range(parts*2+1))
    azimuths[len(azimuths)//2] = azimuth
    for part in range(parts):
        angle = border_h-step*part
        azimuths[part] = azimuth-angle
        azimuths[len(azimuths)-1-part] = azimuth+angle
    coords = [(round(lon,5),round(lat,5))]
    for az in azimuths:
        c_lat = round(lat + length * cos(az * pi / 180) / (6371000 * pi / 180),5)
        c_lon = round(lon + length * sin(az * pi / 180) / cos(lat * pi / 180) / (earth_radius * pi / 180),5)
        coords.append((c_lon,c_lat))
    coords.append(coords[0])
    return coords
if __name__ == "__main__":
    #EXAMPLE
    earth_radius = 6371000
    ASSET_AZIMUTH = 140
    H_BEAM = 59
    LAT = 55.75254445
    LON = 37.60566667

    coords = build_sector(ASSET_AZIMUTH, H_BEAM, LAT, LON)
    print(",0 ".join(f"{i},{j}" for i,j in coords)+',0') #format for kml with 0 height
