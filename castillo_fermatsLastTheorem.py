a = input('Enter a positive integer for variable a: ')
b = input('Enter a positive integer for variable b: ')
c = input('Enter a positive integer for variable c: ')

if(int(a)>=0 and int(b)>=0 and int(c)>=0):

    for ctr in range(3,11):
        
        equation = ((int(a) ** ctr) + (int(b) ** ctr)) == int(c) ** ctr
        print("\nEquation: " + str(a) + "**" + str(ctr) + " + " + str(b) + "**" + str(ctr)+ " " +
                " = " + str(c) + "**" + str(ctr));
        
        if equation == True:
            print("Holy smokes! Fermat is wrong.\n")
        else:
            print("Nope, that's not gonna work.\n")

else:
    print("\nYOU HAVE ENTERED A NON-POSITIVE INTEGER!")