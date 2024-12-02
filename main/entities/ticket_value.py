from entities.EntitiesFields import *
from repositories.repository import updateEntity,getEntityByProperties




def checkTicketValue():
    ticket = getEntityByProperties(TICKET_VALUE,[ID],1)
    print(f"El valor actual de la entrada es: ${ticket[TICKET_VALUE_VALUE]}")


def updateTicketValue():
    value = getEntityByProperties(TICKET_VALUE,[ID],1)
    value[TYPE] = TICKET_VALUE
    value[TICKET_VALUE_VALUE] = input("Ingrese el nuevo valor de la entrada: ")
    updateEntity(value)


