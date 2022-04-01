"""Functions to parse a file containing villager data.""" 


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    # TODO: replace this with your code
    file1 = open(filename)
    for line in file1:
        line.strip()
        split_list = line.split('|')
        species.add(split_list[1])

    return species

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    file1 = open(filename)
    villagers = []

    # TODO: replace this with your code
    for line in file1:
        line.strip()
        split_list = line.split('|')
        if split_list[1] == search_string or search_string == "All":
            #add name of villager to list
            villagers.append(split_list[0])

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    
    # First create a set of all the hobbys of the villagers.
    # Read the file again for each of the hobby in the set.
        # make a list of all villagers name.
        # Add this result to the final output.

    # TODO: replace this with your code 

    #output: 
#    [[Antonio,Annie, Bart], [Alex, Megan, Tyler]...]
    file1 = open(filename)

    hobbies = set()

    #splitting the lines by '|'
    for line in file1:
        line.strip()
        split_list = line.split('|')
        hobbies.add(split_list[3])
    
    def names_hobby(hobby):
        """
            Helper function to get the namem list based on the hobby value passed to the function.
            Takes input as hobby.
            Output is list of names with the same hobby.
        """

        names = []
        file1 = open(filename)

        for line in file1:
            line.strip()
            split_list = line.split('|')
            if hobby == split_list[3]:
                names.append(split_list[0])
        
        return names

    #hobby = list(hobbies)
    hobby = ('Fitness', 'Nature','Education', 'Music', 'Fashion', 'Play')
    result = []

    #calling helper function 'names_hobby' to add each villagers name to the hobby list

    for i in hobby:

        name1 = names_hobby(i)
        name1.sort()
        result.append(name1)

    print(result)
    
    return result


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
