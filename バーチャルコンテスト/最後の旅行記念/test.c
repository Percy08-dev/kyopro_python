#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(void){
    int n, m, k, f;
    f=0;
    scanf("%d %d %d", &n, &m, &k);

    for (int i=0; i<=n; i++){
        for (int j=0; j<=m; j++){
            if (i*(m-j) + j*(n-i) == k){
                printf("Yes\n");
                f=1;
                break;
            }
        }
        if (f){
            break;
        }
    }

    if (!f){
        printf("No\n");
    }
}