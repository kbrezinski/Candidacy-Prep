
class FibEff{

  // Fibonacci Sequence
  private static int fib(int n){
    int [] F = new int [n + 1];

    F[0] = 0;
    F[1] = 1;

    for (int i = 2; i < n + 1; i++)
      F[i] = F[i - 1] + F[i - 2];

    return F[n];
}

  public static void main(String args[]){
    System.out.println(fib(24));
  }



}
