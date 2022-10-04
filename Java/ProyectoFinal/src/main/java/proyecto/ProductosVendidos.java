
package proyecto;

import Consultas.Conexion;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.data.general.DefaultKeyedValuesDataset;
import org.jfree.data.general.DefaultPieDataset;

public class ProductosVendidos extends javax.swing.JFrame {

    
    public ProductosVendidos() {
        initComponents();
        this.setSize(1000,400);
        txtNombre.setVisible(false);
        txtCantidad.setVisible(false);
        JPGrafico.setVisible(false);
        CargarDatos();
        this.setLocationRelativeTo(null);
    }

   
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jScrollPane1 = new javax.swing.JScrollPane();
        tblCantVEntas = new javax.swing.JTable();
        btnRegresar = new javax.swing.JButton();
        JPGrafico = new javax.swing.JPanel();
        btnEliminar = new javax.swing.JButton();
        btnActualisar = new javax.swing.JButton();
        btnGrafico = new javax.swing.JButton();
        txtNombre = new javax.swing.JTextField();
        txtCantidad = new javax.swing.JTextField();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jPanel1.setBackground(new java.awt.Color(146, 203, 206));

        tblCantVEntas.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null},
                {null, null},
                {null, null},
                {null, null}
            },
            new String [] {
                "Nombre", "Cantidad vendida"
            }
        ));
        tblCantVEntas.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                tblCantVEntasMouseClicked(evt);
            }
        });
        jScrollPane1.setViewportView(tblCantVEntas);

        btnRegresar.setText("Regresar");
        btnRegresar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnRegresarActionPerformed(evt);
            }
        });

        JPGrafico.setToolTipText("");

        javax.swing.GroupLayout JPGraficoLayout = new javax.swing.GroupLayout(JPGrafico);
        JPGrafico.setLayout(JPGraficoLayout);
        JPGraficoLayout.setHorizontalGroup(
            JPGraficoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 0, Short.MAX_VALUE)
        );
        JPGraficoLayout.setVerticalGroup(
            JPGraficoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 260, Short.MAX_VALUE)
        );

        btnEliminar.setText("Eliminar");
        btnEliminar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnEliminarActionPerformed(evt);
            }
        });

        btnActualisar.setText("Actualisar");
        btnActualisar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnActualisarActionPerformed(evt);
            }
        });

        btnGrafico.setText("Generar Grafico");
        btnGrafico.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnGraficoActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(78, 78, 78)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addComponent(btnGrafico)
                                .addGap(18, 18, 18)
                                .addComponent(btnActualisar)
                                .addGap(18, 18, 18)
                                .addComponent(btnEliminar)
                                .addGap(18, 18, 18)
                                .addComponent(btnRegresar))
                            .addComponent(JPGrafico, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jScrollPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 825, Short.MAX_VALUE)))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(257, 257, 257)
                        .addComponent(txtNombre, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(237, 237, 237)
                        .addComponent(txtCantidad, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap(64, Short.MAX_VALUE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(35, 35, 35)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 221, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(txtNombre, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(txtCantidad, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(13, 13, 13)
                .addComponent(JPGrafico, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGap(36, 36, 36)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(btnRegresar)
                    .addComponent(btnEliminar)
                    .addComponent(btnActualisar)
                    .addComponent(btnGrafico))
                .addGap(26, 26, 26))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnRegresarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnRegresarActionPerformed
       Menu newframe = new Menu();
        
        newframe.setVisible(true);
        
        this.dispose();
    }//GEN-LAST:event_btnRegresarActionPerformed

    private void tblCantVEntasMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_tblCantVEntasMouseClicked
        int fila = tblCantVEntas.rowAtPoint(evt.getPoint());
        txtNombre.setText(tblCantVEntas.getValueAt(fila,0).toString());
        txtCantidad.setText(tblCantVEntas.getValueAt(fila,1).toString());
    }//GEN-LAST:event_tblCantVEntasMouseClicked

    private void btnEliminarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnEliminarActionPerformed
       Graficos.Eliminar G = new Graficos.Eliminar();
       
       G.Eliminar(txtNombre.getText());
    }//GEN-LAST:event_btnEliminarActionPerformed

    private void btnGraficoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnGraficoActionPerformed
         CrearGrafico();
    }//GEN-LAST:event_btnGraficoActionPerformed

    private void btnActualisarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnActualisarActionPerformed
        CargarDatos();
        CrearGrafico();
    }//GEN-LAST:event_btnActualisarActionPerformed
     
    public void CrearGrafico()
    {
        this.setSize(1000,600);
        JPGrafico.setVisible(true);
       
        
        try 
        {
            DefaultPieDataset datos = new DefaultKeyedValuesDataset();
        
             //Siclo para poder ingresar los datos en el grafico
             for(int i=0; i<tblCantVEntas.getRowCount(); i++)
             {
                 String nombre = tblCantVEntas.getValueAt(i,0).toString();
                 int cant = Integer.parseInt(tblCantVEntas.getValueAt(i,1).toString());
           
                 datos.setValue(nombre,cant);
             }
             //Fin de ciclo
        
             JFreeChart grafico = ChartFactory.createPieChart("Productos Vendidos",datos,true,true,false);
        
             ChartPanel panel = new ChartPanel(grafico);
             panel.setMouseWheelEnabled(true);
             panel.setPreferredSize(new Dimension(200,200));
             
             JPGrafico.setLayout(new BorderLayout());
             JPGrafico.add(panel,BorderLayout.NORTH);
        
             pack();
             repaint();
        }
        catch (Exception e) 
        {
           JOptionPane.showMessageDialog(null,e.toString());
        }
    }
    
    public void CargarDatos()
    {
       DefaultTableModel modeloTabla = (DefaultTableModel) tblCantVEntas.getModel();
       modeloTabla.setRowCount(0);
       
        try 
        {
            Connection con = Conexion.getConexion();
            
            PreparedStatement p = con.prepareStatement("use[Tienda]");
            String f = String.valueOf(p.execute());
            
            PreparedStatement ps = con.prepareStatement("SELECT * FROM RegistroVentas");
            
            ResultSet rs = ps.executeQuery();
            ResultSetMetaData rsms = rs.getMetaData();
            int columas = rsms.getColumnCount();
            
            while(rs.next())
            {
                Object[] fila = new Object[columas];
                
                for(int indice=0; indice<columas; indice++)
                {
                    fila[indice] = rs.getObject(indice+1);
                }
                modeloTabla.addRow(fila);
            }
        }
        catch (SQLException e) 
        {
            JOptionPane.showMessageDialog(null, e.toString());
        }
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
            java.util.logging.Logger.getLogger(ProductosVendidos.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(ProductosVendidos.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(ProductosVendidos.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(ProductosVendidos.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new ProductosVendidos().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JPanel JPGrafico;
    private javax.swing.JButton btnActualisar;
    private javax.swing.JButton btnEliminar;
    private javax.swing.JButton btnGrafico;
    private javax.swing.JButton btnRegresar;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTable tblCantVEntas;
    private javax.swing.JTextField txtCantidad;
    private javax.swing.JTextField txtNombre;
    // End of variables declaration//GEN-END:variables
}
