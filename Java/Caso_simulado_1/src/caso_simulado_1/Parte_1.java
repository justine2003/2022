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
public class Parte_1 {
 
   public void Mensaje()
   {       
    JOptionPane.showMessageDialog(null,"Bienvenido al examen de introduccion a la  programacion"+'\n'
         +"Nombre del estudiante: Justin Gilberto Camacho Garcia"+'\n'+ "Cedula: 1 1875 0568" + '\n'
         +"Nombre del profesor: Roberth Castro Méndez");
   }
    
   public void Limonda()
   {      
       int PagoPaco;
       int PagoLuis;
       int PagoHugo;
       
       double preciolimonada = 10;
       
       double cantLimonada = Integer.parseInt(JOptionPane.showInputDialog(null,"Ingrese la cantidad total de limonada vendida"));
       
       double total = preciolimonada * cantLimonada;
       
       PagoPaco = (int)(total * 0.30);
       PagoLuis = (int)(total * 0.30);
       PagoHugo = (int)(total * 0.40);
       
       JOptionPane.showMessageDialog(null,"EL ingreso total es de: "+total+'\n'
                                     +"Paco gano: "+PagoPaco+'\n'
                                     +"Luis gano: "+PagoLuis+'\n'
                                     +"Hugo gano: "+PagoHugo);
   }
   
}
