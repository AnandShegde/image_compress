#include <bits/stdc++.h>
#include <algorithm>
#include <sstream>
#include <string>

using namespace std;

typedef long long ll;
#define fo(i,n) for(int i=0;i<n;i++)


void solve()
{

    ll n;
    cin>>n;

    vector<ll> arr(2*n,0);
        // cout<<"iofe";

    arr[0] = 0;
    // cout<<"arr[0]: "<<arr[0]<<"\n";
    int i;
    for( i = 1;i<n+1;i++){
        // cout<<"i: "<<i<<"\n; ";
        arr[i] = arr[i-1] + i;
    }
    int j = i;
    for(int i = n-1;i>0;i--){
       
        arr[j] = arr[j-1] + i;
        j++;
    }
   
    ll k;
    cin>>k;


    fo(i,k){
        int j;
        cin>>j;
        cout<<lower_bound(arr.begin(), arr.end(), j) - arr.begin()<<"\n";

    }

    
}

int main()
{
    long long n, k, t,i,j=0,l,m,o,p,no=0,u,v,w,x,y,a,b,c;
    unsigned long long two;
    long double e,f,g;
    // cin>>t;
    i = 1;
    // while(t--){
        // cout<<i<<"\n";
        // cout<<"iofe";
        solve();
        i++; 

    // }
    return 0;
}