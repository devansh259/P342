#include <stdio.h>
#include <stdlib.h>
int main()
{
  int i,j,k,l;
  float dist,sum=0,num_points=0;
  for(i=0;i<6;i++){
      for(j=0;j<6;j++){
          for(k=0;k<6;k++){
              for(l=0;l<6;l++){
                    sum+= abs(i-j) +abs(k-l);
                    num_points+=1;
              }
                  
          }
          
      }
  }
  dist=sum/num_points;
  printf("average distance between the points= %f",dist);
  return 0;
}
