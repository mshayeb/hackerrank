#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
 
int eatenChocolades(int availableCash, int price, int wrapperDiscount){
    int eaten = 0;
    int wraps = 0;
     
    wraps = eaten = availableCash/price;
     
    while (wraps >= wrapperDiscount){
        int newlyEaten = wraps/wrapperDiscount;
        eaten += newlyEaten;
        wraps %= wrapperDiscount;
        wraps += newlyEaten;
    }
     
     
    return eaten;
}
 
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int t,n,c,m;
    cin>>t;
    while(t--){
        cin>>n>>c>>m;
        int answer=0;
        answer = eatenChocolades(n,c,m);
        cout<<answer<<endl;
    }
    return 0;
}