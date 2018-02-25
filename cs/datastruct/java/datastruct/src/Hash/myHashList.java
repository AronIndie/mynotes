package Hash;


import java.util.LinkedList;


public class myHashList<T> {

    private LinkedList<T>[] theLists;
    private static final int DEFAULT_SIZE = 10;

    public myHashList(){
        initial();
    }

    private void initial(){
        initial(DEFAULT_SIZE);
    }

    private void initial(int capacity){

        this.theLists = new LinkedList[capacity]; // 列表初始化，用来存储相应值
        for (int i = 0; i < theLists.length; i++) {
            theLists[i] = new LinkedList<>();
        }
    }

    public void makeEmpty(){
        initial(theLists.length);
    }

    private int myHash(T x){
        int hashVal = x.hashCode();
        return hashVal % theLists.length;
    }

    public void insert(T x){
        if (!contains(x)) {
            int hashVal = myHash(x);
            theLists[hashVal].add(x);
        }
    }

    public boolean contains(T x){
        LinkedList<T> whichList = theLists[myHash(x)];
        return whichList.contains(x);
    }

    public void remove(T x){
        LinkedList<T> whichList = theLists[myHash(x)];
        if (whichList.contains(x)){
            whichList.remove(x);
        }
    }

}
