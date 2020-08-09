#include <stdio.h>

int main() {
    double sum=1;
    double pre=0;
    double k=1;
    int i=1;
        while(k==1){
            sum=sum+1/((double) (i+1));
            pre=pre+1/((double) i);
            if((sum-pre)<0.001){
                k=0;
            }
            else{
                i=i+1;}
        }
        printf("%lf\n",sum);
        
        return 0;
}
