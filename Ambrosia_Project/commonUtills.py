from Ambrosia_Project.models import *


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

        noOfRows = Auction_SubStock.objects.filter(SubID=suId).count()

        if obj is not None:

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