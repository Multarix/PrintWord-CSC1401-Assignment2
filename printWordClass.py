import re; # Import regex, because you didn't say I couldn't, was simply asked for a "validation plan".

# Good code doesn't need to be commented, bad/ hard to read code should always be commented.
# But the requirements said to comment to explain things. So here we are with an overcommented file

# Ternary function
def ternary(condition: bool, trueResult: any, falseResult: any) -> any:
	"""
	Returns the result of the ternary operator
	"""
	if(condition):
		return trueResult;
	else:
		return falseResult;

class GetLetterString:
	"""
	Class for building letters & words.
	"""
	# There wasn't really a reason to wrap these in a class, but I did it anyway.
	# Actually that's a lie, I did it because if I didn't, the best way to call the functions would
	# have been to use eval() or a large number of if statements, which creates potential security risks/ code bloat.
	# Doing it this way, we can call the functions by using getattr().

	# This also allows for expansion of the class to include more letters if needed. (Always a good thing for code maintainablity)
	# Also cause it's a class it technically dives into OOP.
	def __init__(this, word: str, fStr: str = "*", eStr: str = " ",  delimiter: str = "\n"):
		this.word = word;
		this.fStr = fStr;
		this.eStr = eStr;
		this.delimiter = delimiter;

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

	# Function for the letter C
	def letterC(this) -> str:
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
					lineString += this.eStr;
					continue;
				
				# Line 0 & 6
				if(arrayLength in {0, 6}):
					lineString += ternary((stringLength in {2, 3, 4}), this.fStr, this.eStr);
					continue;
				
				# Line 1 & 5
				if(arrayLength in {1, 5}):
					lineString += ternary((stringLength in {1, 5}), this.fStr, this.eStr);
					continue;

				# Line 2, 3 & 4
				if(arrayLength in {2, 3, 4}):
					lineString += ternary((stringLength in {1}), this.fStr, this.eStr);
					continue;

			# End of while loop
			letterArray.append(lineString);
		# End of while loop	

		return this.delimiter.join(letterArray);


	# Function for the letter O
	def letterO(this) -> str:
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
					lineString += this.eStr;
					continue;
				
				# Line 0 & 6
				if(arrayLength in {0, 6}):
					lineString += ternary((stringLength in {2, 3, 4}), this.fStr, this.eStr);
					continue;
				
				# Line 1, 2, 3, 4 & 6
				if(arrayLength in {1, 2, 3, 4, 5}):
					lineString += ternary((stringLength in{1, 5}), this.fStr, this.eStr);
					continue;

			# End of while loop
			letterArray.append(lineString);
		# End of while loop	

		return this.delimiter.join(letterArray);


	# Function for the letter L
	def letterL(this) -> str:
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
					lineString += this.eStr;
					continue;
				
				# Line 0, 1, 2, 3, 4 & 5
				if(arrayLength in {0, 1, 2, 3, 4, 5}):
					lineString += ternary((stringLength in {1}), this.fStr, this.eStr);
					continue;
				
				# Line 6
				if(arrayLength in {6}):
					lineString += ternary((stringLength in {1, 2, 3, 4, 5}), this.fStr, this.eStr);
					continue;

			# End of while loop
			letterArray.append(lineString);
		# End of while loop	

		return this.delimiter.join(letterArray);


	# Function for the letter D
	def letterD(this) -> str:
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
					lineString += this.eStr;
					continue;
				
				# Line 0 & 6
				if(arrayLength in {0, 6}):
					lineString += ternary((stringLength in {1, 2, 3}), this.fStr, this.eStr);
					continue;
				
				# Line 1 & 5
				if(arrayLength in {1, 5}):
					lineString += ternary((stringLength in {1, 4}), this.fStr, this.eStr);
					continue;

				# Line 2, 3 & 4
				if(arrayLength in {2, 3, 4}):
					lineString += ternary((stringLength in {1, 5}), this.fStr, this.eStr);
					continue;

			# End of while loop
			letterArray.append(lineString);
		# End of while loop	

		return this.delimiter.join(letterArray);


	# Function for the letter H
	def letterH(this) -> str:
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
					lineString += this.eStr;
					continue;
				
				# Line 0, 1, 2, 4, 5 & 6
				if(arrayLength in {0, 1, 2, 4, 5, 6}):
					lineString += ternary((stringLength in {1, 5}), this.fStr, this.eStr);
					continue;
				
				# Line 3
				if(arrayLength in {3}):
					lineString += ternary((stringLength in {1, 2, 3, 4, 5}), this.fStr, this.eStr);
					continue;

			# End of while loop
			letterArray.append(lineString);
		# End of while loop	

		return this.delimiter.join(letterArray);


	# Function for the letter T
	def letterT(this) -> str:
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
					lineString += this.eStr;
					continue;
				
				# Line 0
				if(arrayLength in {0}):
					lineString += ternary((stringLength in {1, 2, 3, 4, 5}), this.fStr, this.eStr);
					continue;
				
				# Line 1, 2, 3, 4, 5 & 6
				if(arrayLength in {1, 2, 3, 4, 5, 6}):
					lineString += ternary((stringLength in {3}), this.fStr, this.eStr);
					continue;
			
			# End of while loop
			letterArray.append(lineString);
		# End of while loop	

		return this.delimiter.join(letterArray);


	# Function to call each letter function in order, then add each objects property to a string
	def buildWord(this) -> str:
		"""
		Finds the correct letter function to call and calls it,
		then calls the buildLetter function, before stringing
		(Pun intended) the entire word together.
		"""


		# Function to build each letter
		def buildLetter(obj: dict, array: str) -> None:
			"""
			Gets each letter of the specified word,
			line by line and applys each line to
			the relevent line key in an object
			
			This is an inner function, so that it cannot
			be directly called outside of the class
			"""
			array = array.split(this.delimiter);
			lineNumber = 0;

			# Loop through the array,
			# concat each string into the key of the object
			string: str;
			for string in array:
				obj[lineNumber] += string;
				lineNumber += 1;
				


		wordObject = { 0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "" };
		# For each letter in the word, find the appropriate function
		letter: str;
		for letter in this.word:
			functionName = f"letter{letter}";

			letterFunction = getattr(this, functionName);
			letterArray = letterFunction();

			buildLetter(wordObject, letterArray); # Taking advantage of objects being a memory reference
		
		return this.delimiter.join(wordObject.values());


	# Destructor (Not really needed but added out of proof of knowledge)
	# As such this just uses the pass keyword
	def __del__(self):
		pass


