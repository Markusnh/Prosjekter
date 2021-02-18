#include <iostream>
#include <fstream>
#include <math.h>
#include <vector>

using namespace std;

class Myclass{
  public:
    static int sum;
    static bool same;
    static vector<int> checked;
    string shuffle_l3(string input);
    string shuffle_l4(string input);
    string shuffle_l5(string input);
    string shuffle_l6(string input);
    string shuffle_l7(string input);
    bool test_prime(int number);
    void shuffle2(string input);
    void divide_3_as(string input);
    void divide_4_as(string input);
    void divide_5_as(string input);
    void divide_6_as(string input);
    void divide_7_as(string input);
};

bool test_prime(int number){
  if (number==1){
    return false;
  }else if (number==2){
    return true;
  }
  if (number<=0){
    return false;
  }else if (number%2==0){
    return false;
  }
  double x=sqrt(number);
  int y=(int) x;
  for (int i=3;i<=y;i=i+2){
    if (number%i==0){
      return false;
    }
  }
  return true;
}


string shuffle_l3(string input){
  //--------------------------------------------
  if (test_prime(stoi(input))){
    if (Myclass::same){
      bool notfound=true;
      for (int i=0;i<Myclass::checked.size();i++){
        if (Myclass::checked[i]==stoi(input)){
          notfound=false;
          break;
        }
      }
      if (notfound){
        Myclass::sum++;
        Myclass::checked.push_back(stoi(input));
      }
    }else{
      Myclass::sum++;
    }
  }
  for (int i=0;i<2;i++){
    char temp=input[input.size()-2];
    input[input.size()-2]=input[input.size()-1];
    input[input.size()-1]=temp;
    //--------------------------------------------
    if (test_prime(stoi(input))){
      if (Myclass::same){
        bool notfound=true;
        for (int i=0;i<Myclass::checked.size();i++){
          if (Myclass::checked[i]==stoi(input)){
            notfound=false;
            break;
          }
        }
        if (notfound){
          Myclass::sum++;
          Myclass::checked.push_back(stoi(input));
        }
      }else{
        Myclass::sum++;
      }
    }
    temp=input[input.size()-1];
    input[input.size()-1]=input[input.size()-3];
    input[input.size()-3]=temp;
    //--------------------------------------------
    if (test_prime(stoi(input))){
      if (Myclass::same){
        bool notfound=true;
        for (int i=0;i<Myclass::checked.size();i++){
          if (Myclass::checked[i]==stoi(input)){
            notfound=false;
            break;
          }
        }
        if (notfound){
          Myclass::sum++;
          Myclass::checked.push_back(stoi(input));
        }
      }else{
        Myclass::sum++;
      }
    }
  }
  char temp=input[input.size()-2];
  input[input.size()-2]=input[input.size()-1];
  input[input.size()-1]=temp;
  //--------------------------------------------
  if (test_prime(stoi(input))){
    if (Myclass::same){
      bool notfound=true;
      for (int i=0;i<Myclass::checked.size();i++){
        if (Myclass::checked[i]==stoi(input)){
          notfound=false;
          break;
        }
      }
      if (notfound){
        Myclass::sum++;
        Myclass::checked.push_back(stoi(input));
      }
    }else{
      Myclass::sum++;
    }
  }
  return input;
}

string shuffle_l4(string input){
  input=shuffle_l3(input);
  char temp;
  for (int j=0;j<2;j++){
    temp=input[input.size()-1];
    input[input.size()-1]=input[input.size()-4];
    input[input.size()-4]=temp;
    input=shuffle_l3(input);
  }
  temp=input[input.size()-2];
  input[input.size()-2]=input[input.size()-4];
  input[input.size()-4]=temp;
  input=shuffle_l3(input);
  return input;
}

string shuffle_l5(string input){
  input=shuffle_l4(input);
  for (int j=0;j<4;j++){
    char temp=input[input.size()-1];
    input[input.size()-1]=input[input.size()-5];
    input[input.size()-5]=temp;
    input=shuffle_l4(input);
  }
  return input;
}

