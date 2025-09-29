import logging
from pathlib import Path
from typing import Optional, Dict, Any
import json
from pygbif import species, occurrences

from ..mcp import gis_mcp

logger = logging.getLogger(__name__)

DEFAULT_PATH = Path(__file__).resolve().parent / "ecology_data"

@gis_mcp.resource("gis://operations/ecology")
def get_ecology_operations() -> dict:
    """List available ecology operations."""
    return {"operations": ["download_species_occurrences", "get_species_info"]}

@gis_mcp.tool()
def get_species_info(scientific_name: str) -> Dict[str, Any]:
    """
    Retrieve taxonomic information for a given species name.
    Args:
        scientific_name: Scientific name of the species (e.g., "Puma concolor")
    Returns:
        Taxonomic info dict or error message.
    """
    try:
        result = species.name_backbone(name=scientific_name)
        logger.info("Retrieved species info for %s: %s", scientific_name, result)
        return {"status": "success", "species_info": result}
    except Exception as e:
        logger.exception("Failed to retrieve species info")
        return {"status": "error", "message": str(e)}

@gis_mcp.tool()
def download_species_occurrences(
    scientific_name: str,
    limit: int = 100,
    path: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Download occurrence records for a given species and save as JSON.
    Args:
        scientific_name: Scientific name of the species (e.g., "Puma concolor")
        limit: Number of occurrence records to fetch (default: 100)
        path: Custom output folder (default: ./data/ecology_data)
    Returns:
        {"status": "success", "file_path": "..."} or {"status": "error", "message": "..."}
    """
    try:
        out_dir = Path(path) if path else DEFAULT_PATH
        out_dir.mkdir(parents=True, exist_ok=True)

        # Get taxon key
        species_info = species.name_backbone(name=scientific_name)
        taxon_key = species_info.get("usageKey")
        if not taxon_key:
            msg = f"Taxon key not found for {scientific_name}"
            logger.error(msg)
            return {"status": "error", "message": msg}

        # Get occurrence data
        occ_data = occurrences.search(taxonKey=taxon_key, limit=limit)
        results = occ_data.get("results", [])

        file_name = f"{scientific_name.replace(' ', '_')}_occurrences.json"
        file_path = out_dir / file_name
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump({
                "species_info": species_info,
                "occurrence_data": results
            }, f, indent=4)

        logger.info("Saved occurrence data for %s to %s", scientific_name, file_path)
        return {"status": "success", "file_path": str(file_path)}
    except Exception as e:
        logger.exception("Failed to download species occurrences")
        return {"status": "error", "message": str(e)}
