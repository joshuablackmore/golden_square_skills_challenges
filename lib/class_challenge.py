class GrammarStats:
    def __init__(self):
        self.good_texts = 0
        self.bad_texts = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        
        if text[0].isupper() and text[-1] == ".":
            self.good_texts += 1
            return True
        else:
            self.bad_texts += 1
            return False
        


    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        all_checks = self.good_texts + self.bad_texts
        return self.good_texts / all_checks * 100

# test_instance = GrammarStats()

# test_instance.check("Joshua is a drummer.")
# test_instance.check("Joshua is a drum")
# test_instance.check("joshua is bad")
# test_instance.check("Final text is good.")

# test_instance.percentage_good()