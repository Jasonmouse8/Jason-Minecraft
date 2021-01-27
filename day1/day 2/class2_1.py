from mcpi.minecraft import Minecraft as mc
import time
time.sleep(2)
mcs=mc.create()
x,y,z=mcs.player.getTilePos()
s=80
mcs.setBlocks(x+s,y,z=s)
x,y,z=mcs.player.getTilePos()
mcs.setBlocks(x+s,y,z=s)