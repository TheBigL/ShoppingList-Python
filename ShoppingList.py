shoppingList = []


# This item shows how to navigate the app.
def show_help():
    print("Welcome the shopping app.")

    print("""
---------------------------------------------
SHOW - Show All Items currently on the list
DONE - Finish the list and exit out of the app.
HELP - Show this line.
UPDATE - Updates an item in the index.
DELETE - deletes an item from the list.
---------------------------------------------
""")


def show_help_other():
    print("Welcome the shopping app.")

    print("""
    Instruction
----------------------------------------------
SHOW - Show All Items currently on the list
DONE - Finish the list and exit out of the app.
HELP - Show this line.
----------------------------------------------
""")


# This method adds items to a list.
def add_item(item):
    shoppingList.append(item)
    print("{} added! You now have {} items.".format(item, len(shoppingList)))


# This one simple finish the app and closes.
def finish(item):
    print("Here are your items:")
    for item in shoppingList:
        print(item)

    print("In total, you added {} items".format(len(shoppingList)))


# Shows the items the user has inputted so far.
def show_item():
    if len(shoppingList) == 0:
        print("You don't have any items yet. Come back when you've added some.")
        main()

    else:
        for item in shoppingList:
            print(item)


# This method allows the user to update an item to the list.
def update():
    if len(shoppingList) == 0:
        print("Try added some item and come back again.")


    else:
        item = input("Select the item you want to update")

        while item != "CANCEL" or "SHOW":

            if item in shoppingList:
                new_item = input("Select the item you want to replace it with.")
                for item, new_item, n in shoppingList:
                    if item == shoppingList[n]:
                        shoppingList[n] = new_item
                        print("{} has been replaced with {}".format(item, new_item))
                        main()
                else:
                    print("Item does not exist. Returning to the main program.")
                    main()

            elif item == "SHOW":
                show_item()
                continue

            elif item == "CANCEL":
                main()


            else:
                print("There's no item like that. Try again")
                continue


def delete():
    if len(shoppingList) == 0:
        print("You cannot delete items until you've got some items")
        main()

    else:
        item = input("Select an item on the list that you want to delete\n")

        if item in shoppingList:
            shoppingList.remove(item)
            print("{} has been deleted. It will be free, so be sure to add an item to replace it.")

        elif item == "CANCEL":
            print("Going back to the main menu.")
            main()


        else:
            print("Item does not exist. Press the show button to see the item that exists")
            while item not in shoppingList or item != "CANCEL":
                item = input("Select an item on the list that you want to delete")


def main():
    show_help()
    while True:
        # Ask for new items
        item = input("Enter your item\n")
        if item == "SHOW":
            show_item()
            continue

        elif item == "DONE":
            break

        elif item == "HELP":
            show_help()
            continue


        elif item == "UPDATE":
            update()
            continue


        elif item == "DELETE":
            delete()
            continue

        else:
            add_item(item)



            # List item


main()
