import os
from dotenv import load_dotenv

load_dotenv()

class BankConfig:
    """Classe de configuration contenant des arguments pour le client SDK.

    Contient la configuration de l'URL de base et du backoff progressif.
    """

    bank_base_url: str
    bank_backoff: bool
    bank_backoff_max_time: int

    def __init__(
        self,
        bank_base_url: str = None,
        backoff: bool = True,
        backoff_max_time: int = 30,
    ):
        """Constructeur pour la classe de configuration.

        Contient des valeurs d'initialisation pour écraser les valeurs par défaut.

        Args:
        bank_base_url (optional):
            L'URL de base à utiliser pour tous les appels d'API. Transmettez-la ou définissez-la dans une variable d'environnement.
        bank_backoff:
            Un booléen qui détermine si le SDK doit réessayer l'appel en utilisant un backoff lorsque des erreurs se produisent.
        bank_backoff_max_time:
            Le nombre maximal de secondes pendant lesquelles le SDK doit continuer à essayer un appel API avant de s'arrêter.
        """

        self.bank_base_url = bank_base_url or os.getenv("BANK_API_BASE_URL")
        print(f"BANK_API_BASE_URL in BankConfig init: {self.bank_base_url}")  

        if not self.bank_base_url:
            raise ValueError("L'URL de base est requise. Définissez la variable d'environnement BANK_API_BASE_URL.")

        self.bank_backoff = backoff
        self.bank_backoff_max_time = backoff_max_time

    def __str__(self):
        """Fonction Stringify pour renvoyer le contenu de l'objet de configuration pour la journalisation"""
        return f"{self.bank_base_url} {self.bank_backoff} {self.bank_backoff_max_time}"