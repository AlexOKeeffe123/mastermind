#Chase
class Display:
    """The class constructor

	Attributes:
        textPrompt (String): The prompt to display string lines
        textPrompt (String): Displays what gets passed in
	"""

    def read_int(self, textPrompt):
        """ Returns an integer

        Args:
            self (Display): an instance of Display

        Returns:
            int: Value representing the integer for prompt
        """
        return int(input(textPrompt))


    def read(self, textPrompt):
        """ Returns whatever input is read in

        Args:
            self (Display): an instance of Display

        Returns:
            int: Value representing string the for prompt
        """ 
        return input(textPrompt)



    def write(self, textToPrint):
        """ Prints what is passed in

        Args:
            self (Display): an instance of Display

        Print:
            texttoPrint (String): Display of what gets passed in
        """ 
        print(textToPrint)