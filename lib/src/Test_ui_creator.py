import flet as ft
import Player_database_connector as pdc
from Player_database_reset_manager import database_manager as Dbm
from Player_db_creator import create_all_tables
from Player_creator import run as pc_run 
import random


import time


def main(page: ft.Page):
    
    page.title = "MY R.O.C MANAGER"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_frameless = False



    class new_or_load_management():

        def new_management():
            Dbm.reset_all()
            Player_search.table.rows.clear()
            create_all_tables()
            print("Database info reset")
            pc_run()
            return page.go("/Dashboard")
            
        
        def load_management():
            return page.go("/dashboard")
        


    class Main_menu():
        def side_menu():
            return ft.Row(
                [
                    ft.Container(  
                        expand=False,
                        width=110,
                        height=page.window_height,
                        margin=10,
                        border_radius= 10,
                        border=ft.border.all(2, ft.colors.WHITE24),
                        bgcolor=ft.colors.BLACK12,
                        alignment=ft.alignment.top_center,
                        content=ft.Container(
                            ft.Column(
                                alignment=ft.alignment.center,
                                scroll=ft.ScrollMode.AUTO,
                                controls=
                            [
                                ft.IconButton(
                                    icon=ft.icons.SPACE_DASHBOARD,
                                    icon_color=ft.colors.WHITE60, 
                                    icon_size=50,
                                    tooltip="Dashboard",
                                    on_click=lambda _: page.go("/Dashboard"),
                                ), 
                                ft.IconButton(
                                    icon=ft.icons.SCOREBOARD,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=50,
                                    tooltip="Sim Game",
                                    on_click=lambda _: page.go("/Sim Game")
                                ),
                                ft.IconButton(
                                    icon=ft.icons.CONNECT_WITHOUT_CONTACT,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=50,
                                    tooltip="Online PVP",
                                    on_click=lambda _: page.go("/Online PvP")
                                ),
                                ft.IconButton(
                                    icon = ft.icons.SPORTS_BASKETBALL,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=45,
                                    tooltip="The R.O.C",
                                    on_click=lambda _: page.go("/The Roc")
                                ),
                                ft.IconButton(
                                    icon=ft.icons.PERSON_SEARCH_ROUNDED,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=50,
                                    tooltip="Player Search",
                                    on_click=lambda _: page.go("/Player Search")
                                ),
                                ft.IconButton(
                                    icon=ft.icons.MANAGE_ACCOUNTS,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=50,
                                    tooltip="My R.O.C Team",
                                    on_click=lambda _: page.go("/MY R.O.C Team")
                                ),
                                ft.IconButton(
                                    icon=ft.icons.SETTINGS_SHARP,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=45,
                                    tooltip="Settings",
                                    on_click=lambda _: page.go("/Settings")
                                ),
                                ft.IconButton(
                                    icon=ft.icons.LOGIN,
                                    icon_color=ft.colors.WHITE60,
                                    icon_size=40,
                                    tooltip="Logout",
                                    on_click=lambda _: page.go("/"),
                                ),
                                #ACCOUNT_CIRCLE_ROUNDED
                                #icons.LIST_ALT_ROUNDED
                            ]), 
                        margin=10,)
                    ),
                ],
                expand=False     
                )
        
        def default_menu_backdrop():
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=5,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                content=(ft.Text(
                    "MY R.O.C",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                expand=True)
                
        def management_window():
            return ft.Container(
                margin=5,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                bgcolor=ft.colors.BLACK12,
                content=ft.Container(
                    width=300,
                    height=300,
                    bgcolor=ft.colors.WHITE12,
                    border_radius=20,
                    alignment=ft.alignment.center,
                    content=
                        ft.Column([
                            ft.Text("MY R.O.C",size=50,weight=ft.FontWeight.BOLD),
                            ft.Container(
                                width=160,
                                height=30,
                                bgcolor=ft.colors.TRANSPARENT,
                                alignment=ft.alignment.center_left,
                                content=ft.Column([
                                ft.TextButton(
                                    text="New Management",
                                    disabled=False,
                                    on_click=lambda e: new_or_load_management.new_management()
                                    ),
                                ft.TextButton(
                                    text="Load Management",
                                    disabled=False,)
                                ])
                            ),
                            ],
                            spacing=15,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                ), 
                expand=True,
                alignment=ft.alignment.center
                )

        
            
    class Dashboard():
        def dashboard():
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=5,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                content=(ft.Text(
                    "Dashboard",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                expand=True)

    class Sim_game():
        def sim_game():
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=5,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                content=(ft.Text(
                    "Sim Game",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                expand=True)
        
    class The_Roc():
        def the_Roc():
            print(f"{page.route} Menu item clicked")
            return ft.Container(
            width=page.window_width,
            height=page.window_height,
            margin=5,
            border_radius=10,
            border=ft.border.all(2, ft.colors.WHITE24),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK12,
            content=(ft.Text(
                "The R.O.C",
                size=50,
                color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                )),
            expand=True)


        

    class Player_search():
        
        def player_inserter():
            pdc.mycursor.execute("SELECT * FROM player_hub")
            player_list = pdc.mycursor.fetchall()
            return player_list


        table = ft.DataTable(
            column_spacing=50,
            data_row_max_height=60,
            show_bottom_border=True,
            show_checkbox_column=False,
            
            
            columns=[
                ft.DataColumn(ft.Text(f"Id",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"First name",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Last name",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Age",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Height",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Weight",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"★ Rating",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Position",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Build",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Moral",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Trait",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Team name",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Skill set",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Injured",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Recovery days",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Potential",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Overall",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Offense",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Defense",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Roots",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Three pointer",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Midrange",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Layup",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Dunk",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Ball handle",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Speed",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Stamina",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Passing",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Strength",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Rebounding",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Interior defense",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Perimeter defense",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Steal",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Block",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Points",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Assists",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Rebounds",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Steals",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Blocks",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Turnovers",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Games played",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Points per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Assists per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Steals per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Blocks per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Rebounds per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Turnovers per game",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Field goal %",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f"Three point %",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(f""))
            ],
            rows=[
                #color=ft.colors.with_opacity(0.3,ft.colors.WHITE),
            ],
        )              

        def add_player(player_info):
            new_row = ft.DataRow(
                #on_select_changed="",
                #color=ft.colors.with_opacity(0.3,ft.colors.WHITE),
                cells=[
                ]

            )
            new_row.cells.append(ft.DataCell(ft.Text(f"{player_info[0]}"),placeholder="num"))
            new_row.cells.append(ft.DataCell(ft.CircleAvatar(content=ft.Text(f"{str(player_info[1][0])}{str(player_info[2][0])}",text_align=ft.TextAlign.CENTER,size=20),
                                                             bgcolor=ft.colors.GREY_900,radius=20)))
            for i in range(49):
                if i !=6 and i > 0:
                    new_row.cells.append(ft.DataCell(ft.Text(f"{player_info[i]}")))
                if i == 6:
                    new_row.cells.append(ft.DataCell(ft.Text(f"{(int(player_info[i]) * "★")}"))) #NOTE TO SELF. MIGHT NEED TO ADD THIS FOR THE ATTRIBUTE AND PERCENTS IN FUTURE
            new_row.cells.append(ft.DataCell(ft.CupertinoCheckbox()))
            Player_search.table.rows.append(new_row)
            page.update()


        #Way to delete all the rows to be able to make a new list with filters
        def delete_player():
            print("player deleted")
            for i in range(len(Player_search.table.rows)):
                Player_search.table.rows.pop()
                page.update()
                time.sleep(.001)
        
        def add_multiple():
            for i in range(15):
                Player_search.add_player(Player_search.player_inserter()[i])

        def player_search_menu():  
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=10,
                border_radius=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.with_opacity(0.1,ft.colors.WHITE),
                expand=True,
                content=ft.Row([
                    ft.Container(
                        padding=10,
                        expand=True,
                        border_radius=10,
                        content=ft.Row(
                            [
                                ft.Column(
                                    [Player_search.table,
                                    ft.FilledTonalButton(text="Delete players",on_click=lambda e: Player_search.delete_player()),
                                    ft.FilledTonalButton(text="Add player",on_click=lambda e: Player_search.add_multiple())],
                                    scroll=ft.ScrollMode.AUTO,alignment=ft.alignment.center,on_scroll_interval=.1
                                ),
                            ],
                            scroll=ft.ScrollMode.AUTO,alignment=ft.alignment.center
                            ),
                        alignment=ft.alignment.top_center
                    )
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER
                )
            )   
        

    class Online_pvp():
        def online_pvp():
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=5,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                content=(ft.Text(
                    "Online PvP",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                expand=True)


    class My_ROC_Team():
        def my_roc_team():
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=5,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                content=(ft.Text(
                    "MY R.O.C Team",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                expand=True)

    class Settings():
        def settings():
            print(f"{page.route} Menu item clicked")
            return ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=5,
                border_radius=10,
                border=ft.border.all(2, ft.colors.WHITE24),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                content=(ft.Text(
                    "Settings",
                    size=50,
                    color=ft.colors.with_opacity(0.5,ft.colors.WHITE),
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    )),
                expand=True)



    def route_change(route):
        page.update
        page.views.clear()
        page.views.append(

        ft.View(
            "/",
            [   
                ft.Row ([
                ft.Row(alignment="top_left", spacing=25, controls=[Main_menu.management_window()],expand=True),
                  #Main_dashboard
                ],
                expand=True)
            ],
            
            )
        )
        if page.route == "/Login":
            page.views.append(
                ft.View(
                    "/Login",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_left", spacing=25, controls=[Main_menu.management_window()],expand=True),
                        ],expand=True)
                    ]
                )
            )
        
    
        if page.route == "/Dashboard":
            page.views.append(
                ft.View(
                    "/Dashboard",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_left", spacing=25, controls=[Main_menu.side_menu(),Dashboard.dashboard()],expand=True),
                        ],expand=True)
                    ]
                )
            )
        
        if page.route == "/Sim Game":
            page.views.append(
                ft.View(
                    "/Sim Game",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_let", spacing=25, controls=[Main_menu.side_menu(),Sim_game.sim_game()],expand=True),
                        ],expand=True)
                    ],
                )
            )

        if page.route == "/Online PvP":
            page.views.append(
                ft.View(
                    "/Online PvP",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_let", spacing=25, controls=[Main_menu.side_menu(),Online_pvp.online_pvp()],expand=True),
                        ],expand=True)
                    ],
                )
            )
        if page.route == "/The Roc":
            page.views.append(
                ft.View(
                    "/The Roc",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_left", spacing=25, controls=[Main_menu.side_menu(),The_Roc.the_Roc()],expand=True),
                        ],expand=True)
                    ]
                )
            )
        
        if page.route == "/Player Search":
            page.views.append(
                ft.View(
                    "/Player Search",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_let", spacing=25, controls=[Main_menu.side_menu(),Player_search.player_search_menu()],expand=True),
                        ],expand=True)
                    ],
                )
            )
        if page.route == "/MY R.O.C Team":
            page.views.append(
                ft.View(
                    "/MY R.O.C Team",         
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_let", spacing=25, controls=[Main_menu.side_menu(),My_ROC_Team.my_roc_team()],expand=True),
                        ],expand=True)
                    ],
                )
            )
        if page.route == "/Settings":
            page.views.append(
                ft.View(
                    "/Settings",
                    [
                        ft.Row ([ 
                        ft.Row(alignment="top_let", spacing=25, controls=[Main_menu.side_menu(),Settings.settings()],expand=True),
                        ],expand=True)
                    ],
                )
            )
            
    def page_resive(e):
        page.go(f"'{page.route}'")
       

    page.update()
    page.on_route_change = route_change

    page.go(page.route)
    


ft.app(target=main)
