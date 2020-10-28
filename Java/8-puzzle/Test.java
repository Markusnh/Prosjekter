import java.util.Scanner;
import java.util.ArrayList;

class Test{
  public static void main(String[] args){
    Scanner scanner=new Scanner(System.in);
    System.out.println("please state the size of the 8-puzzle in the form of an int");
    int size=scanner.nextInt();
    Brett brett=Brett.lagBrett(size);
    Tile[][] goalbrett=new Tile[size][size];
    for (int i=0;i<size;i++){
      for (int j=0;j<size;j++){
        goalbrett[i][j]=new Tile(i*size+j);
      }
    }
    Brett goalBrett=new Brett(goalbrett, size);
    Node initialNode=new Node(brett);
    Node.checkedBrett=new ArrayList<Brett>();
    Node.goalBrett=goalBrett;
    Node.leaves=new ArrayList<Node>();
    Node.goal=false;
    initialNode.expand();


  }
}
