##  program name:
##  "examples_pseudo_random_17_bit.py"
##  language: Python 3
##  by Michael John Hawks
##  2020-05-09
###################################
##  Example routines that use
##  17 bit binary pseudo-random
##  integers
###################################
##  These routines use the
##  LINEAR FEEDBACK SHIFT REGISTER
##  (LFSR) method.
##
##  Wikipedia has articles listing
##  various implementations of
##  LFSR. See:
##
##  Linear-feedback shift register
##  From Wikipedia,
##   the free encyclopedia
##    (as of 2020/04/30)
##
##  The following table lists the
##  "tap points" for various n bit
##  binary registers where the
##  highest-order bit is bit 0 and
##  the lowest-order bit is
##  bit n-1.
##
##  For instance, if the number in
##  a 17 bit binary register is
##  represented by the string
##  "00000000000000001"
##  POSITION 0 (the leftmost or
##  highest-order bit) is "0" and
##  POSITION 16 (the rightmost or
##  lowest-order bit) is "1."
###################################
##  LSFR
##  Linear-feedback shift registers
##
##  Bits:  Tap Points:
##  -----  -----------
##   2     0,  1
##   3     0,  1
##   4     0,  1
##   5     0.  2
##   6     0,  1
##   7     0,  1
##   8     0,  2,  3,  4
##   9     0,  4
##  10     0,  3
##  11     0,  2
##  12     0,  1,  2,  8
##  13     0,  1,  2,  5
##  14     0,  1,  2, 12
##  15     0,  1
##  16     0,  1,  3,  8
##  17     0,  3
##  18     0,  7
##  19     0,  1,  2,  5
##  20     0,  3
##  21     0,  2
##  22     0,  1
##  23     0,  5
##  24     0,  1,  2,  7
##  25     0,  3
##  26     0, 20, 24, 25
##  27     0, 22, 25, 26
##  28     0,  3
##  29     0,  2
##  30     0, 24, 26, 29
##  31     0,  3
##  32     0, 10, 30, 31
##  33     0, 13
##  34     0,  7, 32, 33
##  35     0,  2
##  36     0, 11
##  37     0, 32, 33, 34, 35, 36
##  38     0, 32, 33, 37
##  39     0,  4
##  40     0,  2, 19, 21
##  41     0,  3
##  42     0,  1, 22, 23
##  43     0,  1,  5,  6
##  44     0,  1, 26, 27
##  45     0,  1,  3,  4
##  46     0,  1, 20, 21
##  47     0,  5
##  48     0,  1, 27, 28
##  49     0,  9
##  50     0,  1, 26, 27
##  51     0,  1, 15, 16
##  52     0,  3
##  53     0,  1, 15, 16
##  54     0,  1, 36, 37
##  55     0, 24
##  56     0,  1, 21, 22
##  57     0,  7
##  58     0, 19
##  59     0,  1, 21, 22
##  60     0,  1
##  61     0,  1, 15, 16
##  62     0,  1, 56, 57
##  63     0,  1
##  64     0,  1,  3,  4
##  65     0, 18
###################################
##  In this implementation we use a
##  17 bit register (bits numbered
##  0 through 16) with tap points
##  at 0 and 3 with the
##  register shifting one bit to
##  the left (toward the higher
##  bits) with each iteration. The
##  leftmost bit (highest order bit)
##  is shifted out and discarded.
##
##  The idea here is that the bit
##  that is shifted into the low
##  end of the register (from the
##  right) is "0" if the parity of
##  the tapped bits is even and "1"
##  if the parity of the tapped
##  bits is odd.
##
##  The "seed" is the original
##  17 bit number loaded into the
##  register (in our simple case
##  the seed is "00000000000000001").
##  The seed must be non-zero.
##  NOTHING WILL HAPPEN IF THE
##  SEED IS ZERO!
##
##  This implementation generates
##  integers from 1 through 131071.
##  Zero never occurs. Each integer
##  occurs once and only once in
##  the sequence. After 131071
##  cycles the sequence repeats
##  in exactly the same order.
####################################
##  The BIG QUESTION that needs to
##  be asked is why implement the
##  LFSR method when the Python-3
##  language already has a good
##  "random" function which is based
##  on the superior "Mersenne
##  Twister" algorithm?
##
##  The answer is obvious! It's...
##  um... gee, I don't know.
##
##  Advantages of LFSR are that it
##  couldn't be simpler to implement
##  from scratch and it's probably
##  just fine for parlour games.
##
##  The biggest reason, of course,
##  is "because it is there."
####################################

