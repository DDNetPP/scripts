import os

from tml.tml import Teemap
from tml.constants import TML_DIR, TILEINDEX
from tml.items import Layer, TileLayer, TileManager, Tile


print(TML_DIR)

map_path = os.sep.join([TML_DIR, '/maps/dm1'])
t = Teemap(map_path)
pickups = {
    'shotgun': 0,
    'grenade': 0,
    'rifle': 0,
    'ninja': 0,
    'health': 0,
    'armor': 0,
    'solid': 0,
    'air': 0,
    'death': 0,
    'nohook': 0,
}
for tile in t.gamelayer.tiles:
    for key, value in pickups.iteritems():
        if tile.index == TILEINDEX[key]:
            pickups[key] += 1

for k, v in pickups.iteritems():
    print '{value:3}x {key}'.format(value=v, key=k)

t.gamelayer.tiles[0] = Tile(3) # set first tile x/y 0/0 to unhook
t.gamelayer.set_tile(2, 0, Tile(2)) # zilli dreghun stinkt c:
print("should be air(0): " + str(t.gamelayer.get_tile(5,6)))
print("should be shield(197): " + str(t.gamelayer.get_tile(3,7)))
print("should be spawn(192): " + str(t.gamelayer.get_tile(10,10)))
t.save('tml_map')