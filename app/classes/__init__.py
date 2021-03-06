def log(message: str):
    print(f"'\x1b[30;41m {message} \x1b[0m'")


from .blockchain import Blockchain
from .block import Block
from .transaction import Transaction
from .common import list_to_str, list_to_dict
from .transaction_pool_list import TransactionPoolList, consensus_routine
