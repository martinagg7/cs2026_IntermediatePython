"""Practice with writing test cases and performing test-driven development using a
Guess-My-Number game as a problem statement.

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Martina Garcia
"""

import sys
import random

FILENAME_REQ = "numberGuesser.py"
meetsFilenameReq = sys.argv[0].strip().endswith(FILENAME_REQ)
assert meetsFilenameReq, f"File must remain named {FILENAME_REQ} for submission"


def computerNumber():
    ''' This function SHOULD generate a random number in the 1-100 range 
    (inclusive), and return it'''
    return random.randint(1,100)
    # TODO: when testing this function, it can fails sometimes. Investigate why 
    # and fix the code to match the documentation of what the function should do.


def makeSmartGuess(lowest, highest, lastFeedback=None):
    ''' This function should make a smart guess within the given range and return it'''
    # TODO: code here AFTER making some tests (use Test-Driven Development)
    # lastFeedback is accepted but not used here: gameLoop() already narrows
    guess = (lowest + highest) // 2
    return guess
    

def provideFeedback(guess, theNum):
    ''' This function should take as inputs the guess and the number from the computer,
    and will provide feedback as to whether the guess is too low, too high, or correct. 
    It should print the guess and feedback and then return the feedback'''
    # TODO: code here AFTER making some tests (use Test-Driven Development)
    if guess < theNum:
        feedback = "too low"
    elif guess > theNum:
        feedback = "too high"
    else:
        feedback = "correct"
    print(guess, feedback)
    return feedback


def gameLoop():
    ''' This function handles the main game loop, repeatedly calling the makeSmartGuess() and
    provideFeedback() functions until the guess is correct. When the guess is finally correct,
    it will return the number of guesses it took to find the answer. '''
    # TODO: code here AFTER making some tests (use Test-Driven Development)
    target = computerNumber()
    lowest, highest = 1, 100
    feedback = None
    numGuesses = 0

    while True:
        guess = makeSmartGuess(lowest, highest, feedback)
        feedback = provideFeedback(guess, target)
        numGuesses += 1

        if feedback == "correct":
            return numGuesses
        elif feedback == "too low":
            lowest = guess + 1
        elif feedback == "too high":
            highest = guess - 1


###############################################################
# Here is where you will write your basic test case functions
# Do NOT test provideFeedback here. That must go in the structured test further below
# If you wish, you can make all your tests here int the structured form.  

def testGeneratedNumber():
    for i in range(1000):
        aNum = computerNumber() ## calls the function we are testing
        # now verify that the function did as we expected:
        assert 1 <= aNum and aNum <= 100, "The computer generated a number out of valid range"
        # Often, we want to have very simple and direct tests
        # To improve the testing above, we might be do this instead:
        assert type(aNum) == type(1), "computerNumber() didn't generate an integer!"
        assert 1 <= aNum, "The computer generated a number that's too low"
        assert aNum <= 100, "The computer generated a number that's too high"
    # Why no output or return? Because we want fails to be loud, success is silent

### TODO: ADD MORE TEST FUNCTIONS HERE
# to fully test a function, we often need more than one test.  

def testMakeSmartGuessRange():
    for i in range(1000):
        low = random.randint(1, 50)
        high = random.randint(low, 100)
        guess = makeSmartGuess(low, high)
        assert low <= guess <= high, "makeSmartGuess() returned a value outside the given range"


def  testMakeSmartGuessMidpoint():
    for i in range(1000):
        low = random.randint(1, 50)
        high = random.randint(low, 100)
        guess = makeSmartGuess(low, high)
        expected_guess = (low + high) // 2
        assert guess == expected_guess, f"makeSmartGuess() returned {guess}, but expected {expected_guess}"

def testMakeSmartGuessInteger():
    for i in range(1000):
        low = random.randint(1, 50)
        high = random.randint(low, 100)
        guess = makeSmartGuess(low, high)
        assert type(guess) == int, "makeSmartGuess() didn't return an integer"


def  testFeedbackRange():
    target = random.randint(51, 100) 
    lowest,highest=1,100

    guess1 = makeSmartGuess(lowest, highest)
    feedback1 = provideFeedback(guess1, target)
    assert feedback1 == "too low", "Setup assumption failed: expected first guess to be too low"

    #raise the lower bound
    lowest = guess1 + 1
    guess2 = makeSmartGuess(lowest, highest, feedback1)
    assert lowest <= guess2 <= highest, "The narrowed range was not respected by the next guess"
    assert guess2 > guess1, "The next guess did not move up after 'too low' feedback"

