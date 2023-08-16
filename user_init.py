from aiogram.types import Message

USER_IDs = []

def is_user_exists(user_id):
    if user_id in USER_IDs:
        return True
    
    USER_IDs.append(user_id)
    return False