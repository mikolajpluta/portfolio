from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
def tileContainsPoint(self, tile_points, x, y):
    x = x + 0.00001     #needed because of inaccuracy of float,
    y = y + 0.00001     #sometimes when point is located on the border of tile, function does not work properly
    point = Point(x, y)
    tile_area = Polygon([(tile_points[0], tile_points[1]), (tile_points[2], tile_points[3]), (tile_points[4], tile_points[5]), (tile_points[6], tile_points[7])])
    if tile_area.contains(point):
        return True
    return False