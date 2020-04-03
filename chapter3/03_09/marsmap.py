
import io, bs4
import PIL.Image
import matplotlib.pyplot as pp
from mpl_toolkits.basemap import Basemap

def get_location(day):
    xml = bs4.BeautifulSoup(open('locations.xml'), 'lxml-xml')
    locations = xml.find_all('location')
    
    for location in locations:
        if float(location.startSol.string) <= day and day <= float(location.endSol.string):
            return {'lat': float(location.lat.string), 'lon': float(location.lon.string)}


def plot_location(latlon):
    crater = PIL.Image.open('gale_themis_vis_fix_v4_reduced.png')
    
    pp.figure(figsize = (12, 6))
    
    pp.imshow(crater, origin = 'upper', interpolation = 'none',
         cmap = pp.get_cmap('gray'),
         extent = [135.6, 139.9, -7.5, -3.2])
    
    world = Basemap(lon_0 = 180)
    world.plot(latlon['lon'], latlon['lat'], 'r.', latlon = True)
    
    pp.axis(xmin = 137, xmax = 138, ymin = -5 , ymax = -4.5)
    
    buffer = io.BytesIO()
    pp.savefig(buffer, format = 'PNG')
    pp.close()
    
    return buffer
