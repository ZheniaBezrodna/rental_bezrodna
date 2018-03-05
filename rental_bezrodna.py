class Property:
    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        # Allows you to enter data corresponding to this type of property to
        # the user, and returns the dictionary with these data.
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    # The apartment class extends property and is similar in structure
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        # The __init__() and display() methods call their respective parent
        # class methods using super() to ensure the property class is properly
        # initialized.
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        # This method getting dictionary values from parent class, and then
        # adding some additional values of its own.
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does "
            "the property have? ",
            Apartment.valid_laundries)
        balcony = get_valid_input(
            "Does the property have a balcony? ",
            Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    # The function performs an auxiliary role to avoid duplication and clutter
    # code in the methods.
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


def prompt_init():
    # Allows you to enter data corresponding to this type of property to
    # the user, and returns the dictionary with these data.
    parent_init = Property.prompt_init()
    laundry = get_valid_input(
        "What laundry facilities does "
        "the property have? ",
        Apartment.valid_laundries)
    balcony = get_valid_input(
        "Does the property have a balcony? ",
        Apartment.valid_balconies)
    parent_init.update({
        "laundry": laundry,
        "balcony": balcony
    })
    return parent_init


class House(Property):
    # This class has a parallel structure to Apartment, but refuses to
    # different prompts and variables.
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        # Allows you to enter data corresponding to this type of property to
        # the user, and returns the dictionary with these data.
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)

        num_stories = input("How many stories? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        # Allows you to enter data corresponding to this type of property to
        # the user, and returns the dictionary with these data.
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        # Allows you to enter data corresponding to this type of property to
        # the user, and returns the dictionary with these data.
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ",
                                      ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    def prompt_init():
        # Allows you to enter data corresponding to this type of property to
        # the user, and returns the dictionary with these data.
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    def prompt_init():
        # Allows you to enter data corresponding to this type of property to
        # the user, and returns the dictionary with these data.
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    def prompt_init():
        # This method is promoting for initializer to all the super classes.
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    # This class which is responsible for creating new listings and displaying
    # existing one.
    def __init__(self):
        self.property_list = []

    def start(self):
        # This method helps you decide whether to start using the program or
        # not.
        start_1 = input("Do you want to start use this program(yes, no)? ")
        if start_1 != "yes":
            exit("Goodbye!")
        return " "

    def display_properties(self):
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()

        property_class = self.type_map[
            (property_type, payment_type)]
        init_args = property_class.prompt_init()
        self.property_list.append(property_class(**init_args))


agent = Agent()
print(agent.start())
print(agent.add_property())
print(agent.display_properties())
