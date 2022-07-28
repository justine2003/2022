/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Consultas;
import com.mycompany.sqlconection.conexion;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.swing.JOptionPane;

/**
 *
 * @author Justin
 */
public class ConsultaLogin 
{
  
    public static void Login(String Nombre, String Contrasena)
    {
     ResultSet rs;
     
        try 
        {
          Connection con =  conexion.getConexion();
         
          PreparedStatement p = con.prepareStatement("use [Tienda]");
          String f = String.valueOf(p.execute());
          
          PreparedStatement ps = con.prepareStatement("SELECT Nombre,Contrasena FROM usuario where Nombre= ? AND Contrasena = ?");
          
           ps.setString(1, Nombre);
           ps.setString(2, Contrasena);
           
           rs = ps.executeQuery();
           
           if(rs.next() == true)
           {
               JOptionPane.showMessageDialog(null,"Registro exitoso");
           }
           else
           {
               JOptionPane.showMessageDialog(null,"Usario o Contrasena incorrecta");
           }
        }
        catch (SQLException e) 
        {
            JOptionPane.showMessageDialog(null,e.toString());
        }
    }  
}
