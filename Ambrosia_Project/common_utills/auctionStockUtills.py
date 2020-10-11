from Ambrosia_Project.models import *
from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

#Generate id for Auction sub stock
def generateSubStockID():

    try:
        #get last row of the table
        stock = Auction_MainStock.objects.last()

        if stock is not None:
            sid = stock.SubID
            id = sid + 1

        #first catelog
        else:
            id = 1

    except Exception as e:
        print(e)
        id = -999

    return id


#Calculations in auction substock
def calculaionsAuctionSubStock(suId):

    # initialize variables
    tnet = 0
    tgross = 0
    tpkts = 0
    noOfRows = 0

    try:
        #get all from db
        obj = Auction_SubStock.objects.filter(SubID=suId)

        check = Auction_SubStock.objects.filter(SubID=suId).exists()

        noOfRows = Auction_SubStock.objects.filter(SubID=suId).count()

        if check:

            for subStock in obj:
                # calculate total net weight
                tnet = tnet + subStock.net_weight

                #calculate total gross weight
                tgross = tgross + subStock.total_weight

                #calculate total no of packets
                tpkts = tpkts + subStock.no_of_packets

            #assign to a list
            stockList = {'sub':obj, 'tne': tnet, 'tgr': tgross, 'tpk': tpkts, 'rowsNo':noOfRows}

            return stockList

        else:
            return None

    except Exception as e:
        print(e)
        return None


#generate pdf
def finalProductionAuction_render_topdf(template_src, context_dict={}):

    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf' )
    else:
        return None


#search sold stock relevant details to report
def AuctionSoldStockDetails(text, type):

    details = {
        'stock': 0,
    }

    try:
        if type == 'date':
            chk = Auction_SoldStocks.objects.filter(sold_Date=text, active=1).exists()

            if chk:
                sold = Auction_SoldStocks.objects.filter(sold_Date=text, active=1)

                details = {
                    'stock': sold,
                }

        elif type == 'month':
            arr = text.split('-', 1)
            year = arr[0]
            month = arr[1]

            chk = Auction_SoldStocks.objects.filter(sold_Date__year=year, sold_Date__month=month, active=1).exists()

            if chk:
                sold = Auction_SoldStocks.objects.filter(sold_Date__year=year, sold_Date__month=month, active=1)

                details = {
                    'stock': sold,
                }

        elif type == 'year':

            chk = Auction_SoldStocks.objects.filter(sold_Date__year=text, active=1).exists()

            if chk:
                sold = Auction_SoldStocks.objects.filter(sold_Date__year=text, active=1)
                details = {
                    'stock': sold,
                }

        else:
            details = {
                'stock': -99,
            }

    except Exception as e:
        print(e)
        details = {
            'stock': -1,
        }

    return details

#Auction calculate total
def calculateTotalAuction(allStock):

    totalprice = 0
    countSub = 0
    totalN = 0
    totalW = 0

    for stock in allStock:

        totalprice = totalprice + stock.total_price
        countSub = countSub + 1

        sub = Auction_SubStock.objects.get(pk=stock.MainID)
        totalW = totalW + sub.total_weight
        totalN = totalN + sub.net_weight

    sampleW = totalW - totalN

    det = {
        'totalWeight': totalW,
        'netWeight': totalN,
        'samWeight': sampleW,
        'tPrice': totalprice,
        'count': countSub,
    }


    return det
