import hashlib
import datetime
import random
import json
# A simple Block Chainy
class MinimalBlock():
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hashing()
    
    # Making Pointers For The Next Block
    def hashing(self):
        key = hashlib.sha256()
        key.update(str(self.index).encode('utf-8'))
        key.update(str(self.timestamp).encode('utf-8'))
        key.update(str(self.data).encode('utf-8'))
        key.update(str(self.previous_hash).encode('utf-8'))
        return key.hexdigest()


class MinimalChain():
    def __init__(self): # initialize when creating a chain
        self.blocks = [self.get_genesis_block()]
    
    def get_genesis_block(self): 
        return MinimalBlock(0, 
                            datetime.datetime.utcnow(), 
                            'Genesis', 
                            'arbitrary')
    
    def add_block(self, data=[]):
        self.blocks.append(MinimalBlock(len(self.blocks), 
                                        datetime.datetime.utcnow(), 
                                        data, 
                                        self.blocks[len(self.blocks)-1].hash))

    def add_transaction_toblock(self,block,transaction):
        transaction_data = []
        transaction_signature = hashlib.sha256()
        transaction_signature.update(str(transaction).encode('utf-8'))
        transaction_data.append(transaction)
        transaction_data.append({'signature':transaction_signature.hexdigest()})
        self.blocks[block.index].data.append(transaction_data)
    
    def get_chain_size(self): # exclude genesis block
        return len(self.blocks)-1
    
    def verify(self, verbose=True): 
        flag = True
        for i in range(1,len(self.blocks)):.
            if self.blocks[i].index != i:
                flag = False
                if verbose:
                    print(f'Wrong block index at block {i}.')
            if self.blocks[i-1].hash != self.blocks[i].previous_hash:
                flag = False
                if verbose:
                    print(f'Wrong previous hash at block {i}.')
            if self.blocks[i].hash != self.blocks[i].hashing():
                flag = False
                if verbose:
                    print(f'Wrong hash at block {i}.')
            if self.blocks[i-1].timestamp >= self.blocks[i].timestamp:
                flag = False
                if verbose:
                    print(f'Backdating at block {i}.')
        return flag
    
    def fork(self, head='latest'):
        if head in ['latest', 'whole', 'all']:
            return copy.deepcopy(self) # deepcopy since they are mutable
        else:
            c = copy.deepcopy(self)
            c.blocks = c.blocks[0:head+1]
            return c
    
    def get_root(self, chain_2):
        min_chain_size = min(self.get_chain_size(), chain_2.get_chain_size())
        for i in range(1,min_chain_size+1):
            if self.blocks[i] != chain_2.blocks[i]:
                return self.fork(i-1)
        return self.fork(min_chain_size)

# A function to handle serilization of datetime objects 
def convert_timestamp(item_date_object):
    if isinstance(item_date_object, (datetime.date, datetime.datetime)):
        return item_date_object.timestamp()


if __name__ == "__main__":
    block_register = []
    # Initializing the chain
    minimalchain = MinimalChain()
    # Adding Block To The chain 
    minimalchain.add_block([])
    block = minimalchain.blocks[1]
    index = [i for i in range(0,20)] 

    # preparing random datas for building transactions 
    sender_address = ['USA','india','Angola','Argentina','Armenia','Australia','Azerbaijan','Belarus','Bolivia','Brazil','Burundi','Canada','Chad','Cyprus','Egypt','Fiji','Ghana','Guatemala','Haiti','Iran']
    receivers_address = ['Australia', 'Bolivia', 'Haiti', 'Cyprus', 'Fiji', 'Egypt', 'Ghana', 'Belarus', 'USA', 'Burundi', 'Armenia', 'Argentina', 'india', 'Azerbaijan', 'Brazil', 'Canada', 'Guatemala', 'Chad', 'Iran', 'Angola']
    amount = [random.randint(1,500) for i in range(0,20)]

    # preparing array of transactions 
    data_source =  [{'TransactionIndex': T, 'SenderAddress': S,'RecipientAddress':R,'Amount':A,'Message':'testmessage'} for T,S,R,A in zip(index, sender_address,receivers_address,amount)]
    data_iter = iter(data_source)                                                                                                    
    for i in range(1,20+1):
        # appending transaction to the block
        minimalchain.add_transaction_toblock(block,next(data_iter))

    for block in minimalchain.blocks:
        block_register.append({"BlockIndex":block.index,
                                "data":block.data,
                                "timestamp":block.timestamp,
                                "PrevHash":block.previous_hash,
                                "hash":block.hash})

    # writing blocks into a json file 
    f = open("testblock.json", "a")
    f.write(json.dumps(block_register,default=convert_timestamp))
    f.close()

