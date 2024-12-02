from repositories.repository import addEntity
from entities.EntitiesFields import *
from datetime import datetime

def createInvoice(userId,reservations,amount):
    if len(reservations) == 0:
        print("Para generar factura debe tener al menos una reserva")
        return 
    invoice = {}
    invoice[TYPE] = INVOICE
    invoice[INVOICE_USER] = userId
    invoice[INVOICE_AMOUNT] = amount
    invoice[INVOICE_DATE] = str(datetime.now())
    invoiceId = addEntity(invoice)       
    for reservationId in reservations: 
        invoice_reservation = {}
        invoice_reservation[TYPE] = INVOICE_RESERVATION
        invoice_reservation[INVOICE_RESERVATION_INVOICE_ID] = invoiceId
        invoice_reservation[INVOICE_RESERVATION_RESERVATION_ID] = reservationId
        addEntity(invoice_reservation)

