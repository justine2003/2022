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
public class AdministrarCliente 
{
   int ciclo = 0;
   
  ArreglosCliente AC = new ArreglosCliente();
    
  ArrayList<String> Nombre =  new ArrayList<>();
  ArrayList<Integer> Cedula = new ArrayList<>();
  ArrayList<String> Correo = new ArrayList<>();
  ArrayList<String> Direccion = new ArrayList<>();
  ArrayList<Integer> Telefono = new ArrayList<>();
    
 public void cliente()
 {
     Nombre.addAll(AC.Nombre);
     Cedula.addAll(AC.Cedula);
     Correo.addAll(AC.Correo);
     Direccion.addAll(AC.Direccion);
     Telefono.addAll(AC.Telefono);
     
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
                ver();
              break;
                
            case 4:
               Eliminar();
               break;
                
            case 5:
                ciclo = 1;
             break;
        }
    }
 }   
 
 public void Ingresar()
 {
   Nombre.add(JOptionPane.showInputDialog("Ingrese su nombre"));
   Cedula.add(Integer.parseInt(JOptionPane.showInputDialog("Ingrese su cedula")));
   Correo.add(JOptionPane.showInputDialog("Ingrese su correo"));
   Direccion.add(JOptionPane.showInputDialog("Ingrese su direcion"));
   Telefono.add(Integer.parseInt(JOptionPane.showInputDialog("Ingrese su telefono")));
 }
 
 public void Modificar()
 {
      String nombreR = JOptionPane.showInputDialog("Ingrese el nombre del usuario que desea modificar");
    
    int i = 0;
    
    while(Nombre.get(i) != nombreR)
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
           int cedula = Integer.parseInt(JOptionPane.showInputDialog("Ingrese la nueva cedula"));
           Cedula.set(i,cedula);
           
        case 3:
            String correo = JOptionPane.showInputDialog("Ingrese el precio");
            Correo.set(i, correo);
                    
        case 4:
            String direcion = JOptionPane.showInputDialog("Ingrese su nueva direccion");
            Direccion.set(i,direcion);
            
       AC.Nombre.addAll(Nombre);
       AC.Cedula.addAll(Cedula);
       AC.Correo.addAll(Correo);
       AC.Direccion.addAll(Direccion);
       AC.Telefono.addAll(Telefono);
    }
 }
 
 public void ver()
 {
       JOptionPane.showMessageDialog(null,Nombre+"\n"
                                    +Cedula+"\n"
                                    +Correo+"\n"
                                    +Direccion+"\n"
                                    +Telefono+"\n");
 }
 
public void Eliminar()
{
  String nombre = JOptionPane.showInputDialog("Ingrese el nombre que busca");
  
  int i = 0;
  
  while(Nombre.get(i) != nombre)
  {
      i++;
  }
  
  Nombre.remove(Nombre.get(i));
  Cedula.remove(Cedula.get(i));
  Correo.remove(Correo.get(i));
  Direccion.remove(Direccion.get(i));
  Telefono.remove(Telefono.get(i));
  
   AC.Nombre.addAll(Nombre);
   AC.Cedula.addAll(Cedula);
   AC.Correo.addAll(Correo);
   AC.Direccion.addAll(Direccion);
   AC.Telefono.addAll(Telefono);  
}
}
