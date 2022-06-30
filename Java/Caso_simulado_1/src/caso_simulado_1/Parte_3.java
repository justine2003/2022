/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package caso_simulado_1;

import java.net.InterfaceAddress;
import javax.swing.JOptionPane;

/**
 *
 * @author Justin
 */
public class Parte_3 
{
 public void Alquiler()
 {
     String vehiculo = "";
     int Tipovehiculo;
     int dias;
     int precio = 0;
     
     int continuar = 0;
     
     while (continuar == 0)
     {    
     Tipovehiculo = Integer.parseInt(JOptionPane.showInputDialog(null,"Bienvenidoa a la renta de autos" + '\n'
                                                             +"1.Nisan precio: 2500$"+'\n'
                                                             +"2.Toyota precio: 1500$" +'\n'
                                                             +"3.Hyundai precio: 500$"+'\n'
                                                             +"4.Subaru precio: 200$"+'\n'));
     
     dias = Integer.parseInt(JOptionPane.showInputDialog(null,"Ingrese la cantidad de dias que desea rentar el auto"));
     
     if (Tipovehiculo == 1) vehiculo = "Nisan"; precio = 2500;
     if (Tipovehiculo == 2) vehiculo = "Toyota"; precio = 1500;
     if (Tipovehiculo == 3) vehiculo = "Hyundai"; precio = 500;
     if (Tipovehiculo == 4) vehiculo = "Subaru"; precio = 200;
     
     if (dias > 10)
     {
         conDescuento(dias, vehiculo,precio);
     }
     else
     {
         sinDescuento(dias, vehiculo, precio);
     }
     continuar = JOptionPane.showConfirmDialog(null,"Desea rentar otro auto");
     }
     JOptionPane.showMessageDialog(null,"Gracias por usar nuestro servicio");
 }   

public void conDescuento(int dias, String Vehiculo,int precio)
{
  double IVA;
  int descuento;
  int Total;
  double TotalIVA;
  
  descuento = (int)(precio * 0.15);
  Total = precio - descuento;
  IVA = Total * 0.13;
  TotalIVA = (double)(Total - IVA);
  
  JOptionPane.showMessageDialog(null,"Fatura"+'\n'
                                +"Vehiculo rentado: "+Vehiculo+'\n'
                                +"Dias que rento el vehiculo: "+dias+'\n'
                                +"Descuetno: 15%"+'\n'
                                +"Total a pagar con descuento: "+Total+"$"+'\n'
                                +"Total a pagar con IVA: "+TotalIVA+"$");
}
 
public void sinDescuento(int dias, String Vehiculo,int precio)
{
   double IVA;
  int Total;
  double TotalIVA;
  
  Total = precio;
  IVA = Total * 0.13;
  TotalIVA = (double)(Total - IVA);
  
  JOptionPane.showMessageDialog(null,"Fatura"+'\n'
                                +"Vehiculo rentado: "+Vehiculo+'\n'
                                +"Dias que rento el vehiculo: "+dias+'\n'
                                +"Total a pagar: "+Total+"$"+'\n'
                                +"Total a pagar con IVA: "+TotalIVA+"$");
}
}
