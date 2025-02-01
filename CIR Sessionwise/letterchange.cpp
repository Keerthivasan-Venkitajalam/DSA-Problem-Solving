//Letter change from a to b and b to c... 
#include <iostream>
#include <string>
std::string shiftLetters(const std::string& text) {
    std::string shiftedText = "";
    for (char c : text){
        if (isalpha(c)) {
            if (c=='z'){
                shiftedText +='a';
            } else if (c =='Z') {
                shiftedText+='A';
            } else {
                shiftedText+=c+1;
            }
        } else {
            shiftedText+=c;
        }
    }
    return shiftedText;
}
int main() {
    std::string inputText = "abc xyz";
    std::string outputText = shiftLetters(inputText);
    std::cout << outputText << std::endl;
    return 0;
}
