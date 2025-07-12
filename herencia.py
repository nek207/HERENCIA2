import tkinter as tk
from tkinter import messagebox

# Clase base: Employee
class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        return f"ID: {self.emp_id}, Nombre: {self.name}, Puesto: {self.position}, Salario: ${self.salary:,.2f}"

# Clase derivada: Manager
class Manager(Employee):
    def __init__(self, emp_id, name, position, salary, department):
        super().__init__(emp_id, name, position, salary)
        self.department = department

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Departamento: {self.department}"

# Clase derivada: Developer
class Developer(Employee):
    def __init__(self, emp_id, name, position, salary, programming_language):
        super().__init__(emp_id, name, position, salary)
        self.programming_language = programming_language

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Lenguaje: {self.programming_language}"

# Clase principal que gestiona la aplicación con interfaz gráfica
class EmployeeManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Empleados con Herencia")
        self.employees = []

        tk.Label(root, text="ID del Empleado").grid(row=0, column=0, sticky="e")
        self.id_entry = tk.Entry(root)
        self.id_entry.grid(row=0, column=1)

        tk.Label(root, text="Nombre").grid(row=1, column=0, sticky="e")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=1, column=1)

        tk.Label(root, text="Puesto").grid(row=2, column=0, sticky="e")
        self.position_entry = tk.Entry(root)
        self.position_entry.grid(row=2, column=1)

        tk.Label(root, text="Salario").grid(row=3, column=0, sticky="e")
        self.salary_entry = tk.Entry(root)
        self.salary_entry.grid(row=3, column=1)

        tk.Label(root, text="Tipo de Empleado").grid(row=4, column=0, sticky="e")
        self.type_var = tk.StringVar(value="Empleado")
        tk.OptionMenu(root, self.type_var, "Empleado", "Manager", "Developer").grid(row=4, column=1)

        tk.Label(root, text="Dato Extra").grid(row=5, column=0, sticky="e")
        self.extra_entry = tk.Entry(root)
        self.extra_entry.grid(row=5, column=1)

        self.add_button = tk.Button(root, text="Agregar Empleado", command=self.add_employee)
        self.add_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.output_text = tk.Text(root, height=15, width=60)
        self.output_text.grid(row=7, column=0, columnspan=2)

    def add_employee(self):
        try:
            emp_id = int(self.id_entry.get())
            name = self.name_entry.get()
            position = self.position_entry.get()
            salary = float(self.salary_entry.get())
            employee_type = self.type_var.get()
            extra_data = self.extra_entry.get()

            if not name or not position:
                raise ValueError("Todos los campos deben estar completos.")

            if employee_type == "Manager":
                employee = Manager(emp_id, name, position, salary, extra_data)
            elif employee_type == "Developer":
                employee = Developer(emp_id, name, position, salary, extra_data)
            else:
                employee = Employee(emp_id, name, position, salary)

            self.employees.append(employee)
            self.output_text.insert(tk.END, employee.display_info() + "\n")
            self.clear_fields()
        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

    def clear_fields(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.position_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)
        self.extra_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagerApp(root)
    root.mainloop()
