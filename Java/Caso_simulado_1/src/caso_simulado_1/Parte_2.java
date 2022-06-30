/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package caso_simulado_1;

import javax.swing.JOptionPane;

/**
 *
 * @author Justin
 */
public class Parte_2 
{
  public void beca()
  {     
      int cantMateria;
      
      int servicio;
      String calificacion;
      
      int nota1;
      int nota2;
      int nota3;
      int nota4;
      
     cantMateria = Integer.parseInt(JOptionPane.showInputDialog(null,"Bienvenido a el programa de becas Fidelitas ingrese la catidad de materia que lleva"));
     
     if (cantMateria < 4)
     {
         Noapto();
     }
     else
     {
      nota1 = Integer.parseInt(JOptionPane.showInputDialog(null,"Ingrese el promedio de matematicas"));
      nota2 = Integer.parseInt(JOptionPane.showInputDialog(null,"Ingrese el promedio de programacion"));
      nota3 = Integer.parseInt(JOptionPane.showInputDialog(null,"Ingrese el promedio de informatica"));
      nota4 = Integer.parseInt(JOptionPane.showInputDialog(null,"Ingrese el promedio de fundamentos de la computacion "));
     
      if (nota1 >= 90 && nota2 >= 90 && nota3 >= 90 && nota4 >= 90) apto();
      
      if (nota1 <= 70 || nota2 <= 70 || nota3 <= 70 || nota4 <= 70) Noapto();      
      
      if (nota1 >= 85 && nota2 >= 85 && nota3 >= 85 && nota4 >= 85) 
      {
        servicio = JOptionPane.showConfirmDialog(null,"Fue asistente durante el cuatrimestre?");
        
        if (servicio == 0)
        {
            calificacion = JOptionPane.showInputDialog(null,"Ingrese la calificacion que optubo como asistente");
            
            if (calificacion.equals("A") || calificacion.equals("B"))
            { 
              apto();
            }
            else
            {
                Noapto();
            }
        }
        else
        {
          Noapto();
        }
      }
     }
  }    
  
  public void Noapto()
  {
      JOptionPane.showMessageDialog(null,"Lo sentimos pero no es apto para la beca");
  }
  
  public void apto()
  {
      JOptionPane.showMessageDialog(null,"Es apto para la beca");
  }
}
