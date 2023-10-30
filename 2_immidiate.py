import dearpygui.dearpygui as dpg

dpg.create_context()


def button_callback(sender, app_data, user_data):
    print(f"sender: {sender}")
    print(f"app_data: {app_data}")
    print(f"user_data: {user_data()}")


with dpg.window(label="Tutorial"):
    dpg.add_input_text(label="Visible Input")
    dpg.add_input_text(
        label="Password Input", source=dpg.last_item(), password=True, tag="pwd"
    )

    dpg.add_button(
        label="Print to Terminal",
        callback=button_callback,
        user_data={"password": dpg.get_value("pwd")},
        # user_data=lambda: {"password": dpg.get_value("pwd")},
    )

dpg.create_viewport(title="Custom Title", width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
