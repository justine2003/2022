/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.sqlconection;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
/**
 *
 * @author Justin
 */
public class conexion 
{
 public static Connection getConexion()
 {
     String url = "jdbc:sqlserver://localhost:1433;"
             +"databaser=Tienda;"
             + "user=sa;"
             +"password=123;"
             +" TrustServerCertificate=True";
     
     try 
     {
         Connection con = DriverManager.getConnection(url);
         return con;
     }
     catch (SQLException e)
     {
         System.out.println(e.toString());
         return null;
     }
 }   
}
