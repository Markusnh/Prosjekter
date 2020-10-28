import java.util.Scanner;

class IO{


  public int chooseCard(){
    Scanner sc=new Scanner(System.in);
    System.out.println("enter the card number of the card you want to put in, enter 'pass' if no cards are valid or if you want another card");
    int nummer;
    try{
      nummer=sc.nextInt();
      return nummer;
    }catch(Exception e){
      nummer=-1;
      return nummer;
    }
  }
}
