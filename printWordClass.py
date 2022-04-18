import re; # Import regex, because you didn't say I couldn't

# Capital letter bools is a dumb implimentation
true = True; # True to true
false = False; # False to false

# Good code doesn't always need to be commented, bad/ hard to read code should always be commented.
# But the requirements said to comment to explain things. So here we are with an overcommented file
# Mostly because the assignment is fairly vague on commenting requirements

# The relevant functions also have an underscore in front to show they're used internally, consistant with python proffesional naming standards.

# Ternary function
def _ternary(condition: bool, trueResult: any, falseResult: any) -> any:
	"""
	Returns the result of the Ternary operator
	Seeing as python doesn't have one, it was best to implement a version of it myself
	"""
	if(condition):
		return trueResult;
	else:
		return falseResult;

# Using a class helps for dynamically calling whatever letter function we want instead of checking for any specific letter using a bunch of if statements.
# It also helps for the future if we want to add more letters, or potentially symbols.
class GetLetterString:
	"""
	Class for creating letters & words.
	Does all the main work, also written as a class so that it can be imported and used in other files.
	"""
	# __Init__ sets up the class
	def __init__(this, word: str, fStr: str = "*", eStr: str = " ",  delimiter: str = "\n") -> None:
		this.word = word;
		this.fStr = fStr;
		this.eStr = eStr;
		this.delimiter = delimiter;

		# If the word length is 1, then it's a single letter
		if(len(word) == 1):
			this.singleLetter = true;
		else:
			this.singleLetter = false;


	# All the letter functions work on the same principle:
	# 1. Create an array
	# 2. Create a string
	# 3. Check how long the array is
	# 4. Check if array length can be found in specified sets
	# 	4.1. Check if string length can be found in the specified set, if so, add the value of "this.fStr" otherwise add the value of "this.eStr" (Defined above).
	# 5. Repeat steps 3 -> 4.1 until string length is equal to 7
	# 6. Add the string to the array
	# 7. Repeat steps 2-6 until the array length equals 7
	# 8. Join together the array's values into a full letter string with a line break (\n)
	# 9. Return the full letter string

	# In short, they build each letter character by character, line by line.

	# Function for the letter C
	def _C(this) -> str:
		"""
		Returns a string of the letter 'C'
		0'  ***  '
		1' *   * '
		2' *     '
		3' *     '
		4' *     '
		5' *   * '
		6'  ***  ' 
		x 0123456
		"""
		letterArray = [];
		# First loop handles what "line" we're on
		while(7 > len(letterArray)):
			lineString = "";

			# Second loop handles what "column" we're on
			while(7 > len(lineString)):
				arrayLength = len(letterArray);
				stringLength = len(lineString);

				# The first and last characters are always spaces
				if(stringLength in {0, 6}):
					lineString += this.eStr;
					continue;
				
				# Line 0 & 6
				if(arrayLength in {0, 6}):
					lineString += _ternary((stringLength in {2, 3, 4}), this.fStr, this.eStr);
					continue;
				
				# Line 1 & 5
				if(arrayLength in {1, 5}):
					lineString += _ternary((stringLength in {1, 5}), this.fStr, this.eStr);
					continue;

				# Line 2, 3 & 4
				if(arrayLength in {2, 3, 4}):
					lineString += _ternary((stringLength in {1}), this.fStr, this.eStr);
					continue;

			# End of while loop
			letterArray.append(lineString);

		# End of while loop	
		return this.delimiter.join(letterArray);


	# Function for the letter O
	def _O(this) -> str:
		"""
		Returns a string of the letter 'O'
		0'  ***  '
		1' *   * '
		2' *   * '
		3' *   * '
		4' *   * '
		5' *   * '
		6'  ***  ' 
		x 0123456
		"""
		letterArray = [];
		# First loop handles what "line" we're on
		while(7 > len(letterArray)):
			lineString = "";

			# Second loop handles what "column" we're on
			while(7 > len(lineString)):
				arrayLength = len(letterArray);
				stringLength = len(lineString);

				# The first and last characters are always spaces
				if(stringLength in {0, 6}):
					lineString += this.eStr;
					continue;
				
				# Line 0 & 6
				if(arrayLength in {0, 6}):
					lineString += _ternary((stringLength in {2, 3, 4}), this.fStr, this.eStr);
					continue;
				
				# Line 1, 2, 3, 4 & 6
				if(arrayLength in {1, 2, 3, 4, 5}):
					lineString += _ternary((stringLength in{1, 5}), this.fStr, this.eStr);
					continue;

			# End of while loop
			letterArray.append(lineString);

		# End of while loop	
		return this.delimiter.join(letterArray);


	# Function for the letter L
	def _L(this) -> str:
		"""
		Returns a string of the letter 'L'
		0' *     '
		1' *     '
		2' *     '
		3' *     '
		4' *     '
		5' *     '
		6' ***** ' 
		x 0123456
		"""
		letterArray = [];
		# First loop handles what "line" we're on
		while(7 > len(letterArray)):
			lineString = "";

			# Second loop handles what "column" we're on
			while(7 > len(lineString)):
				arrayLength = len(letterArray);
				stringLength = len(lineString);

				# The first and last characters are always spaces
				if(stringLength in {0, 6}):
					lineString += this.eStr;
					continue;
				
				# Line 0, 1, 2, 3, 4 & 5
				if(arrayLength in {0, 1, 2, 3, 4, 5}):
					lineString += _ternary((stringLength in {1}), this.fStr, this.eStr);
					continue;
				
				# Line 6
				if(arrayLength in {6}):
					lineString += _ternary((stringLength in {1, 2, 3, 4, 5}), this.fStr, this.eStr);
					continue;

			# End of while loop
			letterArray.append(lineString);

		# End of while loop	
		return this.delimiter.join(letterArray);


	# Function for the letter D
	def _D(this) -> str:
		"""
		Returns a string of the letter 'D'
		0' ***   '
		1' *  *  '
		2' *   * '
		3' *   * '
		4' *   * '
		5' *  *  '
		6' ***   ' 
		x 0123456
		"""
		letterArray = [];
		# First loop handles what "line" we're on
		while(7 > len(letterArray)):
			lineString = "";

			# Second loop handles what "column" we're on
			while(7 > len(lineString)):
				arrayLength = len(letterArray);
				stringLength = len(lineString);

				# The first and last characters are always spaces
				if(stringLength in {0, 6}):
					lineString += this.eStr;
					continue;
				
				# Line 0 & 6
				if(arrayLength in {0, 6}):
					lineString += _ternary((stringLength in {1, 2, 3}), this.fStr, this.eStr);
					continue;
				
				# Line 1 & 5
				if(arrayLength in {1, 5}):
					lineString += _ternary((stringLength in {1, 4}), this.fStr, this.eStr);
					continue;

				# Line 2, 3 & 4
				if(arrayLength in {2, 3, 4}):
					lineString += _ternary((stringLength in {1, 5}), this.fStr, this.eStr);
					continue;

			# End of while loop
			letterArray.append(lineString);

		# End of while loop	
		return this.delimiter.join(letterArray);


	# Function for the letter H
	def _H(this) -> str:
		"""
		Returns a string of the letter 'H'
		0' *   * '
		1' *   * '
		2' *   * '
		3' ***** '
		4' *   * '
		5' *   * '
		6' *   * ' 
		x 0123456
		"""
		letterArray = [];
		# First loop handles what "line" we're on
		while(7 > len(letterArray)):
			lineString = "";

			# Second loop handles what "column" we're on
			while(7 > len(lineString)):
				arrayLength = len(letterArray);
				stringLength = len(lineString);

				# The first and last characters are always spaces
				if(stringLength in {0, 6}):
					lineString += this.eStr;
					continue;
				
				# Line 0, 1, 2, 4, 5 & 6
				if(arrayLength in {0, 1, 2, 4, 5, 6}):
					lineString += _ternary((stringLength in {1, 5}), this.fStr, this.eStr);
					continue;
				
				# Line 3
				if(arrayLength in {3}):
					lineString += _ternary((stringLength in {1, 2, 3, 4, 5}), this.fStr, this.eStr);
					continue;

			# End of while loop
			letterArray.append(lineString);

		# End of while loop	
		return this.delimiter.join(letterArray);


	# Function for the letter T
	def _T(this) -> str:
		"""
		Returns a string of the letter 'T'
		0' ***** '
		1'   *   '
		2'   *   '
		3'   *   '
		4'   *   '
		5'   *   '
		6'   *   '
		x 0123456
		"""
		letterArray = [];
		# First loop handles what "line" we're on
		while(7 > len(letterArray)):
			lineString = "";

			# Second loop handles what "column" we're on
			while(7 > len(lineString)):
				arrayLength = len(letterArray);
				stringLength = len(lineString);

				# The first and last characters are always spaces
				if(stringLength in {0, 6}):
					lineString += this.eStr;
					continue;
				
				# Line 0
				if(arrayLength in {0}):
					lineString += _ternary((stringLength in {1, 2, 3, 4, 5}), this.fStr, this.eStr);
					continue;
				
				# Line 1, 2, 3, 4, 5 & 6
				if(arrayLength in {1, 2, 3, 4, 5, 6}):
					lineString += _ternary((stringLength in {3}), this.fStr, this.eStr);
					continue;
			
			# End of while loop
			letterArray.append(lineString);

		# End of while loop	
		return this.delimiter.join(letterArray);


	# Function to build each letter
	def _buildLetter(this, obj: dict, letterString: str) -> None:
		"""
		Gets each letter of the specified word,
		line by line and applys each line to
		the relevent line key in an object
		"""
		array = letterString.split(this.delimiter);
		lineNumber = 0;

		# Loop through the array,
		# concat each string into the key of the object
		string: str;
		for string in array:
			obj[lineNumber] += string;
			lineNumber += 1;
		# End of for loop


	# Function to call each letter function in order, then add each objects property to a string
	def buildWord(this) -> str:
		"""
		Finds the correct letter function to call and calls it,
		then calls the buildLetter function, before stringing
		(Pun intended) the entire word together.
		"""

		# If singleLetter is true, then we want to skip straight to building that letter
		# Technically speeds up processing by not having to call buildLetter
		# Also this is requirement as per the assignment
		if(this.singleLetter):
			letterFunction = getattr(this, f"_{this.word}");
			return letterFunction();

		wordObject = { 0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "" };
		# For each letter in the word, find the appropriate function
		letter: str;
		for letter in this.word:
			letterFunction = getattr(this, f"_{letter}");
			letterString = letterFunction();

			this._buildLetter(wordObject, letterString); # Taking advantage of objects being a memory reference
		# End of for loop
		return this.delimiter.join(wordObject.values());


