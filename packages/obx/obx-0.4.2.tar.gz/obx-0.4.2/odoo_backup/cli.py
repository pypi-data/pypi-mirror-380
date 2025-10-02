#!/usr/bin/env python3
"""
Odoo Backup Tool
Interactive tool for backing up Odoo databases and filestore
"""

import os
import sys
import subprocess
import zipfile
import tempfile
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Optional

import click
import psycopg2
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.progress import track

console = Console()


def get_databases(host: str, port: int, user: str, password: str) -> List[str]:
    """Get list of available databases"""
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database='postgres'
        )
        cur = conn.cursor()
        cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
        databases = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()
        return databases
    except Exception as e:
        console.print(f"[red]Error connecting to PostgreSQL: {e}[/red]")
        sys.exit(1)


def create_db_backup(host: str, port: int, user: str, password: str, database: str, output_file: str):
    """Create database backup using pg_dump"""
    env = os.environ.copy()
    if password:
        env['PGPASSWORD'] = password

    cmd = [
        'pg_dump',
        '-h', host,
        '-p', str(port),
        '-U', user,
        '-d', database,
        '--no-password',
        '-f', output_file
    ]

    try:
        result = subprocess.run(cmd, env=env, capture_output=True, text=True)
        if result.returncode != 0:
            console.print(f"[red]Error creating database backup: {result.stderr}[/red]")
            return False
        return True
    except FileNotFoundError:
        console.print("[red]pg_dump not found. Please install PostgreSQL client tools.[/red]")
        return False


def create_filestore_backup(filestore_path: str, temp_dir: str) -> str:
    """Create filestore backup"""
    filestore_backup = os.path.join(temp_dir, "filestore.zip")

    if not os.path.exists(filestore_path):
        console.print(f"[yellow]Filestore path not found: {filestore_path}[/yellow]")
        return None

    with zipfile.ZipFile(filestore_backup, 'w', zipfile.ZIP_DEFLATED) as zipf:
        filestore_path_obj = Path(filestore_path)
        for file_path in track(list(filestore_path_obj.rglob('*')), description="Backing up filestore..."):
            if file_path.is_file():
                arcname = file_path.relative_to(filestore_path_obj.parent)
                zipf.write(file_path, arcname)

    return filestore_backup