# Main Function
def main():
	true = True;
	false = False;

	# Toggle this to true to make the output easier to read
	# (though it might actually make it harder if your console output doesn't support emojis)
	readabilityMode = false;

	# eStr is the string used to represent an empty space
	eStr = ternary(readabilityMode, "⬛", " ");

	# fStr is the string used to represent a filled space
	fStr = ternary(readabilityMode, "⬜", "*");

	# delimiter is the string used to separate each line of the output
	delimiter = "\n";

	# While(true) is considered bad, recursion would probably have been better
	# Buuuuut we could possibly run into a Stack Overflow error
	while(true):
		"""
		Asks the user for an input word, then checks it against several conditions.
		If the input fails any of the checks, an error is printed and this function is called again.
		If the input passes all the checks, builds the word, then calls this function again.
		If the word is 'end', exits the function entirely.
		"""
		# Ask the user for a word/ letter
		inputData = input("Please enter a word (Type \"end\" to exit): ");

		# If the input was empty, go to next iteration
		if(inputData == ""):
			print("Error: Input was empty");
			continue; # Reset

		# If the input word is end, break
		# Specified to be case insensitive
		if(inputData.lower() == "end"):
			break; # End

		# If the word contains any characters other than "C, O, L, D, H, T", go to next iteration
		# Was specified that this is case sensitive, so only capitals work - Using Regex to make life easy.
		match = re.search("[^COLDHT]", inputData);
		if(match):
			print("Error: Input can only contain the letters: C, O, L, D, H & T");
			continue; # Reset
		
		# If the word is a single letter, simply print the relevant letter using the relevent function
		# Then go to the next iteration (Technically this is a pointless check, but it's here as per the requirements)
		if(len(inputData) == 1):
			functionName = f"letter{inputData}";
			
			classItem = GetLetterString(inputData, fStr, eStr, delimiter);
			letterFunction = getattr(classItem, functionName);
			letter = letterFunction()

			print(letter);
			continue; # Reset
		
		# All checks passed, build the word
		word = GetLetterString(inputData, fStr, eStr, delimiter).buildWord();
		print(word);
	# End of while loop


# Call the main function - Also prevents the program from running if this file is imported
if(__name__ == "__main__"):
	main();