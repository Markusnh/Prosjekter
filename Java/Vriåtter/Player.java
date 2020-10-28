import java.util.ArrayList;

class Player{
  private Hand hand;
  private String navn;


  public Player(String navn){
    this.hand=new Hand();
    this.navn=navn;
  }

  public void drawCard(){
    Card card=new Card(Game.random.nextInt(13),Game.navn[Game.random.nextInt(4)]);
    hand.addCard(card);
  }

  public void returnCard(Card card){
    hand.addCard(card);
  }
  public int getHandSize(){
    return hand.getHandSize();
  }

  public ArrayList<Card> getCards(){
    return hand.getCards();
  }

  public String getNavn(){
    return navn;
  }

  public boolean putCard(Card card){
    if (Playgame.pile.checkCard(card)){
      if (hand.cardOnHand(card)){
        Playgame.pile.insertCard(card, this);
        hand.removeCard(card);
        return true;
      }else{
        return false;
      }
    }else{
      return false;
    }
  }

  public void printCards(){
    System.out.print(navn + " sin tur\n\n" +navn +"'s haand:\n");
    ArrayList<Card> cards=this.getCards();
    for (int i=0;i<cards.size();i++){
      System.out.format("[%d]:  %s %s\n", i, cards.get(i).getCardNavn(), Playgame.nummer[cards.get(i).getCardNumber()]);
    }
  }
}
