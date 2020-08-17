#include <stdio.h>
int main ()
{
  int m[3][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
  int n[3][3] = { {-1, 2, 7}, {9, -5, 6}, {7, 8, -9} };
  int p[3][3] = { {0, 0, 0}, {0, 0, 0}, {0, 0, 0} };
  int a[3] = { 2, 5, 7 };
  int b[3];
  int i, j, k, sum;
  
  for(i=0;i<sizeof(m)/sizeof(m[0]);i++){
    sum=0;
    for(j=0;j<sizeof(a)/sizeof(a[0]);j++){
        sum+=m[i][j] * a[j];
        }
    b[i]=sum;    
  }
  printf("Product of A and M = \n");
  for(i=0;i<3;i++){
      printf("%d ",b[i]);
  }
  printf("\n");
  
  for (i = 0; i < sizeof(m)/sizeof(m[0]); i++){
      for(j=0;j < sizeof(n[0])/sizeof(int); j++){
          for(k=0; k < 3; k++){
              p[i][j]+= m[i][k] * n[k][j];
          }
      }
  }
  printf("Product of the 2 matrices =\n"); 
  for (i = 0; i < 3; i++){
      for(j=0;j < 3; j++){
        printf("%d ",p[i][j]);
      } 
      printf("\n");
  }  
  return 0;
}
