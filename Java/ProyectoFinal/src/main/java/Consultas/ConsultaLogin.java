/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Consultas;

import Consultas.Conexion;
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
  public static String nombre = "";
  public static String Contra = "";
  public static String Tipo = "" ;
     
  public static String[] Login(String Nombre)
  {           
    ResultSet rs;
    
      try 
      {
          Connection con = Conexion.getConexion();
          
          PreparedStatement p = con.prepareStatement("use [Tienda]");
          String f = String.valueOf(p.execute());
          
          PreparedStatement ps = con.prepareStatement("SELECT * FROM usuario WHERE Nombre = '"+Nombre+"'");
          
          rs = ps.executeQuery();
          
          if (rs.next())
          {              
            nombre = rs.getString("Nombre");
            Contra = rs.getString("Contrasena");
            Tipo = rs.getString("Tipo");           
            
            String[] lista = new String[3];
           
            lista[0] = nombre;
            lista[1] = Contra;
            lista[2] = Tipo;
            
            return lista;
          }
          else
          {
              JOptionPane.showMessageDialog(null,"Usuario no encontrado");
          }
          
      }
      catch (SQLException e)
      {
          JOptionPane.showMessageDialog(null, e.toString());
      }
      return null;
  } 
}
