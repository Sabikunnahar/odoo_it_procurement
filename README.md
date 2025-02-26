
# IT Procurement Application

## Company Name: Mime Connect

### Overview
The **IT Procurement Application** streamlines purchasing laptops for new employees. It ensures proper workflow management, vendor communication, and multi-layered approval based on purchase order value.

---

## **Purchase Order Process**

### 1. **Creation of Purchase Order**
- The **Procurement Department** creates a purchase order for laptops.

### 2. **Vendor Notification**
- The vendor is notified via email when the purchase order is created.
- Vendors can view the purchase order in their **portal** with **read-only access**.

### 3. **Purchase Order Confirmation & Approval**
#### Approval based on purchase price:
- **≤ 50,000 Taka:** The **COO** confirms and approves the purchase.
- **> 50,000 Taka:** The **COO** confirms, but the **MD** must approve the purchase order.

---

## **Approval Layers & Access Groups**

### **a) Procurement Team**
- ✅ View purchase order list  
- ✅ Create, update, and cancel purchase orders  
- ✅ Send emails to vendors  

### **b) Chief Operating Officer (COO)**
- ✅ Confirm purchase orders  
- ✅ View purchase order list  
- ❌ Cannot create purchase orders  

### **c) Managing Director (MD)**
- ✅ Approve purchase orders  
- ✅ View purchase order list  
- ❌ Cannot create purchase orders  

### **d) Vendor**
- ✅ View assigned purchase orders (read-only)  
- ❌ Cannot create, update, or cancel purchase orders  

---

## **Purchase Order PDF Report**
- A **PDF report** is generated for each purchase order.
- The report includes a **digital signature**.
- A well-structured **PDF template** ensures clarity and compliance.

---

## **Implementation Details**
- **Odoo framework** used for development.
- **Access control groups** enforce security and workflow restrictions.
- **Automated email notifications** ensure vendor awareness.
- **QWeb reports** generate structured PDF documents.

---

## **License & Ownership**
This software is the property of **Mime Connect**. Unauthorized distribution is strictly prohibited.

---

## **Installation & Usage**
1. Install the module in **Odoo 16 or later**.
2. Assign users to their respective **groups**.
3. Create and manage purchase orders through the **Procurement Dashboard**.
4. Approve purchase orders based on defined rules.
5. Generate PDF reports for records.

For further inquiries, contact **support@mimeconnect.com**.

