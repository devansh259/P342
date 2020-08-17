#include <stdio.h>
#include <stdlib.h>
int main()
{
  int i,j;
  float dist,sum=0;
  for(i=0;i<6;i++){
      for(j=0;j<6;j++){
          sum=sum+ abs(j-i);
      }
  }
  dist=sum/36;
  printf("average distance between the points= %f",dist);
  return 0;
}
