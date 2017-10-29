# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample1 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

answers1 = ["function","parameters","none","list"]

sample2 = """Many ___4___s and landmarks in ___1___ are well known, and the city received a record 61 million ___3___s in 2016, hosting three of the world's ten most visited ___3___ attractions in 2013. Several sources have ranked New York the most photographed city in the world. Times Square, iconic as the world's "heart" and its "Crossroads", is the brightly illuminated hub of the Broadway Theater ___4___, one of the world's busiest pedestrian intersections, and a major center of the world's entertainment industry. The names of many of the city's bridges, skyscrapers, and parks are known around the world. Anchored by Wall Street in the Financial ___4___ of Lower ___5___, ___1___ has been called both the most economically powerful city and the leading financial center of the world, and the city is home to the world's two largest stock exchanges by total market capitalization, the New York Stock Exchange and NASDAQ. ___5___'s real estate market is among the most expensive in the world. ___5___'s ___2___ incorporates the highest concentration of Chinese people in the Western Hemisphere, with multiple signature ___2___s developing across the city. Providing continuous 24/7 service, the ___1___ Subway is one of the most extensive metro systems worldwide, with 472 stations in operation. Over 120 colleges and universities are located in ___1___, including Columbia University, New York University, and Rockefeller University, which have been ranked among the top universities in the world."""

answers2 = ["New York City", "Chinatown", "tourist", "district", "Manhattan"]

sample3 = """Typically,  is packaged in a form known as a ___1___ ___2___ (or distro for short) for both ___3___ and ___5___ use. Some of the most popular and mainstream ___1___ ___2___s are Arch ___1___, CentOS, Debian, Fedora, Gentoo ___1___, ___1___ Mint, Mageia, openSUSE and Ubuntu, together with commercial ___2___s such as Red Hat Enterprise ___1___ and SUSE ___1___ Enterprise ___5___. ___2___s include the ___1___ ___6___, supporting utilities and libraries, many of which are provided by the GNU Project, and usually a large amount of application ___4___ to fulfil the ___2___'s intended use. ___3___ ___1___ ___2___s include a windowing system, such as X11, Mir or a Wayland implementation, and an accompanying ___3___ environment such as GNOME or KDE Plasma 5; some ___2___s may also include a less resource-intensive ___3___, such as LXDE or Xfce. ___2___s intended to run on ___5___s may omit all graphical environments from the standard install, and instead include other ___4___ to set up and operate a solution stack such as LAMP. Because ___1___ is freely redistributable, anyone may create a ___2___ for any intended use."""

answers3 = ["Linux","distribution", "desktop", "software", "server", "Kernel"]

answerDict = {sample1 : answers1, sample2 : answers2, sample3 : answers3}

difficulties = [sample1,sample2,sample3]
answers = [answers1, answers2, answers3]
# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

#print sample.find("___%d___" % (4) )
#above proves I can search for

#def findNumBlanks(paragraph):
#    #uses string formatting to count number of blanks
#    blanks = 1
#    while True:
#        if paragraph.find("___%d___" % (blanks)) != -1:
#            blanks += 1
#        else:
#            break
#    return blanks - 1

#def giveWords(num):
#    #gets user input for number of blanks in sample
#    print "Enter the appropriate words, in order, that would make the paragraph complete.  \r Do not repeat words."
#    index = 0
#    answers = []
#    while index < num:
#        word = raw_input("%d:" % (index + 1) )
#        answers.append(word)
#        index += 1
#    return answers

def testAnswers(paragraph, word, num):
    #checks if the entered word is in the answer bank
    if word == answerDict[paragraph][num]:
        return True
    else:
        return False

def replaceWord(originParagraph, newPara, word):
    #replaces all the words in the text
    replaced = "___%d___" % (answerDict[originParagraph].index(word) + 1)
    #print replaced
    #print word
    return newPara.replace(replaced, word)

def gettingAnswers(originParagraph):
    #performs main loop to find correct answers, and replaces blanks in the text
    #prints question after entering correct answer
    index = 0
    questions = len(answerDict[originParagraph])
    question = originParagraph
    answer = ""
    while index < questions:
        answer = raw_input("Please enter an answer for blank number %d: " % (index + 1))
        if testAnswers(originParagraph, answer, index):
            question = replaceWord(originParagraph, question, answer)
            print question
            index += 1
        else:
            print "Please try again.\r"
    return

#def replaceAnswers(paragraph):
#    #replaces sample blanks with answers
#    #this part gets the answer list
#    ansList = giveWords(findNumBlanks(paragraph))
#    index = 1
    #print ansList
#    newPara = paragraph
#    #replacing blanks with answers
#    for word in ansList:
#        #print word
#        question = "___%d___" % (index)
#        newPara = newPara.replace(question, word)
#        index += 1
#    return newPara

def difficultySelect(qlist):
    #this selects the difficulty and returns the sample paragraph to use
    selection = -1
    while selection not in ["0","1","2"]:
        selection = raw_input("Select a difficulty from 0 to 2, 2 being hardest: ")
        print qlist[int(selection)]
    return qlist[int(selection)]

def main(qlist):
    #the method that runs the program
    return gettingAnswers(difficultySelect(qlist))

#print answerDict[sample1][2]
print main(difficulties)
raw_input("press enter to end")
#print main(difficulties)
#print findNumBlanks(sample)
