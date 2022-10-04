
package proyecto;

import Consultas.Conexion;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.util.ArrayList;
import javax.swing.DefaultComboBoxModel;
import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;


public class supermercadoJava extends javax.swing.JFrame {
    
    ArrayList Nombre = new ArrayList();
    ArrayList<Integer> Precio = new ArrayList();   
    ArrayList Tipo = new ArrayList();
    
    DefaultTableModel modeloT = new DefaultTableModel();
    
    int precios = 0;
    int cantidad = 0;
    
    ArrayList<venta> listaVentas = new ArrayList<venta>();
    
    public supermercadoJava() {
        initComponents();
        this.setTitle("Supermercado Java");
        this.setSize(600, 600);
        this.setLocationRelativeTo(null);
        modeloT.addColumn("Nombre");
        modeloT.addColumn("Tipo");
        modeloT.addColumn("Cantidad");
        modeloT.addColumn("Precio");
        modeloT.addColumn("Importe");
        CargarDatos();
        CalcularPrecio();
         
    }
    
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jScrollPane1 = new javax.swing.JScrollPane();
        jTable1 = new javax.swing.JTable();
        jLabel8 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jPanel1 = new javax.swing.JPanel();
        jLabel15 = new javax.swing.JLabel();
        jLabel1 = new javax.swing.JLabel();
        cboproductos = new javax.swing.JComboBox<>();
        jLabel2 = new javax.swing.JLabel();
        spncantidad = new javax.swing.JSpinner();
        jLabel3 = new javax.swing.JLabel();
        lblprecio = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        lblimporte = new javax.swing.JLabel();
        jScrollPane2 = new javax.swing.JScrollPane();
        tblproductos = new javax.swing.JTable();
        btnagregar = new javax.swing.JButton();
        jLabel9 = new javax.swing.JLabel();
        lblsubtotal = new javax.swing.JLabel();
        jLabel10 = new javax.swing.JLabel();
        lbliva = new javax.swing.JLabel();
        jLabel11 = new javax.swing.JLabel();
        lbltotal = new javax.swing.JLabel();
        btnRegresar = new javax.swing.JButton();
        btnComprar = new javax.swing.JButton();

