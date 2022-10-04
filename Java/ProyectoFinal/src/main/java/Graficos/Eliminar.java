/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Graficos;

import Consultas.Conexion;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import javax.swing.JOptionPane;

/**
 *
 * @author Justin
 */
public class Eliminar
{
  public boolean Eliminar(String Nombre)
  {
        try 
     {
         Connection con = Conexion.getConexion();
         PreparedStatement p = con.prepareStatement("use[Tienda]");
         String f = String.valueOf(p.execute());
     
         PreparedStatement ps = con.prepareStatement("DELETE FROM RegistroVentas WHERE Nombre = ?");
     
         int respuesta = JOptionPane.showConfirmDialog(null,"Realmente quieres eliminar este reporte de venta","Eliminar Reporte de ventas",JOptionPane.YES_NO_OPTION,JOptionPane.QUESTION_MESSAGE);
         
         if(respuesta == 0)
         {
         ps.setString(1, Nombre);
         ps.execute();
         JOptionPane.showMessageDialog(null,"Se elimino el usuaio exitosamente","Eliminacion",JOptionPane.INFORMATION_MESSAGE);
         return true; 
         }
         else
         {
             return false;
         }
     }
     catch (SQLException e) 
     {
         JOptionPane.showMessageDialog(null, e.toString());
         return false;
     }
     
  }
}