######################################################
######################################################
##                                                  ##
##                F U N C T I O N S                 ##
##                                                  ##
######################################################
######################################################

def fnc_convert_binary_string_to_integer(str_binary):
    ##  Convert a binary string image to an integer.
    ##  Python-3 does this easily!

    int_result = int(str_binary,2) ## convert binary string image to integer

    return int_result  ##  Return integer and terminate function.

######################################################
######################################################

def fnc_next_random_binary_17_bit_string(str_seed):

    ##  This function accepts as an argument a 17 character string of zeros
    ##    and ones representing the 17 bit binary "seed."
    ##  Using the LFSR method of generating the next binary number in
    ##    the sequence, the parity of positions 0 and 3 is
    ##    determined. When parity is even then the new bit represented by
    ##    "str_x" will be zero else the parity is odd and the new bit
    ##    will be one.
    ##  Determining the parity is fairly easy and there are probably lots of
    ##    ways to do it. Here we compare positions 0 and 3. If they are not
    ##    equal then parity is odd and "str_x" will be "1" else parity is
    ##    even and "str_x" will be "0."
    ##  Then "shift" the bit represented by "str_x" into the right side of
    ##    the seed string and discard the leftmost position. This is now the
    ##    binary image of the next pseudo-random number in the sequence AND
    ##    becomes the new seed for the next time around.

    if str_seed[0] != str_seed[3]:  ##  Find parity of positions 0 and 3
        str_x = "1"                 ##  If not equal, parity is odd or "1"
    else:                           ##    ELSE
        str_x = "0"                 ##  If equal, parity is even or "0"

    str_result = str_seed[1:17] + str_x  ##  "Shift" parity bit into the right
                                         ##    side of the string and discard
                                         ##    the leftmost bit.

    return str_result  ##  Return this result. This string represents as binary
                       ##    the next pseudo-random integer in the sequence.

######################################################
######################################################

def fnc_convert_integer_to_binary_string_image(int_n):
    ##  This function converts an integer into a string of
    ##  0's and 1's representing a binary number.
    ##
    ##  The string will always be 17 characters long.
    ##
    ##  If the integer is larger than what 17 characters can represent,
    ##  this function stops at 17 characters and calls it good.

    str_binary_image = ""  ##  Start with an empty sring to build on

    int_i = 0  ##  Initialize loop

    while int_i < 17:  ##  17 times through loop required

        int_x = int_n % 2  ## (int_n % 2) equals either 0 or 1
                           ##  which is the next higher bit in the sequence
                           ##  being built

        int_n = int_n // 2  ##  Integer division by 2

        if int_x == 0:  ##  Convert int_x to a character
            str_x = "0"
        else:
            str_x = "1"

        ##  Attach the new character to the LEFT side of the string
        ##  being constructed
        str_binary_image = str_x + str_binary_image

        int_i+=1  ##  Increment the loop variable

    return str_binary_image  ##  Return the string of 17 characters
                             ##  and terminate the loop

######################################################
######################################################

def fnc_pseudo_random_1_thru_n(int_n,str_seed):
    ##  This function returns a pseudo-random integer in the range
    ##  1 through n (as long as "n" doesn't exceed (2**n)-1 or 131071).
    ##  Each returned integer has an equal opportunity to appear.
    ##################################################
    ##  IMPORTANT NOTE: This function DOES NOT error check to make
    ##  sure the passed value for "n" is within the range of 1 through
    ##  131071. A value will be returned but it won't be what is desired.

    int_trial = 131071  ##  Initialize the loop by starting with the
                        ##  largest allowed integer which is (2**n)-1.

    ##  It is necessary that the possible returned integers all have
    ##  an equal opportunity to show up. This is only possible when
    ##  the largest possible value generated by a given pseudo-random
    ##  generator is an exact multiple of "n".
    ##
    ##  The largest possible integer generated by our 17 bit LFSR algorithm
    ##  is 131071 but there's a really good chance that 131071 is NOT an
    ##  exact multiple of "n". So we'll subtract 131071 modulo n from 131071
    ##  and now we have a number that IS an exact multiple of "n".
    ##
    ##  What we will do is let the pseudo-random generator spit out integers
    ##  until it gives us one at or below this threshold. Then add one to
    ##  that integer modulo "n" and THAT will be the result we desire.

    ##  Calculate maximum allowed integer as described above.
    int_max = 131071 - (131071 % int_n)

    while int_trial > int_max: ##  int_max is the largest allowed integer

        ##  Get the string binary image of a pseudo-random integer
        str_new = fnc_next_random_binary_17_bit_string(str_seed)

        ##  Convert the string to an integer. This integer either triggers
        ##  or terminates the loop.
        int_trial = fnc_convert_binary_string_to_integer(str_new)

        ##  Be sure to update the seed!!!
        str_seed = str_new

    ##  Once a value within range is found and the loop is terminated,
    ##  add 1 to that value modulo "n" to yield the result desired.
    int_result = 1 + (int_trial % int_n)

    return int_result,str_seed  ##  Return the desired value and
                                ##  the updated seed then terminate
                                ##  the function.

