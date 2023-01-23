class ROI_Calc():

    def __init__(self):
        self.revenue = None
        self.expense = None
        self.investment = None
        self.total_invest = {}
        self.roi = None
        self.data = {}
        self.property = []
        self.name = None


# User needs to input reveneue/money coming in from rental property monthly, then user needs to put in the average monthly cost. As well, user will need to put in initial investment into rental property.
# Then there needs to be a separate calculator function that will take all the user information the user just input and return a final calculation of the annual ROI.
# (Revenue - Cost) = cash flow (monthly basis)
# Initial investment = How much money user put down on the house and how much they invested in renovating it
# Initial Investment / (cash flow * 12)

    def User_Input(self):
        self.data['dictionary'] = {}
        name = input("Please tell us your name. ")
        if name.lower().strip() not in self.data:
            self.data['dictionary']['user'] = {}
            self.data['dictionary']['user']['name'] = name.lower()
            self.name = name
        self.data['dictionary']['user']['properties'] = {}
        property_name = input("What would you like to call your property?")
        if property_name not in self.data['dictionary']['user']['properties']:
            self.data['dictionary']['user']['properties']['property name'] = property_name
            self.property.append(property_name)
        investment_input = input(
            f"Thank you {name}, now please tell what us your initial total investment on {property_name}, type n to quit ")
        if investment_input not in self.data['dictionary']['user']['properties']:
            self.data['dictionary']['user']['properties']["investment"] = investment_input
            self.investment = investment_input
        revenue_input = input(
            "Now please input how much revenue you make off of your rental property ")
        if revenue_input not in self.data['dictionary']['user']['properties']:
            self.data['dictionary']['user']['properties']["revenue"] = revenue_input
            self.revenue = revenue_input
        self.data['dictionary']['user']['properties']['expenses'] = {}
        while True:
            expense_input = input(
                "What is the expense you want to add?, type 'n' to stop ")
            if expense_input == 'n':
                print(self.data)
                self.expense = sum(
                    self.data['dictionary']['user']['properties']["expenses"].values())
                break
            if expense_input not in self.data['dictionary']['user']['properties']:
                expense_amount = int(
                    input("How much is this expense per month? "))
                self.data['dictionary']['user']['properties']["expenses"][expense_input] = expense_amount


# User_options method 1. Look/Edit Expenses 2. View current ROI breakdown 3. Calculate ROI 4. Quit the program


    def Calculator(self):
        cash_flow = int(self.revenue) - int(self.expense)
        ROI_answer = (int(cash_flow) * 12) / int(self.investment)
        print(
            f"Your estimated Annual Return on Investment  is {ROI_answer * 100}%.")
        self.roi = ROI_answer
        # print(self.roi)
        return

    def run_calc(self):
        self.User_Input()
        self.Calculator()

    def run_func(self):
        self.User_Options()

    def roi_breakdown(self):
        self.Calculator()
        print(
            f"Your total investment: {self.data['dictionary']['properties']['investment']}")
        print(
            f"Your monthly revenue from your rental property: {self.data['dictionary']['properties']['revenue']}")
        print(
            f"Here is a breakdown of your monthly expenses: {self.expense}")
        print(f"Your current estimated ROI is {self.roi}")
        return

    def ViewExpenses(self):
        for key, value in self.data['dictionary']['properties']['expenses'].items():
            print(f"Expense: {key} Cost: {value}")
            expense_options = input(
                "Would you like to CHANGE or DELETE any of your current costs?, type n to quit ")
            if expense_options.lower() == 'change':
                key_input = input("What expense would you like to change? ")
                if key_input in self.data['dictionary']['properties']['expenses']:
                    value_input = input(
                        "What would you like to change the expense to? ")
                    self.data['dictionary']['properties']['expenses'][key_input] = value_input
                    print(
                        f"Ok! {key_input} has now been adjusted to {value_input} ")
                else:
                    print(
                        "That expense is not currently being considered. Please add it or try again.")
            elif expense_options.lower() == 'delete':
                key_input = input("What expense would you like to delete? ")
                if key_input in self.dictionary:
                    del self.data['dictionary']['properties']['expenses'][key_input]
            else:
                print("This is not a valid option, please try again.")
        return

  # def AddExpense(self):
      # for key, value in self.dictionary.items():
      #     print(f"Expense: {key} Cost: {value}")
      #     expense_add = input("What expense would you like to add? ")
      #     add_value = input("How much is this new expense per month? ")
      #     self.dictionary[expense_add] = int(add_value)
      #     self.expense = sum(self.dictionary.values())
      #     return
#
  # de#f ViewRevenue(self):
      # print(f"Revenue coming in from your rental property: {self.revenue}")
      # edit_revenue = input("Would you like to edit your revenue? ")
      # if edit_revenue.lower() == 'yes':
      #     new_revenue = int(
      #         input("What would you like to update your revenue to? "))
      #     if new_revenue not in self.data[name][property_name]:
      #     self.revenue = new_revenue
      #     print(f"OK! Your revenue is now {self.revenue}")
      # elif edit_revenue.lower() == "no":
      #     return
