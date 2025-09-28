from pydantic import BaseModel
from typing import Optional, List

# -----------------------------
# Agence
# -----------------------------
class AgenceBase(BaseModel):
    numero_agence: int
    ville: str
    adresse: str

    class Config:
        from_attributes = True


class AgenceSimple(AgenceBase):
    pass


# -----------------------------
# Situation Familiale
# -----------------------------
class SituationFamilleBase(BaseModel):
    numero_client: int
    statut_familliale: Optional[str]
    nombre_enfants: Optional[int]
    age: Optional[int]
    nom_client: Optional[str]
    statut_activite: Optional[str]

    class Config:
        from_attributes = True


class SituationFamilialeSimple(SituationFamilleBase):
    pass


# -----------------------------
# Situation Professionnelle
# -----------------------------
class SituationProBase(BaseModel):
    numero_client: int
    revenu_mensuel_moyen: Optional[int]
    code_regularite_revenus: Optional[int]
    regularite_des_revenus: Optional[str]
    code_statut_emploi: Optional[int]
    regularite_emploi: Optional[str]

    class Config:
        from_attributes = True


class SituationProSimple(SituationProBase):
    pass


# -----------------------------
# Apport
# -----------------------------
class ApportBase(BaseModel):
    numero_demande: int
    apport: Optional[int]

    class Config:
        from_attributes = True


class ApportSimple(ApportBase):
    pass


# -----------------------------
# Demande
# -----------------------------
class DemandeBase(BaseModel):
    numero_demande: int
    montant_operation: Optional[int]
    duree: Optional[int]
    numero_client: int
    accord: Optional[str]
    numero_agence: int
    duree_de_traitement: Optional[int]
    code_accord: Optional[int]

    class Config:
        from_attributes = True


class DemandeSimple(DemandeBase):
    pass


class DemandeDetailed(DemandeBase):
    # Relations corrigées selon modèles SQLAlchemy
    agence: AgenceSimple  # One-to-One côté Demande
    client: SituationProSimple  # One-to-One côté Demande
    apport: Optional[ApportSimple]  # One-to-One côté Demande

    class Config:
        from_attributes = True


# -----------------------------
# Base pour ML
# ------------------------------

class AllDBBase(BaseModel):
    numero_demande: int
    montant_operation: Optional[int]
    duree: Optional[int]
    numero_client: Optional[int]
    accord: Optional[str]
    numero_agence: Optional[int]
    duree_de_traitement: Optional[int]
    code_accord: Optional[int] 
    apport: Optional[int] 
    revenu_mensuel_moyen: Optional[int]
    code_regularite_revenus: Optional[int]
    regularite_des_revenus: Optional[str]
    code_statut_emploi: Optional[int] 
    regularite_emploi: Optional[str]
    situation_familliale: Optional[str]
    nombre_enfants: Optional[int]
    age: Optional[int]
    nom_client: Optional[str] 
    statut_activite: Optional[str]
    ville: Optional[str]
    adresse: Optional[str]

    class Config:
        from_attributes = True

class AllDBSimple(AllDBBase):
    pass
# -----------------------------
# Analytics
# -----------------------------
class AnalyticsResponse(BaseModel):
    demande_count: int
    agence_count: int
    situationpro_count: int
    situationfamille_count: int
    apport_count: int

    class Config:
        from_attributes = True