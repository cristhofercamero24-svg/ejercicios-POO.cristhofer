from modelo_botella import Botella


class BotellaPlastico(Botella):
    
    
    def __init__(self, capacidad, forma, diseno, tapa, grabados, tipo_plastico):
        
        super().__init__(
            material="Plástico",
            capacidad=capacidad,
            forma=forma,
            diseno=diseno,
            tapa=tapa,
            grabados=grabados
        )
       
        self.tipo_plastico = tipo_plastico
    
    
    def reciclar(self):
        print(f"Reciclando botella de plástico tipo {self.tipo_plastico}")