#
    def ViewInvestment(self):
        print(
            f"Your total current investment in this property is: {self.data['dictionary']['properties']['investment']}")
        edit_invest = input("Would you like to edit your investment amount? ")
        if edit_invest.lower() == 'yes':
            new_invest = int(
                input("What would you like to update your revenue to? "))
            self.data['dictionary']['properties']['investment'] = new_invest
            print(
                f"OK! Your revenue is now self.data['dictionary']['properties']['investment']")
        elif edit_invest.lower() == "no":
            return

    # def ChangeUser(self):

    def AddUser(self):
        print(self.data['dictionary']['user'])
        name = input("What is the name of the new user? ")
        if name.lower().strip() not in self.data['dictionary']['user']['name']:
            self.data['dictionary']['user']['name'] = name.lower().strip()
        else:
            print(f"{name} already exists, please choose another")
        property_name = input("What would you like to call your property?")
        if property_name not in self.data['dictionary']['user']['properties']:
            self.data['dictionary']['user']['properties']['property name'] = property_name
        investment_input = input(
            f"Thank you {name}, now please tell what us your initial total investment on {property_name}, type n to quit ")
        if investment_input not in self.data['dictionary']['user']['properties']:
            self.data['dictionary']['user']['properties']["investment"] = investment_input
            self.investment = investment_input
        revenue_input = input(
            "Now please input how much revenue you make off of your rental property ")
        if revenue_input not in self.data['dictionary']['user']['properties']:
            self.data['dictionary']['user']['properties']["revenue"] = revenue_input
            self.revenue = revenue_input
        self.data['dictionary']['user']['properties']['expenses'] = {}
        while True:
            expense_input = input(
                "What is the expense you want to add?, type 'n' to stop ")
            if expense_input == 'n':
                print(self.data)
                self.expense = sum(
                    self.data['dictionary']['user']['properties']["expenses"].values())
                break
            if expense_input not in self.data['dictionary']['user']['properties']["expenses"]:
                expense_amount = int(
                    input("How much is this expense per month? "))
                self.data['dictionary']['user']['properties']["expenses"][expense_input] = expense_amount
                print(self.data['dictionary'])

    def AddProperty(self):
        print(self.data['user'])
        user_input = input(
            "Enter the username you would like to add the property to.")
        if user_input.lower().strip() in self.data['user']['name']:
            print(self.data['user']['name'])
        else:
            print("That user currently isn't registered. Please try again.")
            return
        property_input = input(
            "What would you like to call the property? ")
        if property_input not in self.data['user']['properties']['property name']:
            self.data['user']['properties'][property_input] = {}
        else:
            print(f"{property_input} already exists, please try again")
        investment_input = input(
            f"Thank you {user_input}, now please tell what us your initial total investment on {property_input}, type n to quit ")
        if investment_input not in self.data['user']['properties']['property name']:
            self.data['user']['properties']['property name']["investment"] = investment_input
            self.investment = investment_input
        property_revenue = int(
            input("How much revenue do you make off of this property?"))
        self.data['user']['properties']['property name'][property_input]['revenue'] = property_revenue
        while True:
            expense_input = input(
                "What is the expense you want to add?, type 'n' to stop ")
            if expense_input == 'n':
                print(self.data)
                self.expense = sum(
                    self.data['user']['properties']['property name']["expenses"].values())
                break
            if expense_input not in self.data['user']['properties']['property name']:
                expense_amount = int(
                    input("How much is this expense per month? "))
                self.data['user']['properties']['property name']["expenses"][expense_input] = expense_amount
                print("Your new property has been added!")
                print(self.data)

    def User_Options(self):
        while True:
            print("""
        [1] Calculate ROI (first time only)
        [2] Add/View User
        [3] Change Users
        [4] Add Property
        [5] View Current ROI Breakdown
        [6] View / Edit Expenses
        [7] View / Edit Revenue
        [8] View / Edit Total Investment
        [9] Add to Expenses
        [0] Quit the Program

        """)
            options_input = input("Please choose from the list above ")
            if options_input == "1":
                self.run_calc()
            elif options_input == '2':
                self.AddUser()
            elif options_input == '3':
                self.ChangeUser()
            elif options_input == '4':
                self.AddProperty()
            elif options_input == "5":
                self.roi_breakdown()
            elif options_input == "6":
                self.ViewExpenses()
            elif options_input == "7":
                self.ViewRevenue()
            elif options_input == '8':
                self.ViewInvestment()
            elif options_input == '9':
                self.AddExpense()
            elif options_input == '0':
                break
            else:
                print("This is not a valid option. Please try again.")


roi = ROI_Calc()

roi.run_func()
