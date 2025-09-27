import random
class InteligenciaArtificial:
    def __init__(self, nombre: str):
        """__init__(self, nombre: str)"""
        self.nombre = nombre
        print(f"{self.nombre} inicializada.")
    
    def AI(self, entorno: dict) -> str:
        """Función AI(self, entorno: dict) -> str"""
        acciones = ["explorar", "descansar", "recolectar", "atacar"]
        
        if entorno.get("peligro", False):
            decision = random.choice(["atacar", "escapar"])
        elif entorno.get("cansado", False):
            decision = "descansar"
        elif entorno.get("recursos", 0) > 0:
            decision = "recolectar"
        else:
            decision = "explorar"

        print(f"{self.nombre} decide: {decision}")
        return decision

# Ejecución del programa.        
entorno = {"peligro": True, "cansado": False, "recursos": 3}
ia = InteligenciaArtificial("IA1")
ia.AI(entorno)