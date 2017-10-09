###########################################################
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
###########################################################

def open_file():

    #prompt for file name, open file, return file pointer
    filename = input("Input a file name: ")

    return filename


def revenue(num_sales, sale_price):

    total_revenue = num_sales * sale_price

    return total_revenue


def cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost):

    costs_of_goods_sold = num_ads*ad_price + num_sales*production_cost

    return costs_of_goods_sold


def calculate_ROI(placementCount, placementCost, salesNumber, productPrice, productionCost):

    total_revenue = salesNumber * productPrice
    costs_of_goods_sold = placementCount * placementCost + salesNumber * productionCost
    roi = (total_revenue-costs_of_goods_sold)/costs_of_goods_sold

    return roi


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

    #variables related to current state
    state = 0
    current_product = ""

    #product attributes
    best_performing = ""
    sales = 0
    best_roi = 0.0
    best_roi_ad = ""

    #read the file
    for line in fp:

        product = line[:27].strip()
        ad = line[27:54].strip()
        placement_count = int(line[54:62].strip())
        placement_cost = float(line[-32:-24].strip())
        sales_number = int(line[-24:-16].strip())
        product_price = float(line[-16:-8].strip())
        production_cost = float(line[-8:].strip())

        # pass variables onto functions
        total_revenue = revenue(sales_number, product_price)
        roi = calculate_ROI(placement_count, placement_cost, sales_number, product_price, production_cost)
        total_prod_cost = sales_number * production_cost

        if product != current_product and state != 0:
            state = 3
            #print("New Product")

        #for the first line in the program
        if state == 0:

            if sales_number > sales:
                sales = sales_number
                best_performing = ad
            if roi > best_roi:
                best_roi = roi
                best_roi_ad = ad
            state = 1
            current_product = product

        #for all lines not the first one
        if state == 1 and current_product == product:

            if sales_number > sales:
                sales = sales_number
                best_performing = ad
            if roi > best_roi:
                best_roi = roi
                best_roi_ad = ad
            current_product = product

        else:

            print("\n" + current_product)
            print("  {:27s}{:>11s}".format("Best-Performing Ad", "sales"))
            print("  {:27s}{:>11d}".format(best_performing, sales))
            print("\n  {:27s}{:>11s}".format("Best ROI", "percent"))
            print("  {:27s}{:>10.2f}%".format(best_roi_ad, best_roi))


            best_performing = ""
            sales = 0
            best_roi = 0.0
            best_roi_ad = ""
            state = 1
            current_product = product

            if sales_number > sales:
                sales = sales_number
                best_performing = ad
            if roi > best_roi:
                best_roi = roi
                best_roi_ad = ad

    print("\n" + current_product)
    print("  {:27s}{:>11s}".format("Best-Performing Ad", "sales"))
    print("  {:27s}{:>11d}".format(best_performing, sales))
    print("\n  {:27s}{:>11s}".format("Best ROI", "percent"))
    print("  {:27s}{:>10.2f}%".format(best_roi_ad, best_roi))
    print()

if __name__ == "__main__":
    main()