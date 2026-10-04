'''
MAKE_SET() --> returns a set value (a string containing substrings separated by “,” characters) consisting of the strings that have the corresponding bit in the first argument.
    Syntax : MAKE_SET(bits,str1,str2,...)
        Example : SELECT MAKE_SET(1,'a','b','c');
            output : a

MID() --> extracts a substring from a string. The actual string, position to start extraction and length of the extracted string - all are specified as arguments.
    Syntax : MID(str,pos,len)
        Example : SELECT MID('Ps-Softech',4,3);
            Output : Sof

OCT() --> Returns a string representation of the octal value of N, where N is a longlong (BIGINT) number. Returns NULL if N is NULL.
    Syntax : OCT(N)
        Example : SELECT OCT(12);
            Output : 14

ORD() --> returns the code for the leftmost character if that character is a multi-byte (sequence of one or more bytes) one. If the leftmost character is not a multibyte character, ORD() returns the same value as the ASCII() function.
    Syntax : ORD(str)
        Example : SELECT ORD("Ps-Softech");
            Output : 80
POSITION() --> returns the position of a substring within a string..
    Syntax : POSITION(substr IN str)
        Example : SELECT POSITION("So" IN "Ps-Softech");
            Output : 4

QUOTE() --> Quotes a string to produce a result that can be used as a properly escaped data value in an SQL statement. The string is returned enclosed by single quotation marks and with each instance of backslash (“\”), single quote (“'”), ASCII NUL, and Control+Z preceded by a backslash. If the argument is NULL, the return value is the word “NULL” without enclosing single quotation marks.
    Syntax : QUOTE(str)
        Example : SELECT QUOTE('PS''SOFTECH');
            Output : 'PS\'SOFTECH'
REPEAT() --> repeats a string for a specified number of times. The function returns NULL either any either of the arguments are NULL.
    Syntax : REPEAT(str,count)
        Example : SELECT REPEAT('**-',5);
            Output : **-**-**-**-**-

REPLACE() --> replaces all the occurrences of a substring within a string.
    Syntax : REPLACE(str,from_str,to_str)
        Example : SELECT REPLACE('Ps-Softech','Ps',’Ss');
            Output : Ss-Softech

REVERSE() --> Returns a given string with the order of the characters reversed.
    Syntax : REVERSE(str)
        Example : SELECT REVERSE('Ps-Softech');
            Output : hcetfoS-sP

RIGHT() --> extracts a specified number of characters from the right side of a given string.
    Syntax : RIGHT(str,len)
        Example : SELECT RIGHT('Ps-Softech',4);
            Output : tech

RPAD() --> function pads strings from right. The actual string which is to be padded as str, length of the string returned after padding as len and string which is used for padding as padstr is used as a parameters within the argument.
    Syntax : RPAD(str,len,padstr)
        Example : SELECT RPAD('Ps-Softech',15,'*');
            Output : Ps-Softech*****

RTRIM() --> removes the trailing spaces from a given string.
    Syntax : RTRIM(str)
        Example : SELECT RTRIM('Ps-Softech ');
            (excludes the trailing spaces) Output : Ps-Softech

SOUNDEX() --> function returns soundex string of a string. Soundex is a phonetic algorithm for indexing names after English pronunciation of sound. You can use SUBSTRING() on the result to get a standard soundex string. All non-alphabetic characters in str are ignored. All international alphabetic characters outside the A-Z range are treated as vowels.
    Syntax : SOUNDEX(str)
        Example : SELECT SOUNDEX('Ps-Softech');

SPACE() --> returns the string containing a number of spaces as specified in the argument.
    Syntax : SPACE(N)
        Example : SELECT 'start', SPACE(10), 'end';
            Output : start end SPACE(10)

SUBSTR() --> returns the specified number of characters from a particular position of a given string. SUBSTR() is a synonym for SUBSTRING().
    Syntax : SUBSTR(str,pos,len)
        Example : SELECT SUBSTR('Ps-Softech',4,3);
            Output : Sof

SUBSTRING() --> returns a specified number of characters from a particular position of a given string.
    Syntax : SUBSTRING(str,pos,len)
        Example : SELECT SUBSTRING('Ps-Softech',4,3);
            Output : Sof

SUBSTRING_INDEX() --> returns the substring from the given string before a specified number of occurrences of a delimiter.
Returns from the left of the final delimiter if the number is positive and right of the final delimiter when the number is negative.
If the number is greater than the number of occurrence of delimiter, the returned substring will be the total string. If the specified number is 0, nothing will be fetched from the given string.
    Syntax : SUBSTRING_INDEX(str,delim,count)
        Example : SELECT SUBSTRING_INDEX('www.mytestpage.info','.',2);
            Output : www.mytestpage

TRIM() --> returns a string after removing all prefixes or suffixes from the given string.
    Syntax : TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM] str)
        Example : SELECT TRIM(' trim ');
            Output : trim (leading and trailing space removed)
        Example : SELECT TRIM(LEADING 'leading' FROM 'leadingtext' );
            Output : text
        Example : SELECT TRIM(BOTH 'leadtrail' FROM 'leadtrailtextleadtrail');
            Output : text

UNHEX() --> performs the opposite operation of HEX(). This function interprets each pair of hexadecimal digits (in the argument) as a number and converts it to a character.
    Syntax : UNHEX(str)
        Example : SELECT UNHEX('4D7953514C');
            Output : MySQL
        Example : SELECT UNHEX(HEX('MySQL'));
            Output : MySQL

UPPER() --> converts all the characters in a string to uppercase characters.
    Syntax : UPPER(str)
        Example : SELECT UPPER('myteststring');
            Output : MYTESTSTRING

'''