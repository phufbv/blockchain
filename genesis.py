import datetime as date
import block

def create_genesis_block():
    # Manually construct a block with index zero and arbitrary previous hash
    return block.Block(0, date.datetime.now(), "Genesis Block", "0")