######################################################
######################################################

def fnc_display_current_seed(str_seed):
    ##  This function is called several times to inform the user
    ##  what the value of the current seed is (just FYI for the user)

    int_seed = fnc_convert_binary_string_to_integer(str_seed)
        ##  The only reason we need integer "seed" is so we can
        ##  display it as an integer in the message that follows.

    print("*******************************************************")
    print("Current SEED: ",str_seed," = ",int_seed)
    print("*******************************************************")

    return  ##  Terminate the funtion

######################################################
######################################################

def fnc_shuffle(lst_card_deck,str_seed):
    ##  This function returns a list representing a shuffled deck
    ##  of 52 playing cards given a list representing a sequential,
    ##  unshuffled deck.

    lst_shuffled_deck = ["dummy"]  ##  The initial item in the new
                                   ##  list is a "dummy" bookend.

    int_n = 52  ##  Initialize loop (52 cards in a playing card deck)

    while int_n > 0:  ##  While there are still items left to shuffle:

        ##  Get a pseudo-random index integer in the range 1 through int_n
        int_index,str_seed = fnc_pseudo_random_1_thru_n(int_n,str_seed)

        ##  Append the indexed card to the new deck being constructed
        lst_shuffled_deck += [lst_card_deck[int_index]]

        ##  Pluck out this list item and join the ends of the list
        ##    back together again
        lst_card_deck = lst_card_deck[0:int_index] + lst_card_deck[int_index+1:]

        int_n-=1  ##  Decrement number of cards left in the old deck and
                  ##    try to re-enter the loop

    ##  At this point 52 cards have been appended to the new list and all
    ##    that is left to do is to append a "dummy" bookend to the end of
    ##    the list
    lst_shuffled_deck += ["dummy"]

    return lst_shuffled_deck,str_seed  ##  Return the freshly shuffed deck of
                                       ##  cards and terminate the function

######################################################
######################################################

def fnc_get_card_deck():
    ##  This function builds a list of 52 sequential cards in
    ##  unshuffled order with "dummy" bookends on each end of
    ##  the list. Therefore the completed list has 54 items
    ##  numbered 0 through 53 ([0] and [53] are the dummy bookends)
    ##  with the items representing cards numbered 1 through 52.

    lst_card_deck = ["dummy"]  ##  The initial item in the new
                               ##  list is a "dummy" bookend.
    int_n = 0  ##  Initialize loop
    while int_n < 52:  ##  52 cards in a deck
        int_suit = int_n // 13  ##  4 suits with 13 cards per suit
        if int_suit == 0:
            str_suit = " Spades"
        elif int_suit == 1:
            str_suit = " Clubs"
        elif int_suit == 2:
            str_suit = " Diamonds"
        else:  ##  int_suit == 3:
            str_suit = " Hearts"

        int_value = 1 + (int_n % 13)  ##  Obtain the face value of the card

        if int_value == 1:
            str_value = " A"
        elif int_value == 10:  ##  Special consideration for"10" because
            str_value = "10"   ##  because it is two digits long
        elif int_value == 11:
            str_value = " J"
        elif int_value == 12:
            str_value = " Q"
        elif int_value == 13:
            str_value = " K"
        else:
            str_value = " " + str(int_value)

        str_card = str_value + str_suit  ##  Construct item by appending
                                         ##  the suit to the face value

        lst_card_deck += [str_card]  ##  Append the new card to the growing list
        int_n+=1  ##  Update value to try loop again and construct next card

    lst_card_deck += ["dummy"]  ##  Append a "dummy" entry to the end of the
                                ##  list as a bookend. Later this makes it
                                ##  easier (for me, anyway) to chop the list
                                ##  up and join the ends back together when
                                ##  the cards are shuffled.

    return lst_card_deck  ##  Return the freshly constructed deck and
                          ##  terminate the function

