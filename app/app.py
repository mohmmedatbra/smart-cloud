import reflex as rx
from app.state import AuthState
from app.pages.login import login
from app.pages.main_page import main_page
from app.pages.landing_page import landing_page


def index() -> rx.Component:
    return rx.el.div(
        rx.cond(
            AuthState.is_logged_in,
            main_page(),
            rx.cond(AuthState.show_login, login(), landing_page()),
        )
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")