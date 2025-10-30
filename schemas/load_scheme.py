
def load_helper(load) -> dict:
    return {
        "id": str(load["_id"]),
        "firstStopTime": load["firstStopTime"],
        "route_id": load["route_id"],
        "routeNumber": load.get("routeNumber", ""),
        "lastStopTime": load["lastStopTime"],
        "landFillTimeIn": load["landFillTimeIn"],
        "landFillTimeOut": load["landFillTimeOut"],
        "grossWeight": load["grossWeight"],
        "tareWeight": load["tareWeight"],
        "tons": load["tons"],
        "landFill_id": load["landFill_id"],
        "landfillName": load.get("landfillName", ""),
        "material_id": load["material_id"],
        "materialName": load.get("materialName", ""),
        "ticketNumber": load["ticketNumber"],
        "note": load["note"],
        "images": load.get("images", [])
    }   