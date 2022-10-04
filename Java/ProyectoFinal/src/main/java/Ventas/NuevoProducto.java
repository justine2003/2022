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
public class NuevoProducto 
{
   public static void Nroducto(String Nombre, String Tipo, String Precio)
   {
       try 
       {
           Connection con = Conexion.getConexion();
           
           PreparedStatement p = con.prepareStatement("use [Tienda]");
           String f = String.valueOf(p.execute()); 
           
           PreparedStatement ps = con.prepareStatement("INSERT INTO productos (Nombre,Precio,Tipo) Values (?,?,?)");
           
           ps.setString(1, Nombre);
           ps.setString(2, Precio);
           ps.setString(3, Tipo);
           
           ps.executeUpdate();
           
           JOptionPane.showMessageDialog(null,"Registro exitoso");
       }
       catch (SQLException e) 
       {
           JOptionPane.showMessageDialog(null, e.toString());
       }
   }
}
