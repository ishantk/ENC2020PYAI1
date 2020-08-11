# Program which creates Programs

cpp_program = """
#include <iostream>
using namespace std;

int main() {
	cout<<"Hello World";
	return 0;
}
"""

java_program = """
class MyApp
{
	public static void main (String[] args) throws java.lang.Exception
	{
		System.out.println("Hello World");
	}
}
"""

# print(cpp_program)
# print(java_program)

program = input("Which Program would you like me to generate ?")

if program == "java":
    file = open("MyApp.java", "w")
    file.write(java_program)
elif program == "cpp":
    file = open("MyApp.cpp", "w")
    file.write(cpp_program)
else:
    print("Not Available")


# Assignment:
# Extend this program to 10 different programming languages for printing hello world
# dart, kotlin, typescript, javascript, go, scala