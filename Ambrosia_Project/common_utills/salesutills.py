from Ambrosia_Project.models import *
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

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


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')

    return None