def GameLoopEnd():
    num_guesses=gameLoop()
    assert type(num_guesses) == type(1), "gameLoop() didn't return an integer guess count"
    assert num_guesses >= 1, "gameLoop() reported an invalid (nonpositive) number of guesses"
    # binary search at least log2(n) tries
    assert num_guesses <= 7, "gameLoop() took more guesses than a smart binary search should need"

###############################################################
# For large projects, structured testing like this is *necessary*

import unittest

class TestGuessMyNumber(unittest.TestCase):
    
    # Here is where you will write your structured tests for the provideFeedback function
    def testDemonstrationOfUnittesting(self):
        self.assertEqual(1, 1) # Placeholder example assertion which passes
        hasMessage = True
        self.assertTrue(hasMessage, "Here's the message if this test fails")
        # Actual tests should call a function, then assert/verify the results 
        # and changes from that function are what you expected
        
        # TODO: comment these out, they just demonstrate what test failures look like:
        #self.assertEqual(3, 7, "Demonstration purposes: test fails because 3 != 7")
        #self.fail("Here's a way to immediately fail a test!")
        
    # Here is where you will write your structured tests:
    def testProvideFeedbackLow(self):
        # TODO: make this test!
        result=provideFeedback(10,50)
        self.assertEqual(result, "too low")
        

    def testProvideFeedbackHigh(self):
        # TODO: make this test!
        result=provideFeedback(90,50)
        self.assertEqual(result, "too high")

    ### TODO: CREATE MORE TESTS HERE

    def testProvideFeedbackCorrect(self):
        result = provideFeedback(50, 50)
        self.assertEqual(result, "correct")

    def testMakeSmartGuessRangeStructured(self):
        for i in range(1000):
            low = random.randint(1, 50)
            high = random.randint(low, 100)
            guess = makeSmartGuess(low, high)
            self.assertTrue(low <= guess <= high,
                             "makeSmartGuess() returned a value outside the given range")

    def testMakeSmartGuessMidpointStructured(self):
        for i in range(1000):
            low = random.randint(1, 50)
            high = random.randint(low, 100)
            guess = makeSmartGuess(low, high)
            expected_guess = (low + high) // 2
            self.assertEqual(guess, expected_guess,
                              f"makeSmartGuess() returned {guess}, but expected {expected_guess}")

    def testMakeSmartGuessIntegerStructured(self):
        for i in range(1000):
            low = random.randint(1, 50)
            high = random.randint(low, 100)
            guess = makeSmartGuess(low, high)
            self.assertIsInstance(guess, int, "makeSmartGuess() didn't return an integer")

    def testFeedbackRangeStructured(self):
        target = random.randint(51, 100)
        lowest, highest = 1, 100

        guess1 = makeSmartGuess(lowest, highest)
        feedback1 = provideFeedback(guess1, target)
        self.assertEqual(feedback1, "too low",
                          "Setup assumption failed: expected first guess to be too low")

        #raise the lower bound
        lowest = guess1 + 1
        guess2 = makeSmartGuess(lowest, highest, feedback1)
        self.assertTrue(lowest <= guess2 <= highest,
                         "The narrowed range was not respected by the next guess")
        self.assertGreater(guess2, guess1,
                            "The next guess did not move up after 'too low' feedback")

    def testGameLoopEndStructured(self):
        num_guesses = gameLoop()
        self.assertIsInstance(num_guesses, int, "gameLoop() didn't return an integer guess count")
        self.assertGreaterEqual(num_guesses, 1,
                                 "gameLoop() reported an invalid (nonpositive) number of guesses")
        # binary search at least log2(n) tries
        self.assertLessEqual(num_guesses, 7,
                              "gameLoop() took more guesses than a smart binary search should need")

    def aUtilityFunction(self, param):
        # This is a utility function which unittest.main() will NOT run automatically.
        # Your test functions could still use it though:  self.aUtilityFunction("hello")
        print("Utility function runs! Has parameter:", param)

###############################################################    

def main():
    print("Started basic testing...")
    # Call each one of your basic test functions first:
    testGeneratedNumber()
    # TODO: CALL MORE TEST FUNCTIONS
    testMakeSmartGuessRange()
    testMakeSmartGuessMidpoint()
    testMakeSmartGuessInteger()
    testFeedbackRange()
    GameLoopEnd()
    print("Basic tests done and passed!")
    # Remember, if a basic assertion fails, no other tests will run.  
    # But for structured tests, every test is run and made into one big report
    
    print("Beginning structured tests...", flush=True)
    # This runs all methods in the TestGuessMyNumber that are named 'test...':
    unittest.main()
    print("Structured tests done (see report)")


if __name__ == "__main__":
    main()                     