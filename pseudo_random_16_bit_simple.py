##  program name:
##  "pseudo_random_16_bit_simple.py"
##  language: Python 3
##  by Michael John Hawks
##  2020-05-07
###################################
##  Pseudo Random Number Generator
##  using the
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
##  a 16 bit binary register is
##  represented by the string
##  "0000000000000001"
##  POSITION 0 (the leftmost or
##  highest-order bit) is "0" and
##  POSITION 15 (the rightmost or
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
##  16 bit register (bits numbered
##  0 through 15) with tap points
##  at 0, 1, 3, and 8 with the
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
##  16 bit number loaded into the
##  register (in our simple case
##  the seed is "0000000000000001").
##  The seed must be non-zero.
##  NOTHING WILL HAPPEN IF THE
##  SEED IS ZERO!
##
##  This implementation generates
##  integers from 1 through 65535.
##  Zero never occurs. Each integer
##  occurs once and only once in
##  the sequence. After 65535
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

    int_result = int(str_binary,2) ## convert binary string image to integer
    return int_result

######################################################
######################################################

def fnc_next_random_binary_16_bit_string(str_seed):

    ##  This function accepts as an argument a 16 character string of zeros
    ##    and ones representing the 16 bit binary "seed."
    ##  Using the LFSR method of generating the next binary number in
    ##    the sequence, the parity of positions 0, 1, 3 and 8 is
    ##    determined. When parity is even then the new bit represented by
    ##    "str_x" will be zero else the parity is odd and the new bit
    ##    will be one.
    ##  Determining the parity is fairly easy and there are probably lots of
    ##    ways to do it. Here we start by comparing positions 0 and 1. If
    ##    they are not equal then parity is odd and "str_x" will be "1."
    ##    Next similarly compare "str_x" to position 3 and finally to
    ##    position 8.
    ##  Once parity of positions, 0, 1, 3 and 8 is determined, "shift" the
    ##    bit represented by "str_x" into the right side of the seed string
    ##    and discard the leftmost position. This is now the binary image of
    ##    the next pseudo-random number in the sequence AND becomes the new
    ##    seed for the next time around.

    if str_seed[0] != str_seed[1]:  ##  Find parity of positions 0 and 1
        str_x = "1"                 ##  If not equal, parity is odd or "1"
    else:                           ##    ELSE
        str_x = "0"                 ##  If equal, parity is even or "0"

    if str_seed[3] != str_x:        ##  Compare position 3 to previous result
        str_x = "1"                 ##  If not equal, parity is odd or "1"
    else:                           ##    ELSE
        str_x = "0"                 ##  If equal, parity is even or "0"

    if str_seed[8] != str_x:        ##  Compare position 8 to previous result
        str_x = "1"                 ##  If not equal, parity is odd or "1"
    else:                           ##    ELSE
        str_x = "0"                 ##  If equal, parity is even or "0"

    str_result = str_seed[1:16] + str_x  ##  "Shift" parity bit into the right
                                         ##    side of the string and discard
                                         ##    the leftmost bit.

    return str_result  ##  Return this result. This string represents as binary
                       ##    the next pseudo-random integer in the sequence.

######################################################
######################################################

def fnc_display_farewell_to_user():
    print()
    print("*******************************************************")
    print("Goodbye!")

######################################################
######################################################

def fnc_main_body():
    str_seed = "0000000000000001"  ##  This string represents the 16 bit
                                   ##    binary image of the initial seed

    str_input = ""  ##  In the loop that follows, "str_input" will be the
                    ##    user's response.

    while str_input == "":  ##  Enter the loop. As long as the user keeps
                            ##    hitting <ENTER>, "str_input" will be a null
                            ##    string and the loop will continue.

        ## Based on the string representing the binary image of
        ##   the "seed," find the new string representing the
        ##   binary image of the next pseudo-random integer
        ##   in the sequence:
        str_new = fnc_next_random_binary_16_bit_string(str_seed)

        ##  Convert the string representing the binary number
        ##    to an actual integer:
        int_new = fnc_convert_binary_string_to_integer(str_new)

        ##  Create the string to be displayed which will contain
        ##    the new binary string and the new integer:
        str_display = str_new + " " + str(int_new)+"   "

        ##  The new string becomes the next seed:
        str_seed = str_new

        ##  This line does double duty as it displays the results AND
        ##    accepts the user's response as "str_input."
        ##  As long as the user keeps hitting <ENTER>, "str_input" will
        ##    be a null string and the loop will continue. Any other
        ##    response will cause the loop to terminate.
        str_input = input(str_display)

######################################################
######################################################

def fnc_display_greeting_to_user():
    print("*******************************************************")
    print("This program uses the")
    print("LINEAR FEEDBACK SHIFT REGISTER (LFSR)")
    print("method of generating pseudo-random integers")
    print("using a 16 character string of zeros and ones")
    print("to represent the integer as binary.")
    print('The initial seed is "0000000000000001" --i.e.-- 1.')
    print()
    print("Using 16 bit binary integers the LFSR method")
    print("can generate all the integers from 1 through 65535")
    print("in a pseudo-random fashion (i.e. -- very difficult")
    print("to predict the next integer in the sequence).")
    print("Each integer appears once and only once throughout")
    print("the sequence at which point the sequence will")
    print("repeat itself.")
    print()
    print("THE SEED CAN NEVER ZERO OR ELSE NOTHING WILL HAPPEN!!!")
    print()
    print("Hit <ENTER> to find the next pseudo-random integer")
    print("in the sequence or enter anything else to quit.")
    print("*******************************************************")
    print()
######################################################
######################################################

def main():
    fnc_display_greeting_to_user()
    fnc_main_body()
    fnc_display_farewell_to_user()

######################################################
######################################################
##                                                  ##
##             M A I N   P R O G R A M              ##
##                                                  ##
######################################################
######################################################

main()

######################################################
######################################################
##                                                  ##
##      T H A T ' S   A L L ,   F O L K S !         ##
##                                                  ##
######################################################
######################################################
