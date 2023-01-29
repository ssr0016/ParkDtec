import os

# LEGEND4 GROUP MEMBERS
# RECLUTA JR., SAMSON D.
# PEDROZA, JADE C.
# PANARIGAN, RYAN O.
# ANGELES, EDRIANNE MAE N.

algorithms = {
    "classification": {
        "title": "classification",
        "description":
            """
            A classification algorithm, in general, is a function that weighs the input features so that the output separates one class into positive values and the other into negative values.
            """
    },
    "regression": {
        "title": "regression",
        "description":
            """
            Regression algorithms predict the output values based on input features from the data fed in the system. The go-to methodology is the algorithm builds a model on the features of training data and using the model to predict the value for new data.
            """
    },
    "clustering": {
        "title": "clustering",
        "description":
            """
            Clustering is the task of dividing the population or data points into a number of groups such that data points in the same groups are more similar to other data points in the same group and dissimilar to the data points in other groups.
            """
    },
    "KNN": {
        "title": "KNN",
        "description":
            """
            The k-nearest neighbors algorithm, also known as KNN or k-NN, is a non-parametric, supervised learning classifier, which uses proximity to make classifications or predictions about the grouping of an individual data point.
            """
    },
}


def printVerticalSpaces(n):
    for x in range(n):
        print()


def display_main_menu():
    os.system("cls")

    printVerticalSpaces(2)
    print('Legend 4'.upper())

    printVerticalSpaces(1)

    print('Main menu:')
    print('\t[1] Choose ML Algorithm to display')
    print('\t[2] Display all ML Algorithm')
    print('\t[3] Exit')

    printVerticalSpaces(1)

    chosen_menu = input('input: ')

    if chosen_menu == '1':
        choose_algorithm()
    elif chosen_menu == '2':
        display_all_algorithm()
    elif chosen_menu == '3':
        print('Thank you!'.upper())
        exit()
    else:
        input('Invalid input, enter any key to return...')
        display_main_menu()


def display_all_algorithm():
    os.system('cls')
    printVerticalSpaces(2)
    print('ML ALGORITHMS'.upper())
    printVerticalSpaces(1)

    display_classification_algorithm(clear_the_screen=False)
    display_regression_algorithm(clear_the_screen=False)
    display_clustering_algorithm(clear_the_screen=False)
    display_KNN_algorithm(clear_the_screen=False)

    input('\nEnter any key to return...')
    display_main_menu()


def choose_algorithm():
    os.system('cls')
    printVerticalSpaces(2)
    print('Choose algorithm to display:'.upper())

    print('\t[a] Classification Algorithm')
    print('\t[b] Regression Algorithm')
    print('\t[c] Clustering Algorithm')
    print('\t[d] KNN Algorithm')
    print('\t[e] Go back to Main menu')

    chosen_algo = input('input: ')

    if chosen_algo == 'a':
        display_classification_algorithm()
    elif chosen_algo == 'b':
        display_regression_algorithm()
    elif chosen_algo == 'c':
        display_clustering_algorithm()
    elif chosen_algo == 'd':
        display_KNN_algorithm()
    elif chosen_algo == 'e':
        display_main_menu()
    else:
        print('Invalid input\n')

    input('\nEnter any key to return...')
    choose_algorithm()


def display_classification_algorithm(clear_the_screen=True):
    if clear_the_screen:
        os.system('cls')
    printVerticalSpaces(1)
    algo = algorithms['classification']
    title = (algo["title"] + " algorithm").upper()
    print(title)
    print(algo["description"])

    print('• 🔵        Class A      ⁄')
    print('•      🔵              ⁄')
    print('• 🔵                 ⁄')
    print('                   ⁄')
    print('•   🔵   🔵     ⁄      🔴')
    print('• 🔵      🔵  ⁄   🔴    🔴 ')
    print('•    🔵      ⁄      🔴    🔴 ')
    print('•       🔵 ⁄  🔴  Class B ')
    print('• 🔵     ⁄       🔴')
    print('•   🔵 ⁄     🔴     🔴     🔴 ')
    print('•     ⁄            🔴')
    print('•   ⁄  🔴')
    print('• ⁄')
    print('• • • • • • • • • • • • • • • • • • >')

    if clear_the_screen:
        input('\nEnter any key to return...')
        choose_algorithm()


