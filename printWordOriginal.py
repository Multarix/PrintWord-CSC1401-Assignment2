import re; # Import regex, because you didn't say I couldn't, was simply asked for a "validation plan".

# Fixing all the dumb shit from python, 1 line at a time
# true and false is more natural.
true = True;
false = False;

# A ternary function, given python doesn't have have a proper ternary operator
def ternary(condition: bool, trueResult: str, falseResult: str) -> str:
	"""
	Returns the result of the ternary operator
	"""
	if(condition):
		return trueResult;
	else:
		return falseResult;

# Sadly nothing I can really do about the fact python is lacking switch case
# Sooo we're stuck if ifing or if else if elseing (else is bad, stop using else)

# Toggle this to true to make the output easier to read
# (though it might actually make it harder if your console output doesn't support emojis)
readabilityMode = false;

# Variables that will be used throughout all the letter functions
eStr = ternary(readabilityMode, "⬛", " ");
fStr = ternary(readabilityMode, "⬜", "*");
deliminter = "\n";

# For the record... These function designs are fucking stupid.
# All the letter functions work on the same principle:
# 1. Create an array
# 2. Create a string
# 3. Check how long the array is
# 4. Check if array length can be found in specified sets
# 	4.1. Check if string length can be found in the specified set, if so, add the value of fStr otherwise add the value of eStr (Defined above).
# 5. Repeat steps 3 -> 4.1 until string length is equal to 7
# 6. Add the string to the array
# 7. Repeat steps 2-6 until the array length equals 7
# 8. Join together the array's values into a full letter string with a line break (\n)
# 9. Return the full letter string

# Function for the letter C
def letterC() -> str:
	"""
	Returns a string of the letter 'C'
	0'  ***  '
	1' *   * '
	2' *     '
	3' *     '
	4' *     '
	5' *   * '
	6'  ***  ' 
	  0123456
	"""
	letterArray = [];
	while(7 > len(letterArray)):
		lineString = "";
		while(7 > len(lineString)):
			arrayLength = len(letterArray);
			stringLength = len(lineString);

			# The first and last characters are always spaces
			if(stringLength in {0, 6}):
				lineString += eStr;
				continue;
			
			# Line 0 & 6
			if(arrayLength in {0, 6}):
				lineString += ternary((stringLength in {2, 3, 4}), fStr, eStr);
				continue;
			
			# Line 1 & 5
			if(arrayLength in {1, 5}):
				lineString += ternary((stringLength in {1, 5}), fStr, eStr);
				continue;

			# Line 2, 3 & 4
			if(arrayLength in {2, 3, 4}):
				lineString += ternary((stringLength in {1}), fStr, eStr);
				continue;

		letterArray.append(lineString);
		# End of while loop
	# End of while loop	

	return deliminter.join(letterArray);


# Function for the letter O
def letterO() -> str:
	"""
	Returns a string of the letter 'O'
	0'  ***  '
	1' *   * '
	2' *   * '
	3' *   * '
	4' *   * '
	5' *   * '
	6'  ***  ' 
	  0123456
	"""
	letterArray = [];
	while(7 > len(letterArray)):
		lineString = "";
		while(7 > len(lineString)):
			arrayLength = len(letterArray);
			stringLength = len(lineString);

			# The first and last characters are always spaces
			if(stringLength in {0, 6}):
				lineString += eStr;
				continue;
			
			# Line 0 & 6
			if(arrayLength in {0, 6}):
				lineString += ternary((stringLength in {2, 3, 4}), fStr, eStr);
				continue;
			
			# Line 1, 2, 3, 4 & 6
			if(arrayLength in {1, 2, 3, 4, 5}):
				lineString += ternary((stringLength in{1, 5}), fStr, eStr);
				continue;
		# End of while loop
		letterArray.append(lineString);
	# End of while loop	

	return deliminter.join(letterArray);


# Function for the letter L
def letterL() -> str:
	"""
	Returns a string of the letter 'L'
	0' *     '
	1' *     '
	2' *     '
	3' *     '
	4' *     '
	5' *     '
	6' ***** ' 
	  0123456
	"""
	letterArray = [];
	while(7 > len(letterArray)):
		lineString = "";
		while(7 > len(lineString)):
			arrayLength = len(letterArray);
			stringLength = len(lineString);

			# The first and last characters are always spaces
			if(stringLength in {0, 6}):
				lineString += eStr;
				continue;
			
			# Line 0, 1, 2, 3, 4 & 5
			if(arrayLength in {0, 1, 2, 3, 4, 5}):
				lineString += ternary((stringLength in {1}), fStr, eStr);
				continue;
			
			# Line 6
			if(arrayLength in {6}):
				lineString += ternary((stringLength in {1, 2, 3, 4, 5}), fStr, eStr);
				continue;

		letterArray.append(lineString);
		# End of while loop
	# End of while loop	

	return deliminter.join(letterArray);


