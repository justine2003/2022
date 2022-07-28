/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Consultas;
import com.mycompany.sqlconection.conexion;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import javax.swing.JOptionPane;

/**
 *
 * @author Justin
 */
public class NuevoUSaurio 
{
 public static void NUsuario(String Nombre, String contra, String Tipo)
 {
     try 
     {
         Connection con = conexion.getConexion();
         
         PreparedStatement p = con.prepareStatement("use [Tienda]");
         String f = String.valueOf(p.execute());        
         
         PreparedStatement ps = con.prepareStatement("INSERT INTO usuario (Nombre, Contrasena, Tipo) VALUES (?,?,?)");
         
         ps.setString(1, Nombre);
         ps.setString(2, contra);
         ps.setString(3, Tipo);
         
         ps.executeUpdate();
                 
         JOptionPane.showMessageDialog(null, "Registro exitoso");
     }
     catch (SQLException e) 
     {
         JOptionPane.showMessageDialog(null,e.toString());
     }
 }    
}
