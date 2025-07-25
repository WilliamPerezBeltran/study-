#include <iostream>

using namespace std;

void pro_aritmetica(int inicio, int factor, int tam);

int main()
{
    int inicio, factor, tam;
    cout<<"escriba el numero con el que empezara la pogresion: ";
    cin>>inicio;
    cout<<"escriba el factor para la progresion: ";
    cin>>factor;
    cout<<"cuantos numeros quieres que la progresion muestre: ";
    cin>>tam;
    
    pro_aritmetica(inicio,factor,tam);
    
}

void pro_aritmetica(int inicio, int factor, int tam){
    int cont;
    cout<<"la progresion aritmetica es: ";
    while(cont<tam){
        cout<<inicio<<", ";
        inicio+=factor;
        cont+=1;
    }
}