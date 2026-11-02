import sqlite3


def find_invoices(db_path, customer):
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, total_cents FROM invoices WHERE customer = '{customer}'")
        return cursor.fetchall()
    finally:
        conn.close()


def invoice_total(line_items):
    total = 0.0
    for item in line_items:
        total += item["price"] * item["quantity"]
    return round(total, 2)
