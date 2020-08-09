#include <stdio.h>

int main() {
    int s=1,m=0,n=0,t=0;
    printf("Enter any integer:");
    scanf("%d", &n);
   if (n >= 0){
       int i;
        for(i=1;i<=n;++i){
            s =s*i;
        }
        printf("factorial:%d", s);
   }
   else{
       
        printf("please choose positive integers to find factorial");
    }
    return 0;
}
