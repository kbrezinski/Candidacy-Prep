
1     public void myMethod ( int [] A ) {
2        int n = A.length; # 1
3        recursiveMethod(A, 0, n-1);
4     }
5
6     public void recursiveMethod ( int [] A , int i, int j ) {
7        int mid = (i+j)/2;

9        if (i < j) {
10          recursiveMethod(A, i, mid); # T(n / 2)
11          recursiveMethod(A, mid+1, j); # T(n / 2)
12
13          int max = A[j]; # 1
14
15          for (int m = i ; m < j ; m++) { # sum m = i, i < j
16              if (A[m] > max) # 1
17                  max = A[m]; # 1
18          }
19
20          if (max > 1000) {
21             recursiveMethod(A, i, mid);
22             recursiveMethod(A, mid+1, j);
23          }
24

'''




'''
