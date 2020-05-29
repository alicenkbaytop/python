class File():

    def __init__(self,file_name):

        with open(file_name,"r",encoding = "utf-8") as file:

            file_content = file.read()
            words = file_content.split()

            self.core_words = list()

            for word in words:
                word = word.strip()
                word = word.strip(".")
                word = word.strip(",")
                word = word.strip("\n")

                self.core_words.append(word)
                
    def find_word(self,search):
        
        location = list()
        count = 1
        for word in self.core_words:
            if (word == search):
                location.append(count)
            count += 1

        if (len(location) == 0):
            print("There is no same word in this text...")
            
        else:
            print("{} word in this location {}.".format(search,location))

    def word_histogram(self):
        
        word_frequency = dict()
        set_of_word = set()

        for word in self.core_words:
            set_of_word.add(word)
            
            if (word in word_frequency):
                word_frequency[word] += 1
                
            else:
                word_frequency[word] = 1
                
        print("------Words Frequency------")
        for i, j in word_frequency.items():
            print("{} in this text {} times.".format(i, j))
            print("------------------------------")


file =  File("text.txt")

print(
"""
*****************************************
*                                       *
*     File Processing:                  *
*                                       *
*     1. Learn all words frequency:     *
*                                       *
*     2. Search word:                   *
*                                       *
*     to exit press 'q'.                *
*                                       *
*****************************************
""")

while True:
    operation = input("Please, Choice an Operation:")

    if (operation == "q"):
        print("Exit...")
        break
    
    elif (operation == "1"):
        file.word_histogram()
        
    elif (operation == "2"):
        word = input("What are you searching?")
        file.find_word(word)
        
    else:
        print("Invalid Operation...")