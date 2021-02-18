import java.util.Random;
import java.util.ArrayList;

class Brett{
  Tile[][] brett;
  int size;
  int indeksi;
  int indeksj;
  public static Tile[][] goalbrett;
  int ID;


  static public Brett lagBrett(int size){
    Tile[][] brett=new Tile[size][size];
    ArrayList<Integer> liste=new ArrayList<Integer>();
    Random random=new Random();
    for (int i=0;i<size*size;i++){
      liste.add(i);
    }
    for (int i=0;i<size;i++){
      for (int j=0;j<size;j++){
        int tall=random.nextInt(liste.size());
        Tile something=new Tile(liste.get(tall));
        brett[i][j]=something;
        liste.remove(tall);
      }
    }
    return new Brett(brett, size);
  }

  public boolean checkIfSolvable(){
    int inversions=0;
    for (int i=0;i<size;i++){
      for (int j=0;j<size;j++){
        int utgangspunkt=this.brett[i][j].getTall();
        if (utgangspunkt==0){
          continue;
        }
        for (int k=i;k<size;k++){
          for (int g=0;g<size;g++){
            if (k==i && g<=j){
              continue;
            }else{
              if (this.brett[k][g].getTall()!=0 && utgangspunkt>this.brett[k][g].getTall()){
                inversions++;
              }
            }
          }
        }
      }
    }
    if (inversions%2==0){
      return true;
    }else{
      return false;
    }
  }

  public Brett(Tile[][] brett, int size){
    this.brett=brett;
    this.size=size;
    if (goalbrett==null){
      Tile[][] goal=new Tile[size][size];
      for (int i=0;i<size;i++){
        for (int j=0;j<size;j++){
          goal[i][j]=new Tile(i*size+j);
        }
      }
      goalbrett=goal;
    }
    returnPosition();
  }

  public void skrivUt(){
    System.out.println("-------------------------------------");
    for (int i=0;i<size;i++){
      String streng="";
      for (int j=0;j<size;j++){
        streng=streng+" "+brett[i][j].toString();
      }
      System.out.println("|"+streng+"|");
    }
    System.out.println("-------------------------------------");
  }

  public void returnPosition(){
    for (int i=0;i<size;i++){
      for (int j=0;j<size;j++){
        if (brett[i][j].getTall()==0){
          this.indeksi=i;
          this.indeksj=j;
        }
      }
    }
  }

  public ArrayList<String> checkAvailableMoves(){
    ArrayList<String> liste=new ArrayList<String>();
    if (indeksi!=0){
      liste.add("N");
    }
    if (indeksi!=size-1){
      liste.add("S");
    }
    if (indeksj!=size-1){
      liste.add("E");
    }
    if (indeksj!=0){
      liste.add("W");
    }
    return liste;
  }

  public void moveNorth(){
    brett[indeksi][indeksj]=brett[indeksi-1][indeksj];
    brett[indeksi-1][indeksj]=new Tile(0);
    returnPosition();
  }

  public void moveSouth(){
    brett[indeksi][indeksj]=brett[indeksi+1][indeksj];
    brett[indeksi+1][indeksj]=new Tile(0);
    returnPosition();
  }
  public void moveWest(){
    brett[indeksi][indeksj]=brett[indeksi][indeksj-1];
    brett[indeksi][indeksj-1]=new Tile(0);
    returnPosition();
  }

  public void moveEast(){
    brett[indeksi][indeksj]=brett[indeksi][indeksj+1];
    brett[indeksi][indeksj+1]=new Tile(0);
    returnPosition();
  }

  public boolean equals(Brett annetBrett){
    if (indeksi!=annetBrett.indeksi){
      return false;
    }
    if (indeksj!=annetBrett.indeksj){
      return false;
    }
    for (int i=0;i<size;i++){
      for (int j=0;j<size;j++){
        if (brett[i][j].getTall()!=annetBrett.brett[i][j].getTall()){
          return false;
        }
      }
    }
    return true;
  }

  public Brett makeCopy(){
    Tile[][] brettnett=new Tile[size][size];
    for (int i=0;i<size;i++){
      for (int j=0;j<size;j++){
        brettnett[i][j]=new Tile(brett[i][j].tall);
      }
    }
    Brett brett1=new Brett(brettnett, size);
    brett1.returnPosition();
    return brett1;
  }

  public int heuristic(){
    int heuristic=0;
    for (int i=0;i<size;i++){
      for (int j=0;j<size;j++){
        int tall=brett[i][j].getTall();
        Boolean test=false;
        for (int k=0;k<size && !test;k++){
          for (int l=0;l<size && !test;l++){
            if (tall==goalbrett[k][l].getTall()){
              heuristic=heuristic+Math.abs(i-k)+Math.abs(j-l);
              test=true;
            }
          }
        }
      }
    }
    return heuristic;
  }
}
