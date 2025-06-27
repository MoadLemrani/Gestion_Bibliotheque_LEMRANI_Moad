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

class LivreDejaEmprunteError(Exception):
    def __init__(self, message="Le livre est emprunté. il ne peut pas être supprimé"):
        super().__init__(message)

class LivreNonEmprunteParCeMembreError(Exception):
    def __init__(self, message="Le livre n'est pas emprunté par ce membre. il ne peut pas être retourné"):
        super().__init__(message)
