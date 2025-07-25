#include <iostream>
using namespace std;

int main()
{ 
   // char i;
   string texto;
   int movimientos,cont=0;
   char alfabeto[26], cifrado[26],texto_nuevo[26];
   for( char i='a';i<='z';i++){
       alfabeto[cont]=i;
       cont+=1;
   }

   cout<<"cuantos movimientos tendra su alfabeto: ";
   cin>>movimientos;
   
   if(movimientos<=26){
    for(int j=0; j<26;j++){
       cifrado[j]=alfabeto[(j+movimientos)%26];
    }   
   }else{
       cout<<"no se puede el movimiento es mayor que el alfabeto"<<endl;
   }
   
   cout<<"escriba el texto que va a convertir en cifrado:"<<endl;
   cin>>texto; 
   //abcd--cdef
   for(int z=0;z<texto.size();z++){
       for(int x=0;x<26;x++){
           if(alfabeto[x]==texto[z]){
               cout<<cifrado[x];
           }
       }
       
   }
  }
