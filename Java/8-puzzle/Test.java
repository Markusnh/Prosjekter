
import java.util.ArrayList;

class Test{
  public static void main(String[] args){
    int size=3;
    Brett brett=Brett.lagBrett(size);
    while(!brett.checkIfSolvable()){
      brett=Brett.lagBrett(size);
    }
    System.out.println("Startbrett:");
    brett.skrivUt();
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
    System.out.println("Sluttbrett:");
    initialNode.expand();



  }
}
