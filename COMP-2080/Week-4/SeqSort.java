
class SeqSort{

  // Sequential Search; runtime 2n + 2
  private static int Search(int arr [], int key){

    int n = arr.length;
    int i = 0;

    while (i < n && arr[i] != key){
        i++;
    }
    return i;
}

  public static void main(String args[]){

    int [] arr = {1, 2, 3, 4, 5, 6};

    System.out.println(Search(arr, 2));
  }



}
