'''User management system and database. Stores users, their passwords, 
check access levels, and so on.

peers = [list of logged in peers]
userdb = {"username": {"password": password, "access": LEVEL, "loggedin": BOOL, "peer": (peer,peer)}
Access levels:
OBSERVER: Can only observe region and cities with permission for that user to observe. Good for guests
NORMAL: Normal player with no server level privlidges
GM: Game master, can ban, unban, kick, delete any city, save (but not load), delete users. Can move users to and from observer mode. A moderator to use forum speak. 
ADMIN: Full server control. Load and new Games. Can stop or start the server. Can promote anyone to GM, observer, normal or admin. Can enter any city.
OWNER: Top level. Can only promote others to owner, but this is a non reversible process. Can not be demoted.

The permission system is progressive, so permission checking will check to see if the user is that level or greater.

loggedin and peer are to check that the user is logged in and the peer to contact them by.

It *may* be needed that the user will need to be a class other than the dict, so we will still abstract what we need through functions
'''
import logging
logger = logging.getLogger('server.users')

import sys
sys.path.append("..")
import common.protocol_pb2 as proto

# Access levels
OBSERVER = 0
NORMAL = 1
GM = 2
ADMIN = 3
OWNER = 4

ACCESS = {"observer": OBSERVER, "normal": NORMAL, "gm": GM, "admin": ADMIN, "owner": OWNER}

# {name: userObject}
userdb = {}
# {peer: name}
peers = {}

class User(object):
    '''User class for a little more power than a dict
    self.permissions: {cityID: {'permissionType': Bool}'''
    def __init__(self, name, password, access):
        self.name = name
        self.password = password
        self.access = access
        self.loggedin = False
        self.peer = None
        self.permissions = {}
    
    def setPermission(self, city, parameter, flag):
        '''Adds, if needed, and sets a permission flag'''
        if city not in self.permissions:
            self.permissions[city]
        self.permissions[city][parameter] = flag
    
    def canUser(self, city, parameter):
        if city not in self.permissions:
            return False
        if parameter not in self.permissions[city]:
            return False
        return self.permissions[city][parameter]

# TODO: Dehardcode access level
def addUser(name, password, access="normal"):
    '''Add user to database. access variable is lowercase string.
    If there is no user in the database then the first one added will be the owner'''
    if userdb:
        userdb[name] = User(name, password, ACCESS[access])
        logger.debug("Adding user %s with access %s: %s" %(name, access, userdb))
    else:
        userdb[name] = User(name, password, OWNER)
        logger.debug("No users. Owner added: %s" %userdb)

def login(name, password, peer):
    '''Adds new user to db. Does not auto logon. Returns 0 if not in db, 1 if password does not match, 2 if success'''
    if password != userdb[name].password:
        container = proto.Container()
        container.disconnect = "Incorrect password."
        messenger.send("logout", [peer])
        return 0
        
    userdb[name].loggedin = True
    if userdb[name].peer:
        # This user is already logged in, so we need to log out the old ip
        oldpeer = userdb[name].peer
        container = proto.Container()
        container.disconnect = "Another client signed in with this user name and password. If this is in error please contact the server administrator."
        messenger.send("sendData", [oldpeer, container])
        messenger.send("logout", [userdb[name].peer])
        logger.info("User %s signing in with peer %s. Killing old connection %s" %(name, peer, oldpeer))
    userdb[name].peer = peer
    peers[peer] = name
    return 1

def logout(name):
    peer = userdb[name].peer
    del peers[peer]
    userdb[name].loggedin = False
    userdb[name].peer = None
    logger.info("Logged out %s %s" %(name, peer))

def getType(name):
    '''Returns the user type'''
    return userdb[name].access

def getNameFromPeer(peer):
    '''Messy function to get a user name from the peer.'''
    if peer in peers:
        return peers[peer]

# Check permission for whatever
def isOwner(name):
    if userdb[name].access is OWNER:
        return True

def isAdmin(name):
    if userdb[name].access >= ADMIN:
        return True

def isGm(name):
    if userdb[name].access >= GM:
        return True

def isNormal(name):
    if userdb[name].access >= NORMAL:
        return True

def isObserver(name):
    if userdb[name].access >= OBSERVER:
        return True
    
def canUser(name, city, parameter):
    '''Can the user do the parameter in regards to city stuff?'''
    return userdb[name].canUser(city, parameter)
    
def setPermission(name, city, parameter, flag):
    userdb[name].setPermission(city, parameter, flag)