######################################################
######################################################

def fnc_deal_poker_hands(str_seed):
    ##  This is a menu option that allows the user to simulate
    ##  dealing 5 card POKER hands from a shuffled deck of 52 cards
    ##################################################
    ##  Furthur observations for discussion:
    ##
    ##  This programmer is certain that this LFSR algorithm is
    ##  not robust enough to generate every possible combination
    ##  of cards in a freshly shuffled deck (especially since
    ##  a 17 bit binary register can generate only (2**n)-1
    ##  or 131071 states).
    ##
    ##  THIS MIGHT MATTER!!!
    ##
    ##  For instance--by using my meager probability skills--I propose
    ##  that the actual chance of the top five cards in a REAL freshly
    ##  shuffled deck yeilding a ROYAL FLUSH is 1 out of 649740. Is
    ##  there enough states in this algorithm to ensure that this will
    ##  ever happen?
    ##
    ##  After the first five cards are dealt there are forty-seven
    ##  cards left. This really complicates the probability of a
    ##  ROYAL FLUSH coming up in the remaining cards (the probability
    ##  likely gets better by my way of thinking but is still presumably
    ##  going to be rather small).
    ##
    ##  So, using this LFSR algorithm of 17 bits, is a ROYAL FLUSH likely
    ##  to come up at least once SOMEWHERE?!?
    ##################################################

    fnc_display_current_seed(str_seed)  ##  Display the current seed

    ##  Display info to the user:
    print("Deal Poker Hands with Playing Cards")
    print()
    print("Hit <ENTER> to deal next poker hand")
    print(" or enter anything else to quit.")

    ##  Build a card deck as a list of 52 cards in sequential order:
    lst_card_deck = fnc_get_card_deck()

    ##  Shuffle the cards:
    lst_shuffled_deck,str_seed = fnc_shuffle(lst_card_deck,str_seed)

    print()
    print("52 playing cards are shuffled.")

    ##  Set up the card dealing loop:
    int_remaining_cards = 52  ## Initially there are 52 cards in the deck
    str_input = input()  ##  The user enters something.

    while str_input == "":  ## <ENTER> (an empty string) keeps the loop going
        int_n = 5  ##  5 cards are to be dealt
        while int_n > 0:
            ##  Display the next card in the list
            print(lst_shuffled_deck[int_remaining_cards])

            int_n -= 1  ##  Update number of cards left to be dealt
            int_remaining_cards -= 1  ##  Update number of cards left in list

        ##  Check to see if there are enough cards to deal another hand
        if int_remaining_cards < 5:
            ##  If not, display message to user and reshuffle the cards
            print()
            print("Not enough cards to deal another hand.")
            print("Cards will be reshuffled.")
            ##  Shuffle the cards:
            lst_shuffled_deck,str_seed = fnc_shuffle(lst_card_deck,str_seed)
            int_remaining_cards = 52  ##  Reinitialize number of remaining cards

        str_input = input()  ## <ENTER> (an empty string) keeps the loop going

    return str_seed  ##  Return the updated "seed" string and
                     ##  terminate the function

######################################################
######################################################

def fnc_get_fresh_bingo_numbers():
    ##  This function returns a list of 75 consecutive BINGO numbers
    ##  as strings ("B-1", B-2", B-3", etc.) "bookended" on each end by a
    ##  "dummy" item (therefore there are actually 77 items in the list).
    ##  The BINGO numbers in this 77 item list are items 1 through 75.
    ##  The "dummy" bookends make it easier later to chop up the list
    ##  and rejoin it.

    lst_fresh_bingo_numbers = ["dummy"]  ## "dummy" starts the new list as
                                         ##  item 0 to serve as a "bookend"

    int_n = 1  ##  initialize the loop
    while int_n <= 75:  ##  Start the loop. Total BINGO numbers = 75

        ##  Fresh BINGO numbers are arranged in 5 groups of 15 each.
        ##  Group 0 = B
        ##  Group 1 = I
        ##  Group 2 = N
        ##  Group 3 = G
        ##  Group 4 = O

        ##  Find letter code:
        int_letter_code = (int_n -1) // 15

        ## Assign a BINGO letter to the item:
        if int_letter_code == 0:
            str_bingo_number = "B-"+str(int_n)
        elif int_letter_code == 1:
            str_bingo_number = "I-"+str(int_n)
        elif int_letter_code == 2:
            str_bingo_number = "N-"+str(int_n)
        elif int_letter_code == 3:
            str_bingo_number = "G-"+str(int_n)
        else: ## if int_letter_code == 4
            str_bingo_number = "O-"+str(int_n)

        ##  Add this BINGO item to the growing list:
        lst_fresh_bingo_numbers += [str_bingo_number]

        int_n+=1  ##  Update index number and try the loop again

    ##  Put a "dummy" item on the end of the list to serve as a "bookend":
    lst_fresh_bingo_numbers += ["dummy"]

    return lst_fresh_bingo_numbers  ## Return the list and terminate function