def create_full_backup(db_backup: str, filestore_backup: Optional[str], output_path: str, database: str):
    """Create final ZIP backup with database and filestore"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{database}_{timestamp}.zip"
    full_backup_path = os.path.join(output_path, backup_filename)

    os.makedirs(output_path, exist_ok=True)

    with zipfile.ZipFile(full_backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add database backup
        zipf.write(db_backup, f"{database}.sql")

        # Add filestore if exists
        if filestore_backup and os.path.exists(filestore_backup):
            zipf.write(filestore_backup, "filestore.zip")

    return full_backup_path


def cleanup_old_backups(output_path: str, days: int = 7) -> None:
    """Remove backup files older than specified days"""
    try:
        backup_dir = Path(output_path)
        if not backup_dir.exists():
            return

        cutoff_date = datetime.now() - timedelta(days=days)
        deleted_count = 0

        for backup_file in backup_dir.glob("*.zip"):
            if backup_file.stat().st_mtime < cutoff_date.timestamp():
                try:
                    backup_file.unlink()
                    deleted_count += 1
                    console.print(f"[dim]Deleted old backup: {backup_file.name}[/dim]")
                except Exception as e:
                    console.print(f"[yellow]Could not delete {backup_file.name}: {e}[/yellow]")

        if deleted_count > 0:
            console.print(f"[green]✓ Cleaned up {deleted_count} old backup(s)[/green]")

    except Exception as e:
        console.print(f"[yellow]Warning: Could not cleanup old backups: {e}[/yellow]")


def parse_odoo_config_file(config_path: str) -> Optional[str]:
    """Parse Odoo configuration file to extract data_dir"""
    try:
        with open(config_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('data_dir') and '=' in line:
                    data_dir = line.split('=', 1)[1].strip()
                    # Remove quotes if present
                    data_dir = data_dir.strip('"\'')
                    if data_dir and os.path.exists(data_dir):
                        console.print(f"[green]✓ Found data_dir in {config_path}: {data_dir}[/green]")
                        return data_dir
    except Exception as e:
        console.print(f"[dim]Could not read config file {config_path}: {e}[/dim]")
    return None


def get_odoo_data_dir() -> Optional[str]:
    """Try to detect Odoo data_dir from configuration"""

    # Method 1: Try to import Odoo and get data_dir from config
    try:
        import odoo
        from odoo.tools import config

        # Initialize Odoo config if not already done
        if not hasattr(config, 'loaded'):
            config.parse_config()

        data_dir = config.get('data_dir')
        if data_dir and os.path.exists(data_dir):
            console.print(f"[green]✓ Found Odoo data_dir from config: {data_dir}[/green]")
            return data_dir
        elif data_dir:
            console.print(f"[yellow]Found data_dir in config but path doesn't exist: {data_dir}[/yellow]")
    except ImportError:
        pass
    except Exception as e:
        pass

    # Method 2: Try to find and parse Odoo configuration files
    config_locations = [
        "/etc/odoo/odoo.conf",
        "/etc/odoo.conf",
        "/etc/odoo/odoo-server.conf",
        "/opt/odoo/odoo.conf",
        "/opt/odoo/conf/odoo.conf",
        "./odoo.conf",
        "./odoo-server.conf",
        "../odoo.conf",
        "~/odoo.conf",
        "~/.odoorc",
        "~/.openerp_serverrc",  # Legacy
    ]

    # Windows config locations
    if os.name == 'nt':
        appdata = os.environ.get('APPDATA', '')
        programfiles = os.environ.get('PROGRAMFILES', 'C:\\Program Files')
        if appdata:
            config_locations.extend([
                os.path.join(appdata, "Odoo", "odoo.conf"),
                os.path.join(appdata, "odoo.conf"),
            ])
        config_locations.extend([
            os.path.join(programfiles, "Odoo", "server", "odoo.conf"),
            os.path.join(programfiles, "Odoo", "odoo.conf"),
            "C:\\odoo\\odoo.conf",
        ])

    for config_path in config_locations:
        expanded_path = os.path.expanduser(config_path)
        if os.path.exists(expanded_path):
            data_dir = parse_odoo_config_file(expanded_path)
            if data_dir:
                return data_dir

    return None


def get_filestore_from_database(host: str, port: int, user: str, password: str, database: str) -> Optional[str]:
    """Get filestore path directly from Odoo database configuration"""
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        cur = conn.cursor()

        # Method 1: Check ir_config_parameter for data_dir or filestore path
        cur.execute("""
            SELECT key, value FROM ir_config_parameter
            WHERE key IN ('data_dir', 'database.filestore_path', 'ir_attachment.location')
            ORDER BY
                CASE key
                    WHEN 'database.filestore_path' THEN 1
                    WHEN 'data_dir' THEN 2
                    WHEN 'ir_attachment.location' THEN 3
                END
        """)
        results = cur.fetchall()

        for key, value in results:
            if not value:
                continue

            if key == 'database.filestore_path':
                # Direct filestore path
                if os.path.exists(value):
                    console.print(f"[green]✓ Found filestore: {value}[/green]")
                    cur.close()
                    conn.close()
                    return value
            elif key == 'data_dir':
                # Data directory, filestore should be data_dir/filestore/database
                filestore_path = os.path.join(value, "filestore", database)
                if os.path.exists(filestore_path):
                    console.print(f"[green]✓ Found filestore: {filestore_path}[/green]")
                    cur.close()
                    conn.close()
                    return filestore_path

        # Method 2: Find filestore by examining stored files
        cur.execute("""
            SELECT store_fname FROM ir_attachment
            WHERE store_fname IS NOT NULL
            AND store_fname != ''
            LIMIT 1
        """)
        result = cur.fetchone()

        if result and result[0]:
            store_fname = result[0]

            # Try to locate this file in common locations
            possible_base_dirs = [
                "/var/lib/odoo/.local/share/Odoo",
                "/home/odoo/.local/share/Odoo",
                "/opt/odoo/data",
                "/var/lib/odoo",
                "/home/odoo/data",
                os.path.expanduser("~/.local/share/Odoo"),
            ]

            for base_dir in possible_base_dirs:
                test_path = os.path.join(base_dir, "filestore", database, store_fname[:2], store_fname)
                if os.path.exists(test_path):
                    filestore_path = os.path.join(base_dir, "filestore", database)
                    console.print(f"[green]✓ Found filestore: {filestore_path}[/green]")
                    cur.close()
                    conn.close()
                    return filestore_path

        cur.close()
        conn.close()
        return None

    except Exception as e:
        return None


def detect_filestore_path(database: str) -> Optional[str]:
    """Detect Odoo filestore path automatically using Odoo's standard locations"""
    console.print("[dim]Searching for filestore...[/dim]")

    # Try to get the actual Odoo data_dir from configuration
    odoo_data_dir = get_odoo_data_dir()

    possible_paths = []

    # If we found Odoo data_dir, prioritize it
    if odoo_data_dir:
        possible_paths.append(os.path.join(odoo_data_dir, "filestore", database))

    # Add common locations based on OS
    from pathlib import Path
    home_dir = str(Path.home())

    if os.name == 'nt':  # Windows
        appdata = os.environ.get('APPDATA', '')
        programfiles = os.environ.get('PROGRAMFILES', 'C:\\Program Files')

        possible_paths.extend([
            os.path.join(programfiles, "Odoo", "filestore", database),
            os.path.join(programfiles, "Odoo", "data", "filestore", database),
        ])

        if appdata:
            possible_paths.extend([
                os.path.join(appdata, "Odoo", "filestore", database),
                os.path.join(appdata, "odoo", "filestore", database),
            ])

    else:  # Linux/Unix
        # Standard locations
        possible_paths.extend([
            os.path.join(home_dir, ".local", "share", "Odoo", "filestore", database),
        ])

        # Common system users
        odoo_users = ['odoo', 'odoo-server', 'openerp']
        for user in odoo_users:
            possible_paths.extend([
                f"/var/lib/{user}/.local/share/Odoo/filestore/{database}",
                f"/home/{user}/.local/share/Odoo/filestore/{database}",
                f"/var/lib/{user}/filestore/{database}",
                f"/home/{user}/data/filestore/{database}",
            ])

        # System-wide locations
        possible_paths.extend([
            f"/opt/odoo/data/filestore/{database}",
            f"/var/odoo/filestore/{database}",
        ])

    # Check paths
    for path in possible_paths:
        if os.path.exists(path) and os.path.isdir(path):
            try:
                files = list(Path(path).rglob('*'))
                if len(files) > 0:
                    console.print(f"[green]✓ Found filestore: {path}[/green]")
                    return path
            except (PermissionError, OSError):
                continue

    return None


