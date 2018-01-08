from p2pool.dash import networks

PARENT = networks.nets['xnz']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//20 # shares
REAL_CHAIN_LENGTH = 24*60*60//20 # shares
TARGET_LOOKBEHIND = 100 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 10 # blocks
IDENTIFIER = '157E3F9D22A1CE6A'.decode('hex')
PREFIX = '7C45A1F3BFF797F5'.decode('hex')
COINBASEEXT = '0D2F5032506F6F6C2D444153482F'.decode('hex')
P2P_PORT = 6679
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 7903
BOOTSTRAP_ADDRS = 'seed.xnz.io '.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-xnz'
VERSION_CHECK = lambda v: v >= 120100
