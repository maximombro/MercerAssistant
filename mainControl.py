# Runs the Mercer program

# Imports
import mercer as mercerControl

# Variables

# Main Thread
def main():
    # Startup Mercer
    mercer = mercerControl.MERCER()

    # Learn test text
    mercer.learnTextFile("learn/test.txt")
    mercer.learnTextFile("learn/2049.txt")

    # # Log the dictionary
    # mercer.logDictionary()

    # Write a sentence
    print(mercer.createSentence(7))

    # Exit the dictionary
    mercer.exitMercer()

# Execute Main Thread
main()
