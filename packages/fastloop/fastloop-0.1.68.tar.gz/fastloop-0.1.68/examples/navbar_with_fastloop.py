import reflex as rx

from fastloop.client import FastLoopState, LoopEvent


# Mock theme imports - replace with your actual theme imports
class ColorShades:
    white = "white"

    class gray:
        gray2 = "var(--gray-2)"
        gray4 = "var(--gray-4)"
        gray6 = "var(--gray-6)"
        gray11 = "var(--gray-11)"

    class blue:
        blue5 = "var(--blue-5)"
        blue8 = "var(--blue-8)"
        blue10 = "var(--blue-10)"


class SpacingTokens:
    s0 = "0"
    s1 = "1"
    s3 = "3"
    css_2 = "8px"
    css_3 = "12px"


def get_typography_style(style_name):
    return {"font_size": "14px"}


class NavItem(rx.Base):
    """Navigation item data model."""

    label: str
    route: str
    icon: str | None = None
    is_active: bool = False


class NavbarState(FastLoopState, rx.State):
    """State for navbar with FastLoop integration."""

    # Existing navbar state
    is_collapsed: bool = False

    # FastLoop connection state (automatically available from FastLoopState)
    connection_status: str = "Disconnected"

    def __init__(self):
        # Connect to your FastLoop instance
        super().__init__("http://localhost:8000/navbar")

    def toggle_collapse(self):
        """Toggle the navbar collapse state."""
        self.is_collapsed = not self.is_collapsed

    def event_callback(self, event: LoopEvent):
        """Handle FastLoop events"""
        if event.type == "status_update":
            self.connection_status = event.data.get("status", "Unknown")
        elif event.type == "user_activity":
            # Handle user activity events
            pass

    async def on_mount(self):
        """Initialize connection when navbar mounts"""
        await self.send("navbar_init", {"user": "luke@smartshare.io"})


def nav_item(item: NavItem) -> rx.Component:
    """Render a single navigation item with improved styling."""
    return rx.link(
        rx.hstack(
            rx.cond(
                item.icon,
                rx.icon(
                    item.icon,
                    size=18,
                    color=rx.cond(
                        item.is_active, ColorShades.white, ColorShades.gray.gray11
                    ),
                ),
                rx.box(),
            ),
            rx.cond(
                ~NavbarState.is_collapsed,
                rx.text(
                    item.label,
                    style={
                        "color": rx.cond(
                            item.is_active, ColorShades.white, ColorShades.gray.gray11
                        ),
                        **get_typography_style("textSm"),
                        "font_weight": rx.cond(item.is_active, "500", "400"),
                    },
                ),
                rx.box(),
            ),
            spacing=SpacingTokens.s3,
            align_items="center",
            width="100%",
            padding=rx.cond(
                NavbarState.is_collapsed,
                f"{SpacingTokens.css_2} {SpacingTokens.css_2}",
                f"{SpacingTokens.css_2} {SpacingTokens.css_2}",
            ),
            border_radius="8px",
            background_color=rx.cond(
                item.is_active, ColorShades.blue.blue5, "transparent"
            ),
            border=rx.cond(
                item.is_active,
                f"1px solid {ColorShades.blue.blue8}",
                "1px solid transparent",
            ),
            justify_content=rx.cond(NavbarState.is_collapsed, "center", "flex-start"),
            _hover={
                "background_color": rx.cond(
                    item.is_active, ColorShades.blue.blue10, ColorShades.gray.gray4
                ),
                "cursor": "pointer",
                "transform": "translateY(-1px)",
            },
            _focus={
                "outline": "none",
                "box_shadow": "none",
            },
            transition="all 200ms ease-in-out",
        ),
        href=item.route,
        text_decoration="none",
        width="100%",
        _focus={
            "outline": "none",
            "box_shadow": "none",
        },
    )


