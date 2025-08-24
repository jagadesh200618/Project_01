import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 300
    page.window_height = 400
    
    result = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=260, read_only=True)
    current_number = ""
    operator = None
    previous_number = None
    
    def number_click(e):
        nonlocal current_number
        number = e.control.text
        if current_number == "0":
            current_number = number
        else:
            current_number += number
        result.value = current_number
        page.update()
    
    def operator_click(e):
        nonlocal operator, previous_number, current_number
        if current_number:
            if previous_number is not None:
                calculate()
            operator = e.control.text
            previous_number = float(current_number)
            current_number = ""
            page.update()
    
    def calculate():
        nonlocal previous_number, current_number, operator
        if not all([previous_number, current_number, operator]):
            return
        
        num2 = float(current_number)
        if operator == "+":
            current_number = str(previous_number + num2)
        elif operator == "-":
            current_number = str(previous_number - num2)
        elif operator == "×":
            current_number = str(previous_number * num2)
        elif operator == "÷":
            if num2 == 0:
                current_number = "Error"
            else:
                current_number = str(previous_number / num2)
                
        result.value = current_number
        operator = None
        previous_number = None
    
    def equals_click(e):
        calculate()
        page.update()
    
    def clear_click(e):
        nonlocal current_number, operator, previous_number
        current_number = "0"
        operator = None
        previous_number = None
        result.value = current_number
        page.update()
    
    page.add(
        ft.Column(
            [
                result,
                ft.Row(
                    [
                        ft.ElevatedButton(text="7", width=50, on_click=number_click),
                        ft.ElevatedButton(text="8", width=50, on_click=number_click),
                        ft.ElevatedButton(text="9", width=50, on_click=number_click),
                        ft.ElevatedButton(text="÷", width=50, on_click=operator_click),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.ElevatedButton(text="4", width=50, on_click=number_click),
                        ft.ElevatedButton(text="5", width=50, on_click=number_click),
                        ft.ElevatedButton(text="6", width=50, on_click=number_click),
                        ft.ElevatedButton(text="×", width=50, on_click=operator_click),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.ElevatedButton(text="1", width=50, on_click=number_click),
                        ft.ElevatedButton(text="2", width=50, on_click=number_click),
                        ft.ElevatedButton(text="3", width=50, on_click=number_click),
                        ft.ElevatedButton(text="-", width=50, on_click=operator_click),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.ElevatedButton(text="0", width=50, on_click=number_click),
                        ft.ElevatedButton(text="C", width=50, on_click=clear_click),
                        ft.ElevatedButton(text="=", width=50, on_click=equals_click),
                        ft.ElevatedButton(text="+", width=50, on_click=operator_click),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)
