## Skeleton Code for RobCo Advertising Adstravaganza!
## Initial Commit: when I'm done, I can go eat some Fancy Lads Snack Cakes,
## maybe drink some cola. Better check in my code first.
## -- @RCK -- 8/7/77

def open_file():
    '''prompt for file name, open file, return file pointer'''
    ## Some lines to help with formatting
    filename = ''
    while True:

        try:
            filename = input("Input a file name including (.txt): ")
            break
        except(FileNotFoundError,IOError):
            print("Unable to open file. Please try again.")
            continue
    # return fp
    return filename

def revenue(num_sales, sale_price):
    totalRevenue = num_sales * sale_price
    return totalRevenue



def cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost):
    costsOfGoodsSold = num_ads*ad_price + num_sales*production_cost
    return  costsOfGoodsSold


def calculate_ROI(num_ads, ad_price, num_sales, sale_price, production_cost):
    ROI = (sale_price*num_sales - ((num_ads*ad_price)+(production_cost*num_sales))/((num_ads*ad_price)+(production_cost*num_sales))
    return ROI


def main():
    ## open the file
    fp = open(open_file())
    ## Some print lines to match formatting in Mimir tests
    print()
    print("RobCo AdStats M4000")
    print("-------------------")
    print()
    ## read the file
    for line in fp:
        print(line)

        product = line[:27].strip()
        ad = line[27:54].strip()
        placementCount = int(line[54:62].strip())
        placementCost = float(line[-32:-24].strip())
        salesNumber = int(line[-24:-16].strip())
        productPrice = float(line[-16:-8].strip())
        productionCost = float(line[-8:].strip())

        print(product)
        print(ad)
        print(placementCount)
        print(placementCost)
        print(salesNumber)
        print(productPrice)
        print(productionCost)

        #pass variables onto functions
        calculate_ROI(placementCount, salesNumber, salesNumber, productPrice, productionCost)
        revenue(salesNumber, productPrice)
        cost_of_goods_sold(placementCount, placementCost, salesNumber, productionCost)
        revenue(salesNumber, productPrice)
        totalProductionCost = salesNumber * productionCost

    ##   extract the data
    ##   print each product's best selling ad sales number, and best ROI
    ##   Here are two print lines to assit with formatting to match Mimir tests
    ##   print("  {:27s}{:>11s}".format("Best-Performing Ad","sales"))
    ##   print("  {:27s}{:>11s}".format("Best ROI","percent"))
    pass


if __name__ == "__main__":
    main()