#include <stdio.h>

int main() {
    int s=0,m=0,n=0,t=0;
    printf("Enter any integer");
    scanf("%d", &n);
   if (n >= 0){
       int i;
        for(i=1;i<=n;++i){
            s +=i;
        }
        printf("Sum of integers till the number:%d", s);
   }
   else{
       m=-1*n;
        int i;
        for(i=1;i<=m;++i){
            s +=i;
        }
        t=-1*s;
        printf("Sum of integers till the number:%d", t);
    }
    return 0;
}