def add_to_crontab(cron_line: str) -> bool:
    """Add or modify a line in user's crontab"""
    try:
        # Get current crontab
        result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
        current_crontab = result.stdout if result.returncode == 0 else ""

        # Check if a similar job already exists (looking for 'uvx obx' lines)
        existing_lines = current_crontab.split('\n')
        obx_lines = [line for line in existing_lines if 'uvx obx' in line]

        if obx_lines:
            console.print(f"[yellow]⚠ Found existing obx cron job(s):[/yellow]")
            for i, line in enumerate(obx_lines, 1):
                console.print(f"  {i}. [cyan]{line.strip()}[/cyan]")

            action = Prompt.ask(
                "\nChoose action",
                choices=["replace", "add", "cancel"],
                default="replace"
            )

            if action == "cancel":
                console.print("[yellow]Cron setup cancelled[/yellow]")
                return False
            elif action == "replace":
                # Remove existing obx lines and add new one
                new_lines = [line for line in existing_lines if 'uvx obx' not in line]
                new_lines.append(cron_line.strip())
                new_crontab = '\n'.join(new_lines) + '\n'
                console.print("[green]Replacing existing obx cron job...[/green]")
            else:  # add
                new_crontab = current_crontab + cron_line + "\n"
                console.print("[green]Adding additional cron job...[/green]")
        else:
            # Check if the exact job already exists
            if cron_line.strip() in current_crontab:
                console.print("[yellow]⚠ This exact cron job already exists in your crontab[/yellow]")
                return True

            # Add new line to crontab
            new_crontab = current_crontab + cron_line + "\n"

        # Write back to crontab
        process = subprocess.Popen(['crontab', '-'], stdin=subprocess.PIPE, text=True)
        process.communicate(input=new_crontab)

        if process.returncode == 0:
            console.print("[bold green]✅ Cron job updated successfully in your crontab![/bold green]")
            return True
        else:
            console.print("[red]❌ Failed to update cron job in crontab[/red]")
            return False

    except FileNotFoundError:
        console.print("[red]❌ crontab command not found. Please install cron or add manually.[/red]")
        return False
    except Exception as e:
        console.print(f"[red]❌ Error updating crontab: {e}[/red]")
        return False


