class Tile{
  int tall;

  public Tile(int tall){
    this.tall=tall;
  }

  public String toString(){
    return Integer.toString(tall);
  }

  public int getTall(){
    return tall;
  }
}
