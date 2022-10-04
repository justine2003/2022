/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.caso_simulado_2;

import Ejercicio_2.Arreglos;
import javax.swing.JOptionPane;
/**
 *
 * @author Justin
 */
public class Caso_simulado_2 {
    
    static int ciclo = 0;
    
    public static void main(String[] args)
    {
       Ejercicio_1.Matrices E1 = new Ejercicio_1.Matrices();
       Ejercicio_2.FarmaciaMenu E2 = new Ejercicio_2.FarmaciaMenu();
     
        while (ciclo == 0) 
        {                   
            int n =  Integer.parseInt(JOptionPane.showInputDialog("1.Matrices"+"\n"
                                                                 +"2.Farmacia"+"\n"
                                                                 +"3.Salir"));
             
            switch (n) 
            {
                case 1:
                    E1.CargarMatriz();
                   break;
                    
                case 2:
                    E2.Menu();
                    break;
                    
                case 3:
                   ciclo = 1;
                   break;
            }
        }
    }
}
