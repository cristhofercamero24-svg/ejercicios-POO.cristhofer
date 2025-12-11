from modelo_botella import Botella

class BotellaVidrio(Botella):
    
 
    def __init__(self, capacidad, forma, diseno, tapa, grabados, color_vidrio):
       
        super().__init__(
            material="Vidrio",
            capacidad=capacidad,
            forma=forma,
            diseno=diseno,
            tapa=tapa,
            grabados=grabados
        )
       
        self.color_vidrio = color_vidrio
    
    def esterilizar(self):
        print(f"Esterilizando botella de vidrio color {self.color_vidrio}")
