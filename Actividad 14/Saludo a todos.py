def saludotodos(*todos):
 print(f"\nSaludos a {todos}")
 print(f"Saludos al primero {todos[0]}")
 print(f"Separados por comas {','.join(todos)}")

saludotodos("Juan","Pedro","Luis","Gonzalo")