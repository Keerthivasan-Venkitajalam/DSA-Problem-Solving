//character sort in string
#include <iostream>
#include <string>
#include <algorithm>
std::string sortLetters(const std::string& text) {
    std::string sortedText = text;
    std::sort(sortedText.begin(), sortedText.end());
    return sortedText;
}
int main() {
    std::string inputText = "abc xnbz";
    std::string outputText = sortLetters(inputText);
    std::cout << outputText << std::endl;
    return 0;
}