def navbar() -> rx.Component:
    """Main navigation sidebar component with FastLoop integration."""
    nav_items = [
        NavItem(label="Chat", route="/chat", icon="message_circle", is_active=True),
        NavItem(label="Usage", route="/usage", icon="activity"),
    ]

    return rx.box(
        rx.vstack(
            # Top section with toggle button
            rx.hstack(
                rx.button(
                    rx.icon(
                        rx.cond(
                            NavbarState.is_collapsed,
                            "menu",
                            "x",
                        ),
                        size=18,
                        color=ColorShades.gray.gray11,
                    ),
                    on_click=NavbarState.toggle_collapse,
                    variant="ghost",
                    size="2",
                    padding=SpacingTokens.css_2,
                    background_color="transparent",
                    _hover={
                        "background_color": ColorShades.gray.gray4,
                    },
                    _focus={
                        "outline": "none",
                        "box_shadow": "none",
                    },
                    transition="all 150ms ease-in-out",
                ),
                justify_content=rx.cond(NavbarState.is_collapsed, "center", "flex-end"),
                width="100%",
                padding=f"{SpacingTokens.css_3} {SpacingTokens.css_3}",
                border_bottom=f"1px solid {ColorShades.gray.gray6}",
                margin_bottom=SpacingTokens.css_3,
            ),
            # Navigation items
            rx.vstack(
                *[nav_item(item) for item in nav_items],
                spacing=SpacingTokens.s1,
                width="100%",
                padding=f"0 {SpacingTokens.css_3}",
            ),
            # Spacer to push user section to bottom
            rx.spacer(),
            # User section with FastLoop status
            rx.cond(
                ~NavbarState.is_collapsed,
                rx.box(
                    rx.vstack(
                        # User email
                        rx.text(
                            "luke@smartshare.io",
                            style={
                                "color": ColorShades.gray.gray11,
                                **get_typography_style("textSm"),
                            },
                        ),
                        # FastLoop connection status - MINIMAL ADDITION
                        rx.hstack(
                            rx.box(
                                width="8px",
                                height="8px",
                                border_radius="50%",
                                background_color=rx.cond(
                                    NavbarState.is_connected, "green", "red"
                                ),
                            ),
                            rx.text(
                                rx.cond(
                                    NavbarState.is_connected,
                                    "FastLoop Connected",
                                    "FastLoop Offline",
                                ),
                                style={
                                    "color": ColorShades.gray.gray11,
                                    **get_typography_style("textSm"),
                                    "font_size": "12px",
                                },
                            ),
                            spacing="6px",
                            align_items="center",
                        ),
                        align_items="flex-start",
                        spacing=SpacingTokens.s1,
                    ),
                    padding=f"{SpacingTokens.css_3}",
                    border_top=f"1px solid {ColorShades.gray.gray6}",
                    margin_top=SpacingTokens.css_3,
                    width="100%",
                ),
                # Collapsed state - just show connection dot
                rx.box(
                    rx.box(
                        width="8px",
                        height="8px",
                        border_radius="50%",
                        background_color=rx.cond(
                            NavbarState.is_connected, "green", "red"
                        ),
                        margin="auto",
                    ),
                    padding=f"{SpacingTokens.css_3}",
                    border_top=f"1px solid {ColorShades.gray.gray6}",
                    margin_top=SpacingTokens.css_3,
                    width="100%",
                ),
            ),
            spacing=SpacingTokens.s0,
            height="100vh",
            width="100%",
        ),
        width=rx.cond(NavbarState.is_collapsed, "80px", "250px"),
        background_color=ColorShades.gray.gray2,
        border_right=f"1px solid {ColorShades.gray.gray6}",
        flex_shrink="0",
        transition="width 250ms ease-in-out",
    )


# Example page to show the navbar in action
def main_page():
    return rx.hstack(
        navbar(),
        rx.box(
            rx.vstack(
                rx.heading("Main Content", size="6"),
                rx.text(f"FastLoop Status: {NavbarState.connection_status}"),
                rx.text(f"Loop ID: {NavbarState.loop_id}"),
                rx.button(
                    "Send Test Event",
                    on_click=lambda: NavbarState.send(
                        "test_event", {"timestamp": "now"}
                    ),
                ),
                spacing="4",
                padding="20px",
            ),
            flex="1",
            min_height="100vh",
        ),
        width="100%",
        height="100vh",
    )


app = rx.App()
app.add_page(main_page, route="/")

if __name__ == "__main__":
    app.run()
