import datetime as date
import block

def create_genesis_block():
    # Manually construct a block with index zero and arbitrary previous hash
    return block.Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    # Construct a new block building on the previous block in the chain
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash

    return block.Block(this_index, this_timestamp, this_data, this_hash)
