#include <stdio.h>
int main(){
    long n = 0;
    long cnt = 0;
    long m = 0;
    long d = 0;

    scanf("%ld", &n);
    
    for(long i=1; i<n;i++){
        m = n / i;
        if (i*i*i > n){
            break;
        }
        for (long j=i; j<n;j++){
            d = m/j - j + 1;
            if (d <= 0){
                break;
            }
            cnt += d;
        }
    }

    if (n == 1){
        printf("1\n");
    }else{
        printf("%ld\n", cnt);
    }
}