##############################################################################
# Project 05 - RobCo Advertising
#
#   Open file function
#       returns the file name
#   revenue function
#       calculates and returns total revenue
#   cost of good sold function
#       calculates total cost of producing and advertising and returns it
#   calculate ROI function
#       calculates ROI and returns it
#   Main Method
#       try to open file with file pointer from file function
#       except filenotfound error
#           print error and re-prompt by calling function again
#       print welcome message
#       initialize state and current product
#       initialize product attributes
#       read each line in the file
#           seperate variables from the file via slicing
#           calculate complex values by calling functions
#           if the current product is different and its not the first line
#               state is 3 which is print out the info and reset counters
#           if its the first line
#               calculate best ads
#               set state to 1 and set current product = product
#           if state is 1 and current product = product
#               calculate best ads
#               current product is product
#           else
#               print product info
#               reset counters
#               calculate best ads for next product
#       print product info for last product
#
#   Call the main method
##############################################################################

#open the file and return file pointer
def open_file():

    #prompt for file name, open file, return file pointer
    filename = input("Input a file name: ")

    return filename

#calculate total revenue
def revenue(num_sales, sale_price):

    total_revenue = num_sales * sale_price

    return total_revenue

#calculate cost of goods sold
def cost_of_goods_sold(num_ads, ad_price, num_sales, production_cost):

    costs_of_goods_sold = num_ads*ad_price + num_sales*production_cost

    return costs_of_goods_sold

#calculate roi
def calculate_ROI(placement_count, placement_cost, sales_number, product_price, production_cost):

    total_revenue = revenue(sales_number, product_price)
    costs_of_goods_sold = cost_of_goods_sold(placement_count, placement_cost, sales_number, production_cost)
    roi = (total_revenue-costs_of_goods_sold)/costs_of_goods_sold

    return roi

#main method
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

    #initialize product attributes
    best_performing = ""
    sales = 0
    best_roi = 0.0
    best_roi_ad = ""

    #read the file
    for line in fp:

        #seperate each variable from its place in the file
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

        #handles if the product is different
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

            # find best performing ads
            if sales_number > sales:
                sales = sales_number
                best_performing = ad
            if roi > best_roi:
                best_roi = roi
                best_roi_ad = ad
            current_product = product

        #print out stats about the last product
        else:

            print("\n" + current_product)
            print("  {:27s}{:>11s}".format("Best-Performing Ad", "sales"))
            print("  {:27s}{:>11d}".format(best_performing, sales))
            print("\n  {:27s}{:>11s}".format("Best ROI", "percent"))
            print("  {:27s}{:>10.2f}%".format(best_roi_ad, best_roi))

            #reset values and state
            best_performing = ""
            sales = 0
            best_roi = 0.0
            best_roi_ad = ""
            state = 1
            current_product = product

            #find best performing ads
            if sales_number > sales:
                sales = sales_number
                best_performing = ad
            if roi > best_roi:
                best_roi = roi
                best_roi_ad = ad

    #print stats for last product at end
    print("\n" + current_product)
    print("  {:27s}{:>11s}".format("Best-Performing Ad", "sales"))
    print("  {:27s}{:>11d}".format(best_performing, sales))
    print("\n  {:27s}{:>11s}".format("Best ROI", "percent"))
    print("  {:27s}{:>10.2f}%".format(best_roi_ad, best_roi))
    print()

if __name__ == "__main__":
    main()