# Main Function
def main() -> None:
	# Toggle this to true to make the output easier to read
	# (though it might actually make it harder if your console output doesn't support emojis)
	readabilityMode = false;

	eStr = _ternary(readabilityMode, "⬛", " "); # eStr is the string used to represent an empty space
	fStr = _ternary(readabilityMode, "⬜", "*"); # fStr is the string used to represent a filled space
	delimiter = "\n"; # delimiter is the string used to separate each line

	# While(true) is considered bad, recursion would probably have been better
	# Buuuuut we could possibly run into a Stack Overflow error
	while(true):
		# Ask the user for a word/ letter
		inputData = input("Please enter a word (Type \"end\" to exit): ");

		# If the inputData is empty, print an error and go to next iteration
		if(inputData == ""):
			print("Error: Input was empty");
			continue; # Reset

		# If inputData is "end", break
		# Specified to be case insensitive
		if(inputData.lower() == "end"):
			break; # End

		# If the word contains any characters other than "COLDHT", print an error and go to next iteration
		# Was specified that this is case sensitive, so only capitals work - Using Regex to make life easy.
		match = re.search("[^COLDHT]", inputData); # [^COLDHT]: Match any character that is not any of those expressed here
		if(match): # Match will be truthy if there is a match
			print("Error: Input can only contain the uppercase letters: C, O, L, D, H & T");
			continue; # Reset

		inputData = inputData.upper(); # Just to make sure the letters are indeed uppercase
		
		# All checks passed, build the word
		word = GetLetterString(inputData, fStr, eStr, delimiter).buildWord();
		print(word);
	# End of while loop


# Call the main function - Also prevents the program from running if this file is imported
# Specifically because this script is making use of an infinite while loop. Wouldn't want that running if imported.
if(__name__ == "__main__"):
	main();
