import reflex as rx
from app.state import AuthState


def landing_page() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.icon("cloud", class_name="text-white w-16 h-16"), class_name="mb-6"
            ),
            rx.el.h1(
                "سما كلاود",
                class_name="text-5xl md:text-6xl font-bold text-white mb-8 tracking-wide",
                dir="rtl",
            ),
            rx.el.div(
                rx.el.button(
                    "إنشاء حساب جديد",
                    class_name="bg-white text-blue-600 font-semibold py-3 px-8 rounded-full shadow-lg hover:bg-gray-100 transition-colors duration-300 w-full md:w-auto",
                    dir="rtl",
                ),
                rx.el.button(
                    "تسجيل الدخول",
                    on_click=AuthState.go_to_login,
                    class_name="bg-transparent border-2 border-white text-white font-semibold py-3 px-8 rounded-full hover:bg-white hover:text-blue-600 transition-colors duration-300 w-full md:w-auto",
                    dir="rtl",
                ),
                class_name="flex flex-col md:flex-row items-center gap-6",
            ),
            class_name="flex flex-col items-center justify-center text-center p-8",
        ),
        class_name="font-['Tajawal'] min-h-screen w-full flex items-center justify-center bg-gradient-to-br from-blue-400 to-blue-600",
    )