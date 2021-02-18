import java.util.ArrayList;

class Node{
  Brett brett;
  int lowestF;
  Node lowestChild;
  public static Brett goalBrett;
  public static ArrayList<Brett> checkedBrett;
  public static ArrayList<Node> leaves;
  public static Boolean goal;
  Boolean initial;
  Node parent;
  ArrayList<Node> children;
  int f;
  int steps;
  String path;


  public Node(Brett brett, Node parent, int f, int steps, String path){
    this.brett=brett;
    this.parent=parent;
    children=new ArrayList<Node>();
    this.f=f;
    initial=false;
    this.steps=steps;
    this.path=path;
  }

  public Node(Brett brett){
    this.brett=brett;
    this.parent=null;
    children=new ArrayList<Node>();
    f=this.brett.heuristic();
    initial=true;
    steps=0;
    path="";
  }


  public void expand(){
    if (brett.equals(goalBrett)){
      brett.skrivUt();
      goal=true;
      System.out.println("you have officially made it");
      System.out.println("steps:"+steps+"\npath:"+path);
    }

    if (!initial){
      leaves.remove(this);
    }
    brett.returnPosition();
    if (brett.indeksi!=0){
      brett.moveNorth();
      Boolean north=true;
      for (int i=0;i<checkedBrett.size();i++){
        if (brett.equals(checkedBrett.get(i))){
          north=false;
          break;
        }
      }
      if (north==true){
        int f=brett.heuristic()+1;
        Node child=new Node(brett.makeCopy(), this, f, steps++, path+"N");
        children.add(child);
        checkedBrett.add(brett.makeCopy());
        leaves.add(child);

      }
      brett.moveSouth();
    }


    if (brett.indeksi!=brett.size-1){
      brett.moveSouth();
      Boolean south=true;
      for (int i=0;i<checkedBrett.size();i++){
        if (brett.equals(checkedBrett.get(i))){
          south=false;
          break;
        }
      }
      if (south==true){
        int f=brett.heuristic()+1;
        Node child=new Node(brett.makeCopy(), this, f, steps++, path+"S");
        children.add(child);
        checkedBrett.add(brett.makeCopy());
        leaves.add(child);

      }
      brett.moveNorth();
    }

    if (brett.indeksj!=brett.size-1){
      brett.moveEast();
      Boolean east=true;
      for (int i=0;i<checkedBrett.size();i++){
        if (brett.equals(checkedBrett.get(i))){
          east=false;
          break;
        }
      }
      if (east==true){
        int f=brett.heuristic()+1;
        Node child=new Node(brett.makeCopy(), this, f, steps++, path+"E");
        children.add(child);
        checkedBrett.add(brett.makeCopy());
        leaves.add(child);
      }
      brett.moveWest();
    }

    if (brett.indeksj!=0){
      brett.moveWest();
      Boolean west=true;
      for (int i=0;i<checkedBrett.size();i++){
        if (brett.equals(checkedBrett.get(i))){
          west=false;
          break;
        }
      }
      if (west==true){
        int f=brett.heuristic()+1;
        Node child=new Node(brett.makeCopy(), this, f, steps++, path+"W");
        children.add(child);
        checkedBrett.add(brett.makeCopy());
        leaves.add(child);
      }
      brett.moveEast();
    }

    int lowestF=leaves.get(0).f;
    Node lowestChild=leaves.get(0);
    for (int i=1;i<leaves.size();i++){
      if (leaves.get(i).f<lowestF){
        lowestF=leaves.get(i).f;
        lowestChild=leaves.get(i);
      }
    }

    //only used for debug
    //System.out.println("lowestF="+lowestF);
    //System.out.println("number of leaves="+leaves.size());

    if (leaves.size()>700){
      System.out.println(goal);
      goal=true;
      System.out.println("-------------------------------------------------------------------------------------------------");
    }

    if (!goal){
      lowestChild.expand();
    }
  }

  public void findLowestF(){
    int lowestF=children.get(0).f;
    Node lowestChild=children.get(0);
    for (int i=1;i<children.size();i++){
      if (children.get(i).f<lowestF){
        lowestF=children.get(i).f;
        lowestChild=children.get(i);
      }
    }
    this.lowestF=lowestF;
    this.lowestChild=lowestChild;
  }
}
