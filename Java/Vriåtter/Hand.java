import java.util.Random;
import java.util.ArrayList;

class Hand{
  private ArrayList<Card> cards=new ArrayList<Card>();


  public Hand(){
    for (int i=0;i<5;i++){
      cards.add(new Card(Game.random.nextInt(13),Game.navn[Game.random.nextInt(4)]));
    }
  }

  public void addCard(Card card){
    cards.add(card);
  }

  public ArrayList<Card> getCards(){
    return cards;
  }

  public void removeCard(Card card){
    for (int i=0;i<getHandSize();i++){
      if (cards.get(i).getCardNumber()==card.getCardNumber()){
        if (cards.get(i).getCardNavn().equals(card.getCardNavn())){
          cards.remove(i);
        }
      }
    }
  }

  public boolean cardOnHand(Card card){
    for (int i=0;i<getHandSize();i++){
      if (cards.get(i).getCardNumber()==card.getCardNumber()){
        if (cards.get(i).getCardNavn().equals(card.getCardNavn())){
          return true;
        }
      }
    }
    return false;
  }

  public int getHandSize(){
    return cards.size();
  }
}