def setup_cron_job(command: str):
    """Setup cron job for automated backups"""
    console.print("\n[bold cyan]⏰ Cron Job Configuration[/bold cyan]")
    console.print("Common schedules:")
    console.print("  • [green]0 2 * * *[/green]     - Daily at 2:00 AM")
    console.print("  • [green]0 3 * * 0[/green]     - Weekly on Sunday at 3:00 AM")
    console.print("  • [green]0 1 1 * *[/green]     - Monthly on 1st at 1:00 AM")
    console.print("  • [green]0 */6 * * *[/green]   - Every 6 hours")

    cron_entry = Prompt.ask("\nEnter cron schedule", default="0 2 * * *")
    full_command = f"{cron_entry} {command}"

    console.print(f"\n[bold yellow]📋 Cron job to be added:[/bold yellow]")
    console.print(f"[bold green]{full_command}[/bold green]")

    # Ask if user wants automatic addition to crontab
    if Confirm.ask("\nAdd this cron job to your crontab automatically?", default=True):
        success = add_to_crontab(full_command)

        if success:
            console.print("\n[bold]✅ Setup complete![/bold]")
            console.print("Your automated backup is now configured.")
            console.print("\n[bold]To verify:[/bold]")
            console.print("Run: [cyan]crontab -l[/cyan]")
        else:
            console.print(f"\n[bold yellow]📋 Manual setup required:[/bold yellow]")
            console.print("1. Run: [cyan]crontab -e[/cyan]")
            console.print("2. Add the line above")
            console.print("3. Save and exit")
    else:
        console.print(f"\n[bold yellow]📋 Manual setup:[/bold yellow]")
        console.print("1. Run: [cyan]crontab -e[/cyan]")
        console.print("2. Add the line above")
        console.print("3. Save and exit")

    console.print("\n[dim]💡 Tip: Test the command manually first to ensure it works![/dim]")


