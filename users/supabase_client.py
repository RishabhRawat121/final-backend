from supabase import create_client
import os

SUPABASE_URL = "https://rwocivhozcmfswyilrwy.supabase.co"  # not the PostgreSQL URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."   # anon/service role key

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