######################################################
######################################################

def fnc_bingo_caller_body(str_seed):
    ##  This function is the main body of the BINGO routine.
    ##
    ##  After displaying info to the user, this function builds
    ##  a list of 75 BINGO numbers ("B-1", "B-2", "B-3", etc.).
    ##
    ##  Next this function "randomly" draws an item from the list
    ##  based on how many items are currently in the list.
    ##
    ##  The list then needs to be updated by chopping out the item
    ##  that was selected and joining the front part and the
    ##  remaining part of the list back together again. Now the
    ##  list contains one less item than it did before.
    ##
    ##  In this way, all 75 BINGO numbers are eventually selected
    ##  with no repeats or until the BINGO numbers are refreshed again.

    fnc_display_current_seed(str_seed)  ##  Display the current seed

    ##  Info for the user:
    print("Call BINGO numbers")
    print()
    print("Hit <ENTER> to call next BINGO number")
    print(" or enter anything else to quit.")

    ##  Build a fresh list of 75 consecutive BINGO numbers:
    lst_working_bingo_numbers = fnc_get_fresh_bingo_numbers()

    ##  Set up loop that selects BINGO numbers:
    int_remaining_numbers = 75  ##  Initially there are 75 items

    str_input = input()  ##  User enters a string. A "null" string
                         ##  entered by the user (i.e. - merely hitting
                         ##  <ENTER>) signals the desire to draw another
                         ##  BINGO number.

    ##  BINGO number selection loop. Keep looping as long as user keeps
    ##  hitting <ENTER> --AND-- the list still contains valid items.
    while str_input == "" and int_remaining_numbers > 0:

        int_index,str_seed = fnc_pseudo_random_1_thru_n(int_remaining_numbers,str_seed)
        ##  The returned value "int_index" is a pseudo-random integer
        ##  in the range of 1 through the remaining items in the list.

        ##  Here the selected BINGO number is plucked from the list of
        ##  remaining BINGO entries
        str_chosen_bingo_number = lst_working_bingo_numbers[int_index]

        ##  This chops out the item that was selected and joins the front
        ##  part and the remaining part of the list back together again.
        lst_working_bingo_numbers = \
            lst_working_bingo_numbers[0:int_index] \
            + lst_working_bingo_numbers[int_index + 1:]

        ##  Display BINGO number and get user's input
        str_input = input(str_chosen_bingo_number+"    ")

        int_remaining_numbers -=1  ##  Update the number of remaining items

    ##  At this point the above selection loop has somehow been terminated.
    ##  Either the list ran out of BINGO numbers or the user decided to exit.

    ##  Display updated info to the user:
    print()
    if int_remaining_numbers == 0:
        print("All BINGO numbers have been selected.")

    return str_seed  ##  Return the updated "seed" string and
                     ##  terminate this function

    ##  Now control returns to the main BINGO loop
    ##  where the user can decide whether to start the BINGO process
    ##  over again or move on to something else.

######################################################
######################################################

def fnc_bingo_caller(str_seed):
    ##  This is a menu option that allows the user to simulate drawing
    ##  BINGO numbers from a "pot" initially containing 75 BINGO numbers.
    ##
    ##  This function sets up the user loop that keeps looping
    ##  as long as the user keeps entering a "null" string by merely
    ##  hitting <ENTER>.
    ##################################################
    ##  Furthur observation for discussion:
    ##  This programmer suspects that this LFSR algorithm is not
    ##  robust enough to generate every possible sequence of BINGO
    ##  numbers. But after all we are playing BINGO so WHO CARES?!?

    str_input = ""  ##  Give str_input a "null" initial value

    while str_input == "":  ##  Keep looping while string is "null"

        str_seed = fnc_bingo_caller_body(str_seed)  ##  call bingo caller body

        print("Hit <ENTER> to refresh the numbers and start over")
        print(" or enter anything else to quit.")

        str_input = input()  ##  Get user input.
                             ##  "Null" string means "keep looping"

    return str_seed  ##  Return the updated "seed" string and
                     ##  terminate the function