@click.command()
@click.option('--host', default=None, help='PostgreSQL host')
@click.option('--port', default=None, type=int, help='PostgreSQL port')
@click.option('--user', default=None, help='PostgreSQL user')
@click.option('--password', default=None, help='PostgreSQL password')
@click.option('--database', default=None, help='Database name')
@click.option('--output-path', default=None, help='Output directory for backups')
@click.option('--cron', is_flag=True, help='Setup cron job for automated backups')
@click.option('--cleanup-days', default=None, type=int, help='Remove backups older than N days (default: 7)')
@click.option('--non-interactive', is_flag=True, help='Run in non-interactive mode')
def main(host, port, user, password, database, output_path, cron, cleanup_days, non_interactive):
    """Odoo Backup Tool - Interactive backup for Odoo databases and filestore"""

    console.print("[bold blue]🗄️  Odoo Backup Tool[/bold blue]")
    console.print()

    # If only setting up cron, handle it separately
    if cron and not non_interactive:
        console.print("[bold]📅 Cron Setup Mode[/bold]")
        console.print("Configure automatic daily backups\n")

        if not host:
            host = Prompt.ask("PostgreSQL host", default="localhost")
        if not port:
            port = int(Prompt.ask("PostgreSQL port", default="5432"))
        if not user:
            user = Prompt.ask("PostgreSQL user", default="odoo")
        if not password:
            password = Prompt.ask("PostgreSQL password", password=True, default="")

    # Interactive mode if parameters not provided
    if not non_interactive and not cron:
        if not host:
            host = Prompt.ask("PostgreSQL host", default="localhost")
        if not port:
            port = int(Prompt.ask("PostgreSQL port", default="5432"))
        if not user:
            user = Prompt.ask("PostgreSQL user", default="odoo")
        if not password:
            password = Prompt.ask("PostgreSQL password", password=True, default="")

    # Set defaults for non-interactive mode
    host = host or "localhost"
    port = port or 5432
    user = user or "odoo"
    password = password or ""

    # Get available databases if not specified
    if not database:
        console.print("\n[bold]Available databases:[/bold]")
        databases = get_databases(host, port, user, password)

        if not databases:
            console.print("[red]No databases found[/red]")
            sys.exit(1)

        table = Table()
        table.add_column("Index", style="cyan")
        table.add_column("Database", style="green")

        for i, db in enumerate(databases, 1):
            table.add_row(str(i), db)

        console.print(table)

        if non_interactive:
            console.print("[red]Database must be specified in non-interactive mode[/red]")
            sys.exit(1)

        choice = Prompt.ask("\nSelect database index", choices=[str(i) for i in range(1, len(databases) + 1)])
        database = databases[int(choice) - 1]

    # Autodetect filestore path - query database first (like Odoo web interface does)
    # First, try to get filestore path directly from database
    filestore_path = get_filestore_from_database(host, port, user, password, database)

    if not filestore_path:
        # Fallback to filesystem detection
        filestore_path = detect_filestore_path(database)

    if not filestore_path:
        # Last resort: use default path
        filestore_path = f"/opt/odoo/data/filestore/{database}"
        console.print(f"[yellow]⚠ Could not detect filestore, using default: {filestore_path}[/yellow]")

    # Get output path
    if not output_path and not non_interactive:
        output_path = Prompt.ask("Output directory", default="./backups")
    elif not output_path:
        output_path = "./backups"

    # Ask about cleanup in interactive mode
    if not non_interactive and cleanup_days is None:
        if Confirm.ask("\n[bold]Would you like to automatically delete old backups?[/bold]", default=True):
            cleanup_days = int(Prompt.ask("Keep backups for how many days?", default="7"))

    console.print(f"\n[bold]Backup Configuration:[/bold]")
    console.print(f"Database: {database}")
    console.print(f"Filestore: {filestore_path}")
    console.print(f"Output: {output_path}")
    if cleanup_days:
        console.print(f"Retention: {cleanup_days} days")

    # If only setting up cron, skip the backup and go straight to cron setup
    if cron and not non_interactive:
        console.print("\n[bold]Setting up cron job...[/bold]")
        command_parts = [
            f"--host {host}",
            f"--port {port}",
            f"--user {user}",
            f"--database {database}",
            f"--output-path '{output_path}'",
            "--non-interactive"
        ]
        if password:
            command_parts.append(f"--password '{password}'")
        if cleanup_days:
            command_parts.append(f"--cleanup-days {cleanup_days}")

        # Use uvx obx for cron command (filestore is autodetected)
        full_command = f"uvx obx {' '.join(command_parts)}"
        setup_cron_job(full_command)
        return

    if not non_interactive and not Confirm.ask("\nProceed with backup?"):
        console.print("[yellow]Backup cancelled[/yellow]")
        sys.exit(0)

    # Create backup
    with tempfile.TemporaryDirectory() as temp_dir:
        console.print("\n[bold]Creating backup...[/bold]")

        # Database backup
        db_backup_file = os.path.join(temp_dir, f"{database}.sql")
        console.print("📊 Backing up database...")
        if not create_db_backup(host, port, user, password, database, db_backup_file):
            sys.exit(1)

        # Filestore backup
        filestore_backup_file = None
        if filestore_path and os.path.exists(filestore_path):
            console.print("📁 Backing up filestore...")
            filestore_backup_file = create_filestore_backup(filestore_path, temp_dir)

        # Create final backup
        console.print("🗜️  Creating final backup...")
        backup_file = create_full_backup(db_backup_file, filestore_backup_file, output_path, database)

        console.print(f"\n[bold green]✅ Backup completed successfully![/bold green]")
        console.print(f"[green]Backup saved to: {backup_file}[/green]")

        # File size
        backup_size = os.path.getsize(backup_file)
        size_mb = backup_size / (1024 * 1024)
        console.print(f"[blue]Backup size: {size_mb:.2f} MB[/blue]")

    # Cleanup old backups if requested
    if cleanup_days:
        console.print(f"\n[bold]🧹 Cleaning up backups older than {cleanup_days} days...[/bold]")
        cleanup_old_backups(output_path, cleanup_days)

    # Ask about cron setup in interactive mode (after backup)
    if not non_interactive:
        console.print("\n[bold]📅 Automated Backups[/bold]")
        if Confirm.ask("Would you like to set up automatic daily backups with cron?", default=False):
            console.print("\n[bold]Setting up cron job...[/bold]")
            command_parts = [
                f"--host {host}",
                f"--port {port}",
                f"--user {user}",
                f"--database {database}",
                f"--output-path '{output_path}'",
                "--non-interactive"
            ]
            if password:
                command_parts.append(f"--password '{password}'")
            if cleanup_days:
                command_parts.append(f"--cleanup-days {cleanup_days}")

            # Use uvx obx for cron command (filestore is autodetected)
            full_command = f"uvx obx {' '.join(command_parts)}"
            setup_cron_job(full_command)


if __name__ == "__main__":
    main()