string shuffle_l6(string input){
  input=shuffle_l5(input);
  for (int k=0;k<2;k++){
    char temp=input[input.size()-1];
    input[input.size()-1]=input[input.size()-6];
    input[input.size()-6]=temp;
    input=shuffle_l5(input);
  }
  char temp;
  for (int k=2;k<5;k++){
    temp=input[input.size()-k];
    input[input.size()-k]=input[input.size()-6];
    input[input.size()-6]=temp;
    input=shuffle_l5(input);
  }
  return input;
}

string shuffle_l7(string input){
  input=shuffle_l6(input);
  char temp;
  for (int k=0;k<6;k++){
    temp=input[input.size()-1];
    input[input.size()-1]=input[input.size()-7];
    input[input.size()-7]=temp;
    input=shuffle_l6(input);
  }
  return input;
}

void shuffle2(string input){
  //--------------------------------------------
  if (test_prime(stoi(input))){
    if (Myclass::same){
      bool notfound=true;
      for (int i=0;i<Myclass::checked.size();i++){
        if (Myclass::checked[i]==stoi(input)){
          notfound=false;
          break;
        }
      }
      if (notfound){
        Myclass::sum++;
        Myclass::checked.push_back(stoi(input));
      }
    }else{
      Myclass::sum++;
    }
  }
  char temp=input[0];
  input[0]=input[1];
  input[1]=temp;
  //--------------------------------------------
  if (test_prime(stoi(input))){
    if (Myclass::same){
      bool notfound=true;
      for (int i=0;i<Myclass::checked.size();i++){
        if (Myclass::checked[i]==stoi(input)){
          notfound=false;
          break;
        }
      }
      if (notfound){
        Myclass::sum++;
        Myclass::checked.push_back(stoi(input));
      }
    }else{
      Myclass::sum++;
    }
  }
}

void divide_3_as(string input){
  string output;
  //oners
  for (int i=0;i<input.size();i++){
    //--------------------------------------------
    if (test_prime(stoi(input.substr(i,1)))){
      if (Myclass::same){
        bool notfound=true;
        for (int j=0;j<Myclass::checked.size();j++){
          if (Myclass::checked[j]==stoi(input.substr(i,1))){
            notfound=false;
            break;
          }
        }
        if (notfound){
          Myclass::sum++;
          Myclass::checked.push_back(stoi(input.substr(i,1)));
        }
      }else{
        Myclass::sum++;
      }
    }
  }
  //twoers
  for (int i=1;i<input.size();i++){
    for (int j=0;j<(input.size()-i);j++){
      output="";
      output.append(input.substr(j,1));
      output.append(input.substr(j+i,1));
      shuffle2(output);
    }
  }
}


void divide_4_as(string input){
  string output;
  divide_3_as(input);
  //threers
  for (int i=1;i<input.size();i++){
    for (int j=1;j<(input.size()-i);j++){
      for (int k=0;k<(input.size()-i-j);k++){
        output="";
        output.append(input.substr(k,1));
        output.append(input.substr(k+j,1));
        output.append(input.substr(k+j+i,1));
        shuffle_l3(output);
      }
    }
  }
}


void divide_5_as(string input){
  string output;
  divide_4_as(input);
  //fourers
  for (int i=1;i<input.size();i++){
    for (int j=1;j<(input.size()-i);j++){
      for (int k=1;k<(input.size()-i-j);k++){
        for (int l=0;l<(input.size()-i-j-k);l++){
            output="";
            output.append(input.substr(l,1));
            output.append(input.substr(l+k,1));
            output.append(input.substr(l+k+j,1));
            output.append(input.substr(l+k+j+i,1));
            shuffle_l4(output);
        }
      }
    }
  }
}



