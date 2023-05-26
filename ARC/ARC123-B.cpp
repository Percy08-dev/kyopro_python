#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;

int main(void){
    int n, sb, sc, cnt, i;

    cin >> n;

    vector<long> a(n);
    vector<long> b(n);
    vector<long> c(n);

    for (int i=0; i<n; i++){
        cin >> a[i];
    }
    for (int i=0; i<n; i++){
        cin >>b[i];
    }

    for (int i=0; i<n; i++){
        cin >> c[i];
    }

    sort(a.begin(), a.end() );
    sort(b.begin(), b.end() );
    sort(c.begin(), c.end() );

    sb = 0;
    sc = 0;
    cnt = 0;
    for (i=0; i<n; i++){
        if (sb == n | sc == n) break;
        for (int j=sb; j<n; j++){
            if (a[i] < b[j]){
                sb = j;
                break;
            }
        }
        for (int k=sc; k<n; k++){
            if (b[sb] < c[k]){
                sc = k;
                break;
            }
        }
        cnt++;
        sb++;
        sc++;
    }
    
    if (!(a[i-1] < b[sb-1] & b[sb-1] < c[sc-1])) cnt--;
    cout << cnt << endl;
    /*
    for_each(a.begin(), a.end(), [](long x){
        cout << x << " ";
    });
    cout << endl;
    for_each(b.begin(), b.end(), [](long x){
        cout << x << " ";
    });
    cout << endl;
    for_each(c.begin(), c.end(), [](long x){
        cout << x << " ";
    });
    cout << endl;
    */
}