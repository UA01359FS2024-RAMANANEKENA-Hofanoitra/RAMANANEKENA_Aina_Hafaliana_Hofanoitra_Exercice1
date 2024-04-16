def afficher_premiere_forme_canonique(table_de_verite, variable_names):

    nb_variables = len(table_de_verite[0]) - 1
    lignes_vraies = [i for i in range(len(table_de_verite)) if table_de_verite[i][-1] == 1]

    forme_canonique = ""
    for ligne in lignes_vraies:
        forme_canonique += "("
        for i in range(nb_variables):
            valeur = table_de_verite[ligne][i]
            if valeur == 1:
                forme_canonique += variable_names[i]
            else:
                forme_canonique += f"-{variable_names[i]}"
        forme_canonique += ") + "

    forme_canonique = forme_canonique[:-3]
    print(f"La première forme canonique est:\n{forme_canonique}")



def afficher_deuxieme_forme_canonique(table_de_verite, variable_names):

    nb_variables = len(table_de_verite[0]) - 1
    lignes_fausses = [i for i in range(len(table_de_verite)) if table_de_verite[i][-1] == 0]

    forme_canonique = ""
    for ligne in lignes_fausses:
        forme_canonique += "("
        for i in range(nb_variables):
            valeur = table_de_verite[ligne][i]
            if valeur == 0:
                forme_canonique += variable_names[i]
            else:
                forme_canonique += f"-{variable_names[i]}"
        forme_canonique += ") * "

    forme_canonique = forme_canonique[:-3]
    print(f"La deuxième forme canonique est:\n{forme_canonique}")



def get_user_input():

    try:
        num_variables = int(input("Entrez le nombre de variables: "))
    except ValueError:
        print("Il y a un erreur. Veuillez entrer un entier pour le nombre de variables.")
        return None, None, None

    variable_names = []
    for I in range(num_variables):
        variable_names.append(input("Entrez le nom de la variable {}: ".format(I + 1)))

    logic_function = input("Entrez la fonction logique (e.g., a et b ou non c): ")
    function_python = logic_function.replace("et", "and").replace("ou", "or").replace("non", "not")
    return num_variables, variable_names, function_python



def create_truth_table(num_variables):
   
    values = [0, 1]
    table_de_verite = []
    for I in range(2**num_variables):  # Generate all combinations using bit manipulation
        combination = []
        for j in range(num_variables):
            combination.append(values[I % 2])
            I //= 2
        table_de_verite.append(combination)
    return table_de_verite



def evaluate_function(function_python, variable_values):

    try:
        Function_result = eval(function_python, variable_values)
    except (NameError, SyntaxError) as e:
        print("Error evaluating expression:", e)
        return None
    return Function_result



def print_header(variable_names):

    print("=" * (14 + 5 * len(variable_names)))
    print("| ", end="")
    for name in variable_names:
        print(f"{name:5}", end="")
    print("| F({})".format(", ".join(variable_names)))
    print("=" * (14 + 5 * len(variable_names)))



def print_row(row):

    print("| ", end=" ")
    for value in row:
        print(f"{value:5}", end="")
    print("| ")



def main():
    """
    Fonction principale du programme.
    """
    # Obtenir les informations de l’utilisateur
    num_variables, variable_names, function_python = get_user_input()
    if num_variables is None:
        return

    # Créer le tableau de vérité
    table_de_verite = create_truth_table(num_variables)

    # Evaluer la fonction pour chaque ligne du tableau de vérité
    for I in range(len(table_de_verite)):
        Variable_values = dict(zip(variable_names, table_de_verite[I]))
        Result = evaluate_function(function_python, Variable_values)
        if Result is not None:
            table_de_verite[I].append(Result)  # Ajouter le résultat à la ligne
	
    # Afficher l’en-tête du tableau de vérité
    print_header(variable_names)

    # Afficher chaque ligne du tableau de vérité
    for row in table_de_verite:
        print_row(row)

    # Afficher les formes canoniques
    afficher_premiere_forme_canonique(table_de_verite.copy(), variable_names)
    afficher_deuxieme_forme_canonique(table_de_verite.copy(), variable_names)
	


if __name__ == "__main__":
    main()