######################################################
######################################################

def fnc_display_die_image(int_result):
    ##  Given an integer 1 through 6, this function displays
    ##  a face of the rolled die.

    if int_result == 1:
        print("+++++++++")
        print("+       +")
        print("+   @   +   1")
        print("+       +")
        print("+++++++++")

    elif int_result == 2:
        print("+++++++++")
        print("+ @     +")
        print("+       +   2")
        print("+     @ +")
        print("+++++++++")

    elif int_result == 3:
        print("+++++++++")
        print("+ @     +")
        print("+   @   +   3")
        print("+     @ +")
        print("+++++++++")

    elif int_result == 4:
        print("+++++++++")
        print("+ @   @ +")
        print("+       +   4")
        print("+ @   @ +")
        print("+++++++++")

    elif int_result == 5:
        print("+++++++++")
        print("+ @   @ +")
        print("+   @   +   5")
        print("+ @   @ +")
        print("+++++++++")

    else:
        print("+++++++++")
        print("+ @   @ +")
        print("+ @   @ +   6")
        print("+ @   @ +")
        print("+++++++++")

######################################################
######################################################

def fnc_roll_die(str_seed):
    ##  This is a menu option that allows the user to simulate rollin a die

    fnc_display_current_seed(str_seed)  ##  Display the current seed

    ##  Info for the user:
    print("ROLL A DIE")
    print()
    print("Hit <ENTER> to continue rolling a die")
    print(" or enter anything else to quit.")

    int_n = 6  ##  There are 6 faces on the die.

    str_input = input()  ##  User enters a "null" string (i.e. merely
                         ##  hitting <ENTER>) to signal desire to
                         ##  roll the die. Any other response signals
                         ##  no desire to roll the die.

    while str_input == "":

        int_die_face,str_seed=fnc_pseudo_random_1_thru_n(int_n,str_seed)
        ## int_n = 6, so this function will return an integer 1 through 6
        ## plus the updated "seed" string

        fnc_display_die_image(int_die_face)
        ##  This function displays the die face

        str_input = input()  ##  Get user input.
                             ##  User enters a "null" string (i.e. merely
                             ##  hitting <ENTER>) to signal desire to
                             ##  roll the die. Any other response signals
                             ##  no desire to roll the die.

    return str_seed  ##  Return the updated "seed" string and
                     ##  terminate the function

######################################################
######################################################

def fnc_coin_toss(str_seed):
    ##  This is a menu option that allows the user to simulate coin tosses

    fnc_display_current_seed(str_seed)  ##  Display the current seed

    ##  Info for the user:
    print("COIN TOSS")
    print()
    print("Hit <ENTER> to continue flipping a coin")
    print(" or enter anything else to quit.")

    str_input = ""  ##  The loop ahead will be entered with "null" string input

    str_result = ""  ##  Once the loop gets going, the result will be
                     ##  either "Heads   " or " Tails  ".

    int_n = 2  ##  A coin has 2 sides.

    while str_input == "":  ##  As long as the user keeps entering a
                            ##  "null" string the loop will continue.

        str_input = input(str_result)  ##  Previous result is displayed as
                                       ##  the input prompt and then
                                       ##  the user enters something

        int_heads_or_tails,str_seed = fnc_pseudo_random_1_thru_n(int_n,str_seed)
            ##  When int_n ==2, this function returns one of
            ##  two possible values: 1 or 2

        if int_heads_or_tails == 1:
            str_result = "Heads   "
        else:  ##  int_heads_or_tails == 2
            str_result = " Tails  "

    return str_seed  ##  Return the updated "seed" string and
                     ##  terminate the function

######################################################
######################################################

