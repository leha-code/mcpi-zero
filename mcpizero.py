import mcpi.minecraft as minecr
mc = None

def start(adress=None, port=None):
    '''The function to connect to minecraft.'''
    global mc
    if adress or port:
        mc = minecr.Minecraft.create(adress, port)
    else:
        mc = minecr.Minecraft.create()
def chat(string):
    '''posts to the chat.'''
    mc.postToChat(string)

def place(x, y, z, id_, type_=None):
    '''analogue for setBlock
    basically sets a block in the given x,y,z
    id_ is the block id, and type_ is the block additional
    id. '''
    if type_:
        mc.setBlock(x,y,z,id_,type_)
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
    mc.getPlayerEntityIds()


def cuboid(x1,y1,z1,x2,y2,z2,id_,type_=None):
    if type_:
        mc.setBlocks(x1,y1,z1,x2,y2,z2,id_,type_)
        return
    mc.setBlocks(x1,y1,z1,x2,y2,z2,id_)
def whereAmI(player=None):
    if not player:
        mc.player.getTilePos()
    else:
        mc.entity.getTilePos(player)    

start()

if __name__ == '__main__':
    chat('Hello Minecraft World!')
