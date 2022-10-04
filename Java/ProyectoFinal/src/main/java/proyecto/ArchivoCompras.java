/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto;

import javax.swing.JOptionPane;

/**
 *
 * @author Justin
 */
public class ArchivoCompras 
{
   private static String Tipousuario;   
   private static String Precio;
   private static String IVA;
   
   public String getTipousuario() {
        return Tipousuario;
   }

    public void setTipousuario(String Tipousuario) {
        this.Tipousuario = Tipousuario;
    }
    
    public String getPrecio(){
        return Precio;
    }
    
    public void setPrecio(String precio){
        this.Precio = precio;
    }
    
    public String getIVA(){
        return IVA;
    }
    
    public void setIVA(String iva){
        this.IVA = iva;
    }
}
