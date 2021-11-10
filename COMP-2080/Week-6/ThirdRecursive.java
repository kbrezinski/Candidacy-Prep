import java.util.Arrays;

class ThirdRecursive{
  // Recursive Helper
  private static void recursiveHelper(int i, int j, int [] A){
    int firstThird = (2 * i + j) / 3;
    int secondThird = (2 * j + i) / 3;

    if (i < j){
      for (int k = i; k <= j; k++)
        A[k]++;
      recursiveHelper(i, firstThird, A);
      recursiveHelper(firstThird + 1, secondThird, A);
      recursiveHelper(secondThird + 1, j, A);
    }
}

// Main Recursive
public static int [] rootMethod(int [] A){
  int n = A.length;
  recursiveHelper(0, n - 1, A);
  return A;
}

  public static void main(String args[]){
    int [] A = {2, 5, 3, 6, 1, 0, -2, 4, 10, 6, -1, 0};
    System.out.println(Arrays.toString(rootMethod(A)));
  }


}
