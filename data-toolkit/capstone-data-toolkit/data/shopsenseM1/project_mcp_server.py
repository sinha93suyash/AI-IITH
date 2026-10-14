
import csv
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ShopSense MCP Server")


@mcp.tool()
def get_order_status(order_ref: str) -> dict:
    orders_path = Path("../shopsense/mock_api/orders.csv")

    with orders_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["order_ref"] == order_ref:
                return {
                    "order_ref": row["order_ref"],
                    "customer_ref": row["customer_ref"],
                    "sku": row["sku"],
                    "quantity": int(row["quantity"]),
                    "order_value_inr": float(row["order_value_inr"]),
                    "placed_at": row["placed_at"],
                    "payment_method": row["payment_method"],
                    "status": row["status"],
                    "delivery_promise_days": int(row["delivery_promise_days"]),
                    "actual_delivery_days": (
                        float(row["actual_delivery_days"])
                        if row["actual_delivery_days"]
                        else None
                    )
                }

    return {
        "order_ref": order_ref,
        "status": "not_found"
    }






@mcp.tool()
def get_shipping_status(order_ref: str) -> dict:
    shipments_path = Path("../shopsense/mock_api/shipments.csv")

    with shipments_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["order_ref"] == order_ref:
                return {
                    "tracking_id": row["tracking_id"],
                    "order_ref": row["order_ref"],
                    "carrier": row["carrier"],
                    "last_scan": row["last_scan"],
                    "last_scan_at": row["last_scan_at"],
                    "scan_location": row["scan_location"]
                }

    return {
        "order_ref": order_ref,
        "status": "not_found"
    }



@mcp.tool()
def get_refund_status(order_ref: str) -> dict:
    refunds_path = Path("../shopsense/mock_api/refunds.csv")

    with refunds_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["order_ref"] == order_ref:
                return {
                    "refund_id": row["refund_id"],
                    "order_ref": row["order_ref"],
                    "amount_inr": float(row["amount_inr"]),
                    "reason_code": row["reason_code"],
                    "status": row["status"],
                    "approved_by": row["approved_by"],
                    "requested_on": row["requested_on"]
                }

    return {
        "order_ref": order_ref,
        "status": "not_found"
    }

if __name__ == "__main__":
    mcp.run(transport="stdio")
