"""
Entity Processing Utilities for PII Detection

This module provides utilities for processing and expanding PII entity types
to ensure comprehensive detection coverage. It includes logic for automatically
expanding related entity groups when any member of the group is requested.
"""

from typing import List, Set
from loguru import logger
from .constants import GLINER_MODEL_ENTITIES


class EntityGroups:
    """
    Defines entity groups for comprehensive PII detection.
    
    Entity groups allow users to specify any member of a group and automatically
    get comprehensive detection for all related entity types.
    """
    
    # Email-related entities that should be grouped together
    EMAIL_RELATED = ["email", "email address", "gmail"]
    
    # Phone-related entities that should be grouped together  
    PHONE_RELATED = [
        "phone number", 
        "mobile phone number", 
        "landline phone number", 
        "fax number"
    ]
    
    # Credit card related entities
    CREDIT_CARD_RELATED = [
        "credit card number",
        "credit card brand", 
        "credit card expiration date",
        "cvv",
        "cvc"
    ]
    
    # Social security related entities
    SSN_RELATED = [
        "social security number",
        "social_security_number"
    ]
    
    # All entity groups mapping
    ENTITY_GROUPS = {
        "email": EMAIL_RELATED,
        "phone": PHONE_RELATED,
        "credit_card": CREDIT_CARD_RELATED,
        "ssn": SSN_RELATED
    }


def expand_entity_groups(entities_to_detect: List[str]) -> List[str]:
    """
    Automatically expand entity groups for comprehensive detection.
    
    If any entity from a related group is requested, all entities from that group 
    are included to ensure comprehensive detection coverage.
    
    Args:
        entities_to_detect: List of entity types requested by the user
        
    Returns:
        Expanded list of entity types for comprehensive detection
        
    Example:
        >>> expand_entity_groups(["email"])
        ["email", "email address", "gmail"]
        
        >>> expand_entity_groups(["phone number", "person"])
        ["phone number", "mobile phone number", "landline phone number", "fax number", "person"]
    """
    if not entities_to_detect:
        return entities_to_detect
    
    expanded_entities: Set[str] = set(entities_to_detect)
    entities_lower = [entity.lower().strip() for entity in entities_to_detect]
    
    # Check each entity group for expansion
    for group_name, group_entities in EntityGroups.ENTITY_GROUPS.items():
        group_entities_lower = [entity.lower() for entity in group_entities]
        
        # If any entity from this group is requested, include all entities from the group
        if any(entity_lower in group_entities_lower for entity_lower in entities_lower):
            logger.info(f"{group_name.title()}-related entity detected in request. "
                       f"Including all {group_name}-related entities for comprehensive detection.")
            expanded_entities.update(group_entities)
    
    return list(expanded_entities)


def validate_and_expand_entities(pii_entities: str) -> List[str]:
    """
    Parse, expand, and validate PII entity types against supported entities.
    
    This function provides a complete pipeline for processing user-provided
    entity types: parsing from comma-separated string, expanding related groups,
    and validating against supported entities.
    
    Args:
        pii_entities: Comma-separated string of PII entity types
        
    Returns:
        List of valid, expanded entity types ready for detection
        
    Example:
        >>> validate_and_expand_entities("email, person")
        ["email", "email address", "gmail", "person"]
    """
    if not pii_entities or not pii_entities.strip():
        logger.warning("No PII entities provided, using all supported entities")
        return GLINER_MODEL_ENTITIES
    
    # Parse comma-separated string
    entities_to_detect = [entity.strip() for entity in pii_entities.split(',') if entity.strip()]
    
    # Expand entity groups
    expanded_entities = expand_entity_groups(entities_to_detect)
    
    # Create case-preserving mapping for validation
    original_case_map = {entity.lower(): entity for entity in GLINER_MODEL_ENTITIES}
    
    # Validate against supported entities
    valid_entities = [
        original_case_map[entity.lower()]
        for entity in expanded_entities 
        if entity.lower() in original_case_map
    ]
    
    if not valid_entities:
        logger.warning("No valid PII entities found after expansion and validation, using all supported entities")
        return GLINER_MODEL_ENTITIES
    
    # Log the final entity list for debugging
    logger.debug(f"Final entity list for detection: {sorted(valid_entities)}")
    
    return valid_entities


def get_entity_groups_info() -> dict:
    """
    Get information about defined entity groups.
    
    Returns:
        Dictionary containing entity group information for documentation/debugging
    """
    return {
        "entity_groups": EntityGroups.ENTITY_GROUPS,
        "supported_entities": GLINER_MODEL_ENTITIES,
        "total_groups": len(EntityGroups.ENTITY_GROUPS),
        "total_supported_entities": len(GLINER_MODEL_ENTITIES)
    }