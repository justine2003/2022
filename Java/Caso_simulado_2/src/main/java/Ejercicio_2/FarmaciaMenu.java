/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicio_2;

import javax.swing.JOptionPane;

/**
 *
 * @author Justin
 */
public class FarmaciaMenu
{
  int ciclo = 0;
    
 public void Menu()
 {
     AdministrarProductos AP = new AdministrarProductos();
     AdministrarCliente AC = new AdministrarCliente();
     Compras C = new Compras();
     Arreglos a = new Arreglos();
     ArreglosCliente Acliente = new ArreglosCliente();
     
     a.Codigo.add(0);
     a.Nombre.add("Vitaminas");
     a.Tipo.add("Pastilla");
     a.Precio.add(1500);
     a.Cantidad.add(98);
     
     Acliente.Nombre.add("Justin");
     Acliente.Cedula.add(123456789);
     Acliente.Correo.add("Correo@gmail.com");
     Acliente.Direccion.add("500MTros Norte");
     Acliente.Telefono.add(11875464);
     
    while(ciclo == 0)
    {
         int num = Integer.parseInt(JOptionPane.showInputDialog("1.Administracion de inventario"+"\n"
                                           +"2.Administracion de Cliente" +"\n"
                                           +"3.Compras"+"\n"
                                           +"4.Salir"));
         
         switch (num) 
         {
             case 1:
                AP.productos();
                break;
             case 2:
                AC.cliente();
                 break;
             case 3:
                 C.Compra();
                 break;
             case 4:
                 ciclo = 1;
                 break;
         }
    }
 }    
}
