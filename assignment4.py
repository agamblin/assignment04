import matplotlib.pyplot as plt


class MarginalUtilityDefiner:
    happiness_arr = []
    qty_arr = []

    def init(self):
        self.product = input('Please enter a product\n')
        self.qty = int(input('Please enter the maximum quantity\n'))

    def calculateQty(self):
        for i in range(0, self.qty):
            happiness_unit = input(
                'For ' + str(i + 1) + ' ' + self.product + ' what added happiness do you get ?\n')
            self.happiness_arr.append(int(happiness_unit))
            self.qty_arr.append(i + 1)

    def drawGraph(self):
        plt.plot(self.qty_arr, self.happiness_arr)
        plt.ylabel('Utility')
        plt.xlabel(self.product.capitalize() + ' qty')
        plt.title('Marginal utility for ' + self.product.lower())
        plt.legend(['Marginal utility'])
        plt.show()


marginalUtility = MarginalUtilityDefiner()

marginalUtility.init()
marginalUtility.calculateQty()
marginalUtility.drawGraph()
