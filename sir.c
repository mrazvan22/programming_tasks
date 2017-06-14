#include <iostream>
#include <cstring>

using namespace std;


int main()
{
  char* sir = new char[50];
  cout << "Introduceti sirul\n";
  cin >> sir;
  cout << sir;
  cout << strlen(sir);

}

