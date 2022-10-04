/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Consultas;

import com.mycompany.sqlconection.conexion;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.Statement;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.swing.JOptionPane;
import com.mycompany.sqlconection.Consulta;
/**
 *
 * @author Justin
 */
public class Pruebas 
{
    public static void main(String[] args)
    {
        Consulta c = new Consulta();
        
       ResultSet rs;
       String nombre = "Justin";
       
       String Nombre;
       String Contra;
       String Tipo;
               
       try 
        {
            Connection con = conexion.getConexion();
            
            PreparedStatement p = con.prepareStatement("use [Tienda]");
            String f = String.valueOf(p.execute());
            
             PreparedStatement ps = con.prepareStatement("select * From usuario where Nombre = '"+nombre+"'");
            
            rs = ps.executeQuery();
            
            if(rs.next())
            {
             JOptionPane.showMessageDialog(null, rs.getString("Nombre"));
             JOptionPane.showMessageDialog(null, rs.getString("Contrasena"));
             JOptionPane.showMessageDialog(null, rs.getString("Tipo"));
             
             c.setNombre("Justin");
            }
            else
            {
                JOptionPane.showMessageDialog(null,"Usuario no encontrado");
            }
        }
        catch (SQLException e) 
        {
            JOptionPane.showMessageDialog(null,e.toString());
        }
    JOptionPane.showMessageDialog(null,c.getNombre());
    }
}
