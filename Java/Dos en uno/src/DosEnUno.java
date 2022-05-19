
import javax.swing.JOptionPane;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/**
 *
 * @author Justin
 */
public class DosEnUno {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
        String Nombre;
        int edad;
        
      //System.out.println("Su nombre es "+nombre + "\n" + "Su edad es " + edad);
      
      Nombre = JOptionPane.showInputDialog("Ingrese su nombre");
      edad = Integer.parseInt(JOptionPane.showInputDialog("Ingrese su edad"));
      
      JOptionPane.showMessageDialog(null,"Su nombre es "+Nombre + "\n" + "Su edad es "+ edad);
    }
    
}
