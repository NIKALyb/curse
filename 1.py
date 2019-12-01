#connect library
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block
import time
import random
#variable
def createGB():
    x = random.randint(0,50)
    z = random.randint(0,50)
    y = 134
pos = mc.player.getTilePos()
createGB
#setBlock
#mc.setBlocks(0,130,0,55,150,55,0)
#mc.setBlocks(51,130,51,-1,131,-1,22)
#mc.setBlocks(50,131,50,0,131,0,0)
#setGOLD
mc.setBlock(x,y,z,41)
#loop
while True:
    pos = mc.player.getTilePos()
    if round(pos.x) == x and round(pos.z) == z:
        mc.setBlock(x,y,z,0)
        mc.postToChat("Nice, you found GOLD")
