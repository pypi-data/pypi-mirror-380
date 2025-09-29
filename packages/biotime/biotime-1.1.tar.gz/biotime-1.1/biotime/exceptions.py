

class AuthenticationError(Exception):
    """Token olish yoki yangilashda xatolik bo‘lsa."""
    pass

class APIRequestError(Exception):
    """API chaqiruvida boshqa xatoliklar uchun."""
    pass
