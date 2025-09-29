#!/usr/bin/env python3
"""
Integrated PostgreSQL Date Check and Transtore Migration Script + working

This script combines two functionalities:
1. Checks PostgreSQL dates against transtore paths and performs database migration
2. Automatically updates transtore directory structure with new dates

The script automatically discovers matching dates and paths, then offers to:
- Migrate PostgreSQL database data
- Update transtore file structure and content

Dependencies: pip install psycopg2-binary

Usage: script.py
Created by: Ashish
"""

import os
import sys
import shutil
import re
import psycopg2
from datetime import datetime, timedelta
from pathlib import Path
import logging
import getpass

# Configuration
MAX_RETRY_COUNT = 3  # Configurable retry count

# Global variables to store user inputs
DB_CONFIG = {}
TRANSTORE_PATH = ""
CURRENT_DATE = None

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PostgreSQLMigrator:
    def __init__(self, db_config):
        """Initialize database connection parameters from config"""
        self.host = db_config['host']
        self.database = db_config['database']
        self.username = db_config['user']
        self.password = db_config.get('password', '')
        self.port = int(db_config['port'])
        self.connection = None
        
    def connect(self) -> bool:
        """Establish connection to PostgreSQL database"""
        try:
            connect_params = {
                'host': self.host,
                'database': self.database,
                'user': self.username,
                'port': self.port
            }
            
            if self.password:
                connect_params['password'] = self.password
                
            self.connection = psycopg2.connect(**connect_params)
            print(f"✅ Successfully connected to PostgreSQL database: {self.database}")
            return True
        except Exception as e:
            print(f"❌ Error connecting to database: {e}")
            return False
    
    def check_and_cleanup_target_date(self, target_date: str) -> bool:
        """Check if data exists for target date and delete if found"""
        
        # Queries to check for existing data
        check_queries = [
            {
                "table": "trans_details",
                "query": "SELECT COUNT(*) FROM okean_sch.trans_details WHERE DATE(timestamp_start) = %(target_date)s"
            },
            {
                "table": "trans_event_details",
                "query": "SELECT COUNT(*) FROM okean_sch.trans_event_details WHERE DATE(timestamp_start) = %(target_date)s"
            },
            {
                "table": "alert_details", 
                "query": "SELECT COUNT(*) FROM okean_sch.alert_details WHERE DATE(timestamp_start) = %(target_date)s"
            },
            {
                "table": "pp_stats",
                "query": "SELECT COUNT(*) FROM okean_sch.pp_stats WHERE DATE(from_time) = %(target_date)s"
            }
        ]
        
        # Cleanup queries - order matters due to foreign key constraints
        cleanup_queries = [
            {
                "table": "alert_details",
                "query": "DELETE FROM okean_sch.alert_details WHERE DATE(timestamp_start) = %(target_date)s"
            },
            {
                "table": "trans_event_details",
                "query": "DELETE FROM okean_sch.trans_event_details WHERE DATE(timestamp_start) = %(target_date)s"
            },
            {
                "table": "trans_details",
                "query": "DELETE FROM okean_sch.trans_details WHERE DATE(timestamp_start) = %(target_date)s"
            },
            {
                "table": "pp_stats",
                "query": "DELETE FROM okean_sch.pp_stats WHERE DATE(from_time) = %(target_date)s"
            }
        ]
        
        try:
            cursor = self.connection.cursor()
            
            # First, check if any data exists for the target date
            total_records = 0
            print(f"🔍 Checking for existing data on {target_date}...")
            
            for check in check_queries:
                cursor.execute(check['query'], {'target_date': target_date})
                count = cursor.fetchone()[0]
                if count > 0:
                    print(f"   📊 {check['table']}: {count} records found")
                    total_records += count
            
            if total_records == 0:
                print(f"✅ No existing data found for {target_date}. Ready for migration.")
                return True
            
            # If data exists, ask for confirmation and delete
            print(f"⚠️  Found {total_records} total records for {target_date}")
            print(f"🗑️  Cleaning up existing data for {target_date}...")
            
            # Execute cleanup queries
            total_deleted = 0
            for cleanup in cleanup_queries:
                cursor.execute(cleanup['query'], {'target_date': target_date})
                deleted_rows = cursor.rowcount
                if deleted_rows > 0:
                    print(f"   🗑️  {cleanup['table']}: {deleted_rows} records deleted")
                    total_deleted += deleted_rows
            
            # Commit the cleanup
            self.connection.commit()
            print(f"✅ Cleanup completed! {total_deleted} total records deleted and committed.")
            
            # Verify cleanup was successful
            print(f"🔍 Verifying cleanup...")
            verification_failed = False
            for check in check_queries:
                cursor.execute(check['query'], {'target_date': target_date})
                count = cursor.fetchone()[0]
                if count > 0:
                    print(f"   ❌ {check['table']}: {count} records still remain!")
                    verification_failed = True
            
            if verification_failed:
                print(f"❌ Cleanup verification failed! Some data still exists for {target_date}")
                return False
            else:
                print(f"✅ Cleanup verification successful! Target date {target_date} is now clean.")
                return True
            
        except Exception as e:
            print(f"❌ Error during cleanup: {e}")
            if self.connection:
                self.connection.rollback()
                print("🔄 Cleanup transaction rolled back")
            return False
        
        finally:
            if cursor:
                cursor.close()
    
    def execute_migration_queries(self, old_date: str, new_date: str) -> bool:
        """Execute all migration queries with the provided dates"""
        
        # SQL queries with parameterized dates
        queries = [
            {
                "name": "trans_details",
                "query": """
                WITH base AS (
                    SELECT *,
                           row_number() OVER () AS rn
                    FROM okean_sch.trans_details
                    WHERE DATE(timestamp_start) = %(old_date)s
                    ORDER BY timestamp_start DESC
                )
                INSERT INTO okean_sch.trans_details (
                    trans_id,
                    epu_id,
                    cam_id,
                    timestamp_start,
                    timestamp_end,
                    video_id,
                    replicate_transaction
                )
                SELECT
                    regexp_replace(trans_id, '\\d{8}', to_char(%(new_date)s::date, 'YYYYMMDD')) AS trans_id,
                    epu_id,
                    cam_id,
                    %(new_date)s::date + (timestamp_start::time) AS timestamp_start,
                    %(new_date)s::date + (timestamp_end::time) AS timestamp_end,
                    video_id,
                    replicate_transaction
                FROM base;
                """
            },
            {
                "name": "trans_event_details", 
                "query": """
                WITH base AS (
                    SELECT *,
                           row_number() OVER () AS rn
                    FROM okean_sch.trans_event_details
                    WHERE DATE(timestamp_start) = %(old_date)s
                    ORDER BY timestamp_start DESC
                )
                INSERT INTO okean_sch.trans_event_details (
                    event_id,
                    event_type_seq,
                    epu_id,
                    cam_id,
                    zone_id_seq,
                    is_group_event,
                    event_type,
                    trans_id,
                    event_attr,
                    timestamp_start,
                    timestamp_end,
                    replicate_transaction,
                    analytics_type,
                    is_alert,
                    offline_attr
                )
                SELECT
                    regexp_replace(event_id, '\\d{8}', to_char(%(new_date)s::date, 'YYYYMMDD')) AS event_id,
                    event_type_seq,
                    epu_id,
                    cam_id,
                    zone_id_seq,
                    is_group_event,
                    event_type,
                    regexp_replace(trans_id, '\\d{8}', to_char(%(new_date)s::date, 'YYYYMMDD')) AS trans_id,
                    regexp_replace(
                        regexp_replace(event_attr::text, '\\d{4}-\\d{2}-\\d{2}', to_char(%(new_date)s::date, 'YYYY-MM-DD'), 'g'),
                        '\\d{8}',
                        to_char(%(new_date)s::date, 'YYYYMMDD'),
                        'g'
                    )::jsonb AS event_attr,
                    %(new_date)s::date + (timestamp_start::time) AS timestamp_start,
                    %(new_date)s::date + (timestamp_end::time) AS timestamp_end,
                    replicate_transaction,
                    analytics_type,
                    is_alert,
                    offline_attr
                FROM base;
                """
            },
            {
                "name": "alert_details",
                "query": """
                WITH base AS (
                    SELECT *,
                           row_number() OVER () AS rn
                    FROM okean_sch.alert_details
                    WHERE DATE(timestamp_start) = %(old_date)s
                    ORDER BY timestamp_start DESC
                )
                INSERT INTO okean_sch.alert_details (
                    alert_id,
                    event_id,
                    alert_type_seq,
                    alert_type,
                    alert_attr,
                    timestamp_start,
                    timestamp_end,
                    replicate_transaction,
                    analytics_type
                )
                SELECT
                    regexp_replace(alert_id, '\\d{8}', to_char(%(new_date)s::date, 'YYYYMMDD')) AS alert_id,
                    regexp_replace(event_id, '\\d{8}', to_char(%(new_date)s::date, 'YYYYMMDD')) AS event_id,
                    alert_type_seq,
                    alert_type,
                    regexp_replace(
                        regexp_replace(alert_attr::text, '\\d{4}-\\d{2}-\\d{2}', to_char(%(new_date)s::date, 'YYYY-MM-DD'), 'g'),
                        '\\d{8}',
                        to_char(%(new_date)s::date, 'YYYYMMDD'),
                        'g'
                    )::jsonb AS alert_attr,
                    %(new_date)s::date + (timestamp_start::time) AS timestamp_start,
                    %(new_date)s::date + (timestamp_end::time) AS timestamp_end,
                    replicate_transaction,
                    analytics_type
                FROM base;
                """
            },
            {
                "name": "pp_stats",
                "query": """
                WITH base AS (
                    SELECT *,
                           row_number() OVER () AS rn
                    FROM okean_sch.pp_stats
                    WHERE DATE(from_time) = %(old_date)s
                    ORDER BY from_time DESC
                )
                INSERT INTO okean_sch.pp_stats (
                    cam_id,
                    zone_id,
                    frequency,
                    from_time,
                    to_time,
                    trans_count,
                    event_count,
                    ev_stat_details,
                    alert_count,
                    al_stat_details,
                    zone_id_seq
                )
                SELECT
                    cam_id,
                    zone_id,
                    frequency,
                    %(new_date)s::date + (from_time::time) AS from_time,
                    %(new_date)s::date + (to_time::time) AS to_time,
                    trans_count,
                    event_count,
                    ev_stat_details,
                    alert_count,
                    al_stat_details,
                    zone_id_seq
                FROM base;
                """
            }
        ]
        
        try:
            cursor = self.connection.cursor()
            
            print(f"🔄 Starting data migration from {old_date} to {new_date}...")
            
            # Execute each query
            for query_info in queries:
                print(f"   🔄 Migrating {query_info['name']}...")
                
                cursor.execute(query_info['query'], {
                    'old_date': old_date,
                    'new_date': new_date
                })
                
                affected_rows = cursor.rowcount
                print(f"   ✅ {query_info['name']}: {affected_rows} rows migrated")
            
            # Commit all changes
            self.connection.commit()
            print(f"✅ All migrations completed successfully and committed!")
            return True
            
        except Exception as e:
            print(f"❌ Error executing migration queries: {e}")
            if self.connection:
                self.connection.rollback()
                print("🔄 Migration transaction rolled back")
            return False
        
        finally:
            if cursor:
                cursor.close()
    
    def close_connection(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            print("🔒 Database connection closed")

class EnhancedTranstoreDateUpdater:
    def __init__(self, base_transtore_path, current_date):
        self.base_transtore_path = Path(base_transtore_path).resolve()
        self.current_date = current_date
        
        # Extract original date from transtore path
        self.original_date = self.extract_date_from_path(str(self.base_transtore_path))
        if not self.original_date:
            raise ValueError("Could not extract date from transtore path")
        
        # Create new base path with current date
        self.new_base_transtore_path = self.create_new_base_path()
        
        # Date format conversions
        self.original_date_formats = self.get_date_formats(self.original_date)
        self.current_date_formats = self.get_date_formats(self.current_date)
        
        print(f"Original date: {self.original_date}")
        print(f"Current date: {self.current_date}")
        print(f"Original base path: {self.base_transtore_path}")
        print(f"New base path: {self.new_base_transtore_path}")
    
    def extract_date_from_path(self, path):
        """Extract date from path format like /2025/06/22/ or /2025/06/22"""
        # Try different date patterns
        patterns = [
            r'/(\d{4})/(\d{2})/(\d{2})/?$',   # /2025/06/22/ or /2025/06/22 at end
            r'/(\d{4})/(\d{2})/(\d{2})/',     # /2025/06/22/ anywhere in path
            r'(\d{4})/(\d{2})/(\d{2})'        # 2025/06/22 without leading slash
        ]
        
        for pattern in patterns:
            match = re.search(pattern, path)
            if match:
                year, month, day = match.groups()
                return f"{year}{month}{day}"
        
        print(f"Debug: Could not find date pattern in path: {path}")
        print("Expected format: /path/to/YYYY/MM/DD/ or /path/to/YYYY/MM/DD")
        return None
    
    def get_date_formats(self, date_str):
        """Convert date string to different formats used in the system"""
        if len(date_str) != 8:
            raise ValueError(f"Date must be 8 digits (YYYYMMDD), got: {date_str}")
        
        year = date_str[:4]
        month = date_str[4:6]
        day = date_str[6:8]
        
        return {
            'full': date_str,           # 20250625
            'short': date_str[2:],      # 250625
            'path': f"/{year}/{month}/{day}/",  # /2025/06/25/
            'year': year,
            'month': month,
            'day': day
        }
    
    def create_new_base_path(self):
        """Create new transtore base path with current date"""
        path_str = str(self.base_transtore_path)
        
        # Get date formats
        original_formats = self.get_date_formats(self.original_date)
        current_formats = self.get_date_formats(self.current_date)
        
        # Try different replacement patterns
        new_path = path_str
        
        # Pattern 1: /2025/06/22/ (with trailing slash)
        if original_formats['path'] in path_str:
            new_path = path_str.replace(original_formats['path'], current_formats['path'])
        # Pattern 2: /2025/06/22 (without trailing slash at the end)
        elif path_str.endswith(original_formats['path'].rstrip('/')):
            old_pattern = original_formats['path'].rstrip('/')
            new_pattern = current_formats['path'].rstrip('/')
            new_path = path_str.replace(old_pattern, new_pattern)
        # Pattern 3: Match year/month/day pattern anywhere in path
        else:
            date_pattern = f"/{original_formats['year']}/{original_formats['month']}/{original_formats['day']}"
            new_date_pattern = f"/{current_formats['year']}/{current_formats['month']}/{current_formats['day']}"
            new_path = path_str.replace(date_pattern, new_date_pattern)
        
        return Path(new_path)
    
    def find_c_folders(self):
        """Find all C-folders (C001, C002, etc.) in the base transtore path"""
        c_folders = []
        
        if not self.base_transtore_path.exists():
            raise FileNotFoundError(f"Base transtore path does not exist: {self.base_transtore_path}")
        
        # Pattern to match C-folders (C followed by digits)
        c_pattern = re.compile(r'^C\d+$')
        
        for item in self.base_transtore_path.iterdir():
            if item.is_dir() and c_pattern.match(item.name):
                c_folders.append(item.name)
        
        # Sort C-folders for consistent processing order
        c_folders.sort()
        
        if not c_folders:
            raise ValueError(f"No C-folders found in {self.base_transtore_path}")
        
        print(f"Found C-folders: {', '.join(c_folders)}")
        return c_folders
    
    def update_filename(self, filename):
        """Update date references in filename"""
        new_filename = filename
        
        # Replace full date (20250625)
        new_filename = new_filename.replace(
            self.original_date_formats['full'],
            self.current_date_formats['full']
        )
        
        # Replace short date (250625)
        new_filename = new_filename.replace(
            self.original_date_formats['short'],
            self.current_date_formats['short']
        )
        
        return new_filename
    
    def update_file_content(self, file_path):
        """Update date references inside file content"""
        try:
            # Read file content
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Replace all date formats in content
            updated_content = content
            
            # Handle specific transtore path patterns in XML files
            # Pattern 1: /mnt/d/Data1/2025/06/25/
            original_full_path = f"/mnt/d/Data1{self.original_date_formats['path']}"
            current_full_path = f"/mnt/d/Data1{self.current_date_formats['path']}"
            updated_content = updated_content.replace(original_full_path, current_full_path)
            
            # Pattern 2: /mnt/Data1/2025/06/25/ (missing 'd')
            original_no_d_path = f"/mnt/Data1{self.original_date_formats['path']}"
            current_no_d_path = f"/mnt/d/Data1{self.current_date_formats['path']}"
            updated_content = updated_content.replace(original_no_d_path, current_no_d_path)
            
            # Pattern 3: /mnt/Data1//2025/06/25/ (double slash, missing 'd')
            original_double_slash = f"/mnt/Data1/{self.original_date_formats['path']}"
            current_fixed_path = f"/mnt/d/Data1{self.current_date_formats['path']}"
            updated_content = updated_content.replace(original_double_slash, current_fixed_path)
            
            # Generic path format replacements
            updated_content = updated_content.replace(
                self.original_date_formats['path'],
                self.current_date_formats['path']
            )
            
            # Replace full date 20250625
            updated_content = updated_content.replace(
                self.original_date_formats['full'],
                self.current_date_formats['full']
            )
            
            # Replace short date 250625
            updated_content = updated_content.replace(
                self.original_date_formats['short'],
                self.current_date_formats['short']
            )
            
            # Clean up any double slashes that might have been created
            updated_content = re.sub(r'/+', '/', updated_content)
            
            # Write updated content back
            if updated_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                return True
            
        except Exception as e:
            print(f"Warning: Could not update content of {file_path}: {e}")
        
        return False
    
    def copy_and_update_c_folder(self, c_folder_name):
        """Copy and update a specific C-folder"""
        source_c_path = self.base_transtore_path / c_folder_name
        dest_c_path = self.new_base_transtore_path / c_folder_name
        
        print(f"\n--- Processing {c_folder_name} ---")
        print(f"Source: {source_c_path}")
        print(f"Destination: {dest_c_path}")
        
        # Create destination directory
        dest_c_path.mkdir(parents=True, exist_ok=True)
        
        files_processed = 0
        files_updated = 0
        
        # Walk through source C-folder
        for root, dirs, files in os.walk(source_c_path):
            root_path = Path(root)
            
            # Calculate relative path from source C-folder
            relative_path = root_path.relative_to(source_c_path)
            
            # Create corresponding directory in destination C-folder
            dest_dir = dest_c_path / relative_path
            dest_dir.mkdir(parents=True, exist_ok=True)
            
            # Process files in current directory
            for filename in files:
                source_file = root_path / filename
                
                # Update filename with new date
                new_filename = self.update_filename(filename)
                dest_file = dest_dir / new_filename
                
                # Copy file
                shutil.copy2(source_file, dest_file)
                files_processed += 1
                
                # Update file content for text-based files
                file_ext = dest_file.suffix.lower()
                text_extensions = ['.xml', '.json', '.txt', '.html', '.csv']
                
                if any(file_ext.endswith(ext) for ext in text_extensions):
                    updated = self.update_file_content(dest_file)
                    if updated:
                        files_updated += 1
                    status = "✓ updated" if updated else "✓ copied"
                else:
                    status = "✓ copied"
                
                if relative_path == Path('.'):
                    print(f"  {filename} -> {new_filename} {status}")
                else:
                    print(f"  {relative_path}/{filename} -> {relative_path}/{new_filename} {status}")
        
        print(f"--- {c_folder_name} completed: {files_processed} files processed, {files_updated} files updated ---")
        return files_processed, files_updated
    
    def copy_and_update_all_c_folders(self):
        """Main function to copy all C-folders and update all date references"""
        # Find all C-folders
        c_folders = self.find_c_folders()
        
        # Check if destination base path exists
        if self.new_base_transtore_path.exists():
            print(f"\n⚠️  Destination base path already exists: {self.new_base_transtore_path}")
            response = input("Overwrite existing transtore data? (y/N): ")
            if response.lower() != 'y':
                print("Transtore operation cancelled")
                return False
            shutil.rmtree(self.new_base_transtore_path)
        
        print(f"\nStarting to process {len(c_folders)} C-folders...")
        
        total_files_processed = 0
        total_files_updated = 0
        
        # Process each C-folder
        for c_folder in c_folders:
            files_processed, files_updated = self.copy_and_update_c_folder(c_folder)
            total_files_processed += files_processed
            total_files_updated += files_updated
        
        print(f"\n=== TRANSTORE OPERATION COMPLETED SUCCESSFULLY ===")
        print(f"Processed {len(c_folders)} C-folders: {', '.join(c_folders)}")
        print(f"Total files processed: {total_files_processed}")
        print(f"Total files updated: {total_files_updated}")
        print(f"New transtore path: {self.new_base_transtore_path}")
        return True
    
    def validate_date_format(self, date_str):
        """Validate date format YYYYMMDD"""
        if len(date_str) != 8:
            return False
        
        try:
            datetime.strptime(date_str, '%Y%m%d')
            return True
        except ValueError:
            return False

def get_user_inputs():
    """Get database details, transtore path, and current date from user"""
    global DB_CONFIG, TRANSTORE_PATH, CURRENT_DATE
    
    print("=" * 50)
    print("OKEAN CONFIGURATION SETUP")
    print("=" * 50)
    
    # Get database details
    print("\nEnter Database Configuration:")
    host = input("Enter Database Host (default: 127.0.0.1): ").strip() or "127.0.0.1"
    database = input("Enter Database Name (default: okean_db): ").strip() or "okean_db"
    user = input("Enter Database User (default: okean_dbuser): ").strip() or "okean_dbuser"
    port = input("Enter Database Port (default: 5432): ").strip() or "5432"
    
    # Ask if password is needed
    need_password = input("Does database require password? (y/n, default: n): ").strip().lower()
    
    DB_CONFIG = {
        'host': host,
        'database': database,
        'user': user,
        'port': port
    }
    
    if need_password in ['y', 'yes']:
        password = getpass.getpass("Enter Database Password: ")
        DB_CONFIG['password'] = password
    
    # Get transtore path
    print("\nEnter Transtore Configuration:")
    TRANSTORE_PATH = input("Enter Transtore Path (default: /mnt/d/Data1/): ").strip() or "/mnt/d/Data1/"
    if not TRANSTORE_PATH.endswith('/'):
        TRANSTORE_PATH += '/'
    
    # Get current date
    print("\nEnter Current Date:")
    while True:
        current_date_str = input("Enter Current Date (YYYY-MM-DD format, or press Enter for today): ").strip()
        
        if not current_date_str:
            # Use today's date if nothing entered
            CURRENT_DATE = datetime.now().date()
            break
        else:
            try:
                CURRENT_DATE = datetime.strptime(current_date_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format (e.g., 2025-09-10)")
    
    # Display configuration summary
    print("\n" + "=" * 50)
    print("CONFIGURATION SUMMARY")
    print("=" * 50)
    print(f"Database Host: {DB_CONFIG['host']}")
    print(f"Database Name: {DB_CONFIG['database']}")
    print(f"Database User: {DB_CONFIG['user']}")
    print(f"Database Port: {DB_CONFIG['port']}")
    print(f"Password Required: {'Yes' if 'password' in DB_CONFIG else 'No'}")
    print(f"Transtore Path: {TRANSTORE_PATH}")
    print(f"Current Date: {CURRENT_DATE}")
    print(f"Current Date (Compact): {CURRENT_DATE.strftime('%Y%m%d')}")
    print("=" * 50)
    
    # Confirm configuration
    confirm = input("\nIs this configuration correct? (y/n, default: y): ").strip().lower()
    if confirm in ['n', 'no']:
        print("Please restart the script to re-enter configuration.")
        exit(1)
    
    return DB_CONFIG, TRANSTORE_PATH, CURRENT_DATE

def connect_to_postgres():
    """Establish connection to PostgreSQL database"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        logger.error(f"Error connecting to PostgreSQL: {e}")
        return None

def get_latest_pg_date(conn):
    """Get the latest date from PostgreSQL database"""
    try:
        cursor = conn.cursor()
        # Get the latest date from okean_sch.trans_details table
        query = "SELECT MAX(DATE(timestamp_start)) FROM okean_sch.trans_details"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        
        if result and result[0]:
            return result[0]
        else:
            logger.warning("No date found in PostgreSQL")
            return None
    except Exception as e:
        logger.error(f"Error getting latest date from PostgreSQL: {e}")
        return None

def get_previous_pg_dates(conn, current_date, days_back=10):
    """Get previous dates from PostgreSQL in descending order"""
    try:
        cursor = conn.cursor()
        # Get distinct previous dates from okean_sch.trans_details table
        query = """
        SELECT DISTINCT DATE(timestamp_start) 
        FROM okean_sch.trans_details 
        WHERE DATE(timestamp_start) < %s 
        ORDER BY DATE(timestamp_start) DESC 
        LIMIT %s
        """
        cursor.execute(query, (current_date, days_back))
        results = cursor.fetchall()
        cursor.close()
        
        return [result[0] for result in results]
    except Exception as e:
        logger.error(f"Error getting previous dates from PostgreSQL: {e}")
        return []

def check_transtore_date(date_obj):
    """Check if the transtore path exists for the given date"""
    try:
        # Format date as YYYY/MM/DD
        date_str = date_obj.strftime("%Y/%m/%d")
        full_path = os.path.join(TRANSTORE_PATH, date_str)
        
        logger.info(f"Checking transtore path: {full_path}")
        return os.path.exists(full_path), full_path
    except Exception as e:
        logger.error(f"Error checking transtore date: {e}")
        return False, None

def run_integrated_migration(matched_pg_date, current_date):
    """
    Integrated migration function that handles both database and transtore migration
    
    Args:
        matched_pg_date: The PostgreSQL date that matched (date object)  
        current_date: The current date provided by user (date object)
    """
    logger.info("=" * 50)
    logger.info("MATCH FOUND - PostgreSQL and Transtore dates align!")
    logger.info("=" * 50)

    # Store matched values in variables
    pg_date = matched_pg_date
    user_current_date = current_date
    
    # Format date for different uses
    old_date_iso = pg_date.strftime("%Y-%m-%d")           # 2025-06-19
    new_date_iso = user_current_date.strftime("%Y-%m-%d") # 2025-09-12
    current_date_compact = user_current_date.strftime("%Y%m%d") # 20250912
    
    # Get transtore path
    _, transtore_full_path = check_transtore_date(pg_date)
    
    # Print the match information
    print(f"📅 PostgreSQL Date (Source): {pg_date} ({old_date_iso})")
    print(f"📅 Current Date (Target): {user_current_date} ({new_date_iso})")
    print(f"✅ Transtore path exists for source date: {transtore_full_path}")
    
    # Ask user what operations to perform
    print("\n" + "=" * 50)
    print("MIGRATION OPTIONS")
    print("=" * 50)
    print("This will perform both database migration AND transtore update by default.")
    print("Available operations:")
    print("1. Database migration only")
    print("2. Transtore update only")
    print("3. Both database migration AND transtore update (recommended)")
    print("4. Skip all operations")
    
    # Default to option 3 - both operations
    choice = input("\nSelect operation (1-4, default: 3 - both operations): ").strip() or "3"
    
    # Validate choice
    if choice not in ['1', '2', '3', '4']:
        print(f"Invalid choice '{choice}', defaulting to option 3 (both operations)")
        choice = '3'
    
    if choice == '4':
        print("⏭️  All operations skipped by user choice.")
        logger.info("All operations skipped - user choice")
        return
    
    # Track success of operations
    db_migration_success = False
    transtore_update_success = False
    
    # Perform database migration if requested
    if choice in ['1', '3']:
        print("\n" + "🚀 Starting database migration process..." + "\n")
        logger.info("User confirmed database migration - proceeding")
        
        # Create migrator instance
        migrator = PostgreSQLMigrator(DB_CONFIG)
        
        try:
            # Connect to database for migration
            if not migrator.connect():
                print("❌ Failed to connect to database for migration!")
                logger.error("Migration failed - database connection error")
            else:
                # Step 1: Check and cleanup target date data
                if not migrator.check_and_cleanup_target_date(new_date_iso):
                    print("❌ Pre-migration cleanup failed!")
                    logger.error("Migration failed - cleanup error")
                else:
                    # Step 2: Execute migration queries
                    if migrator.execute_migration_queries(old_date_iso, new_date_iso):
                        print("🎉 Database migration completed successfully!")
                        logger.info("Database migration completed successfully")
                        db_migration_success = True
                    else:
                        print("❌ Database migration failed!")
                        logger.error("Database migration failed during execution")
        finally:
            # Always close migration connection
            migrator.close_connection()
    
    # Perform transtore update if requested
    if choice in ['2', '3']:
        print("\n" + "🚀 Starting transtore update process..." + "\n")
        logger.info("User confirmed transtore update - proceeding")
        
        try:
            # Create transtore updater instance
            updater = EnhancedTranstoreDateUpdater(transtore_full_path, current_date_compact)
            
            # Validate current date format
            if not updater.validate_date_format(current_date_compact):
                print(f"❌ Invalid date format: {current_date_compact}. Expected YYYYMMDD")
                logger.error("Transtore update failed - invalid date format")
            else:
                # Find C-folders first to show what will be processed
                c_folders = updater.find_c_folders()
                
                print(f"\nTransstore operation details:")
                print(f"Source: {updater.base_transtore_path}")
                print(f"Target: {updater.new_base_transtore_path}")
                print(f"C-folders: {', '.join(c_folders)}")
                print(f"Date change: {updater.original_date} → {current_date_compact}")
                
                # Perform the transtore update
                if updater.copy_and_update_all_c_folders():
                    print("🎉 Transtore update completed successfully!")
                    logger.info("Transtore update completed successfully")
                    transtore_update_success = True
                else:
                    print("❌ Transtore update failed or was cancelled!")
                    logger.error("Transtore update failed")
                    
        except Exception as e:
            print(f"❌ Error during transtore update: {e}")
            logger.error(f"Transtore update failed with error: {e}")
    
    # Final summary
    print("\n" + "=" * 50)
    print("INTEGRATED MIGRATION SUMMARY")
    print("=" * 50)
    
    if choice in ['1', '3']:
        status = "✅ SUCCESS" if db_migration_success else "❌ FAILED"
        print(f"Database Migration: {status}")
    
    if choice in ['2', '3']:
        status = "✅ SUCCESS" if transtore_update_success else "❌ FAILED"
        print(f"Transtore Update: {status}")
    
    # Overall result
    if choice == '1':
        overall_success = db_migration_success
    elif choice == '2':
        overall_success = transtore_update_success
    elif choice == '3':
        overall_success = db_migration_success and transtore_update_success
    
    if overall_success:
        print("🎉 OVERALL RESULT: All requested operations completed successfully!")
    else:
        print("⚠️  OVERALL RESULT: Some operations failed. Check logs above.")
    
    print("=" * 50)
    logger.info("Integrated migration completed")

def main():
    """Main function to orchestrate the integrated migration process"""
    # Get user inputs first
    db_config, transtore_path, current_date = get_user_inputs()
    
    logger.info("Starting integrated PostgreSQL and Transtore migration script")
    logger.info(f"Using current date: {current_date}")
    
    # Step 1: Connect to PostgreSQL and get latest date
    conn = connect_to_postgres()
    if not conn:
        logger.error("Failed to connect to PostgreSQL. Exiting.")
        return
    
    try:
        # Get latest date from PostgreSQL
        pg_date = get_latest_pg_date(conn)
        if not pg_date:
            logger.error("Could not retrieve latest date from PostgreSQL")
            return
        
        logger.info(f"Latest PostgreSQL date: {pg_date}")
        
        # Step 2: Check if transtore path exists for the latest date
        transtore_exists, transtore_full_path = check_transtore_date(pg_date)
        
        if transtore_exists:
            logger.info(f"Transtore path found: {transtore_full_path}")
            logger.info("PostgreSQL date matches transtore date - running integrated migration")
            run_integrated_migration(pg_date, current_date)
            return
        
        logger.info(f"Transtore path not found for latest date: {pg_date}")
        
        # Step 3: Try previous dates (with configurable retry count)
        logger.info(f"Searching for previous dates (max {MAX_RETRY_COUNT} attempts)")
        
        previous_dates = get_previous_pg_dates(conn, pg_date)
        if not previous_dates:
            logger.warning("No previous dates found in PostgreSQL")
            return
        
        attempts = 0
        for prev_date in previous_dates:
            if attempts >= MAX_RETRY_COUNT:
                break
            
            attempts += 1
            logger.info(f"Attempt {attempts}/{MAX_RETRY_COUNT}: Checking date {prev_date}")
            
            transtore_exists, transtore_full_path = check_transtore_date(prev_date)
            
            if transtore_exists:
                logger.info(f"Match found! Transtore path: {transtore_full_path}")
                logger.info(f"PostgreSQL date {prev_date} matches transtore date - running integrated migration")
                run_integrated_migration(prev_date, current_date)
                return
            else:
                logger.info(f"No transtore path found for date: {prev_date}")
        
        # Step 4: No match found after all attempts
        logger.warning(f"No matching transtore path found after {MAX_RETRY_COUNT} attempts")
        logger.warning("No matching dates found - script completed without running migration")
    
    finally:
        conn.close()
        logger.info("PostgreSQL connection closed")

if __name__ == "__main__":
    main()
