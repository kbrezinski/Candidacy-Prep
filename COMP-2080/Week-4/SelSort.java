
import java.util.Arrays;

class SelSort{

  // Sequential Search; runtime 2n + 2
  private static int [] Search(int [] arr){

    int n = arr.length;

    for (int x = 0; x < n - 1; x++){
      for (int y = x + 1; y < n; y++){
        if (arr[x] > arr[y]){
          int tmp = arr[x];
          arr[x] = arr[y];
          arr[y] = tmp;
        }
      }
    }
    return arr;
  }

  public static void main(String args[]){

    int [] arr = {2, 5, 3, 8, -3, 0};
    //System.out.println(Arrays.toString(Search(arr)));
    System.out.println(4 << 2);
  }

}
