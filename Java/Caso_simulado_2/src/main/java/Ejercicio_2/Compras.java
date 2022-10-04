/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicio_2;

import java.util.ArrayList;
import javax.swing.JOptionPane;

/**
 *
 * @author Justin
 */
public class Compras 
{
    ArreglosCliente AC = new ArreglosCliente();
    Arreglos A = new Arreglos();
    
    ArrayList<String> listacompras = new ArrayList<>();
    
    int total;
    int cantidad;
    
    int ciclo = 0;
    
    String TNombre;
    int TCedula;
    String TCorreo;
    String TDireccion;
    int TTelefono;
    
 public void Compra()
 {
          TCedula = Integer.parseInt(JOptionPane.showInputDialog("Ingrese su cedula")); 
          
          Boolean Bcedula = AC.Cedula.contains(TCedula);
          
          if(Bcedula == true)
          {
              Usuario();
     
              while(ciclo == 0)
              {
                 articulo();
                 ciclo = JOptionPane.showConfirmDialog(null,"Desea añadir otro articulo");
              }
              factura();
          }
          else
          {
              JOptionPane.showMessageDialog(null,"Usuario no encontrado");
          }      
 }  
 
 public void Usuario()
 {
     int i = 0;
     
     while(TCedula != AC.Cedula.get(i))
     {
         i++;
     }
     
     TNombre = AC.Nombre.get(i);
     TCorreo = AC.Correo.get(i);
     TDireccion = AC.Direccion.get(i);
     TTelefono = AC.Telefono.get(i);
     
 }
 
 public void articulo()
 {
     int i = 0;
     boolean b = true;
     
     int codigo = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el codigo del producto qe desea agregar a la lista"));
     
     while(A.Codigo.get(i) != codigo && b == true)
     {
         i++;
         if(i == A.Codigo.size())
         {
             b = false;
         }
     }   
     
    cantidad = Integer.parseInt(JOptionPane.showInputDialog("Ingrese la cantidad del producto que va a comprar"));
    
    listacompras.add(A.Nombre.get(i));
    A.Cantidad.set(i,A.Cantidad.get(i)-cantidad);
    total += A.Precio.get(i) * cantidad;
 }
 
 public void factura()
 {
     JOptionPane.showMessageDialog(null,"Factura"+"\n"
                                        +"Productos: "+listacompras+"\n"
                                        +"Cantidad: "+cantidad+"\n"
                                        +"Total: "+total);
 }
}
