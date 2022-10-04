/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyecto;

import Consultas.Conexion;
import java.awt.Dimension;
import java.io.FileWriter;
import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author fab22
 */
public class FacturaElectronica extends javax.swing.JFrame {    
    
     ArchivoCompras TU = new ArchivoCompras();
     
    static String Fecha;
    static String Nombre;
    static String Identidad;
    static String Telefono;
    
    public FacturaElectronica() {
        this.setTitle("Factura");
        this.setSize(200,200);
        initComponents();
        lblPRecio.setText(TU.getPrecio());
        lblIVA.setText(TU.getIVA());
        CargarDatos();
        cargarfecha();
    }

    
    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jColorChooser1 = new javax.swing.JColorChooser();
        jSeparator1 = new javax.swing.JSeparator();
        Jframe = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        txtFecha = new javax.swing.JTextField();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        txtNombre = new javax.swing.JTextField();
        txtIdentidad = new javax.swing.JTextField();
        txtTelefono = new javax.swing.JTextField();
        jScrollPane1 = new javax.swing.JScrollPane();
        tblFactura = new javax.swing.JTable();
        btnImprimir = new javax.swing.JButton();
        btnRegresar = new javax.swing.JButton();
        jLabel6 = new javax.swing.JLabel();
        lblPRecio = new javax.swing.JLabel();
        jLabel7 = new javax.swing.JLabel();
        lblIVA = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        addWindowListener(new java.awt.event.WindowAdapter() {
            public void windowClosing(java.awt.event.WindowEvent evt) {
                formWindowClosing(evt);
            }
        });

        Jframe.setBackground(new java.awt.Color(146, 203, 206));
        Jframe.setFocusCycleRoot(true);
        Jframe.setRequestFocusEnabled(false);

        jLabel1.setFont(new java.awt.Font("Tahoma", 1, 18)); // NOI18N
        jLabel1.setForeground(new java.awt.Color(0, 0, 102));
        jLabel1.setText("FACTURA DE VENTA");

        jLabel2.setText("Fecha de emision");

        txtFecha.setEditable(false);
        txtFecha.setHorizontalAlignment(javax.swing.JTextField.CENTER);

        jLabel3.setText("Nombre");

        jLabel4.setText("Identidad");

        jLabel5.setText("Telefono");

        txtNombre.setHorizontalAlignment(javax.swing.JTextField.CENTER);

        txtIdentidad.setHorizontalAlignment(javax.swing.JTextField.CENTER);

        txtTelefono.setHorizontalAlignment(javax.swing.JTextField.CENTER);

