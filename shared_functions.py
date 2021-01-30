import mcpi.minecraft as minecr
from mcpi.vec3 import Vec3
mc=0
ON = True
OFF = False
def start(adress=None, port=None):
    '''The function to connect to minecraft.'''
    global mc
    if adress or port:
        mc = minecr.Minecraft.create(adress, port)
    else:
        mc = minecr.Minecraft.create()

if __name__ == '__main__':
    start()

def chat(string):
    '''posts to the chat.'''
    mc.postToChat(string)

def place(x, y, z, id_, type_=None):
    '''analogue for setBlock
    basically sets a block in the given x,y,z
    id_ is the block id, and type_ is the block additional
    id. '''
    if type_:
        blk = mc.setBlock(x,y,z,id_,type_)
        return
    mc.setBlock(x,y,z,id_)
def teleport(x,y,z, player_id=None):
    '''teleports the main player to x y z
    Advanced use: add the argument player_id to
    teleport a specific player
    use getPlayers for a list of players
    on your server'''
    if player_id:
        mc.entity.setPos(player_id, x, y, z)
    else:
        mc.player.setPos(x,y,z)
def getPlayers():
    '''returns the ids of the players'''
    return mc.getPlayerEntityIds()

MAIN_PLAYER = getPlayers()[0]

def cuboid(x1,y1,z1,x2,y2,z2,id_,type_=None):
    if type_:
        mc.setBlocks(x1,y1,z1,x2,y2,z2,id_,type_)
        return
    mc.setBlocks(x1,y1,z1,x2,y2,z2,id_)

def whereAmI():
    x,y,z = mc.player.getTilePos()
    pos = Vec3(x,y,z)
    return pos

def whereIsHe(playerId):
    x,y,z = mc.entity.getTilePos(playerId)
    pos = Vec3(x,y,z)
    return pos

def worldImmutable(state=ON):
    if state:
        mc.setting('world_immutable', True)
    else:
        mc.setting('world_immutable', False)


def nameTags(state=ON):
    if state:
        mc.setting('nametags_visible', True)
    else:
        mc.setting('nametags_visible', False)

def autoJump(state=ON):
    if state:
        mc.setting('autojump', True)
    else:
        mc.setting('autojump', False)

def includeNBT(state=ON):
    if state:
        mc.setting('include_nbt_with_data', True)
    else:
        mc.setting('include_nbt_with_data', False)

def camMode(mode, playerId=MAIN_PLAYER,x=0,y=0,z=0):
    try:
        modeLowered = mode.lower()
    except:
        modeLowered = 0
    if modeLowered:
        if modeLowered == 'normal':
            mode = 1
        elif modeLowered == 'fixed':
            mode = 2
        elif modeLowered == 'follow':
            mode = 3
        elif modeLowered == 'pos':
            mode = 4
    if mode == 1:
        mc.camera.setNormal(playerId)
    elif mode == 2:
        mc.camera.setFixed()
    elif mode == 3:
        mc.camera.setFollow(playerId)
    elif mode == 4:
        mc.camera.setPos(x,y,z)
        
