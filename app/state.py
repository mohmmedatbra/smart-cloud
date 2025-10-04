import reflex as rx
import asyncio


class AuthState(rx.State):
    """The authentication state for the app."""

    is_logged_in: bool = False
    show_login: bool = False
    active_tab: str = "طالب"
    background_image: str | None = None
    loading: bool = False

    @rx.event
    def go_to_login(self):
        self.show_login = True

    @rx.event
    def set_active_tab(self, tab: str):
        self.active_tab = tab

    @rx.event
    async def handle_login(self, form_data: dict):
        self.loading = True
        yield
        await asyncio.sleep(2)
        is_student = self.active_tab == "طالب"
        identifier = (
            form_data.get("university_id") if is_student else form_data.get("username")
        )
        password = form_data.get("password")
        if identifier and password:
            self.is_logged_in = True
        else:
            error_message = (
                "الرجاء إدخال رقم الجامعة وكلمة المرور"
                if is_student
                else "الرجاء إدخال اسم المستخدم وكلمة المرور"
            )
            yield rx.toast.error(error_message)
        self.loading = False

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        if not files:
            yield rx.toast.error("لم يتم اختيار أي ملف")
            return
        file = files[0]
        upload_data = await file.read()
        upload_dir = rx.get_upload_dir()
        upload_dir.mkdir(parents=True, exist_ok=True)
        file_path = upload_dir / file.name
        with file_path.open("wb") as f:
            f.write(upload_data)
        self.background_image = file.name
        yield rx.toast.success(f"تم تحميل الخلفية بنجاح")