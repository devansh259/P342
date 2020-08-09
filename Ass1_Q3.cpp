#include <stdio.h>

int main() {
    double sum=1;
    double pre=0;
    double k=1;
    double d,summ;
    int n,m;
    printf("Integer input:");
    scanf("%d", &n);
    if(n>0){
        for(int i=1;sum-pre>0.001 && k==1;){
            if (i==n){k=0;}
            else{
                i=i+1;
                d=i;
                pre=sum;
                sum=sum+1/d;
            }
        }
        printf("%lf\n", sum);
    }
    else{
        m=-n;
        for(int i=1;sum-pre>0.001 && k==1;){
            if (i==m){k=0;}
            else{
                i=i+1;
                d=i;
                pre=sum;
                sum=sum+1/d;
            }
        }
        summ=-sum;
        printf("%lf\n", summ);
    }
    return 0;
}
