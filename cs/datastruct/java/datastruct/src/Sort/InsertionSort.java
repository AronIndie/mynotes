package Sort;


public class InsertionSort {

    public static <T extends Comparable<? super T>> void insertionSort(T[] a){
        // 一个static方法，无法访问泛型类的类型参数，所以，若要static方法需要使用泛型能力，必须使其成为泛型方法。
        for (int i = 0; i < a.length; i++) {
            T tmp = a[i];
            for (int j = i; j > 0 && tmp.compareTo(a[j-1]) <0 ; j--) {
                a[j] = a[j - 1];

            }
        }
    }

    /** 插入排序算法
     * 稳定
     空间复杂度O(1)
     时间复杂度O(n2)
     最差情况：反序，需要移动n*(n-1)/2个元素
     最好情况：正序，不需要移动元素
     数组在已排序或者是“近似排序”时，插入排序效率的最好情况运行时间为O(n)；
     插入排序最坏情况运行时间和平均情况运行时间都为O(n2)。
     通常，插入排序呈现出二次排序算法中的最佳性能。
     对于具有较少元素（如n<=15）的列表来说，二次算法十分有效。
     在列表已被排序时，插入排序是线性算法O(n)。
     在列表“近似排序”时，插入排序仍然是线性算法。
     在列表的许多元素已位于正确的位置上时，就会出现“近似排序”的条件。
     通过使用O(nlog2n)效率的算法（如快速排序）对数组进行部分排序，
     然后再进行选择排序，某些高级的排序算法就是这样实现的。
     * @param x
     * @param <T>
     */
    public static <T extends Comparable<? super T>> void myInsertionSort(T[] x){

        for (int i = 1; i < x.length; i++) { // 从1开始
            T temp = x[i];
            int j = i;
            while (j>0 && temp.compareTo(x[j-1]) < 0){ // 逆向扫描前面已排序的子列表，直到遇到合适的位置，跳出循环，插入
                x[j] = x[j-1];
                j--;
            }
            x[j] = temp;
        }

    }

    /*
    希尔排序

    实质是分组插入：先将待排序序列按照增量分成若干子序列，待到所有子序列基本有序时，再对所有子序列进行一次插入排序，以缩短时间
    示例：（希尔增量 h_k = h_{k+1} / 2）
    8 9 1 7 2 3 5, len = 7
    step 1. 7 / 2 = 3，按照1 2 3 1 2 3 1分成三组:(8,7,5), (9, 2), (1,3)
    step 2. 每组内部排序，并放入原数组相应位置:(5,7,8), (2,9), (1,3) ==> 5 2 1 7 9 3 8
    step 3. 缩小增量，用上次得到的3,除以2，3 / 2 = 1，则增量为1，分成1组(5,2,1,7,9,3,8)对上述数组进行插入排序，完成。

     */
    public static <T extends Comparable<? super T>> void shellSort(T[] x){
        for (int gap = x.length / 2; gap > 0; gap/=2) {
            for (int i = 0; i < gap; i++) { // 每个gap进行插入排序
                for (int j = i + gap; j < x.length; j+=gap) { // 参考前面的插入排序
                    T temp = x[j];
                    int k = j;
                    while (k-gap > 0 && temp.compareTo(x[k-gap]) < 0){ // 注意这边是k-gap 大于0，防止下标越界
                        x[k] =  x[k - gap];
                        k -= gap;
                    }
                    x[k] = temp;
                }
            }
        }
    }

    /**
     * 冒泡排序，每一次排序都会找到较大值，放在最后（第一次排序最后的必是最大值），所以一共需要n-1次排序
     * 第i次排序后只需要对前n-i个元素进行排序，每次排序后元素都在减少。
     * 时间复杂度O(n^2)
     * @param x
     */
    public static void bubbleSort(int[] x){
        for (int i = 0; i < x.length-1; i++) {
            for (int j = 0; j < x.length - 1 - i; j++) {
                if (x[j] > x[j+1]){
                    int temp = x[j];
                    x[j] = x[j+1];
                    x[j+1] = temp;
                }
            }
        }
    }

    public static void main(String[] args){
        Integer[] a1 = new Integer[]{1,3,4,2,5,0,9,12,6};
//        myInsertionSort(a1);
        shellSort(a1);
        for (Integer i : a1) {
            System .out.println(i.toString());
        }
    }
}
