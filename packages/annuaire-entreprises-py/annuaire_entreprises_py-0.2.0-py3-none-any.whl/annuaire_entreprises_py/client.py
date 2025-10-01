from difflib import get_close_matches
from requests import Session
class AnnuaireEntreprisesGet:
    """Client pour l'API Annuaire Entreprises (API.gouv.fr)."""
    
    BASE_URL = "https://recherche-entreprises.api.gouv.fr/search"
    
    def __init__(self, session=None):
        self.session = session or Session()
    
    def _get(self, params:dict, format:str="dict") -> dict:
        """Effectue une requête GET et retourne le JSON."""
        response = self.session.get(self.BASE_URL, params=params)
        response.raise_for_status()

        if format == "dict":
            return response.json()
        elif format == "json":
            return response.text
        else:
            raise ValueError("format doit être 'dict' ou 'json'")
    
    def get_by_siret(self, siret: str) -> dict:
        return self._get({"siret": siret})
    
    def search(self, **kwargs) -> dict:
        """Recherche avec plusieurs paramètres en même temps.
        Exemples : ape_code="6201Z", code_postal="75001"
        """

        mapping = {
            "ape_code": "activite_principale",
            "siret": "siret",
            "code_postal": "code_postal",
            "departement": "departement",
            "region": "region",
            "commune": "code_commune",
            "page": "nb_pages",
            "per_page": "nb_par_pages",
            "q": "q"
        }

        params = {mapping.get(k, k): v for k, v in kwargs.items()}

        params.setdefault("page", self.default_page)
        params.setdefault("per_page", self.default_per_page)

        return self._get(params)

class Departements:
    _data = {
        "01": "Ain",
        "02": "Aisne",
        "03": "Allier",
        "04": "Alpes de Haute Provence",
        "05": "Hautes-Alpes",
        "06": "Alpes-Maritimes",
        "07": "Ardèche",
        "08": "Ardennes",
        "10": "Aube",
        "11": "Aude",
        "12": "Aveyron",
        "13": "Bouches-du-Rhône",
        "14": "Calvados",
        "15": "Cantal",
        "16": "Charente",
        "17": "Charente Maritime",
        "18": "Cher",
        "19": "Corrèze",
        "2A": "Corse-du-Sud",
        "2B": "Haute-Corse",
        "21": "Côte-d'Or",
        "22": "Côtes-d'Armor",
        "23": "Creuse",
        "24": "Dordogne",
        "25": "Doubs",
        "26": "Drôme",
        "27": "Eure",
        "28": "Eure-et-Loir",
        "29": "Finistère",
        "30": "Gard",
        "31": "Haute-Garonne",
        "32": "Gers",
        "33": "Gironde",
        "34": "Hérault",
        "35": "Ille-et-Vilaine",
        "36": "Indre",
        "37": "Indre-et-Loire",
        "38": "Isère",
        "39": "Jura",
        "40": "Landes",
        "41": "Loir-et-Cher",
        "42": "Loire",
        "43": "Haute Loire",
        "44": "Loire-Atlantique",
        "45": "Loiret",
        "46": "Lot",
        "47": "Lot-et-Garonne",
        "48": "Lozère",
        "49": "Maine-et-Loire",
        "50": "Manche",
        "51": "Marne",
        "52": "Haute-Marne",
        "53": "Mayenne",
        "54": "Meurthe-et-Moselle",
        "55": "Meuse",
        "56": "Morbihan",
        "57": "Moselle",
        "58": "Nièvre",
        "59": "Nord",
        "60": "Oise",
        "61": "Orne",
        "62": "Pas-de-Calais",
        "63": "Puy de Dôme",
        "64": "Pyrénées-Atlantique",
        "65": "Hautes-Pyrénées",
        "66": "Pyrénées-Orientales",
        "67": "Bas-Rhin",
        "68": "Haut-Rhin",
        "69": "Rhône",
        "70": "Haute-Saône",
        "71": "Saône-et-Loire",
        "72": "Sarthe",
        "73": "Savoie",
        "74": "Haute-Savoie",
        "75": "Paris",
        "76": "Seine-Maritime",
        "77": "Seine-et-Marne",
        "78": "Yvelines",
        "79": "Deux-Sèvres",
        "80": "Somme",
        "81": "Tarn",
        "82": "Tarn-et-Garonne",
        "83": "Var",
        "84": "Vaucluse",
        "85": "Vendée",
        "86": "Vienne",
        "87": "Haute-Vienne",
        "88": "Vosges",
        "89": "Yonne",
        "90": "Territoire de Belfort",
        "91": "Essonne",
        "92": "Hauts-de-Seine",
        "93": "Seine-Saint-Denis",
        "94": "Val-de-Marne",
        "95": "Val-d'Oise",
        "971": "Guadeloupe",
        "972": "Martinique",
        "973": "Guyane",
        "974": "La Réunion",
        "976": "Mayotte",
    }

    @classmethod
    def get_by_code(cls, code: str) -> str | None:
        """Retourne le nom du département à partir du code."""
        return cls._data.get(code)

    @classmethod
    def get_by_name(cls, name: str) -> str | None:
        """Retourne le code du département à partir du nom.
        Cherche aussi par proximité si aucune correspondance exacte.
        """
        departement = name.lower()
        # Recherche exacte
        for code, name in cls._data.items():
            if name.lower() == departement:
                return code

        # Recherche par proximité (fuzzy)
        names = [name for name in cls._data.values()]
        close = get_close_matches(departement, names, n=1, cutoff=0.6)
        if close:
            # Retourne le code correspondant au nom proche trouvé
            for code, name in cls._data.items():
                if name == close[0]:
                    return code
        return None
    
class Region:
    _data = {
        "01": "Guadeloupe",
        "02": "Martinique",
        "03": "Guyane",
        "04": "La Réunion",
        "05": "Mayotte",
        "11": "Île-de-France",
        "24": "Centre-Val de loire",
        "27": "Bourgogne-Franche-Comté",
        "28": "Normandie",
        "32": "Hauts-de-France",
        "44": "Grand-Est",
        "52": "Pays de la loire",
        "53": "Bretagne",
        "75": "Nouvelle Aquitaine",
        "76": "Occitanie",
        "84": "Auvergne-Rhône-Alpes",
        "93": "Provence-Alpes-Côte d'Azur",
        "94": "Corse",
    }

    @classmethod
    def get_by_code(cls, code:int) -> str :
        return cls._data.get(code)
    
    @classmethod
    def get_by_name(cls, name:str) -> str :
        region = name.lower()
        # Recherche exacte
        for code, name in cls._data.items():
            if name.lower() == region:
                return code

        # Recherche par proximité (fuzzy)
        names = [name for name in cls._data.values()]
        close = get_close_matches(region, names, n=1, cutoff=0.6)
        if close:
            # Retourne le code correspondant au nom proche trouvé
            for code, name in cls._data.items():
                if name == close[0]:
                    return code
        return None