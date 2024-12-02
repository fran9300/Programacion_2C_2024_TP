from entities.EntitiesFields import *
from repositories.repository import updateEntity,getEntityByProperties
from entities.utils import clear




def checkTicketValue():
    ticket = getEntityByProperties(TICKET_VALUE,[ID],1)
    clear()
    print(f"El valor actual de la entrada es: ${ticket[TICKET_VALUE_VALUE]}\n")


def updateTicketValue():
    ticket = getEntityByProperties(TICKET_VALUE,[ID],1)
    ticket[TYPE] = TICKET_VALUE
    clear()
    ticket[TICKET_VALUE_VALUE] = input("Ingrese el nuevo valor de la entrada: ")
    updateEntity(ticket)
    print(f"\nEl valor actual de la entrada es: ${ticket[TICKET_VALUE_VALUE]}\n")

