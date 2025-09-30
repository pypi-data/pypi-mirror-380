import asyncio
from TonTools import TonCenterClient
from TonTools import Wallet
from ..core import account


async def send(destination_address, amount, payload=""):
    """
    Send TON to specified address using v4r2 wallet
    
    Args:
        destination_address (str): The recipient's TON wallet address
        amount (float): Amount to send in TON
        payload (str, optional): Payload for the transaction (base64 encoded cell or plain text)
        
    Returns:
        dict: Transaction result information
    """
    # Validate inputs
    if not destination_address or not isinstance(destination_address, str):
        return {
            "success": False,
            "error": "Invalid destination address",
            "source": "v4r2_send"
        }
    
    if not amount or amount <= 0:
        return {
            "success": False,
            "error": "Invalid amount. Must be greater than 0",
            "source": "v4r2_send"
        }
    
    # Check if required credentials are available
    if not account.toncenter_api_key:
        return {
            "success": False,
            "error": "TonCenter API key not set. Set account.toncenter_api_key",
            "source": "v4r2_send"
        }
    
    if not account.wallet_seed:
        return {
            "success": False,
            "error": "Wallet seed not set. Set account.wallet_seed",
            "source": "v4r2_send"
        }
    
    try:
        # Initialize TonCenter client
        client = TonCenterClient(account.toncenter_api_key)
        
        # Create wallet from mnemonics
        mnemonics_list = account.wallet_seed.split()
        sender_wallet = Wallet(
            provider=client, 
            mnemonics=mnemonics_list, 
            version='v4r2'
        )
        
        # Check balance before sending
        balance = await sender_wallet.get_balance()
        balance_ton = balance / 1_000_000_000  # Convert from nanotoms to TON
        
        if balance_ton < amount:
            return {
                "success": False,
                "error": f"Insufficient funds. Required {amount} TON, available {balance_ton:.4f} TON",
                "balance": {
                    "nano": balance,
                    "ton": balance_ton
                },
                "source": "v4r2_send"
            }
        
        # Send transaction
        await sender_wallet.transfer_ton(
            destination_address=destination_address,
            amount=amount,
            message=payload
        )
        
        return {
            "success": True,
            "transaction": {
                "destination": destination_address,
                "amount": amount,
                "payload": payload,
                "sender": sender_wallet.address
            },
            "balance": {
                "nano": balance,
                "ton": balance_ton
            },
            "source": "v4r2_send"
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "source": "v4r2_send"
        }


def send_sync(destination_address, amount, payload=""):
    """
    Synchronous wrapper for send function
    
    Args:
        destination_address (str): The recipient's TON wallet address
        amount (float): Amount to send in TON
        payload (str, optional): Payload for the transaction (base64 encoded cell or plain text)
        
    Returns:
        dict: Transaction result information
    """
    return asyncio.run(send(destination_address, amount, payload))
