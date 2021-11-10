
class Fib{

  // Fibonacci Sequence
  private static int fib(int n){
    int result = -1;

    if (n == 0 || n == 1)
      result = n;
    else if (n > 1)
      result = fib(n - 1) + fib(n - 2);

    return result;
}

  public static void main(String args[]){
    System.out.println(fib(24));
  }



}