void divide_6_as(string input){
  string output;
  divide_5_as(input);
  //fivers
  for (int i=1;i<input.size();i++){
    for (int j=1;j<(input.size()-i);j++){
      for (int k=1;k<(input.size()-i-j);k++){
        for (int l=1;l<(input.size()-i-j-k);l++){
          for (int o=0;o<(input.size()-i-j-k-l);o++){
            output="";
            output.append(input.substr(o,1));
            output.append(input.substr(o+l,1));
            output.append(input.substr(o+l+k,1));
            output.append(input.substr(o+l+k+j,1));
            output.append(input.substr(o+l+k+j+i,1));
            shuffle_l5(output);
          }
        }
      }
    }
  }
}


void divide_7_as(string input){
  string output;
  divide_6_as(input);
  //sixers
  for (int i=1;i<input.size();i++){
    for (int j=1;j<(input.size()-i);j++){
      for (int k=1;k<(input.size()-i-j);k++){
        for (int l=1;l<(input.size()-i-j-k);l++){
          for (int o=1;o<(input.size()-i-j-k-l);o++){
            for (int m=0;m<(input.size()-i-j-k-l-o);m++){
              output="";
              output.append(input.substr(m,1));
              output.append(input.substr(m+o,1));
              output.append(input.substr(m+o+l,1));
              output.append(input.substr(m+o+l+k,1));
              output.append(input.substr(m+o+l+k+j,1));
              output.append(input.substr(m+o+l+k+j+i,1));
              shuffle_l6(output);
            }
          }
        }
      }
    }
  }
}


int Myclass::sum=0;
bool Myclass::same;
vector<int> Myclass::checked;

int main(){
  //ifstream filereader("sample.in");
  Myclass u;
  int k;
  int number;
  string N;
  Myclass::same=false;
  cout << "Enter a number for how many numbers you want to test for:";
  cin >> k;
  bool first=true;



  for (int i=0;i<k;i++){
    Myclass::checked.clear();
    if (first){
      first=false;
    }else{
      cout << "\n";
    }
    Myclass::same=true;
    cout << "Enter a number you want to test for:";
    cin >> N;
    bool itssame=false;
    for (int i=0;i<N.size();i++){
      for (int j=i+1;j<N.size();j++){
        if (N[i]==N[j]){
          itssame=true;
          break;
        }
      }
      if (itssame){
        break;
      }
    }
    if (itssame){
      Myclass::same=true;
    }
    Myclass::sum=0;
    int length=N.size();
    number=stoi(N);
    if (length==1){
      if (test_prime(number)){
        cout << "1";
      }else{
        cout << "0";
      }
    }else if (length==2){
      if ((N[0]=='0') || (N[1]=='0')){
        for (int i=0;i<2;i++){
          if (test_prime(stoi(N.substr(i,1)))){
            Myclass::sum++;
          }
        }
      }else{
        if (N[0]!=N[1]){
          for (int i=0;i<2;i++){
            if (test_prime(stoi(N.substr(i,1)))){
              Myclass::sum++;
            }
          }
        }else{
          if (test_prime(stoi(N.substr(0,1)))){
            Myclass::sum++;
          }
        }
        if (N[0]!=N[1]){
          if (test_prime(number)){
            Myclass::sum++;
          }
          char temp=N[0];
          N[0]=N[1];
          N[1]=temp;
          if (test_prime(stoi(N))){
            Myclass::sum++;
          }
        }else{
          if (test_prime(number)){
            Myclass::sum++;
          }
        }
      }
      cout << Myclass::sum;

    }else if (length==3){
      shuffle_l3(N);
      divide_3_as(N);
      cout << Myclass::sum;
    }else if (length==4){
      shuffle_l4(N);
      divide_4_as(N);
      cout << Myclass::sum;
    }else if (length==5){
      shuffle_l5(N);
      divide_5_as(N);
      cout << Myclass::sum;
    }else if (length==6){
      shuffle_l6(N);
      divide_6_as(N);
      cout << Myclass::sum;
    }else if (length==7){
      shuffle_l7(N);
      divide_7_as(N);
      cout << Myclass::sum;
    }else{
      cout << "Must input a number that is no longer than 7 digits";
    }
  }
  return 0;
}
