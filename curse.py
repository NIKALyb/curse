#Connect library
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block
import time
#variable
a = 0
#infinite loop
while a < 20:
    pos = mc.player.getTilePos()
    x = round(pos.x)
    y = round(pos.y)
    z = round(pos.z)
    mc.setBlocks(x, y, z, x, y+1, z, 8)
    a += 1
    time.sleep(0.5)
    	mc.postToChat("You death soon")