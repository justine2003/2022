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
public class AdministrarProductos 
{
 int ciclo = 0;
 
Arreglos a = new Arreglos();
 
static ArrayList<Integer> Codigo = new ArrayList<>();
static ArrayList<String> Nombre = new ArrayList<>();
static ArrayList<String> Tipo = new ArrayList<>();
static ArrayList<Integer> Precio = new ArrayList<>();
static ArrayList<Integer> Cantidad = new ArrayList<>();     

 public void productos()
 {     
    
     Codigo.addAll(a.Codigo);
     Nombre.addAll(a.Nombre);
     Tipo.addAll(a.Tipo);
     Precio.addAll(a.Precio);
     Cantidad.addAll(a.Cantidad);
     
    while(ciclo == 0)
    {
       int num = Integer.parseInt(JOptionPane.showInputDialog("1.Ingresar datos"+"\n"
                                                              +"2.Modificar inventario"+"\n"
                                                              +"3.Ver"+"\n"
                                                              +"4.Eliminar"+"\n"
                                                              +"5.Salir"));
       
        switch (num)
        {
            case 1:
                Ingresar();
               break;
                
            case 2:
                Modificar();
              break;
                
            case 3:
                Ver();
              break;
                
            case 4:
               Eliminar();
               break;
                
            case 5:
                datos();
                ciclo = 1;
             break;
        }
    }
 }
 
 public void Ingresar()
 {
   Nombre.add(JOptionPane.showInputDialog("Ingrese el nombre del producto"));
   Tipo.add(JOptionPane.showInputDialog("Ingrese EL tipo del producto"));
   Precio.add(Integer.parseInt(JOptionPane.showInputDialog("Ingrese el precio")));
   Cantidad.add(Integer.parseInt(JOptionPane.showInputDialog("Ingrese la cantidad en inventario del producto")));
   Codigo.add(Integer.parseInt(JOptionPane.showInputDialog("Ingrese le codigo del produto")));
 }
 
public void Modificar()
{
    int codigoR = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el codigo del producto que desea modificar"));
    
    int i = 0;
    
    while(Codigo.get(i) != codigoR)
    {
        i++;
    }
    
    int opcion = Integer.parseInt(JOptionPane.showInputDialog("1.Nombre"+"\n"
                                                              +"2.Tipo"+"\n"
                                                              +"3.Precio"+"\n"
                                                              +"4.Catidad"+"\n"));
    
    switch (opcion)
    {
        case 1:
           String nombre = JOptionPane.showInputDialog("Ingrese el nuevo nombre");
           Nombre.set(i,nombre);
            
        case 2:
           String tipo = JOptionPane.showInputDialog("Ingrese el nuevo tipo del producto");
           Tipo.set(i,tipo);
           
        case 3:
            int precio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el precio"));
            Precio.set(i, precio);
                    
        case 4:
            int cantidad = Integer.parseInt(JOptionPane.showInputDialog("Ingrese la nueva cantidad"));
            Cantidad.set(i, cantidad);
            
       a.Codigo.addAll(Codigo);
       a.Nombre.addAll(Nombre);
       a.Tipo.addAll(Tipo);
       a.Precio.addAll(Precio);
       a.Cantidad.addAll(Cantidad);
    }
}

public void Ver()
{
   JOptionPane.showMessageDialog(null,Codigo+"\n"
                                    +Nombre+"\n"
                                    +Tipo+"\n"
                                    +Precio+"\n"
                                    +Cantidad+"\n");
}

public void Eliminar()
{
  int code = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el codigo del producto que desea elimianr"));
  
  int i = 0;
  
  while(Codigo.get(i) != code)
  {
      i++;
  }
  
  Codigo.remove(Codigo.get(i));
  Nombre.remove(Nombre.get(i));
  Tipo.remove(Tipo.get(i));
  Precio.remove(Precio.get(i));
  Cantidad.remove(Cantidad.get(i));
  
   a.Codigo.addAll(Codigo);
   a.Nombre.addAll(Tipo);
   a.Tipo.addAll(Tipo);
   a.Precio.addAll(Precio);
   a.Cantidad.addAll(Cantidad);  
}

public void datos()
{
       a.Codigo.addAll(Codigo);
       a.Nombre.addAll(Tipo);
       a.Tipo.addAll(Tipo);
       a.Precio.addAll(Precio);
       a.Cantidad.addAll(Cantidad);
}
}