def fnc_pseudo_random_integers(str_seed):
    ##  This is a menu option that allows the user to view
    ##  a sequence of pseudo-random integers

    fnc_display_current_seed(str_seed)  ##  Display the current seed

    ##  Info for the user:
    print("DISPLAY PSEUDO-RANDOM INTEGERS")
    print()
    print("Hit <ENTER> to display next pseudo-random integer")
    print(" or enter anything else to quit.")

    str_input = input() ##  In the loop that follows, "str_input" will be the
                        ##    user's response.

    while str_input == "":  ##  Enter the loop. As long as the user keeps
                            ##    hitting <ENTER>, "str_input" will be a null
                            ##    string and the loop will continue.

        ## Based on the string representing the binary image of
        ##   the "seed," find the new string representing the
        ##   binary image of the next pseudo-random integer
        ##   in the sequence:
        str_new = fnc_next_random_binary_17_bit_string(str_seed)

        ##  Convert the string representing the binary number
        ##    to an actual integer:
        int_new = fnc_convert_binary_string_to_integer(str_new)

        ##  Create the display string which will contain
        ##    the new binary string and the new integer:
        str_display = str_new + " = " + str(int_new)+"   "

        ##  The new binary number string becomes the next seed:
        str_seed = str_new

        ##  This line does double duty as it displays the results AND
        ##    accepts the user's response as "str_input."
        ##  As long as the user keeps hitting <ENTER>, "str_input" will
        ##    be a null string and the loop will continue. Any other
        ##    response will cause the loop to terminate.
        str_input = input(str_display)

    return str_seed

######################################################
######################################################

def fnc_select_seed():
    ##  This is a menu option that allows the user to
    ##  change the "seed" for the pseudo-random generator.

    import time  ##  The PYTHON "time" module is needed to find elapsed time
                 ##  if required later on.

    ##  Info displayed to user:
    print("*******************************************************")
    print("The SEED is an integer between 0 and 131072.")
    print()
    print("To select your own custom SEED enter an integer.")
    print(" (If selected integer is out of range it will be")
    print("  adjusted to be within range.)")
    print()
    print("To select a SEED based on elapsed time (fairly random!)")
    print("  merely hit <ENTER>.")

    int_seed = -1  ##  Enter the loop with a purposely invalid seed value.
    while int_seed <= 0:  ##  Keep looping as long as seed value is invalid.
        str_input = input()  ##  User offers an input string.

        if str_input == "":  ##  "null" string signals to use elapsed
                             ##  time as follows:
            int_seed = 1+(int(time.clock()*1000000) % 131071)
            ##  "time.clock" returns the number of seconds since the
            ##  clock became active represented as a float value.
            ##  This value is supposedly accurate down to a millionth
            ##  of a second. So we will multiply this value by one million,
            ##  convert it to an integer, find modulo 131071 (which yields
            ##  a value of 0 through 131070), then add 1. This gives us
            ##  a final value that is non-zero and within the required range.

        else:  ##  If the user actually enered something, try to convert
               ##  it into a valid integer:
            try:
                int_seed = 1+((int(str_input)-1) % 131071)
                ##  If "str_input" entered by the user does not represent
                ##  a valid integer, then "int(str_input)" will cause an
                ##  error that is trapped by the "except" clause which follows.
                ##  Otherwise the user's response will be FORCED into a valid
                ##  integer by subtracting 1, finding modulo 131071 (which
                ##  yields a value of 0 through 131070), then add 1. This
                ##  gives us a final value that is non-zero and within the
                ##  required range.
            except:
                int_seed = -1  ## error trapping yields an invalid value of -1

        if int_seed <= 0:
            print("Input was not valid. Please try again.")

    str_seed = fnc_convert_integer_to_binary_string_image(int_seed)
               ##  This function merely converts the integer into a
               ##  string image of the binary number equivalent.

    return str_seed  ##  Return the string representing the new "seed"
                     ##  in binary format and terminate the function.

######################################################
######################################################

def fnc_user_selects_menu_option(int_n):
    ##  Here the user can offer string input to select options 0 through int_n.
    ##  If "q" is offered as a response it will be interpreted as 0.

    int_pick = -1  ## This initial value is purposely invalid.

    while int_pick < 0:  ##  This is the start of the selection loop.
                         ##  Keep looping while responses are invalid.

        str_input = input()  ##  User offers input as a string.
                             ##  The user can respond with "0" or "q"
                             ##  as well as a string representing
                             ##  an integer.

        if str_input == "q":  ##  Responding with "q" is treated the
            int_pick = 0      ##  same as responding with "0"
        else:  ##  Try to convert the string offered by the user into an integer
            try:
                int_pick = int(str_input)  ## Convert user's string to ingeter
            except:
                int_pick = -1  ##  If conversion attempt fails,
                               ##   then int_pick = -1
        if int_pick > int_n:  ##  Does user's choice exceed upper range?
            int_pick = -1     ##  If not, this value of -1 will be
                              ##  recognized as an invalid choice.
        if int_pick < 0:  ##  An integer less than 0 means that the
                          ##  user's input was not valid.
            print("Input not valid. Please try again.")

    return int_pick  ##  Terminate function and return an integer 0 through int_n

