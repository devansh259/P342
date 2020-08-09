#include <stdio.h>
int main() {
    int s =0, i;
    for (i = 1; i <= 100; ++i) {
        
        s=s+i;
    }
    printf("Sum of numbers from 1 to 100 = %d" , s);
     return 0;
}
