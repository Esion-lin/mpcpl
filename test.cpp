#include <iostream>
#include <string>

using namespace std;
const char* hello(){return __func__;}

int main(){
    cout << hello() << endl;
}