######################################################
######################################################

def fnc_user_menu(str_old_seed):
    ##  This is the main menu where the user can decide how to proceed

    str_seed = str_old_seed
    fnc_display_current_seed(str_seed)
    print('Enter "q" or "0" to QUIT or')
    print("Select an option you would like to explore.")
    print()
    print(" 1.) Display Pseudo-Random Integers")
    print(" 2.) Coin Toss")
    print(" 3.) Roll a Die")
    print(" 4.) Call BINGO numbers")
    print(" 5.) Deal Poker hands")
    print(" 6.) Choose a different SEED")

    int_n = 6  ##  This is the number of valid options available from the menu
    int_option = fnc_user_selects_menu_option(int_n)
    ##  User selects option.
    ##  If user chooses to quit, 0 will be returned.

    bool_keep_looping = True
        ##  "bool_keep_looping" is the bool value that will be returned by
        ##  this function to determine if the user wants to keep looping
        ##  through the menu
    if int_option == 1:  ##  Choice #1: display pseudo-random integers
        str_seed = fnc_pseudo_random_integers(str_seed)
    elif int_option == 2:  ##  Choice #2: simulate coin tosses
        str_seed = fnc_coin_toss(str_seed)
    elif int_option == 3:  ##  Choice #3: simulate rolling a single 6 faced die
        str_seed =  fnc_roll_die(str_seed)
    elif int_option == 4:  ##  Choice #4: simulate drawing 75 bingo numbers
                           ##  from a pot
        str_seed =  fnc_bingo_caller(str_seed)
    elif int_option == 5:  ##  Simulate dealing 5 playing cards from a 52 card deck
        str_seed = fnc_deal_poker_hands(str_seed)
    elif int_option == 6:  ##  Offer the user the ability to change the "seed"
        str_seed = fnc_select_seed()
    else:  ##  This occurs when int_option == 0
        bool_keep_looping = False  ##  USER wishes to QUIT

    return bool_keep_looping,str_seed

######################################################
######################################################

def fnc_display_farewell_to_user():
    print("*******************************************************")
    print("Goodbye!")

######################################################
######################################################

def fnc_user_interaction_loop():
    ##  The purpose of this function is to define an
    ##  an initial "seed" for the pseudo-random
    ##  functions that follow and also to keep looping
    ##  through the user menu until the user decides
    ##  to quit.

    bool_keep_looping = True  ##  Set up "keep looping" condition.

    str_seed = "00000000000000001"  ##  Set up an initial "seed".
    ##  NOTE: This "seed" is essential to ALL the functions that
    ##  require pseudo-randomness so the string representing the
    ##  seed MUST be passed to, updated by, and returned by MOST
    ##  of the functions defined above!

    while bool_keep_looping == True:
        ##  keep looping as long as condition is "True"

        bool_keep_looping,str_seed = fnc_user_menu(str_seed)
                                 ##  user menu which allows user
                                 ##  to select an option

######################################################
######################################################

def fnc_display_greeting_to_user():
    print("*******************************************************")
    print("EXAMPLE ROUTINES USING PSEUDO-RANDOM INTEGERS")
    print("*******************************************************")
    print("These routines employ the")
    print("LINEAR FEEDBACK SHIFT REGISTER (LFSR)")
    print("method of generating pseudo-random integers")
    print("using a 17 character string of zeros and ones")
    print("to represent the integer as binary.")
    print()
    print("Using 17 bit binary integers the LFSR method")
    print("can generate all the integers from 1 through 131071")
    print("in a pseudo-random fashion (i.e. -- very difficult")
    print("to predict the next integer in the sequence).")
    print("Each integer appears once and only once throughout")
    print("the sequence at which point the sequence will")
    print("repeat itself.")
    print()
    print("THE SEED CAN NOT BE ZERO OR ELSE NOTHING WILL HAPPEN!!!")

######################################################
######################################################
##                                                  ##
##             M A I N   P R O G R A M              ##
##                                                  ##
######################################################
######################################################

def main():
    fnc_display_greeting_to_user()
    fnc_user_interaction_loop()
    fnc_display_farewell_to_user()

main()

######################################################
######################################################
##                                                  ##
##      T H A T ' S   A L L ,   F O L K S !         ##
##                                                  ##
######################################################
######################################################
