import java.util.Random;
import java.util.Scanner;

class Game{
  public static String[] navn=new String[4];
  public static Random random=new Random();

  public static void main(String[] args){
    navn[0]="spar";
    navn[1]="ruter";
    navn[2]="hjerter";
    navn[3]="klover";

    System.out.println("how many players will play?");
    Scanner sc=new Scanner(System.in);
    int numberofplayers=sc.nextInt();
    Playgame game=new Playgame(numberofplayers);
    game.playGame();
  }
}

class Playgame{
  IO io=new IO();
  public static Pile pile;
  public static String[] nummer={"ess","2","3","4","5","6","7","8","9","10","knekt","dame","konge"};
  Player[] players;

  public Playgame(int numberOfPlayers){
    Scanner scanner=new Scanner(System.in);
    players=new Player[numberOfPlayers];
    for (int i=0;i<numberOfPlayers;i++){
      System.out.format("Player%d's navn:\n", i);
      String navn=scanner.next();
      players[i]=new Player(navn);
    }
    pile=new Pile();
  }


  public void playGame(){
    boolean empty=false;
    //this is the game loop, doesnt run if one of the player has zero cards
    while (!empty){

      //goes through all the players in turn
      for (Player player:players){

        //checks if the player has zero cards
        if (player.getHandSize()!=0){

          //prints out the showing card in pile
          System.out.println("\nthe visible card in pile is:");
          Card temp=pile.getShowingCard();
          System.out.format("%s  %s\n\n", temp.getCardNavn(), nummer[temp.getCardNumber()]);

          boolean played=false;
          int cardsindeks=0;
          int numberofpasses=0;
          while (!played){

            System.out.println("\nthe visible card in pile is:");
            System.out.format("%s  %s\n\n", temp.getCardNavn(), nummer[temp.getCardNumber()]);
            player.printCards();
            cardsindeks=io.chooseCard();

            //draws a new card if player enters pass or any other string
            if (cardsindeks==-1){
              numberofpasses++;
              player.drawCard();
              if (numberofpasses==3){
                played=true;
                System.out.println("\nthe visible card in pile is:");
                System.out.format("%s  %s\n\n", temp.getCardNavn(), nummer[temp.getCardNumber()]);
                player.printCards();
                cardsindeks=io.chooseCard();
                if (cardsindeks>-1){
                  Card card=player.getCards().get(cardsindeks);
                  if (!player.putCard(card)){
                    System.out.println("-------------------------------------\ninvalid card\n-------------------------------------");
                  }
                }
              }

              //tries to play the card, and if sucsesscfull breaks out of the while-loop
            }else{
              Card card=player.getCards().get(cardsindeks);
              if (player.putCard(card)){
                played=true;
              }else{
                System.out.println("--------------------------------------\ninvalid card, try again\n--------------------------------------");
              }
            }
          }
        }else{
          empty=true;
          System.out.println(player.getNavn()+" er vinnern!!");
          break;
        }
      }
    }
  }
}
