from EntitiesFields import *
from repositories.repository import addEntity

def createInvoice(userId,reservations,amount):
    if len(reservations) == 0:
        print("Para generar factura debe tener al menos una reserva")
        return 
    invoice = {}
    invoice[TYPE] = INVOICE
    invoice[INVOICE_USER] = userId
    invoice[INVOICE_AMOUNT] = amount
    invoiceId = addEntity(invoice)   
    
    for reservation in reservations: 
        invoice_reservation = {}
        invoice_reservation[TYPE] = INVOICE_RESERVATION
        invoice_reservation[INVOICE_RESERVATION_INVOICE_ID] = invoiceId
        invoice_reservation[INVOICE_RESERVATION_RESERVATION_ID] = reservation[ID]
        addEntity(invoice_reservation)

