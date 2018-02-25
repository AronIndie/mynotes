package Sort;

/*
ref : https://www.cnblogs.com/coderising/p/5708801.html
 */
public class FastSort {

    public static void main(String[] args){
        int[] a = {1,4,3,2,5,0,9};
        fastSort(a, a.length-1, 0);
        for (int i : a) {
            System.out.println(i);
        }
    }

    public static void fastSort(int[] array, int hi, int lo){
        if(lo>=hi){
            return ;
        }
        int index=partition(array,lo,hi);
        fastSort(array,lo,index-1);
        fastSort(array,index+1,hi);
    }

    public static int partition(int []array,int lo,int hi){
        //固定的切分方式
        int key=array[lo];
        while(lo<hi){
            while(array[hi]>=key&&hi>lo){//从后半部分向前扫描
                hi--;
            }
            array[lo]=array[hi];
            while(array[lo]<=key&&hi>lo){ // 从前半部分向后扫描
                lo++;
            }
            array[hi]=array[lo];
        }
        array[hi]=key;
        return hi;
    }


}
