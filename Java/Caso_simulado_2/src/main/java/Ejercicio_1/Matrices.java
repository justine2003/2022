/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicio_1;

import javax.swing.JOptionPane;

/**
 *
 * @author Justin
 */
public class Matrices 
{
   int numeros[][] = new int [4][3]; 
   int par;
   int impar;
   int mayor;
   int menor;
  public void CargarMatriz()
  {
      for (int i=0; i<4;i++)
      {
          for (int u=0; u<3;u++)
          {
              int numM = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el numero con el que desea llenar la matriz"));
              
              numeros[i][u] = numM;
          } 
      } 
      ParImpar();
      Mayor();
      Menor();
      
      JOptionPane.showMessageDialog(null,"La cantidad de numeros pares es: "+par+"\n"
                                    +"la cantidad de numeros impares es: "+impar+"\n"
                                    +"el numero mayor es: "+mayor+"\n"
                                    +"el numero menor es: "+menor);
  }
  
  public void ParImpar()
  {
   for(int i=0; i<4;i++)
   {
       for(int u=0;u<3;u++)
       {
           if(numeros[i][u]%2==0)
           {
               par++;
           }
           else
           {
               impar++;
           }
       }
   }   
  }
  
  public void Mayor()
  {
     mayor = numeros[0][0];      
     for(int i=0; i<4;i++)
   {
       for(int u=0;u<3;u++)
       {
           if(numeros[i][u] > mayor)
           {
               mayor = numeros[i][u];
           }
       }
   }   
  }
  
  public void Menor()
  {
   menor = numeros[0][0]; 
   for(int i=0; i<4;i++)
   {
       for(int u=0;u<3;u++)
       {
           if(numeros[i][u] < menor)
           {
               menor = numeros[i][u];
           }
       }
   }   
  }
}
