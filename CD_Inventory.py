#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# JFallon, 2022-Mar-19, added code to complete the TODO's; change internal data storage to objects
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        description:  creates a string formatted description of the object
        __str__:  custom __str()__ method that invokes description method
        addCD:  appends the object to lstOfCDObjects
        csv:  formats object attributes as csv 
        

    """
    # TODone Add Code to the CD class
    # -- Fields -- #

    # -- Constructor -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        #   -- Attributes -- #
        self.__iden = cd_id
        self.__title = cd_title
        self.__artist = cd_artist

    # -- Properties -- #
    @property
    def iden(self):
        return self.__iden
    
    @iden.setter
    def iden(self, value):
        self.__iden = value
        
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        self.__title = value
        
    @property
    def artist(self):
        return self.__artist
    
    @artist.setter
    def artist(self, value):
        self.__artist = value

    # -- Methods -- #
    def description(self):
        return '{}, {}, {}'.format(self.iden, self.title, self.artist)
    
    def __str__(self):
        return self.description()
    
    def addCD(self):
        lstOfCDObjects.append(self)
              
    def csv(self):
        return '{},{},{}'.format(self.iden, self.title, self.artist)
        

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        read_file(file_name, table): -> None
        write_file(file_name): -> (table (a list of CD objects))

    """
    # TODone Add code to process data from a file
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of objects

        Reads the data from file identified by file_name into a 2D table
        (list of objects) table one line in the file represents one object in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime

        Returns:
            None.
        """        
        try:
            table.clear()  # this clears existing data and allows to load data from file
            objFile = open(file_name, 'r') # open the file
            for line in objFile: # read the lines in the file
                data = line.strip().split(',') # separate out the values in the line
                # assign the values to variables
                cd_id = data[0]
                title = data[1]
                artist = data[2]
                CDobject = CD(cd_id, title, artist) # create a CD object and use values from file for object attributes
                CDobject.addCD() # append the CD object to lstOfCDObjects
            objFile.close()
        except FileNotFoundError:
            print('\nYour CD inventory is empty. Try adding a CD.\n')
    # TODone Add code to process data to a file
    @staticmethod
    def write_file(file_name, table):
        """Function to save data to text file

        Saves the data from a 2D table to text file identified by file_name

        Args:
            file_name (string): name of file used to read the data from
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime

        Returns:
            None.
        """
        # add some error handling
        try:
            objFile = open(file_name, 'w')
            for item in table:
                strItem = item.csv() # call the csv method to put the object's attributes in csv format
                objFile.write(strItem + '\n')
            objFile.close()
            print('\nYour inventory is saved to file now.\n')
        except:
            print('\nSomething went wrong. Make sure you have permission to save to this location.\n')

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODone add docstring
    """Handling Input / Output"""
    # TODone add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] Exit\n')
    # TODone add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    # TODone add code to display the current data on screen
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for item in table:
            print(item)
        print('======================================')
    # TODone add code to get CD data from user
    @staticmethod
    def get_inventory():
        """Gets user input, and returns values for, CD ID, Title, and Artist 

        Args:
            None.

        Returns:
            cd_id (string): a string of the user selected ID value
            title (string): a string of the user input for CD name
            artist (string): a string of the user input for Artist

        """
        cd_id = '' # set cd_id to empty; we'll get a value for it below
        while type(cd_id) != int: # don't let the user go anywhere until they enter a number
            try: # set up error handling to catch non-numeric id values
                cd_id = int(input('Enter an ID number: ').strip())
            except ValueError: # added ValueError exception type
                print('That value was not a number, or wasn\'t a whole number. Please try again.')        
        title = input('What is the CD\'s title? ').strip()
        artist = input('What is the Artist\'s name? ').strip()
        return cd_id, title, artist

# -- Main Body of Script -- #
# TODone Add Code to the main body
# Load data from file into a list of CD objects on script start
FileIO.read_file(strFileName, lstOfCDObjects)

while True:
    # Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # let user exit program
    if strChoice == 'x':
        break
    # let user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Type \'yes\' to continue and reload from file. Otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.read_file(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('Canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # let user add data to the inventory
    elif strChoice == 'a':
        # ask user for new ID, CD Title and Artist
        strID, strAlbum, strArtist = IO.get_inventory()
        # create a CD object
        CDobject = CD(strID, strAlbum, strArtist)
        # append the CD object to lstOfCDObjects
        CDobject.addCD()
        print('\nThat CD has been added to your inventory.\n')
        continue  # start loop back at top.
    # show user current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # let user save inventory to file
    elif strChoice == 's':
        # display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # process choice
        if strYesNo == 'y':
            # save data
            FileIO.write_file(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')