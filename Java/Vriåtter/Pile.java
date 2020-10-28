class Pile{
  private Card showing;

  public Pile(){
    Card card=new Card(Game.random.nextInt(13), Game.navn[Game.random.nextInt(4)]);
    showing=card;
  }

  public boolean checkCard(Card card){
    boolean riktignummer=showing.getCardNumber()==card.getCardNumber();
    boolean riktigfarge=showing.getCardNavn().equals(card.getCardNavn());
    if (riktignummer){
      return true;
    }else if (riktigfarge){
      return true;
    }else{
      return false;
    }
  }

  public void insertCard(Card card, Player player){
    if (checkCard(card)){
      showing=card;
    }else{
      System.out.println("Error: card not valid for insertion and the card is returned");
      player.returnCard(card);
    }
  }

  public Card getShowingCard(){
    return showing;
  }
}
