
import java.util.Scanner;
import javax.swing.JOptionPane;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/**
 *
 * @author Justin
 */
public class SalarioTravajador {

    /**
     * @param args the command line arguments
     */
    
    
    public static void main(String[] args) 
    {
       String nombre;
       double salario;
       double total;
       
       nombre = JOptionPane.showInputDialog("Ingrese su nombre");
       
       salario = Double.parseDouble(JOptionPane.showInputDialog("Ingrese su salario"));

        total = salario + (salario*0.1);
        
        JOptionPane.showInternalMessageDialog(null,"Estimado: "+nombre+"  "+"Su salario: "+total);
    }
    
}
