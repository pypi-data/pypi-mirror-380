import httpx
from typing import Optional, List, Literal, Union
import pandas as pd
from .schemas import (
    DemandeSimple,
    DemandeDetailed,
    AgenceSimple,
    SituationProSimple,
    SituationFamilialeSimple,
    ApportSimple,
    AllDBSimple,
    AnalyticsResponse,
)
from .bank_config import BankConfig


class DemandeClient:
    def __init__(self, config: Optional[BankConfig] = None):
        self.config = config or BankConfig()
        if not self.config.bank_base_url:
            raise ValueError("L'URL de base est requise. Définissez BankConfig.bank_base_url.")
        self.bank_base_url = self.config.bank_base_url

    def _format_output(self, data, model, output_format: Literal["pydantic", "dict", "pandas"]):
        if output_format == "pydantic":
            return [model(**item) for item in data]
        elif output_format == "dict":
            return data
        elif output_format == "pandas":
            return pd.DataFrame(data)
        else:
            raise ValueError("Invalid output_format. Choose from 'pydantic', 'dict', or 'pandas'.")

    # --- Monitoring ---
    def health_check(self) -> dict:
        url = f"{self.bank_base_url}/"
        response = httpx.get(url, follow_redirects=True)
        response.raise_for_status()
        return response.json()

    # --- Demandes ---
    def get_demande(self, demande_id: int) -> DemandeDetailed:
        url = f"{self.bank_base_url}/demandes/{demande_id}/"  # ✓ Déjà correct
        response = httpx.get(url, follow_redirects=True)
        response.raise_for_status()
        return DemandeDetailed(**response.json())

    def list_demandes(
        self,
        skip: int = 0,
        limit: int = 100,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic",
        **filters
    ) -> Union[List[DemandeSimple], List[dict], pd.DataFrame]:
        url = f"{self.bank_base_url}/demandes/"  # ✓ Déjà correct
        params = {"skip": skip, "limit": limit, **filters}
        response = httpx.get(url, params=params, follow_redirects=True)
        response.raise_for_status()
        return self._format_output(response.json(), DemandeSimple, output_format)

    # --- Agences ---
    def get_agence(self, agence_id: int) -> AgenceSimple:
        url = f"{self.bank_base_url}/agences/{agence_id}/"  # ✓ Déjà correct
        response = httpx.get(url, follow_redirects=True)
        response.raise_for_status()
        return AgenceSimple(**response.json())

    def list_agences(
        self,
        skip: int = 0,
        limit: int = 100,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[AgenceSimple], List[dict], pd.DataFrame]:
        url = f"{self.bank_base_url}/agences/"  # ✓ Déjà correct
        params = {"skip": skip, "limit": limit}
        response = httpx.get(url, params=params, follow_redirects=True)
        response.raise_for_status()
        return self._format_output(response.json(), AgenceSimple, output_format)

    # --- Situation Professionnelle ---
    def get_situation_pro(self, client_id: int) -> SituationProSimple:
        url = f"{self.bank_base_url}/situations_pro/{client_id}/"  # ✓ Déjà correct
        response = httpx.get(url, follow_redirects=True)
        response.raise_for_status()
        return SituationProSimple(**response.json())

    def list_situation_pros(
        self,
        skip: int = 0,
        limit: int = 100,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[SituationProSimple], List[dict], pd.DataFrame]:
        url = f"{self.bank_base_url}/situations_pro/"  # ✓ Déjà correct
        params = {"skip": skip, "limit": limit}
        response = httpx.get(url, params=params, follow_redirects=True)
        response.raise_for_status()
        return self._format_output(response.json(), SituationProSimple, output_format)

    # --- Situation Familiale ---
    def get_situation_famille(self, client_id: int) -> SituationFamilialeSimple:
        url = f"{self.bank_base_url}/situations_famille/{client_id}/"  # ✓ Déjà correct
        response = httpx.get(url, follow_redirects=True)
        response.raise_for_status()
        return SituationFamilialeSimple(**response.json())

    def list_situations_famille(
        self,
        skip: int = 0,
        limit: int = 100,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[SituationFamilialeSimple], List[dict], pd.DataFrame]:
        url = f"{self.bank_base_url}/situations_famille/"  # ✓ Déjà correct
        params = {"skip": skip, "limit": limit}
        response = httpx.get(url, params=params, follow_redirects=True)
        response.raise_for_status()
        return self._format_output(response.json(), SituationFamilialeSimple, output_format)

    # --- Apports ---
    def get_apport(self, demande_id: int) -> ApportSimple:
        url = f"{self.bank_base_url}/apports/{demande_id}/"  # ✓ Déjà correct
        response = httpx.get(url, follow_redirects=True)
        response.raise_for_status()
        return ApportSimple(**response.json())

    def list_apports(
        self,
        skip: int = 0,
        limit: int = 100,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[ApportSimple], List[dict], pd.DataFrame]:
        url = f"{self.bank_base_url}/apports/"  # ✓ Déjà correct
        params = {"skip": skip, "limit": limit}
        response = httpx.get(url, params=params, follow_redirects=True)
        response.raise_for_status()
        return self._format_output(response.json(), ApportSimple, output_format)

    # --- All Demandes (fusionnées pour ML) ---
    def get_all_demandes(self, db_id: int) -> AllDBSimple:
        url = f"{self.bank_base_url}/all_demandes/{db_id}/"  # ✓ Déjà correct
        response = httpx.get(url, follow_redirects=True)
        response.raise_for_status()
        return AllDBSimple(**response.json())

    def list_all_demandes(
        self,
        skip: int = 0,
        limit: int = 100,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[AllDBSimple], List[dict], pd.DataFrame]:
        # CORRECTION : Ajout du slash à la fin de l'URL
        url = f"{self.bank_base_url}/all_demandes/"  # ← Slash ajouté ici
        params = {"skip": skip, "limit": limit}
        response = httpx.get(url, params=params, follow_redirects=True)
        response.raise_for_status()
        return self._format_output(response.json(), AllDBSimple, output_format)

    # --- Analytics ---
    def get_analytics(self) -> AnalyticsResponse:
        url = f"{self.bank_base_url}/analytics/"  # ✓ Déjà correct
        response = httpx.get(url, follow_redirects=True)
        response.raise_for_status()
        return AnalyticsResponse(**response.json())