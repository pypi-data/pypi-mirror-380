"""
Command-line interface for StopWeb
"""

import sys
from datetime import datetime
from typing import Optional, List

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

from .hosts import HostsManager, get_domain_from_url
from .duration import TimeManager, validate_duration_format, get_supported_duration_formats


console = Console()


@click.group(invoke_without_command=True)
@click.option('--duration', '-d', help='Block duration (e.g., 2h, 1d, 1w). Default: 1d')
@click.option('--list', '-l', 'list_sites', is_flag=True, help='List blocked sites')
@click.option('--remove', '-r', help='Remove blocked site')
@click.option('--clear', is_flag=True, help='Remove all blocked sites')
@click.option('--cleanup', is_flag=True, help='Remove expired blocks')
@click.argument('websites', nargs=-1)
@click.pass_context
def main(ctx, duration: Optional[str], list_sites: bool, remove: Optional[str], 
         clear: bool, cleanup: bool, websites: tuple):
    """
    StopWeb - Block websites temporarily to stay focused
    
    Examples:
      stopweb facebook.com youtube.com          # Block for 1 day (default)
      stopweb -d 2h reddit.com                 # Block for 2 hours
      stopweb --list                           # List blocked sites
      stopweb --remove facebook.com            # Unblock a site
      stopweb --clear                          # Remove all blocks
    """
    
    hosts_manager = HostsManager()
    time_manager = TimeManager()
    
    # Check permissions first
    if not hosts_manager.check_permissions():
        console.print("❌ [red]Permission denied![/red]")
        if hosts_manager._requires_sudo():
            console.print("💡 [yellow]Please run with sudo privileges:[/yellow]")
            console.print(f"   [cyan]sudo {' '.join(sys.argv)}[/cyan]")
        else:
            console.print("💡 [yellow]Please run as administrator[/yellow]")
        sys.exit(1)
    
    # Handle different operations
    if cleanup:
        handle_cleanup(hosts_manager)
        return
    
    if clear:
        handle_clear(hosts_manager)
        return
    
    if remove:
        handle_remove(hosts_manager, remove)
        return
    
    if list_sites:
        handle_list(hosts_manager, time_manager)
        return
    
    if websites:
        handle_block(hosts_manager, time_manager, websites, duration)
        return
    
    # No arguments provided, show help
    if ctx.invoked_subcommand is None:
        show_welcome()
        ctx.get_help()


def handle_block(hosts_manager: HostsManager, time_manager: TimeManager, 
                websites: tuple, duration: Optional[str]):
    """Handle blocking websites"""
    
    # Validate duration format if provided
    if duration and not validate_duration_format(duration):
        console.print(f"❌ [red]Invalid duration format:[/red] {duration}")
        console.print(get_supported_duration_formats())
        sys.exit(1)
    
    try:
        expires_at = time_manager.calculate_expires_at(duration)
    except ValueError as e:
        console.print(f"❌ [red]{e}[/red]")
        sys.exit(1)
    
    # Clean up expired sites first
    hosts_manager.cleanup_expired_sites()
    
    success_count = 0
    failed_sites = []
    
    for website in websites:
        domain = get_domain_from_url(website)
        
        if hosts_manager.add_blocked_site(domain, expires_at):
            success_count += 1
            console.print(f"✅ [green]Blocked[/green] {domain}")
        else:
            failed_sites.append(domain)
            console.print(f"❌ [red]Failed to block[/red] {domain}")
    
    if success_count > 0:
        duration_text = time_manager.format_time_remaining(expires_at)
        console.print(f"\n🎯 [bold green]Successfully blocked {success_count} site(s)[/bold green]")
        console.print(f"⏰ [yellow]Will be unblocked {duration_text}[/yellow]")
        
        # Show instructions for immediate effect
        console.print("\n💡 [dim]Note: You may need to clear your browser cache or restart your browser for immediate effect.[/dim]")
    
    if failed_sites:
        console.print(f"\n⚠️  [yellow]Failed to block:[/yellow] {', '.join(failed_sites)}")


def handle_list(hosts_manager: HostsManager, time_manager: TimeManager):
    """Handle listing blocked sites"""
    
    # Clean up expired sites first
    removed_count = hosts_manager.cleanup_expired_sites()
    if removed_count > 0:
        console.print(f"🧹 [dim]Cleaned up {removed_count} expired block(s)[/dim]\n")
    
    blocked_sites = hosts_manager.get_blocked_sites()
    
    if not blocked_sites:
        console.print("📭 [yellow]No sites are currently blocked[/yellow]")
        return
    
    table = Table(title="🚫 Blocked Websites")
    table.add_column("Website", style="cyan", no_wrap=True)
    table.add_column("Status", style="magenta")
    table.add_column("Expires", style="yellow")
    
    now = datetime.now()
    active_count = 0
    
    for domain, expires_at in blocked_sites:
        if expires_at > now:  # Active block
            status = "🔒 Active"
            expires_text = time_manager.format_time_remaining(expires_at)
            active_count += 1
        else:  # Expired (shouldn't happen after cleanup)
            status = "⌛ Expired"
            expires_text = "Should be cleaned up"
        
        table.add_row(domain, status, expires_text)
    
    console.print(table)
    console.print(f"\n📊 [bold]{active_count} active block(s)[/bold]")


def handle_remove(hosts_manager: HostsManager, domain: str):
    """Handle removing a blocked site"""
    domain = get_domain_from_url(domain)
    
    if hosts_manager.remove_blocked_site(domain):
        console.print(f"✅ [green]Unblocked[/green] {domain}")
        console.print("💡 [dim]You may need to clear your browser cache for immediate effect.[/dim]")
    else:
        console.print(f"❌ [red]Failed to unblock[/red] {domain}")


def handle_clear(hosts_manager: HostsManager):
    """Handle clearing all blocked sites"""
    removed_count = hosts_manager.remove_all_blocked_sites()
    
    if removed_count > 0:
        console.print(f"✅ [green]Removed {removed_count} blocked site(s)[/green]")
        console.print("💡 [dim]You may need to clear your browser cache for immediate effect.[/dim]")
    else:
        console.print("📭 [yellow]No blocked sites found[/yellow]")


def handle_cleanup(hosts_manager: HostsManager):
    """Handle cleaning up expired blocks"""
    removed_count = hosts_manager.cleanup_expired_sites()
    
    if removed_count > 0:
        console.print(f"🧹 [green]Cleaned up {removed_count} expired block(s)[/green]")
    else:
        console.print("✨ [yellow]No expired blocks found[/yellow]")


def show_welcome():
    """Show welcome message"""
    welcome_text = Text("StopWeb", style="bold blue")
    subtitle = Text("Block websites temporarily to stay focused", style="dim")
    
    panel = Panel.fit(
        f"{welcome_text}\n{subtitle}",
        border_style="blue",
        padding=(1, 2)
    )
    
    console.print(panel)
    console.print()


@click.command()
def version():
    """Show version information"""
    from . import __version__
    console.print(f"StopWeb version {__version__}")


# Add version command to main group
main.add_command(version)


if __name__ == '__main__':
    main()