        jTable1.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null}
            },
            new String [] {
                "Title 1", "Title 2", "Title 3", "Title 4"
            }
        ));
        jScrollPane1.setViewportView(jTable1);

        jLabel8.setText("jLabel8");

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setBackground(new java.awt.Color(153, 204, 255));

        jPanel1.setBackground(new java.awt.Color(145, 203, 207));

        jLabel15.setFont(new java.awt.Font("Tahoma", 1, 24)); // NOI18N
        jLabel15.setForeground(new java.awt.Color(0, 0, 102));
        jLabel15.setText("SUPERMERCADO JAVA");

        jLabel1.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        jLabel1.setText("PRODUCTO");

        cboproductos.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        cboproductos.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                cboproductosActionPerformed(evt);
            }
        });

        jLabel2.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        jLabel2.setText("CANTIDAD");

        spncantidad.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        spncantidad.setModel(new javax.swing.SpinnerNumberModel(1, 1, 100, 1));
        spncantidad.setRequestFocusEnabled(false);
        spncantidad.addChangeListener(new javax.swing.event.ChangeListener() {
            public void stateChanged(javax.swing.event.ChangeEvent evt) {
                spncantidadStateChanged(evt);
            }
        });

        jLabel3.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        jLabel3.setText("PRECIO");

        lblprecio.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        lblprecio.setText("0.00 COLONES");

        jLabel5.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        jLabel5.setText("IMPORTE");

        lblimporte.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        lblimporte.setText("0.00 COLONES");

        tblproductos.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        tblproductos.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null, null},
                {null, null, null, null, null},
                {null, null, null, null, null},
                {null, null, null, null, null}
            },
            new String [] {
                "Nombre", "Tipo", "Catidad", "Precio", "Importe"
            }
        ));
        tblproductos.getTableHeader().setReorderingAllowed(false);
        jScrollPane2.setViewportView(tblproductos);

        btnagregar.setText("Agregar");
        btnagregar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnagregarActionPerformed(evt);
            }
        });

        jLabel9.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        jLabel9.setText("SUBTOTAL");

        lblsubtotal.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        lblsubtotal.setText("0.00 COLONES");

        jLabel10.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        jLabel10.setText("IVA");

        lbliva.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        lbliva.setText("0.00 COLONES");

        jLabel11.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        jLabel11.setText("TOTAL");

        lbltotal.setFont(new java.awt.Font("Tahoma", 1, 14)); // NOI18N
        lbltotal.setText("0.00 COLONES");

        btnRegresar.setText("Regresar");
        btnRegresar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnRegresarActionPerformed(evt);
            }
        });

        btnComprar.setText("Comprar");
        btnComprar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnComprarActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(33, 33, 33)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, 540, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addComponent(jLabel11)
                                .addGap(35, 35, 35))
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jLabel10)
                                    .addComponent(jLabel9))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)))
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(lblsubtotal)
                            .addComponent(lbliva)
                            .addComponent(lbltotal))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(btnComprar)
                            .addComponent(btnRegresar))
                        .addGap(170, 170, 170))))
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jLabel1)
                            .addComponent(jLabel2))
                        .addGap(18, 18, 18)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(spncantidad, javax.swing.GroupLayout.PREFERRED_SIZE, 56, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(cboproductos, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(41, 41, 41)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jLabel5)
                            .addComponent(jLabel3))
                        .addGap(18, 18, 18)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(lblimporte)
                            .addComponent(lblprecio)))
                    .addComponent(jLabel15, javax.swing.GroupLayout.PREFERRED_SIZE, 287, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(42, 42, 42)
                .addComponent(btnagregar)
                .addContainerGap(97, Short.MAX_VALUE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(25, 25, 25)
                .addComponent(jLabel15)
                .addGap(36, 36, 36)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel1)
                    .addComponent(cboproductos, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel3)
                    .addComponent(lblprecio)
                    .addComponent(btnagregar))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel5)
                    .addComponent(lblimporte)
                    .addComponent(jLabel2)
                    .addComponent(spncantidad, javax.swing.GroupLayout.PREFERRED_SIZE, 29, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(49, 49, 49)
                .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, 120, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(34, 34, 34)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                        .addComponent(btnComprar)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(btnRegresar))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel9)
                            .addComponent(lblsubtotal))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(lbliva)
                            .addComponent(jLabel10, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(lbltotal)
                            .addComponent(jLabel11))))
                .addContainerGap(111, Short.MAX_VALUE))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel4)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(80, 80, 80)
                .addComponent(jLabel4)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void spncantidadStateChanged(javax.swing.event.ChangeEvent evt) {//GEN-FIRST:event_spncantidadStateChanged
      CalcularPrecio();
    }//GEN-LAST:event_spncantidadStateChanged

    private void btnComprarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnComprarActionPerformed
              
      if(GuardarFactura())
      {
          ArchivoCompras TU = new ArchivoCompras();
          
          TU.setPrecio(lbltotal.getText());
          
          TU.setIVA(lbliva.getText());
          
          FacturaElectronica FE = new FacturaElectronica();
      
          FE.setVisible(true);
      
          this.dispose();
      }      
      
    }//GEN-LAST:event_btnComprarActionPerformed

    private void btnagregarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnagregarActionPerformed
        venta venta = new venta();
        venta.setId(cboproductos.getSelectedIndex());
        venta.setNombre(cboproductos.getSelectedItem().toString());
        venta.SetTipo(Tipo.get(cboproductos.getSelectedIndex()).toString());
        venta.setPrecio(precios);
        venta.setCantidad(cantidad);
        venta.setImporte(precios*cantidad);
        
        if(!buscarVenta(venta)){
            listaVentas.add(venta);
        }
        actualisarTabla();
        borrarventa();
    }//GEN-LAST:event_btnagregarActionPerformed

    private void cboproductosActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_cboproductosActionPerformed
     CalcularPrecio();
     spncantidad.setValue(1);
    }//GEN-LAST:event_cboproductosActionPerformed

    private void btnRegresarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnRegresarActionPerformed
        ArchivoCompras TU = new ArchivoCompras();
        
        if("Travajador".equals(TU.getTipousuario()))
        {
            Menu m = new Menu();
            
            m.setVisible(true);
            this.dispose();
        }
        else
        {
            login l = new login();
            
            l.setVisible(true);
            this.dispose();
        }
    }//GEN-LAST:event_btnRegresarActionPerformed
    
    public boolean GuardarFactura()
    {
      if(modeloT.getRowCount() >= 1)
      {
          try
          {
              Connection con = Conexion.getConexion();
          
              PreparedStatement p = con.prepareStatement("use [Tienda]");
              String f = String.valueOf(p.execute()); 
         
              for(int i=0; i<modeloT.getRowCount();i++)
              {
                  PreparedStatement ps = con.prepareStatement("INSERT INTO GFactura (Nombre,Tipo,Cantidad,Precio,Importe) VALUES (?,?,?,?,?)");
          
                  String Nombres = modeloT.getValueAt(i, 0).toString();
                  String Tipos = modeloT.getValueAt(i,1).toString();
                  String Cantidad = modeloT.getValueAt(i,2).toString();
                  String Precios = modeloT.getValueAt(i,3).toString();
                  String Importe = modeloT.getValueAt(i,4).toString();
          
                  ps.setString(1,Nombres);
                  ps.setString(2,Tipos);
                  ps.setString(3,Cantidad);
                  ps.setString(4,Precios);
                  ps.setString(5,Importe);
          
                  ps.executeUpdate();
               }
              return true;
            }
            catch(SQLException e)
            {
                JOptionPane.showMessageDialog(null, e.toString());
                return false;
            }
        }
      else
      {
        JOptionPane.showMessageDialog(null,"No puede mandar una factura basia");
        return false;
      }
    }
    
    public void borrarventa()
    {
        precios = 0;
        cantidad = 1;
        cboproductos.setSelectedIndex(0);
        spncantidad.setValue(1);
        CalcularPrecio();
    }
    
    public void CalcularPrecio(){
       
        try 
        {
            precios =  Precio.get(cboproductos.getSelectedIndex());
            cantidad = Integer.parseInt(spncantidad.getValue().toString());
            lblprecio.setText(Moneda(precios));
            lblimporte.setText(Moneda(precios*cantidad));
        } 
        catch (Exception e)
        {
            System.out.println(e.toString());
        }
    }
    
    public boolean buscarVenta(venta nueva)
    {
        for(venta v: listaVentas){
            if(v.getId() == nueva.getId())
            {
                int Ncantidad = v.getCantidad()+nueva.getCantidad();
                v.setCantidad(Ncantidad);
                v.setImporte(v.getCantidad()*v.getPrecio());
                return true;
            }
        }
        return false;
    }
        
    public String Moneda(double precio)
    {
        return "$ " + Math.round(precio*100.0)/100.0;
    }
    
    public void actualisarTabla(){
         while(modeloT.getRowCount()>0){
             modeloT.removeRow(0);
         }
         double subtotal=0;
         for(venta v: listaVentas){
             Object x []= new Object [5];
             x [0]= v.getNombre();
             x [1]= v.getTipo();
             x [2]= v.getCantidad();
             x [3]= Moneda(v.getPrecio());
             x [4]= Moneda(v.getImporte());
             subtotal+= v.getImporte();
            modeloT.addRow(x);
            
         }
         double iva= subtotal*0.16;
         double total= subtotal+ iva;
         lblsubtotal.setText(Moneda(subtotal));
         lbliva.setText(Moneda(iva));
         lbltotal.setText(Moneda(total));
         tblproductos.setModel(modeloT); 
    }
    
     public void CargarDatos()
     {
          try 
         {
            Connection con = Conexion.getConexion();
            
            PreparedStatement p = con.prepareStatement("use[Tienda]");
            String f = String.valueOf(p.execute());
            
            PreparedStatement ps = con.prepareStatement("SELECT Nombre,Precio,Tipo From productos");
            
            ResultSet rs = ps.executeQuery();
            
            while(rs.next())
            {
               cboproductos.addItem(rs.getString("Nombre"));
               Nombre.add(rs.getString("Nombre"));
               Precio.add(rs.getInt("Precio"));
               Tipo.add(rs.getString("Tipo"));
            }
         }
         catch (SQLException e)
         {
             JOptionPane.showMessageDialog(null,e.toString());
         }
     }
     
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
            java.util.logging.Logger.getLogger(supermercadoJava.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(supermercadoJava.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(supermercadoJava.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(supermercadoJava.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new supermercadoJava().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnComprar;
    private javax.swing.JButton btnRegresar;
    private javax.swing.JButton btnagregar;
    private javax.swing.JComboBox<String> cboproductos;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel11;
    private javax.swing.JLabel jLabel15;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JTable jTable1;
    private javax.swing.JLabel lblimporte;
    private javax.swing.JLabel lbliva;
    private javax.swing.JLabel lblprecio;
    private javax.swing.JLabel lblsubtotal;
    private javax.swing.JLabel lbltotal;
    private javax.swing.JSpinner spncantidad;
    private javax.swing.JTable tblproductos;
    // End of variables declaration//GEN-END:variables
}
