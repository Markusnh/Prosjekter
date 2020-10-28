class Card{
  int card_number;
  String colour;

  public Card(int card_number, String colour){
    this.card_number=card_number;
    this.colour=colour;
  }
  public int getCardNumber(){
    return card_number;
  }

  public String getCardNavn(){
    return colour;
  }
}