# Function for the letter D
def letterD() -> str:
	"""
	Returns a string of the letter 'D'
	0' ***   '
	1' *  *  '
	2' *   * '
	3' *   * '
	4' *   * '
	5' *  *  '
	6' ***   ' 
	  0123456
	"""
	letterArray = [];
	while(7 > len(letterArray)):
		lineString = "";
		while(7 > len(lineString)):
			arrayLength = len(letterArray);
			stringLength = len(lineString);

			# The first and last characters are always spaces
			if(stringLength in {0, 6}):
				lineString += eStr;
				continue;
			
			# Line 0 & 6
			if(arrayLength in {0, 6}):
				lineString += ternary((stringLength in {1, 2, 3}), fStr, eStr);
				continue;
			
			# Line 1 & 5
			if(arrayLength in {1, 5}):
				lineString += ternary((stringLength in {1, 4}), fStr, eStr);
				continue;

			# Line 2, 3 & 4
			if(arrayLength in {2, 3, 4}):
				lineString += ternary((stringLength in {1, 5}), fStr, eStr);
				continue;

		letterArray.append(lineString);
		# End of while loop
	# End of while loop	

	return deliminter.join(letterArray);


# Function for the letter H
def letterH() -> str:
	"""
	Returns a string of the letter 'H'
	0' *   * '
	1' *   * '
	2' *   * '
	3' ***** '
	4' *   * '
	5' *   * '
	6' *   * ' 
	  0123456
	"""
	letterArray = [];
	while(7 > len(letterArray)):
		lineString = "";
		while(7 > len(lineString)):
			arrayLength = len(letterArray);
			stringLength = len(lineString);

			# The first and last characters are always spaces
			if(stringLength in {0, 6}):
				lineString += eStr;
				continue;
			
			# Line 0, 1, 2, 4, 5 & 6
			if(arrayLength in {0, 1, 2, 4, 5, 6}):
				lineString += ternary((stringLength in {1, 5}), fStr, eStr);
				continue;
			
			# Line 3
			if(arrayLength in {3}):
				lineString += ternary((stringLength in {1, 2, 3, 4, 5}), fStr, eStr);
				continue;

		letterArray.append(lineString);
		# End of while loop
	# End of while loop	

	return deliminter.join(letterArray);


# Function for the letter T
def letterT() -> str:
	"""
	Returns a string of the letter 'T'
	0' ***** '
	1'   *   '
	2'   *   '
	3'   *   '
	4'   *   '
	5'   *   '
	6'   *   '
	  0123456
	"""
	letterArray = [];
	while(7 > len(letterArray)):
		lineString = "";
		while(7 > len(lineString)):
			arrayLength = len(letterArray);
			stringLength = len(lineString);

			# The first and last characters are always spaces
			if(stringLength in {0, 6}):
				lineString += eStr;
				continue;
			
			# Line 0
			if(arrayLength in {0}):
				lineString += ternary((stringLength in {1, 2, 3, 4, 5}), fStr, eStr);
				continue;
			
			# Line 1, 2, 3, 4, 5 & 6
			if(arrayLength in {1, 2, 3, 4, 5, 6}):
				lineString += ternary((stringLength in {3}), fStr, eStr);
				continue;

		letterArray.append(lineString);
		# End of while loop
	# End of while loop	

	return deliminter.join(letterArray);


# Function to build each letter
def buildLetter(obj: dict, array: str) -> None:
	"""
	Gets each letter of the specified word,
	line by line and applys each line to
	the relevent line key in an object
	"""
	array = array.split(deliminter);
	lineNumber = 0;

	# Loop through the array,
	# concat each string into the key of the object
	string: str;
	for string in array:
		obj[lineNumber] += string;
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
		functionName = f"letter{letter.upper()}()";

		letterArray: str;
		letterArray = eval(functionName);  # Better than a bunch of if statements, but dangerous if used incorrectly

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

	# If the word contains any characters other than "C, O, L, D, H, T", go to next iteration
	# Was specified that this is case sensitive, so only capitals work - Using Regex to make life easy.
	match = re.search("[^COLDHT]", inputWord);
	if(match):
		print("Error: Input can only contain the letters: C, O, L, D, H & T");
		continue; # Reset
	
	# If the word is a single letter, simply print the relevant letter
	# Then go to the next iteration
	if(len(inputWord) == 1):
		functionName = f"letter{inputWord.upper()}()";
		
		letter: str;
		letter = eval(functionName); # Better than a bunch of if statements, but dangerous if used incorrectly

		print(letter);
		continue; # Reset
	
	# All checks passed, build the word
	word = buildWord(inputWord);
	print(word);
# End of while loop