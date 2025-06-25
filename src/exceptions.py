class LivreIndisponibleError(Exception) : 
    def __init__(self, message = "Le livre n'est pas disponible") : 
        super().__init__(message)

class QuotaEmpruntDepasseError(Exception) : 
    def __init__(self, message = "Quota dépassé") : 
        super().__init__(message)

class MembreInexistantError(Exception) : 
    def __init__(self, message = "Le membre spécifié n'existe pas") : 
        super().__init__(message)

class LivreInexistantError(Exception) : 
    def __init__(self, message = "Le livre spécifié n'existe pas") : 
        super().__init__(message)

class LivreDejaDisponibleError(Exception):
    def __init__(self, message="Le livre est déjà disponible. il ne peut pas être retourné"):
        super().__init__(message)
