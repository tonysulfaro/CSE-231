## Skeleton Code for RobCo Advertising Adstravaganza!

def open_file():
    '''prompt for file name, open file, return file pointer'''
    ## Some lines to help with formatting
    filename = input("Input a file name: ")

    return filename

def revenue(num_sales, sale_price):

    totalRevenue = num_sales * sale_price

    return totalRevenue


def cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost):

    costsOfGoodsSold = num_ads*ad_price + num_sales*production_cost

    return  costsOfGoodsSold


def calculate_ROI(placementCount, placementCost, salesNumber, productPrice, productionCost):

    totalRevenue = salesNumber * productPrice
    costsOfGoodsSold = placementCount * productPrice + salesNumber * productionCost
    ROI = (totalRevenue-costsOfGoodsSold)/costsOfGoodsSold

    return ROI


def find_state(state,product):

    return state


def main():
    ## open the file
    try:
        fp = open(open_file())
    except FileNotFoundError:
        print("Unable to open file. Please try again.")
        fp = open(open_file())

    ## Some print lines to match formatting in Mimir tests
    print()
    print("RobCo AdStats M4000")
    print("-------------------")
    ## read the file

    state = 0
    currentProduct = ""

    bestPerforming = ""
    sales = 0
    bestROI = 0.0
    bestROIad = ""

    for line in fp:

        product = line[:27].strip()
        ad = line[27:54].strip()
        placementCount = int(line[54:62].strip())
        placementCost = float(line[-32:-24].strip())
        salesNumber = int(line[-24:-16].strip())
        productPrice = float(line[-16:-8].strip())
        productionCost = float(line[-8:].strip())

        # pass variables onto functions
        totalRevenue = revenue(salesNumber, productPrice)
        costofGoods = cost_of_goods_sold(placementCount, placementCost, salesNumber, productionCost)
        roi = calculate_ROI(placementCount, placementCost, salesNumber, productPrice, productionCost)
        totalProdCost = salesNumber * productionCost

        if product != currentProduct and state != 0:
            state = 3
            #print("New Product")

        #for the first line in the program
        if state == 0:
            #print("CASE 1")
            if salesNumber > sales:
                sales = salesNumber
                bestPerforming = ad
            if roi > bestROI:
                bestROI = roi
                bestROIad = ad
            state = 1
            currentProduct = product

        #for all lines not the first one
        if state == 1 and currentProduct == product:

            #print("CASE 2")

            if salesNumber > sales:
                sales = salesNumber
                bestPerforming = ad
            if roi > bestROI:
                bestROI = roi
                bestROIad = ad
            currentProduct = product

        else:
            #print("CASE 3")
            print("\n" + currentProduct)
            print("  {:27s}{:>11s}".format("Best-Performing Ad", "sales"))
            print("  {:27s}{:>11d}".format(bestPerforming, sales))
            print("\n  {:27s}{:>11s}".format("Best ROI", "percent"))
            print("  {:27s}{:>10.2f}%".format(bestROIad, bestROI))
            #print("END CASE 3")

            bestPerforming = ""
            sales = 0
            bestROI = 0.0
            bestROIad = ""
            state = 1
            currentProduct = product

            if salesNumber > sales:
                sales = salesNumber
                bestPerforming = ad
            if roi > bestROI:
                bestROI = roi
                bestROIad = ad

    #print("CASE 3")
    print("\n" + currentProduct)
    print("  {:27s}{:>11s}".format("Best-Performing Ad", "sales"))
    print("  {:27s}{:>11d}".format(bestPerforming, sales))
    print("\n  {:27s}{:>11s}".format("Best ROI", "percent"))
    print("  {:27s}{:>10.2f}%".format(bestROIad, bestROI))
    print()
    #print("END CASE 3")

if __name__ == "__main__":
    main()