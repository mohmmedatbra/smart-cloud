import reflex as rx
from app.state import AuthState


def tab_button(text: str) -> rx.Component:
    is_active = AuthState.active_tab == text
    return rx.el.button(
        text,
        on_click=AuthState.set_active_tab(text),
        class_name=rx.cond(
            is_active,
            "px-6 py-2 text-sm font-semibold text-blue-600 bg-white rounded-full shadow-md",
            "px-6 py-2 text-sm font-semibold text-gray-600 bg-transparent rounded-full",
        ),
        dir="rtl",
    )


def login_form() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            tab_button("طالب"),
            tab_button("أستاذ"),
            tab_button("مشرف"),
            class_name="flex justify-center items-center bg-gray-100 p-1 rounded-full mb-8",
            dir="rtl",
        ),
        rx.el.form(
            rx.el.div(
                rx.el.label(
                    rx.cond(
                        AuthState.active_tab == "طالب", "رقم الجامعة", "اسم المستخدم"
                    ),
                    class_name="text-right w-full block text-sm font-medium text-gray-700 mb-1",
                    dir="rtl",
                ),
                rx.el.input(
                    name=rx.cond(
                        AuthState.active_tab == "طالب", "university_id", "username"
                    ),
                    placeholder="",
                    class_name="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500",
                    dir="rtl",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "كلمة المرور",
                    class_name="text-right w-full block text-sm font-medium text-gray-700 mb-1",
                    dir="rtl",
                ),
                rx.el.input(
                    name="password",
                    type="password",
                    placeholder="",
                    class_name="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500",
                    dir="rtl",
                ),
                class_name="mb-6",
            ),
            rx.el.button(
                rx.cond(
                    AuthState.loading,
                    rx.spinner(class_name="text-white"),
                    "تسجيل الدخول",
                ),
                type="submit",
                class_name="w-full bg-blue-600 text-white font-semibold py-3 rounded-md hover:bg-blue-700 transition-colors duration-300 flex justify-center items-center",
                dir="rtl",
                disabled=AuthState.loading,
            ),
            rx.el.a(
                "نسيت كلمة المرور؟",
                href="#",
                class_name="block text-center mt-4 text-sm text-blue-600 hover:underline",
                dir="rtl",
            ),
            on_submit=AuthState.handle_login,
            class_name="w-full",
        ),
        class_name="bg-white p-8 rounded-2xl shadow-lg w-full max-w-sm",
    )


def login() -> rx.Component:
    return rx.el.div(
        rx.cond(
            AuthState.background_image.is_not_none(),
            rx.el.div(
                style={
                    "background_image": rx.get_upload_url(AuthState.background_image),
                    "background_size": "cover",
                    "background_position": "center",
                    "filter": "blur(4px)",
                    "position": "absolute",
                    "top": 0,
                    "left": 0,
                    "right": 0,
                    "bottom": 0,
                    "z_index": -1,
                }
            ),
        ),
        rx.el.div(
            rx.upload.root(
                rx.el.button(
                    "تحميل صورة خلفية",
                    class_name="absolute top-4 right-4 bg-white/50 text-black px-3 py-1.5 rounded-lg text-sm font-medium",
                ),
                id="bg_upload",
                multiple=False,
                accept={
                    "image/png": [".png"],
                    "image/jpeg": [".jpg", ".jpeg"],
                    "image/gif": [".gif"],
                },
                on_drop=AuthState.handle_upload(rx.upload_files(upload_id="bg_upload")),
                style={
                    "width": "auto",
                    "height": "auto",
                    "border": "none",
                    "padding": "0",
                },
            ),
            login_form(),
            class_name="relative min-h-screen flex flex-col items-center justify-center p-4 font-['Tajawal']",
        ),
    )