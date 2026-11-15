import flet as ft


def main(page: ft.Page):
    page.title = "Flet بالعربي"
    page.rtl = True
    page.bgcolor = ft.Colors.GREY_50
    page.padding = 24
    page.scroll = ft.ScrollMode.AUTO

    status = ft.Text(
        "جاهز؟ اضغط الزر لتجربة التفاعل.",
        color=ft.Colors.WHITE,
        size=14,
    )

    def show_demo():
        status.value = "ممتاز! هذا الزر يعمل باستخدام Python وFlet."
        page.update()

    header = ft.Row(
        controls=[
            ft.Text("Flet بالعربي", size=22, weight=ft.FontWeight.W_700, color=ft.Colors.BLUE_GREY_900),
            ft.Container(
                content=ft.Text("تطبيق تجريبي", size=13, color=ft.Colors.BLUE_700),
                bgcolor=ft.Colors.LIGHT_BLUE_50,
                padding=ft.Padding.symmetric(horizontal=14, vertical=8),
                border_radius=ft.BorderRadius.all(20),
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        wrap=True,
    )

    hero = ft.Container(
        width=980,
        padding=32,
        bgcolor=ft.Colors.BLUE_GREY_900,
        border_radius=ft.BorderRadius.all(24),
        content=ft.Column(
            controls=[
                ft.Text("PYTHON  +  FLET", size=13, color=ft.Colors.LIGHT_BLUE_200, weight=ft.FontWeight.W_700),
                ft.Text(
                    "حوّل أفكارك إلى تطبيقات جميلة",
                    size=34,
                    weight=ft.FontWeight.W_700,
                    color=ft.Colors.WHITE,
                ),
                ft.Text(
                    "Flet يسهّل بناء واجهات تفاعلية ببايثون، ويمكنك تشغيلها كتطبيق أو على الويب.",
                    size=16,
                    color=ft.Colors.BLUE_GREY_100,
                ),
                ft.Button(
                    content=ft.Text("جرّب التفاعل"),
                    bgcolor=ft.Colors.LIGHT_BLUE_200,
                    color=ft.Colors.BLUE_GREY_900,
                    on_click=show_demo,
                ),
                status,
            ],
            spacing=16,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
    )

    features = ft.Row(
        controls=[
            feature_card("🧩", "واجهة واحدة", "أنشئ واجهات متناسقة تعمل على أكثر من منصة."),
            feature_card("🐍", "بايثون ببساطة", "اكتب منطق التطبيق باستخدام Python ومكتباتها."),
            feature_card("⚡", "تفاعل مباشر", "حدّث الواجهة واستجب لنقرات المستخدم بسهولة."),
        ],
        spacing=16,
        run_spacing=16,
        wrap=True,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    code_sample = ft.Container(
        width=980,
        padding=20,
        bgcolor=ft.Colors.BLUE_GREY_50,
        border=ft.Border.all(1, ft.Colors.BLUE_GREY_100),
        border_radius=ft.BorderRadius.all(16),
        content=ft.Column(
            controls=[
                ft.Text("بداية صغيرة بالكود", size=19, weight=ft.FontWeight.W_700, color=ft.Colors.BLUE_GREY_900),
                ft.Text(
                    'import flet as ft\n\ndef main(page: ft.Page):\n    page.add(ft.Text("مرحبًا من Flet!"))\n\nft.run(main)',
                    font_family="monospace",
                    size=14,
                    color=ft.Colors.BLUE_GREY_800,
                    rtl=False,
                    text_align=ft.TextAlign.LEFT,
                ),
            ],
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
    )

    page.add(
        ft.Column(
            controls=[
                ft.Container(width=980, content=header),
                hero,
                ft.Container(
                    width=980,
                    content=ft.Column(
                        controls=[
                            ft.Text("لماذا Flet؟", size=24, weight=ft.FontWeight.W_700, color=ft.Colors.BLUE_GREY_900),
                            features,
                        ],
                        spacing=16,
                    ),
                ),
                code_sample,
                ft.Text("صُنع ببايثون وFlet", size=13, color=ft.Colors.BLUE_GREY_500),
            ],
            spacing=24,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


def feature_card(emoji: str, title: str, description: str) -> ft.Container:
    return ft.Container(
        width=300,
        padding=20,
        bgcolor=ft.Colors.WHITE,
        border=ft.Border.all(1, ft.Colors.GREY_200),
        border_radius=ft.BorderRadius.all(16),
        content=ft.Column(
            controls=[
                ft.Text(emoji, size=28),
                ft.Text(title, size=18, weight=ft.FontWeight.W_700, color=ft.Colors.BLUE_GREY_900),
                ft.Text(description, size=14, color=ft.Colors.BLUE_GREY_600),
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
    )


ft.run(main)
