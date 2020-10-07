from Ambrosia_Project.models import *


def generateinvoiceid():
    try:
        # get last row of the table
        trans = Transactions.objects.last()

        if trans is not None:
            invoiceid = trans.invoice_id
            bid = invoiceid + 1

        else:
            bid = 1

    except Exception as e:
        print(e)
        id = -999

    return bid


def calculateTotalprice(details):
    qty = details['qty']
    weight = details['weight']
    cat = details['cat']
    price = 0

    priceTbl = Price_Table.objects.filter(category=cat)

    for priceObj in priceTbl:
        if priceObj.weight == weight:
            price = priceObj.price

    total = price * qty

    priceDetails = {
        'totalPrice': total,
        'itemPrice': price
    }

    return priceDetails


def transactioncalTotal(tbid):
    tprice = 0

    try:
        ob = BillItems.objects.filter(invoice_id=tbid)

        if ob is not None:

            for invoice in ob:
                tprice = tprice + invoice.price

            return tprice

        else:
            return None

    except Exception as e:
        print(e)

    return None


def viewbill(vbill):
    try:
        viewob = BillItems.objects.filter(invoice_id=vbill)

        if viewob is not None:

            for viewBill in viewob:
                id = viewBill.id
                date = viewBill.date
                itemname=viewBill.itemname
                weight=viewBill.weight
                Quantity = viewBill.Quantity
                itemprice = viewBill.itemPrice
                price = viewBill.price

                View = {
                    'id': id,
                    'date': date,
                    'itemname': itemname,
                    'Quantity': Quantity,
                    'weight': weight,
                    'itemprice': itemprice,
                    'price': price

                }
                return View
            else:
                return None

    except Exception as e:
        print(e)

    return None