def display_regression_algorithm(clear_the_screen=True):
    if clear_the_screen:
        os.system('cls')
    printVerticalSpaces(1)
    algo = algorithms['regression']
    title = (algo["title"] + " algorithm").upper()
    print(title)
    print(algo["description"])

    print('•       🟢 🟢🟢       ⁄   🟢          ')
    print('•         🟢 🟢      ⁄ 🟢🟢         ')
    print('•     🟢 🟢🟢      ⁄🟢🟢 🟢          ')
    print('• 🟢    🟢 🟢🟢🟢⁄🟢 🟢 🟢     🟢       ')
    print('•    🟢🟢 🟢 🟢⁄🟢🟢  🟢  🟢         ')
    print('•   🟢 🟢 🟢  ⁄🟢🟢 🟢 🟢 🟢   ')
    print('•   🟢🟢🟢  ⁄🟢🟢 🟢        ')
    print('• 🟢🟢🟢  ⁄🟢 🟢🟢🟢            ')
    print('•🟢  🟢  ⁄    🟢 🟢 🟢           ')
    print('• 🟢🟢 ⁄ 🟢  🟢    🟢   🟢                 ')
    print('•🟢  ⁄🟢 🟢  🟢 🟢🟢       🟢 🟢🟢                     ')
    print('•   ⁄                                   ')
    print('• • • • • • • • • • • • • • • • • • >')

    if clear_the_screen:
        input('\nEnter any key to return...')
        choose_algorithm()


def display_clustering_algorithm(clear_the_screen=True):
    if clear_the_screen:
        os.system('cls')
    printVerticalSpaces(1)
    algo = algorithms['clustering']
    title = (algo["title"] + " algorithm").upper()
    print(title)
    print(algo["description"])

    print('^')
    print('•     🟢🟢 🟢.      🔴 🔴 ')
    print('•🟢🟢 🟢🟢    .    🔴 🔴🔴 🔴 🔴🔴')
    print('• 🟢 🟢🟢🟢🟢  . 🔴 🔴🔴 🔴🔴🔴🔴')
    print('• 🟢🟢🟢  🟢  .   🔴 🔴 🔴🔴🔴🔴')
    print('•🟢🟢🟢🟢🟢     . 🔴🔴🔴🔴🔴🔴')
    print('•🟢 🟢🟢    .     . 🔴🔴 🔴🔴')
    print('•   . 🟣 🟣🟣🟣 .   🔴 🔴')
    print('•  . 🟣🟣🟣🟣 🟣  .')
    print('•🟣🟣🟣🟣🟣🟣🟣. ')
    print('• 🟣 🟣🟣🟣')
    print('• 🟣🟣')
    print('• • • • • • • • • • • • • • • • • • >')

    if clear_the_screen:
        input('\nEnter any key to return...')
        choose_algorithm()


def display_KNN_algorithm(clear_the_screen=True):
    if clear_the_screen:
        os.system('cls')
    printVerticalSpaces(1)
    algo = algorithms['KNN']
    title = (algo["title"] + " algorithm").upper()
    print(title)
    print(algo["description"])

    print('^')
    print('• 🟢🟢🟢 Class A       🔴 🔴 ')
    print('•🟢🟢🟢🟢         🔴🔴🔴 🔴 🔴🔴 Class B')
    print('•🟢 🟢🟢🟢.🟢.  .   🔴.🔴🔴🔴🔴🔴🔴')
    print('• 🟢🟢.🟢🟢         🔴 .🔴 🔴🔴')
    print('•    🟢🟢. 🟢  🟡    🔴.🔴🔴🔴🔴🔴')
    print('•🟢 🟢 .            . 🔴🔴  🔴🔴')
    print('•         . 🟣🟣.  . k=3    🔴')
    print('•  🟣   🟣🟣🟣         ')
    print('•🟣 🟣🟣🟣🟣       ')
    print('• 🟣 🟣🟣🟣🟣🟣🟣')
    print('• 🟣🟣🟣 Class C')
    print('• • • • • • • • • • • • • • • • • • >')

    if clear_the_screen:
        input('\nEnter any key to return...')
        choose_algorithm()


display_main_menu()