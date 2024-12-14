from logger_config import logger
import parsing
import thread_manager
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table

console = Console()

def show_menu():
    menu_table = Table(show_header=False, show_edge=False, box=None)
    menu_table.add_row("[magenta]👤 Автор:[/magenta] [cyan]КИАНА[/cyan]")
    menu_table.add_row("[magenta]🌐 Форум:[/magenta] [cyan]https://zelenka.guru/kqlol/[/cyan]")
    menu_table.add_row("[magenta]📅 Дата создания:[/magenta] [cyan]15.12.2024[/cyan]")
    menu_table.add_row("")
    menu_table.add_row("[yellow]1.[/yellow] [cyan]📊 Спарсить темы[/cyan]")
    menu_table.add_row("[yellow]2.[/yellow] [cyan]🔄 Управление темами[/cyan]")
    menu_table.add_row("[yellow]3.[/yellow] [cyan]🚪 Выход[/cyan]")
    
    panel = Panel(
        menu_table,
        title="[bold yellow]🎮 Меню[/bold yellow]",
        border_style="cyan",
        padding=(1, 2)
    )
    console.print(panel)

def main():
    logger.info("✨ Программа запущена")
    try:
        while True:
            show_menu()
            choice = console.input("[green]📝 Выберите действие (1/2/3): [/green]")
            
            if choice == "1":
                parsing.parse_threads()
            elif choice == "2":
                thread_manager.manage_threads()
            elif choice == "3":
                logger.info("🎉 Программа завершена")
                console.print("\n[yellow]✨ Спасибо за использование программы![/yellow]")
                break
            else:
                logger.error("❌ Введен неверный выбор")
    except KeyboardInterrupt:
        console.print("\n[yellow]👋 Программа завершена пользователем[/yellow]")
        logger.info("🎉 Программа завершена")
    except Exception as e:
        logger.error(f"❌ Непредвиденная ошибка: {str(e)}")
    finally:
        console.print("[cyan]👋 До свидания![/cyan]")

if __name__ == "__main__":
    main()