        tblFactura.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null, null},
                {null, null, null, null, null},
                {null, null, null, null, null},
                {null, null, null, null, null}
            },
            new String [] {
                "Nombre", "Tipo", "Cantidad", "Precio", "Importe"
            }
        ));
        jScrollPane1.setViewportView(tblFactura);

        btnImprimir.setText("Imprimir");
        btnImprimir.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnImprimirActionPerformed(evt);
            }
        });

        btnRegresar.setText("Regresar");
        btnRegresar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnRegresarActionPerformed(evt);
            }
        });

        jLabel6.setText("Total");

        lblPRecio.setText("0");

        jLabel7.setText("IVA:");

        lblIVA.setText("0");

        javax.swing.GroupLayout JframeLayout = new javax.swing.GroupLayout(Jframe);
        Jframe.setLayout(JframeLayout);
        JframeLayout.setHorizontalGroup(
            JframeLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(JframeLayout.createSequentialGroup()
                .addGroup(JframeLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(JframeLayout.createSequentialGroup()
                        .addGap(227, 227, 227)
                        .addComponent(jLabel1))
                    .addGroup(JframeLayout.createSequentialGroup()
                        .addGap(43, 43, 43)
                        .addGroup(JframeLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jLabel2)
                            .addComponent(jLabel3)
                            .addComponent(jLabel4)
                            .addComponent(jLabel5))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addGroup(JframeLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(txtFecha)
                            .addComponent(txtNombre)
                            .addComponent(txtIdentidad)
                            .addComponent(txtTelefono, javax.swing.GroupLayout.DEFAULT_SIZE, 132, Short.MAX_VALUE)))
                    .addGroup(JframeLayout.createSequentialGroup()
                        .addGap(96, 96, 96)
                        .addGroup(JframeLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jLabel7)
                            .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGroup(JframeLayout.createSequentialGroup()
                                .addGap(94, 94, 94)
                                .addComponent(btnImprimir)
                                .addGap(18, 18, 18)
                                .addComponent(btnRegresar))))
                    .addGroup(JframeLayout.createSequentialGroup()
                        .addGap(86, 86, 86)
                        .addComponent(jLabel6)
                        .addGap(18, 18, 18)
                        .addGroup(JframeLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(lblIVA)
                            .addComponent(lblPRecio))))
                .addContainerGap(59, Short.MAX_VALUE))
        );
        JframeLayout.setVerticalGroup(
            JframeLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(JframeLayout.createSequentialGroup()
                .addGap(64, 64, 64)
                .addComponent(jLabel1)
                .addGap(23, 23, 23)
                .addGroup(JframeLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel2)
                    .addComponent(txtFecha))
                .addGap(25, 25, 25)
                .addGroup(JframeLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel3)
                    .addComponent(txtNombre, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(JframeLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(txtIdentidad, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel4))
                .addGap(18, 18, 18)
                .addGroup(JframeLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel5)
                    .addComponent(txtTelefono, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(47, 47, 47)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 98, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(39, 39, 39)
                .addGroup(JframeLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel7)
                    .addComponent(lblIVA))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(JframeLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel6)
                    .addComponent(lblPRecio))
                .addGap(18, 18, 18)
                .addGroup(JframeLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(btnImprimir)
                    .addComponent(btnRegresar))
                .addContainerGap())
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(Jframe, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(Jframe, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnImprimirActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnImprimirActionPerformed
     RutaArchivo RA = new RutaArchivo();
     
     if("".equals(txtNombre.getText()) || "".equals(txtIdentidad.getText()) || "".equals(txtTelefono.getText()))
     {
         JOptionPane.showMessageDialog(null,"No puede dejar ningun campo vacio","Error",JOptionPane.ERROR_MESSAGE);
     }
     else
     {
        Fecha = txtFecha.getText();
        Nombre = txtNombre.getText();
        Identidad = txtIdentidad.getText();
        Telefono = txtIdentidad.getText();
         
         RA.setVisible(true);
     }
    }//GEN-LAST:event_btnImprimirActionPerformed

    private void btnRegresarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnRegresarActionPerformed
      int respuesta = JOptionPane.showConfirmDialog(null,"Tenga el cuenta que al regresar se eliminaran todos los datos","Regresar",JOptionPane.YES_NO_OPTION,JOptionPane.QUESTION_MESSAGE);
        
      if(respuesta == 0)
      {
        supermercadoJava  SJ = new supermercadoJava();  
        
        Eliminar();
        
        SJ.setVisible(true);
        this.dispose();
      }    
    }//GEN-LAST:event_btnRegresarActionPerformed

    private void formWindowClosing(java.awt.event.WindowEvent evt) {//GEN-FIRST:event_formWindowClosing
        Eliminar();
    }//GEN-LAST:event_formWindowClosing
    
    public void Imprimir(String ruta)
    {
     ArchivoCompras AC = new ArchivoCompras();
     
     try 
     {
      FileWriter fichero = new FileWriter(ruta);
       
      fichero.write("Fecha "+Fecha+"\n");
      fichero.write("Nombre "+Nombre+"\n");
      fichero.write("Identidad "+Identidad+"\n");
      fichero.write("Telefono "+Telefono+"\n");
      
      for(int i=0; i<tblFactura.getRowCount();i++)
      {
          String NombreT = tblFactura.getValueAt(i,0).toString();
          String TipoT = tblFactura.getValueAt(i,1).toString();
          String CantidadT = tblFactura.getValueAt(i,2).toString();
          String PrecioT = tblFactura.getValueAt(i,3).toString();
          String ImporteT = tblFactura.getValueAt(i,4).toString();
                  
          fichero.write("Nombre:"+ NombreT +" Tipo:"+ TipoT +" Cantidad:"+ CantidadT +" Precio:"+ PrecioT +" Importe:"+ ImporteT +"\n");
      }
      
      fichero.write("------------------------------------------------------------------------------------------------"+"\n");
      
      fichero.write("IVA: "+TU.getIVA()+"\n");
      fichero.write("Total: "+TU.getPrecio());      
      
      fichero.close();
      NuevosDatos();
     } 
     catch (IOException ex) 
     {
      JOptionPane.showMessageDialog(null,ex.toString());
     }
    }
    
    public void NuevosDatos()
    {
       for(int i=0; i<tblFactura.getRowCount();i++)
       {
           String NombreS = tblFactura.getValueAt(i,0).toString();
           
           try 
           {
               Connection con = Conexion.getConexion();
            
               PreparedStatement p = con.prepareStatement("use[Tienda]");
               String f = String.valueOf(p.execute());
               
               PreparedStatement ps = con.prepareStatement("SELECT Nombre,CantVendida FROM RegistroVentas where Nombre = '"+NombreS+"'");              
               
               ResultSet rs = ps.executeQuery();
               
               if(rs.next())
               {
                  int num = rs.getInt("CantVendida");
                  int numV = Integer.parseInt(tblFactura.getValueAt(i,2).toString());
                  int total = num + numV;                  
                  
                  PreparedStatement update = con.prepareStatement("UPDATE RegistroVentas SET CantVendida = '"+total+"' WHERE Nombre = '"+NombreS+"'");
                  update.executeUpdate();
               }
               else
               {
                   PreparedStatement newR = con.prepareStatement("INSERT INTO RegistroVentas (Nombre,CantVendida) VALUES (?,?)");
         
                   int NumeroNew = Integer.parseInt(tblFactura.getValueAt(i,2).toString());
                   
                   newR.setString(1,NombreS);
                   newR.setInt(2,NumeroNew);
                   
                   newR.executeUpdate();
               }
           }
           catch (SQLException e) 
           {
               JOptionPane.showMessageDialog(null,e.toString());
           }
       }
    }
    
    public void Eliminar()
    {
        try 
        {
            Connection con = Conexion.getConexion();
            
            PreparedStatement p = con.prepareStatement("use[Tienda]");
            String f = String.valueOf(p.execute());
            
            PreparedStatement ps = con.prepareStatement("Delete FROM GFactura ");
            
            ps.execute();
        }
        catch (SQLException e) 
        {
            JOptionPane.showMessageDialog(null,e.toString());
        }
    }
    
    public void CargarDatos()
    {      
        DefaultTableModel modeloTabla = (DefaultTableModel) tblFactura.getModel();
        modeloTabla.setRowCount(0);
        
        try 
        {
         Connection con = Conexion.getConexion();
         
         PreparedStatement p = con.prepareStatement("use[Tienda]");
         String f = String.valueOf(p.execute());
         
         PreparedStatement ps = con.prepareStatement("SELECT * FROM GFactura");
         
         ResultSet rs = ps.executeQuery();
         ResultSetMetaData rsms = rs.getMetaData();
         int Columnas = rsms.getColumnCount();
         
         while(rs.next())
         {
             Object[] fila = new Object[Columnas];
             
             for (int indice = 0; indice < Columnas; indice++) 
             {
                 fila[indice] = rs.getObject(indice+1);
             }
            modeloTabla.addRow(fila);
         }
        }
        catch (SQLException e) 
        {
            JOptionPane.showMessageDialog(null,e.toString());
        }
    }
    
    public void cargarfecha()
    {
      DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");
      txtFecha.setText(dtf.format(LocalDateTime.now()));
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(FacturaElectronica.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(FacturaElectronica.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(FacturaElectronica.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(FacturaElectronica.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new FacturaElectronica().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JPanel Jframe;
    private javax.swing.JButton btnImprimir;
    private javax.swing.JButton btnRegresar;
    private javax.swing.JColorChooser jColorChooser1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JSeparator jSeparator1;
    private javax.swing.JLabel lblIVA;
    private javax.swing.JLabel lblPRecio;
    private javax.swing.JTable tblFactura;
    private javax.swing.JTextField txtFecha;
    private javax.swing.JTextField txtIdentidad;
    private javax.swing.JTextField txtNombre;
    private javax.swing.JTextField txtTelefono;
    // End of variables declaration//GEN-END:variables

}