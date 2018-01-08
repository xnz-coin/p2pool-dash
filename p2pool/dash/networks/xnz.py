import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'bf0c6bbd'.decode('hex')
P2P_PORT = 6669
ADDRESS_VERSION = 53
SCRIPT_ADDRESS_VERSION = 16
RPC_PORT = 6668
RPC_CHECK = defer.inlineCallbacks(lambda xnzd: defer.returnValue(
            'dashaddress' in (yield xnzd.rpc_help()) and
            not (yield xnzd.rpc_getinfo())['testnet']
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('dash_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('dash_hash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'XNZ'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'XnzCore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/XnzCore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.xnzcore'), 'xnz.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://explorer.dash.org/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://explorer.dash.org/address/'
TX_EXPLORER_URL_PREFIX = 'https://explorer.dash.org/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUST_THRESHOLD = 0.001e8
