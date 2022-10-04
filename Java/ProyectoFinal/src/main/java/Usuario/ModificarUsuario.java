/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Usuario;

import Consultas.Conexion;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import javax.swing.JOptionPane;
/**
 * 
 * @author Justin
 */
public class ModificarUsuario 
{
 public void modUsuario(String Nombre, String contra, String Tipo)
 {
     try 
     {          
       Connection con = Conexion.getConexion();
         
       PreparedStatement p = con.prepareStatement("use [Tienda]");
       String f = String.valueOf(p.execute());  
         
       PreparedStatement ps = con.prepareStatement("UPDATE usuario SET Nombre ='"+Nombre+"', Contrasena ='"+contra+"' ,Tipo='"+Tipo+"' WHERE Nombre = '"+Nombre+"'");
                  
       ps.executeUpdate();
            
       JOptionPane.showMessageDialog(null,"Usuario modificado exitosamente","Modificacion Exitosa",JOptionPane.INFORMATION_MESSAGE);
     }
     catch (SQLException e) 
     {
       JOptionPane.showMessageDialog(null,e.toString());
     }
 }    
}
