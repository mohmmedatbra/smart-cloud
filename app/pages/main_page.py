import reflex as rx


def main_page() -> rx.Component:
    """The main page of the app, displayed after login."""
    return rx.el.main(
        rx.el.div(
            rx.el.h1(
                "أهلاً بك في الصفحة الرئيسية",
                class_name="text-4xl md:text-5xl font-bold text-gray-800 mb-12 tracking-wide",
                dir="rtl",
            ),
            class_name="flex flex-col items-center justify-center text-center p-8",
        ),
        class_name="font-['Tajawal'] min-h-screen w-full flex items-center justify-center bg-gray-50",
    )