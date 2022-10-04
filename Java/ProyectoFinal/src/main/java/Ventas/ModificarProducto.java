/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ventas;

import Consultas.Conexion;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import javax.swing.JOptionPane;

/**
 *
 * @author Justin
 */
public class ModificarProducto 
{
 
   public void modProducto(String Nombre, String Tipo, String Precio)
  {
      try 
      {
          Connection con = Conexion.getConexion();
          
          PreparedStatement p = con.prepareStatement("use [Tienda]");
          String f = String.valueOf(p.execute()); 
          
          PreparedStatement ps = con.prepareStatement("UPDATE productos SET Nombre='"+Nombre+"', Tipo='"+Tipo+"', Precio='"+Precio+"' WHERE Nombre='"+Nombre+"'");
          
          ps.executeUpdate();
          
          JOptionPane.showMessageDialog(null,"Producto modificado exitosamente");
      }
      catch (SQLException e) 
      {
          JOptionPane.showMessageDialog(null, e.toString());
      }
  }
}
