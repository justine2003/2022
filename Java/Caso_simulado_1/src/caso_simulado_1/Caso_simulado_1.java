/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package caso_simulado_1;

import javax.swing.JOptionPane;

/**
 *
 * @author Justin
 */
public class Caso_simulado_1 {

    
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
      Parte_1 parte_1 = new Parte_1();
      Parte_2 parte_2 = new Parte_2();
      Parte_3 parte_3 = new Parte_3();
      
      int ciclo = 1; 
      
      while (ciclo == 1)
      {
      
      int decision = Integer.parseInt(JOptionPane.showInputDialog(null,"Seleccione un numero"+'\n'
              +"1.Mensaje"+'\n'+"2.Limonada"+'\n'+"3.Beca"+'\n'+"4.Alquieler de autos"+'\n'+"5.Salir"));
      
      if (decision == 1) parte_1.Mensaje();
      if (decision == 2) parte_1.Limonda();
      if (decision == 3) parte_2.beca();
      if (decision == 4) parte_3.Alquiler();
      if (decision == 5) ciclo = 0;
      
      }
     }
}
