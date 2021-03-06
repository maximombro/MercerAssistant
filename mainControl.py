# Runs the Mercer program

# Imports
import mercer as mercerControl
import generalUtilities as utils

# Variables
MERCER = None

# Main Thread
def main():
    # Indicate global
    global MERCER

    # Startup Mercer in specified mode
    mode = utils.askUserYesNo("Start in Debug Mode?",True)
    MERCER = mercerControl.MERCER(mode)

    # Welcome message
    print("\n<< Welcome to Mercer Main Control >>")

    # Enter menu functions
    options = ["Learning Menu","Generation Menu","Administration Menu"]
    utils.textMenu("Mercer Main Menu",options,"Save and Quit",mainMenuFunctions)

    # Exit Mercer safely
    MERCER.exitMercer()

    # Safe to exit message
    print("\nMercer has shutdown successfully.\nIt is now safe to close this window.")

# Functions for the main menu
def mainMenuFunctions(answer):
    # Because Python Switch statements don't exist
    if answer == "0":
        # Open Learning Menu
        options = ["Learn from File","Learn from Subreddit"]
        utils.textMenu("Learning Menu",options,"Back to Main Menu",learningMenuFunctions)
    elif answer == "1":
        # Open Generation Menu
        options = ["Generate Sentence","Write to File","Write to Console","Manually Set Word Type"]
        utils.textMenu("Generation Menu",options,"Back to Main Menu",generationMenuFunctions)
    elif answer == "2":
        # Open Admin Menu
        options = ["Log Dictionary","Show Dictionary Statistics","Toggle Debug Mode","Set Max Generation Attempts","Set Max Commonality Difference"]
        utils.textMenu("Administration Menu",options,"Back to Main Menu",adminMenuFunctions)

# Functions for the learning menu
def learningMenuFunctions(answer):
    # Indicate global
    global MERCER

    # Because Python Switch statements don't exist
    if answer == "0":
        # Learn from File process
        # Get filename from user
        fileName = utils.managedInput("Enter the file path to the .txt file","Cancel")

        # Check if response valid
        if fileName != None:
            # Learn from the file
            print("")
            learned = MERCER.learnTextFile(fileName)

            # Check if success
            if not learned:
                print("'"+fileName+"' could not be read.")
    elif answer == "1":
        # Learn from Subreddit process
        # Get subreddit
        subreddit = utils.managedInput("Enter the subreddit to skim","Cancel")

        # Check if valid
        if subreddit != None:
            # Get the post limit
            postLimit = utils.managedInputNumber("Max number of posts to read in /r/"+subreddit,"Cancel")

            # Check if valid
            if postLimit != None:
                # Learn from the subreddit
                learned = MERCER.learnFromSubReddit(postLimit,subreddit)

                # Check if success
                if not learned:
                    print("/r/"+subreddit+" could not be read. Check the log for details.")

# Functions for the generation menu
def generationMenuFunctions(answer):
    # Indicate global
    global MERCER

    # Because Python Switch statements don't exist
    if answer == "0":
        # Generate Sentence process
        print("Generating Sentence.")
        print(MERCER.createSentence(7))
    elif answer == "1":
        # Write to file process
        # Ask where
        path = utils.managedInput("Output file path","Cancel")

        # Check if valid
        if path != None:
            # Ask for file length
            length = utils.managedInputNumber("Max number of lines to generate","Cancel")

            # Check if valid
            if length != None:
                # Generate the file
                MERCER.writeTextToFile(length,7,path)

                # Report done
                print("File at '"+path+"' has been generated.")
    elif answer == "2":
        # Write to console process
        # Ask for file length
        length = utils.managedInputNumber("Max number of lines to generate","Cancel")

        # Check if valid
        if length != None:
            # Print to the console
            print("------------------")
            print(MERCER.writeText(length,7))
            print("------------------")
    elif answer == "3":
        # Manually set word type process
        # Ask for word
        word = utils.managedInput("Word to modify","Cancel")

        # Check if valid
        if word != None:
            # Build list of type options
            options = []
            for wordType in MERCER.getWordTypeTags():
                options.append(wordType.capitalize())
            
            # Add None option
            options.append("Unknown")

            # Add cancel option
            options.append("Cancel")

            # Ask user to choose one
            wordType = utils.askUser("What should the type be?",options)

            # Check if canceled
            if wordType != "Cancel":
                # Switch unknown tag
                if wordType == "Unknown":
                    wordType = MERCER.getNoneTag()

                # Set type
                success = MERCER.setWordType(word.lower(),wordType)

                # Check success
                if success:
                    print("'"+word+"' was successfully changed to a '"+wordType+"' type word.")
                else:
                    print("Word type could not be changed. Check the log for details.")

# Functions for the admin menu
def adminMenuFunctions(answer):
    # Indicate global
    global MERCER

    # Because Python Switch statements don't exist
    if answer == "0":
        # Log dictionary process
        # Ask if user is sure
        print("This is a massive text dump that is often not human readable.")
        shouldContinue = utils.askUserYesNo("Are you sure you want to continue?",True)

        # Check if should continue
        if shouldContinue:
            print(MERCER.logDictionary())
    elif answer == "1":
        # Show dictionary statistics process
        MERCER.getDictionaryStats()
    elif answer == "2":
        # Show toggle debug mode process
        # Ask for mode to switch
        mode = utils.askUserYesNo("Enable Debug Mode?",True)

        # Set the mode
        MERCER.setDebug(mode)
        
        # Choose print
        if mode:
            print("Debug Mode has been enabled.")
        else:
            print("Debug Mode has been disabled.")
    elif answer == "3":
        # Show set max generation attempts process
        # Enter number
        maxNum = utils.managedInputNumber("Set max generation attempts to","Cancel")

        # Check
        minLimit = 1
        if maxNum != None and maxNum >= minLimit:
            # Set max generation attempts
            MERCER.setMaxGenerationAttempts(maxNum)

            # Report
            print("Set max generation attempts to "+str(maxNum)+".")
        elif maxNum < minLimit:
            # Report
            print(str(minLimit)+" is minimum max generation attempts that can be set.")
    elif answer == "4":
        # Set max commonality difference process
        # Notes
        print("Higher numbers will allow more words to be considered as options under most circumstances.")
        print("Max commonality difference is currently set to top "+str(MERCER.getMaxCommonalityDifference())+"%.")

        # Get number
        amount = utils.managedInputNumberRange("Set max commonality difference to",100,1,"Cancel")

        # Check
        if amount != None:
            # Set number
            MERCER.setMaxCommonalityDifference(amount)

            # Report
            print("Set max commonality difference to top "+str(amount)+"%.")


# Execute Main Thread
main()
