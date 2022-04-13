import re; # Import regex, because you didn't say I couldn't, was simply asked for a "validation plan".

# Fixing all the dumb shit from python, 1 line at a time
# true and false is more natural.
true = True;
false = False;

# A ternary function, given python doesn't have have a proper ternary operator
def ternary(statement, a, b):
	"""
	If the statement is truthy, return a,
	If the statement is falsey, return b
	"""
	if(statement):
		return a;
	
	return b;

# Sadly nothing I can really do about the fact python is lacking switch case
# Sooo we're stuck if ifing or if else if elseing (else is bad, stop using else)

# Toggle this to true to make the output easier to read
# (though it might actually make it harder if your console output doesn't support emojis)
readabilityMode = true;

# Variables that will be used throughout all the letter functions
offStr = ternary(readabilityMode, "⬛", " ");
onStr = ternary(readabilityMode, "⬜", "*");
deliminter = "\n";

characters = {
	"A": [ 8, 28, 34, 34, 62, 34, 34],
	"B": [60, 34, 34, 60, 34, 34, 60],
	"C": [28, 34, 32, 32, 32, 34, 28],
	"D": [60, 18, 18, 18, 18, 18, 60],
	"E": [62, 32, 32, 56, 32, 32, 62],
	"F": [62, 32, 32, 56, 32, 32, 32],
	"G": [28, 34, 32, 32, 38, 34, 28],
	"H": [34, 34, 34, 62, 34, 34, 34],
	"I": [62,  8,  8,  8,  8,  8, 62],
	"J": [62,  4,  4,  4,  4, 36, 24],
	"K": [34, 36, 40, 48, 40, 36, 34],
	"L": [32, 32, 32, 32, 32, 32, 62],
	"M": [34, 54, 54, 42, 42, 34, 34],
	"N": [34, 34, 50, 42, 38, 34, 34],
	"O": [28, 34, 34, 34, 34, 34, 28],
	"P": [60, 34, 34, 60, 32, 32, 32],
	"Q": [28, 34, 34, 34, 42, 36, 26],
	"R": [60, 34, 34, 60, 40, 36, 34],
	"S": [28, 34, 32, 28,  2, 34, 28],
	"T": [62,  8,  8,  8,  8,  8,  8],
	"U": [34, 34, 34, 34, 34, 34, 28],
	"V": [34, 34, 34, 20, 20, 20,  8],
	"W": [34, 34, 34, 42, 42, 54, 34],
	"X": [34, 34, 20,  8, 20, 34, 34],
	"Y": [34, 34, 20,  8,  8,  8,  8],
	"Z": [62,  2,  4,  8, 16, 32, 62],
	" ": [ 0,  0,  0,  0,  0,  0,  0],
	"1": [ 8, 24,  8,  8,  8,  8, 28],
	"2": [28, 34,  2,  4,  8, 16, 62],
	"3": [62,  4,  8,  4,  2, 34, 28],
	"4": [ 4, 12, 20, 36, 62,  4,  4],
	"5": [62, 32, 60,  2,  2, 34, 28],
	"6": [12, 16, 32, 60, 34, 34, 28],
	"7": [62,  2,  4,  8, 16, 16, 16],
	"8": [28, 34, 34, 28, 34, 34, 28],
	"9": [28, 34, 34, 30,  2,  4, 24],
	"0": [28, 34, 38, 42, 50, 34, 28],
	"$": [ 8, 30, 40, 28, 10, 60,  8],
	"#": [20, 20, 62, 20, 62, 20, 20],
	"&": [24, 36, 40, 16, 42, 36, 26],
	"%": [48, 50,  4,  8, 16, 38,  6],
	"*": [62, 62, 62, 62, 62, 62, 62],
	"?": [28, 34,  2,  4,  8,  0,  8],
	"!": [ 8,  8,  8,  8,  0,  0,  8],
	"-": [ 0,  0,  0, 62,  0,  0,  0],
	"+": [ 0,  8,  8, 62,  8,  8,  0],
	"=": [ 0,  0, 62,  0, 62,  0,  0],
	":": [ 0, 24, 24,  0, 24, 24,  0],
	";": [ 0, 24, 24,  0, 24,  8, 16],
	"'": [24,  8, 16,  0,  0,  0,  0],
	",": [ 0,  0,  0,  0, 24,  8, 16],
	".": [ 0,  0,  0,  0,  0, 24, 24],
	"_": [ 0,  0,  0,  0,  0,  0, 62]
}	

# Function to build each letter
def buildLetter(obj: dict, array: list) -> None:
	"""
	Gets each letter of the specified word,
	line by line and applys each line to
	the relevent line key in an object
	"""

	lineNumber = 0;

	# Loop through the array,
	# concat each string into the key of the object
	num: int;
	for num in array:
		binary = bin(num).replace("0b", "");
		while(7 > len(binary)):
			binary = "0" + binary;

		binary = binary.replace("0", offStr).replace("1", onStr);

		obj[lineNumber] += binary;
		lineNumber += 1;


# Function to call each letter function in order, then add each objects property to a string
def buildWord(word: str) -> str:
	"""
	Finds the correct letter function to call and calls it,
	then calls the buildLetter function, before stringing
	(Pun intended) the entire word together.
	"""
	wordObject = { 0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "" };
	# For each letter in the word, find the appropriate function
	letter: str;
	for letter in word:
		letterArray = characters[letter.upper()];
		buildLetter(wordObject, letterArray); # Taking advantage of objects being a memory reference

	return f"{wordObject[0]}\n{wordObject[1]}\n{wordObject[2]}\n{wordObject[3]}\n{wordObject[4]}\n{wordObject[5]}\n{wordObject[6]}";


 # While(true) is considered bad, recursion would probably have been better
 # Buuuuut we could possibly run into a max recursion depth limit
while(true):
	"""
	Asks the user for an input word, then checks it against several conditions.
	If the input fails any of the checks, an error is printed and this function is called again.
	If the input passes all the checks, builds the word, then calls this function again.
	If the word is 'end', exits the function entirely.
	"""
	inputWord = input("Please enter a word (Type \"end\" to exit): ");

	# If the input was empty, go to next iteration
	if(len(inputWord) == 0):
		print("Error: Input was empty");
		continue; # Reset

	# If the input word is end, break
	# Specified to be case insensitive
	if(inputWord.lower() == "end"):
		break; # End

	# If the word contains any characters other than "those specified", go to next iteration
	# Was specified that this is case sensitive, so only capitals work - Using Regex to make life easy.
	match = re.search("[^A-Za-z0-9?!#$%&*:;'+=_ ,.\-]", inputWord);
	if(match):
		print("Error: Input can only contain the characters A-Z");
		continue; # Reset
		
	# All checks passed, build the word
	word = buildWord(inputWord);
	print(word);
# End of while loop