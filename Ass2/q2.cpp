#include <stdio.h>
#include <stdlib.h>
int main()
{
    int a[3]={2,5,7};
    int b[3]={3,8,1};
    int c[3];
    int i,sum=0;
    for(i=0;i<3;i++){
        c[i]=a[i]+b[i];
        sum+=a[i]*b[i];
    }


  printf("sum of the A and B vectors=\n");
 
  for(i=0;i<3;i++){
      printf("%d\n",c[i]);
  }
  printf("dot product of the 2 vectors=%d",sum);
  return 0;
}
