from modelo_botella import Botella
from modelo_botella_plastico import BotellaPlastico
from modelo_botella_vidrio import BotellaVidrio

print("="*60)
print("GESTOR DE BOTELLAS - POO")
print("="*60)

print("\nEJEMPLO 1: BOTELLA DE PLÁSTICO ")
print("-"*60)

botella_plastico = BotellaPlastico(
    capacidad=1.5,
    forma="Cilíndrica",
    diseno="Transparente",
    tapa="Rosca clasica",
    grabados="Marca comercial",
    tipo_plastico="PET"
)

print(botella_plastico.mostrar_info())  
botella_plastico.contener_liquidos(2.0)
botella_plastico.cierre_hermetico("cerrada")
botella_plastico.transporte("Supermercado")
botella_plastico.compatibilidad_bebidas_calientes_frias("frías")
botella_plastico.reciclar()

print("\nEJEMPLO 2: BOTELLA DE VIDRIO ")
print("-"*60)

botella_vidrio = BotellaVidrio(
    capacidad=0.75,
    forma="Estilizada",
    diseno="clasica azul clarito",
    tapa="corcho clasico",
    grabados="Logo en relieve",
    color_vidrio="Verde"
)

print(botella_vidrio.mostrar_info())  
botella_vidrio.contener_liquidos(0.75)
botella_vidrio.facilitar_vertido()
botella_vidrio.cierre_hermetico("abierta")
botella_vidrio.manejo()
botella_vidrio.esterilizar()
botella_vidrio.reutilizacion()
botella_vidrio.transparencia()

print("\n" + "="*60)
print("✓ Programa finalizado correctamente")
print("="*60)

