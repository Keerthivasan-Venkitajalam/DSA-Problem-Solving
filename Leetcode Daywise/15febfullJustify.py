# class Solution:
#     def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
#         result=[] #each value is gonna be the line in result
#         currLine,  currLineLength=[],0 #array as line not a string - useful for us as we count the number of words -- currLineLength --> all the characters in each of the word length is needed
#         i=0 #pointer assignment
#         while i<len(words): #2 cases 
#             if currLineLength + len(currLine) + len(words[i]) > maxWidth:
# #length + number of spaces + length of current word > maxWidth
#                 #case 1 - line complete
#                 extra_space=maxWidth-currLineLength #even spacing -- easy hit as no spaces in currLineLength
#                 spaces=extra_space//max(1,len(currLine)-1) #to handle what if len(currLine)=1 => we get divided by 0 error
#                 remainder=extra_space%max(1,len(currLine)-1) #these are sort of spaces that is going to be distributed in a greedy way from L to R

#                 for j in range(max(1,len(currLine)-1)): #no space after and handle one word edge case
#                     currLine[j]+=" "*spaces #string space * integer -> integer number of spaces
#                     if remainder:
#                         currLine[j]+=" "#atleast one space
#                         remainder-=1
#                 result.append(" ".join(currLine)) #all words joined
#                 currLine,  currLineLength=[],0  #reset line and string
#             #case 2 - when line is not complete we add cuurent word to current line and update length of current line --> currLineLength+=len(words[]) not inclusing the space
#             #code of that logic
#             currLine.append(words[i])
#             currLineLength+=len(words[i])
#             i+=1

#         #handle last line
#         last_line=" ".join(currLine)
#         trailing_space=maxWidth-len(last_line)
#         result.append(last_line + " " * trailing_space)
#         return result

# from typing import List

# class Solution:
#     def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
#         result=[] #each value is gonna be the line in result
#         currLine,  currLineLength=[],0 #array as line not a string - useful for us as we count the number of words -- currLineLength --> all the characters in each of the word length is needed
#         i=0 #pointer assignment
#         while i<len(words): #2 cases 
#             if currLineLength + len(currLine) + len(words[i]) > maxWidth:
# #length + number of spaces + length of current word > maxWidth
#                 #case 1 - line complete
#                 extra_space=maxWidth-currLineLength #even spacing -- easy hit as no spaces in currLineLength
#                 if len(currLine) == 1: #only one word in the line
#                     currLine[0] += " " * extra_space  #add all spaces at the end
#                 else:
#                     # spaces=extra_space//max(1,len(currLine)-1) #to handle what if len(currLine)=1 => we get divided by 0 error
#                     spaces = extra_space // (len(currLine) - 1)  # FIXED: Removed unnecessary max(1,...) check, as len(currLine) == 1 case is already handled above
                    
#                     # remainder=extra_space%max(1,len(currLine)-1) #these are sort of spaces that is going to be distributed in a greedy way from L to R
#                     remainder = extra_space % (len(currLine) - 1)  # FIXED: Same as above, removed unnecessary max(1,...) check

#                     for j in range(len(currLine) - 1): #no space after and handle one word edge case
#                         currLine[j]+=" "*spaces #string space * integer -> integer number of spaces
#                         if remainder:
#                             currLine[j]+=" "#atleast one space
#                             remainder-=1
                
#                 result.append(" ".join(currLine)) #all words joined
#                 currLine,  currLineLength=[],0  #reset line and string
#             #case 2 - when line is not complete we add cuurent word to current line and update length of current line --> currLineLength+=len(words[]) not inclusing the space
#             #code of that logic
#             currLine.append(words[i])
#             currLineLength+=len(words[i])
#             i+=1

#         #handle last line
#         last_line=" ".join(currLine)
#         trailing_space=maxWidth-len(last_line)
#         result.append(last_line + " " * trailing_space)
#         return result

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result=[] #each value is gonna be the line in result
        currLine, currLineLength = [], 0 #array as line not a string - useful for us as we count the number of words -- currLineLength --> all the characters in each of the word length is needed
        i=0 #pointer assignment

        while i < len(words): #2 cases 
            if currLineLength + len(currLine) + len(words[i]) > maxWidth:
#length + number of spaces + length of current word > maxWidth
                #case 1 - line complete
                extra_space = maxWidth - currLineLength #even spacing -- easy hit as no spaces in currLineLength
                if len(currLine) == 1: #only one word in the line
                    currLine[0] += " " * extra_space  #add all spaces at the end
                else:
                    # Incorrect: spaces=extra_space//max(1,len(currLine)-1) 
                    spaces = extra_space // (len(currLine) - 1)  # FIXED: evenly distribute spaces
                    # Incorrect: remainder=extra_space%max(1,len(currLine)-1) 
                    remainder = extra_space % (len(currLine) - 1)  # FIXED: distribute remaining spaces from L to R

                    for j in range(len(currLine) - 1): #no space after last word
                        currLine[j] += " " * spaces #string space * integer -> integer number of spaces
                        if remainder > 0:  # Remaining spaces to distribute left to right
                            currLine[j] += " "
                            remainder -= 1  # Reduce remainder count

                result.append("".join(currLine)) #all words joined
                currLine, currLineLength = [], 0  #reset line and string
            
            #case 2 - when line is not complete we add current word to current line and update length of current line
            currLine.append(words[i])
            currLineLength += len(words[i])
            i += 1

        #handle last line
        last_line = " ".join(currLine)
        trailing_space = maxWidth - len(last_line)
        result.append(last_line + " " * trailing_space)
        
        return result
