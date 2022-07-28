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
public class EliminarUsuario 
{
 public boolean Eusuario(String Nombre)
 {
     try 
     {
         Connection con = conexion.getConexion();
         
         PreparedStatement p = con.prepareStatement("use[Tienda]");
         String f = String.valueOf(p.execute());
         
         PreparedStatement ps = con.prepareStatement("DELETE FROM usuario WHERE Nombre = ?");
         
         ps.setString(0, Nombre);
         ps.execute();
         return true; 
     }
     catch (SQLException e) 
     {
         JOptionPane.showMessageDialog(null, e.toString());
         return false;
     }
 }
}
