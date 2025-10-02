"""
Strict GLiNER-based PII Detection and Anonymization Service

This module provides strict PII detection and anonymization capabilities using GLiNER
and Presidio models. It offers a stable API for both detection-only and full anonymization modes.

API Contract:
    - get_anonymize_prompt_strict_gliner() supports 'detection_only: bool = False' parameter
    - This parameter is guaranteed stable in zt-guardrails-lib v0.1.3+
    - Backward compatibility is maintained for existing callers

Supported Operations:
    - PII Detection: Identify personally identifiable information in text
    - PII Anonymization: Replace detected PII with generic placeholders
    - File Processing: Handle uploaded files (PDF, DOCX, CSV, TXT)
    - Safeguard Checks: Validate against prohibited keywords
"""

import traceback
from typing import Dict, List, Optional
from zt_guardrails_lib.tools.pii_detection.services.detect_pii_gliner import extract_pii_elements_gliner_only, create_pii_array_with_custom_keywords, get_fict_pii
from zt_guardrails_lib.tools.pii_detection.utils.constants import GLINER_MODEL_ENTITIES, GLINER_MODEL_THRESHOLD, PDF_DOCX_FILE, CSV_FILE, TXT_FILE, ANONYMIZED_FILE_PATH
from zt_guardrails_lib.tools.pii_detection.utils.entity_processing import validate_and_expand_entities
from loguru import logger
from fastapi import UploadFile
import re
from datetime import datetime
import os

# API Version and Compatibility Information
__version__ = "0.1.3"
__api_stable__ = True
DETECTION_ONLY_SUPPORTED = True  # Explicitly indicate support for detection_only parameter

# Try to import optional dependencies
try:
    import fitz  # PyMuPDF for PDF processing
except ImportError:
    fitz = None

try:
    import pandas as pd
except ImportError:
    pd = None

try:
    import aiofiles
except ImportError:
    aiofiles = None

class AnonymizedPromptResponse:
    """Response structure for anonymized prompts."""
    def __init__(self):
        self.anonymized_prompt = ""
        self.highlighted_original_prompt = ""
        self.highlighted_anonymized_prompt = ""
        self.pii_list = []
        self.pii_entities = []
        self.safe_guard_error_message = ""
        self.file_location = ""
        self.file_pii_array = []

def check_keywords_in_prompt_case_insensitive(prompt: str, comma_separated_keywords: str, preserve_keywords: str = "") -> list:
    """
    Checks if specified keywords are present in the given prompt (case-insensitive).
    """
    try:
        keywords = (
            [word.strip().lower() for word in comma_separated_keywords.split(",")]
            if comma_separated_keywords
            else []
        )
        preserve_keywords_list = (
            [word.strip().lower() for word in preserve_keywords.split(",")]
            if preserve_keywords
            else []
        )
        
        # Convert the prompt to lowercase for case-insensitive matching
        prompt_lower = prompt.lower()

        # Check for presence of each keyword in the prompt
        custom_keyword_found_in_prompt = [
            word for word in keywords if word in prompt_lower and word not in preserve_keywords_list
        ]

        logger.info(
            f"Custom keywords found : {custom_keyword_found_in_prompt} in the prompt, excluding preserved keywords: {preserve_keywords_list}."
        )

        return custom_keyword_found_in_prompt

    except Exception as e:
        logger.error(f"Error checking keywords in prompt: {e}")
        return []

async def anonymize_custom_keyword_with_strict_gliner(
    prompt: str, anonymize_keywords: str, pii_entities, preserve_keywords: str = ""
) -> list:
    """
    Anonymizes custom keywords using strict GLiNER method.
    """
    try:
        custom_keyword_anonymize_result: list = list()
        anonymize_keywords_in_prompt = check_keywords_in_prompt_case_insensitive(
            prompt, anonymize_keywords, preserve_keywords=preserve_keywords
        )

        if anonymize_keywords_in_prompt:
            custom_keyword_anonymize_result = create_pii_array_with_custom_keywords(anonymize_keywords, prompt, pii_entities=pii_entities)

        logger.info(f"Custom keyword PII detection completed for: {anonymize_keywords_in_prompt}")
        return custom_keyword_anonymize_result

    except Exception as e:
        logger.error(f"Error in anonymize_custom_keyword_with_strict_gliner: {e}")
        return []

def check_safeguard_keyword(prompt: str, keyword_safeguard: str) -> list:
    """
    Checks if any safeguard keywords are present in the prompt.
    """
    return (
        [
            keyword
            for keyword in keyword_safeguard.split(",")
            if keyword.strip().lower() in prompt.lower()
        ]
        if keyword_safeguard
        else []
    )

def extract_text_from_file(uploaded_file: UploadFile) -> str:
    """
    Extracts text from a PDF, DOCX, CSV, XLS, XML, or TXT file uploaded via FastAPI UploadFile.
    """
    file_text: str = str()

    try:
        # Identify file type based on content type or file extension
        file_extension = uploaded_file.filename.split(".")[-1].lower()
        logger.info(f"Uploaded file: {file_extension}")

        # Handle PDF/DOCX files
        if file_extension in PDF_DOCX_FILE:
            if fitz is None:
                raise ImportError("PyMuPDF (fitz) is required for PDF/DOCX processing but not installed")
            document = fitz.open(
                stream=uploaded_file.file.read(), filetype=file_extension
            )
            for page in document:
                file_text += page.get_text()
            document.close()

        # Handle CSV files
        elif file_extension == CSV_FILE:
            if pd is None:
                raise ImportError("pandas is required for CSV processing but not installed")
            df = pd.read_csv(uploaded_file.file)
            file_text = df.to_string()

        # Handle TXT files
        elif file_extension in TXT_FILE:
            file_text = uploaded_file.file.read().decode("utf-8")

        else:
            logger.info(f"File extension not supported: {file_extension}")
            raise ValueError(f"Unsupported file format: {file_extension}")

        logger.info(
            f"Extracted text from {uploaded_file.filename} file: {len(file_text)}"
        )
        return file_text

    except Exception as e:
        logger.error(
            f"Error occurred while extracting text from {uploaded_file.filename}: {str(e)}"
        )
        raise e

async def save_anonymized_content_to_file(anonymized_content: str) -> str:
    """
    Saves anonymized content to a specified directory, generating a unique file name with a timestamp.
    """
    try:
        # Generate a unique file name with a timestamp
        cur_timestamp = datetime.now()
        file_name = f"file_{cur_timestamp.strftime('%y%m%d%H%M%S')}.txt"
        file_location = os.path.join(ANONYMIZED_FILE_PATH, file_name)

        logger.info(f"Saving anonymized content to {file_location}")

        parent_directory = os.path.dirname(file_location)
        if parent_directory and not os.path.exists(parent_directory):
            os.makedirs(parent_directory, exist_ok=True)

        # Write the anonymized content to the file asynchronously
        if aiofiles is None:
            # Fallback to synchronous file write if aiofiles not available
            with open(file_location, "w", encoding="utf-8") as file_object:
                file_object.write(anonymized_content)
        else:
            async with aiofiles.open(file_location, "w", encoding="utf-8") as file_object:
                await file_object.write(anonymized_content)

        logger.info(f"Anonymized content successfully saved at {file_location}")

        return file_location

    except Exception as e:
        logger.error(
            f"Failed to save anonymized content to {ANONYMIZED_FILE_PATH}. Error: {str(e)}"
        )
        raise e

async def get_pii_from_user_prompt_strict_gliner(
    prompt: str, anonymize_keywords: str, pii_entities: str, preserve_keywords: str = ""
) -> dict:
    """
    Processes the input prompt using strict GLiNER and anonymizes the content.
    """
    try:
        logger.info("Starting strict anonymization process for the prompt.")

        # Use strict PII detection
        detected_pii_in_prompt = strict_pii_detection(prompt, pii_entities, preserve_keywords=preserve_keywords)

        detected_custom_pii_prompt = await anonymize_custom_keyword_with_strict_gliner(
                prompt, 
                anonymize_keywords,
                pii_entities=pii_entities,
                preserve_keywords=preserve_keywords,
                )
        
        logger.info(
            "Strict anonymization completed successfully for custom keyword and pii in prompt."
        )

        return {
            "detected_pii_in_prompt": detected_pii_in_prompt,
            "detected_custom_pii_prompt": detected_custom_pii_prompt,
        }

    except Exception as e:
        logger.error(f"Error in get_pii_from_user_prompt_strict_gliner: {e}")
        raise e

async def get_pii_from_file_content_strict_gliner(
    file_content: str, anonymize_keywords: str, pii_entities, preserve_keywords: str = ""
) -> dict:
    """
    Processes the input file content using strict GLiNER and anonymizes the content.
    """
    try:
        if not file_content:
            raise ValueError("File content is empty or invalid.")

        logger.info("Starting strict anonymization process for file content.")

        # Use strict PII detection for file content
        detected_pii_in_file = strict_pii_detection(file_content, pii_entities, preserve_keywords=preserve_keywords)

        detected_custom_pii_file = await anonymize_custom_keyword_with_strict_gliner(
            file_content,
            anonymize_keywords,
            pii_entities=pii_entities,
            preserve_keywords=preserve_keywords,
        )

        logger.info("Strict anonymization completed successfully for file content.")

        return {
            "detected_pii_in_file": detected_pii_in_file,
            "detected_custom_pii_file": detected_custom_pii_file,
        }

    except Exception as e:
        logger.error(f"Error in get_pii_from_file_content_strict_gliner: {e}")
        raise e

def detect_critical_patterns(text: str, requested_entities: str) -> list:
    """
    Pattern-based fallback detection for critical PII entities that GLiNER might miss.
    Uses regex patterns to catch common PII formats.
    """
    pattern_results = []
    
    # Only run patterns for requested entity types
    requested_lower = requested_entities.lower()
    
    # Credit card pattern (16 digits with spaces or dashes)
    if any(cc_term in requested_lower for cc_term in ['credit card', 'card number']):
        cc_pattern = r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b'
        for match in re.finditer(cc_pattern, text):
            pattern_results.append([match.group().strip(), '<CREDIT_CARD>'])
    
    # SSN pattern (XXX-XX-XXXX)
    if any(ssn_term in requested_lower for ssn_term in ['social security', 'ssn']):
        ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
        for match in re.finditer(ssn_pattern, text):
            pattern_results.append([match.group().strip(), '<US_SSN>'])
    
    # Email pattern 
    if 'email' in requested_lower:
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        for match in re.finditer(email_pattern, text):
            pattern_results.append([match.group().strip(), '<EMAIL_ADDRESS>'])
    
    # Phone pattern (various formats)
    if 'phone' in requested_lower:
        phone_pattern = r'[+]?\d{1,3}[-\s]?\(?\d{3,4}\)?[-\s]?\d{3,4}[-\s]?\d{3,5}'
        for match in re.finditer(phone_pattern, text):
            phone_text = match.group().strip()
            # Only consider as phone if it has reasonable length and format
            if len(phone_text.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')) >= 10:
                pattern_results.append([phone_text, '<PHONE_NUMBER>'])
    
    return pattern_results


def merge_detection_results(gliner_results: list, pattern_results: list) -> list:
    """
    Merge GLiNER and pattern-based detection results, avoiding duplicates.
    Pattern results take priority for critical entities.
    """
    merged = []
    pattern_texts = {item[0].lower().strip() for item in pattern_results}
    
    # Add pattern results first (higher priority)
    merged.extend(pattern_results)
    
    # Add GLiNER results that don't conflict with pattern results
    for item in gliner_results:
        if isinstance(item, list) and len(item) >= 2:
            text = item[0].lower().strip()
            # Avoid adding duplicates or partial matches
            if not any(pattern_text in text or text in pattern_text for pattern_text in pattern_texts):
                merged.append(item)
        else:
            merged.append(item)
    
    return merged


def filter_pii_labels(pii_results: list) -> list:
    """
    Filter out common PII labels that are not actual sensitive data.
    Removes labels like 'CVV', 'IBAN', 'DOB', 'SSN' etc. that are descriptive text.
    """
    common_labels = {
        'cvv', 'cvc', 'iban', 'dob', 'ssn', 'account', 'card', 'exp', 'expiry',
        'passport', 'license', 'number', 'id', 'pin', 'code', 'username', 'user',
        'email', 'phone', 'mobile', 'address', 'name', 'age', 'gender', 'date',
        'birth', 'social', 'security', 'credit', 'debit', 'visa', 'mastercard',
        'amex', 'discover', 'txn', 'transaction', 'ref', 'reference', 'brand',
        'twitter', 'website', 'diagnosis', 'pwd', 'password', 'gmail', 'yahoo',
        'hotmail', 'outlook', 'instagram', 'facebook', 'linkedin', 'type',
        'medication', 'insurance', 'plate', 'vin', 'flight', 'reservation',
        'booking', 'ticket', 'passport', 'national', 'driver', 'health'
    }
    
    filtered_results = []
    for item in pii_results:
        if isinstance(item, list) and len(item) >= 2:
            text = item[0].lower().strip()
            
            # Filter out single words that are common labels
            if len(text.split()) == 1 and text in common_labels:
                continue
                
            # Filter out very short generic terms
            if len(text) <= 3 and text.isalpha() and text in common_labels:
                continue
                
            # Filter out descriptive words that appear in common contexts
            if text in ['brand', 'twitter', 'website', 'diagnosis', 'pwd', 'gmail', 'type']:
                continue
                
            # Keep items that look like actual data patterns
            # Credit card patterns (has digits and spaces/dashes)
            if re.search(r'\d{4}[\s-]\d{4}[\s-]\d{4}[\s-]\d{4}', text):
                # Force correct classification for credit cards
                item[1] = '<CREDIT_CARD>'
                filtered_results.append(item)
                continue
                
            # SSN patterns (XXX-XX-XXXX)
            if re.search(r'\d{3}-\d{2}-\d{4}', text):
                # Force correct classification for SSN
                item[1] = '<US_SSN>'
                filtered_results.append(item)
                continue
                
            # CVV patterns (3-4 digits only)
            if re.match(r'^\d{3,4}$', text) and len(text) <= 4:
                # Force correct classification for CVV
                item[1] = '<CVV>'
                filtered_results.append(item)
                continue
                
            # Phone patterns (contains country code or formatting)
            if re.search(r'[+]?\d{1,3}[-\s]?\(?\d{3,4}\)?[-\s]?\d{3,4}[-\s]?\d{3,5}', text):
                # Force correct classification for phone
                item[1] = '<PHONE_NUMBER>'
                filtered_results.append(item)
                continue
                
            # Don't filter actual data that doesn't match label patterns
            filtered_results.append(item)
        else:
            filtered_results.append(item)
    
    return filtered_results


def strict_pii_detection(text: str, pii_entities: str = None, preserve_keywords: str = "", top_n: int = None):
    """
    Performs strict PII detection using GLiNER with custom filtering logic.
    Excludes 'person' entities from GLiNER but includes them from Presidio.
    Applies plausibility checks for locations, organizations, and persons.
    
    Args:
        text: The input text to analyze
        pii_entities: Comma-separated string of PII entity types to detect (optional)
        preserve_keywords: Keywords that should not be considered as PII
        top_n: Maximum number of entities to return (optional)
        
    Returns:
        List of filtered PII entities in format [text, <LABEL>]
    """
    import re
    
    # Use provided entities or default to all
    if pii_entities:
        entities = pii_entities
    else:
        entities = ','.join([e for e in GLINER_MODEL_ENTITIES])
    
    result = extract_pii_elements_gliner_only(
        text=text,
        pii_entities=entities,
        preserve_keywords=preserve_keywords,
        top_n=top_n,
        threshold=0.5, #GLINER_MODEL_THRESHOLD,  # Use optimal threshold (0.2) for better detection
        exclude_entities=['person'],  # Don't exclude person entities - let user control what they want
        include_presidio=True
    )

    def is_plausible_address(text):
        # Match addresses with street number, street name, and city/country
        address_patterns = [
            r"\d+\s+\w+\s+(Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|Square|Sq|Place|Pl|Terrace|Ter|Way|Park|Pkwy|Circle|Cir)",
            r"\d+\s+\w+\s+\w+", # e.g., 221B Baker Street
            r"\d+\s+\w+", # e.g., 1600 Pennsylvania
        ]
        for pat in address_patterns:
            if re.search(pat, text, re.IGNORECASE):
                return True
        # Also allow if contains a comma and at least 2 words (e.g., "London, UK")
        if "," in text and len(text.split()) > 2:
            return True
        return False

    def is_plausible_org(text):
        # Common organization suffixes and keywords
        org_keywords = [
            "inc", "ltd", "llc", "company", "corporation", "corp", "bank", "institute", "foundation", "group", "partners", "associates", "systems", "solutions", "industries", "plc", "gmbh", "s.a.", "s.r.l.", "co.", "limited", "trust", "board", "enterprise", "holdings", "ventures", "labs", "centre", "consortium", "ngo", "nonprofit"
        ]
        # Exclude generic government/location terms and common non-orgs
        generic_orgs = [
            "national parliament", "supreme court", "union buildings", "parliament", "court", "government", "city", "state", "province", "district", "department", "ministry", "office", "building", "center", "committee", "council", "school", "hospital", "clinic", "academy", "university", "college", "agency", "authority", "club", "society", "league", "alliance", "press", "media", "network", "studio", "federation", "union", "association", "chamber"
        ]
        # Remove any keyword from org_keywords that is also in generic_orgs
        org_keywords = [k for k in org_keywords if k not in generic_orgs]
        text_lower = text.lower().strip()
        # Exclude country names, continents, regions, and common non-org phrases
        country_names = [
            "south africa", "united states", "usa", "canada", "india", "china", "russia", "brazil", "germany", "france", "italy", "spain", "uk", "united kingdom", "australia", "japan", "mexico", "argentina", "egypt", "nigeria", "kenya", "sweden", "norway", "denmark", "finland", "switzerland", "netherlands", "belgium", "poland", "turkey", "saudi arabia", "uae", "israel", "iran", "pakistan", "bangladesh", "indonesia", "thailand", "vietnam", "philippines", "malaysia", "singapore", "south korea", "north korea", "new zealand", "ireland", "scotland", "wales", "portugal", "greece", "hungary", "czech republic", "slovakia", "austria", "romania", "bulgaria", "croatia", "serbia", "slovenia", "estonia", "latvia", "lithuania", "ukraine", "belarus", "moldova", "georgia", "armenia", "azerbaijan", "kazakhstan", "uzbekistan", "turkmenistan", "kyrgyzstan", "tajikistan", "mongolia", "afghanistan", "iraq", "syria", "lebanon", "jordan", "kuwait", "qatar", "oman", "yemen", "bahrain", "morocco", "algeria", "tunisia", "libya", "sudan", "ethiopia", "somalia", "tanzania", "uganda", "zambia", "zimbabwe", "botswana", "namibia", "angola", "mozambique", "madagascar", "cameroon", "ghana", "senegal", "mali", "burkina faso", "niger", "chad", "benin", "ivory coast", "guinea", "sierra leone", "liberia", "gabon", "congo", "democratic republic of the congo", "central african republic", "equatorial guinea", "cape verde", "mauritius", "seychelles", "comoros", "djibouti", "eritrea", "south sudan", "lesotho", "eswatini", "palestine", "vatican", "monaco", "liechtenstein", "andorra", "san marino", "luxembourg", "iceland", "greenland", "fiji", "papua new guinea", "solomon islands", "vanuatu", "samoa", "tonga", "kiribati", "tuvalu", "nauru", "palau", "micronesia", "marshall islands", "bahamas", "barbados", "antigua", "dominica", "grenada", "saint kitts", "saint lucia", "saint vincent", "trinidad", "jamaica", "haiti", "cuba", "dominican republic", "puerto rico", "guatemala", "honduras", "el salvador", "nicaragua", "costa rica", "panama", "colombia", "venezuela", "ecuador", "peru", "chile", "bolivia", "paraguay", "uruguay"
        ]
        continents = ["africa", "asia", "europe", "north america", "south america", "antarctica", "australia", "oceania"]
        regions = ["middle east", "far east", "eastern europe", "western europe", "northern europe", "southern europe", "central america", "latin america", "caribbean", "scandinavia", "balkans", "maghreb", "sub-saharan africa", "southeast asia", "pacific islands"]
        non_org_phrases = ["world", "earth", "globe", "continent", "region", "zone", "area", "territory", "district", "province", "state", "city", "village", "town", "municipality", "county", "suburb", "neighborhood", "metropolis", "capital", "country", "nation", "republic", "kingdom", "empire", "federation", "union", "community", "society", "club", "league", "association", "chamber", "council", "committee", "board", "office", "department", "ministry", "agency", "authority", "press", "media", "network", "studio", "school", "hospital", "clinic", "academy", "university", "college", "building", "center", "centre"]
        for word in country_names + continents + regions + non_org_phrases:
            if text_lower == word:
                return False
        # Include if ends with a business domain extension
        business_domains = [".ai", ".com", ".org", ".net", ".io", ".co", ".tech", ".biz", ".info", ".app", ".cloud", ".dev", ".inc", ".solutions", ".systems", ".agency", ".company", ".consulting", ".digital", ".finance", ".group", ".holdings", ".industries", ".international", ".media", ".network", ".partners", ".software", ".studio", ".ventures"]
        for ext in business_domains:
            if text_lower.endswith(ext):
                return True
        # Exclude generic orgs (exact or partial match)
        for g in generic_orgs:
            if g in text_lower or text_lower == g:
                return False
        # Include if matches org keywords (suffix or word in name)
        for k in org_keywords:
            if re.search(rf"\b{k}\b", text_lower):
                return True
        # Include if matches common company formats (e.g., 'X & Y Ltd', 'ABC Inc.', 'XYZ LLC')
        if re.search(r"[A-Z][A-Za-z0-9&\-\. ]+ (Inc|Ltd|LLC|PLC|GmbH|S\.A\.|S\.R\.L\.|Co\.|Corporation|Company|Corp|Bank|Trust|Holdings|Ventures|Labs|Foundation|Group|Partners|Associates|Systems|Solutions|Industries|Consortium|NGO|Nonprofit)$", text):
            return True
        # Include if contains at least two capitalized words (likely a proper name)
        if len([w for w in text.split() if w and w[0].isupper()]) >= 2:
            # Exclude if all words are capitalized (likely an acronym or not a real org)
            if not all(w.isupper() for w in text.split()):
                return True
        # Allow plausible single-word organizations (not in exclusion lists, not generic)
        if len(text.split()) == 1 and len(text) > 2:
            # Exclude if word is in exclusion lists or generic terms
            if text_lower not in country_names and text_lower not in continents and text_lower not in regions and text_lower not in non_org_phrases:
                # Exclude if word is all lowercase (likely not a proper noun)
                if not text.islower():
                    return True
        # Exclude if text is very short or generic
        if len(text.split()) < 2 or len(text) < 5:
            return False
        # Exclude if text contains only generic terms or locations
        if re.search(r"\b(city|state|province|district|building|center|committee|council|school|hospital|clinic|academy|university|college|agency|authority|club|society|league|alliance|press|media|network|studio|federation|union|association|chamber)\b", text_lower):
            return False
        return False

    def is_generic_person(name):
        generic_names = {
            "someone", "user", "person", "individual", "people", "somebody", "anyone", "everybody", "nobody", "guest", "member", "participant", "personne", "persona", "some one", "test", "demo", "sample", "anonymous", "unknown", "client", "customer", "visitor", "viewer", "reader", "author", "writer", "admin", "administrator", "operator", "agent", "actor", "subject", "object", "entity", "thing", "guy", "gal", "man", "woman", "boy", "girl"
        }
        return name.strip().lower() in generic_names

    def is_sensitive_entity(entity):
        # entity: [text, <LABEL>]
        label = entity[1].strip("<>").replace("_", " ").lower()
        if label == "location":
            return is_plausible_address(entity[0])
        if label == "org":
            return is_plausible_org(entity[0])
        if label == "person":
            return not is_generic_person(entity[0])
        return True

    # Apply label filtering first, then sensitivity filtering
    label_filtered_result = filter_pii_labels(result)
    
    # Add pattern-based fallback detection for critical entities that GLiNER might miss
    pattern_detected = detect_critical_patterns(text, entities)
    
    # Merge pattern-detected with GLiNER results, avoiding duplicates
    combined_result = merge_detection_results(label_filtered_result, pattern_detected)
    
    filtered_result = [ent for ent in combined_result if is_sensitive_entity(ent)]
    return filtered_result

def process_pii(pii_list, detection_only=False):
    """
    Converts PII list format [text, <LABEL>] to anonymized format.
    If detection_only=True, returns generic tags like <CREDIT_CARD>, <PERSON>.
    If detection_only=False, generates fake data using Faker.
    """
    result = []
    for item in pii_list:
        if len(item) < 2:
            continue  # Skip malformed entries
        original = item[0]
        pii_type = item[1].strip('<>').upper()  # Remove angle brackets and standardize
        
        if detection_only:
            # Return generic tag for detection-only mode
            anonymized = f"<{pii_type}>"
        else:
            # Generate fake data for full anonymization mode
            anonymized = get_fict_pii(pii_type)
        
        result.append({
            "Anonymized": anonymized,
            "Original": original,
            "PII_Type": pii_type
        })
    return result

def anonymize_prompt_and_highlight(prompt: str, pii_data: List[Dict]) -> dict:
    """
    Anonymizes the prompt and creates highlighted versions.
    """
    try:
        # Initialize list to store unique values by PII type and entities
        pii_list: list = list()
        pii_entities: list = list()

        # Initialize prompt variables
        anonymized_prompt = prompt
        highlighted_original_prompt = prompt
        highlighted_anonymized_prompt = prompt

        for item in pii_data:
            if isinstance(item, list) and len(item) >= 2:
                # Handle [text, <LABEL>] format from strict detection
                original = item[0]
                pii_type = item[1].strip("<>")
                anonymized = get_fict_pii(pii_type)
            elif isinstance(item, dict):
                # Handle dict format if needed
                anonymized = item.get("Anonymized", "")
                original = item.get("Original", "")
                pii_type = item.get("PII_Type", "")
            else:
                continue

            # Appending to pii_list
            pii_list.append([original, anonymized])

            # Appending to pii_entities
            pii_entities.append([original, pii_type])

            # Use regex to replace original values with anonymized values (matching word boundaries)
            anonymized_prompt = re.sub(
                r"\b" + re.escape(original) + r"\b", anonymized, anonymized_prompt
            )

            # Wrap original values in <pii_text> tags for tagged prompt
            highlighted_original_prompt = re.sub(
                r"\b" + re.escape(original) + r"\b",
                f"<pii_text>{original}</pii_text>",
                highlighted_original_prompt,
            )

            # Wrap original values in <pii_text> tags for highlighted prompt
            highlighted_anonymized_prompt = re.sub(
                r"\b" + re.escape(original) + r"\b",
                f"<pii_text>{anonymized}</pii_text>",
                highlighted_anonymized_prompt,
            )

        logger.info(
            f"Processed PII data successfully: {len(pii_list)} PII items found and anonymized prompt with wrapping tag"
        )

        final_anonymized_result = {
            "anonymized_prompt": anonymized_prompt,
            "highlighted_original_prompt": highlighted_original_prompt,
            "highlighted_anonymized_prompt": highlighted_anonymized_prompt,
            "pii_list": pii_list,
            "pii_entities": pii_entities,
        }

        return final_anonymized_result

    except Exception as e:
        logger.error(f"Error in anonymize_prompt_and_highlight: {e}")
        raise e


async def get_anonymize_prompt_strict_gliner(
    form_data, 
    detection_only: bool = False
) -> AnonymizedPromptResponse:
    """
    Main service function for strict GLiNER-based PII detection and anonymization.
    Handles both prompt and uploaded file processing with safeguard checks.
    
    This function provides a stable API contract for PII processing with two modes:
    1. Full anonymization mode (default): Detects and anonymizes PII
    2. Detection-only mode: Detects PII but returns original text without anonymization
    
    Args:
        form_data: Form data containing prompt, entities, keywords, etc.
                  Expected to have attributes: prompt, pii_entities, anonymize_keywords,
                  deanonymize_keywords, keyword_safeguard, uploaded_file
        detection_only (bool, optional): 
            - False (default): Detect and anonymize PII in the text
            - True: Only detect PII without performing anonymization
            
    Returns:
        AnonymizedPromptResponse: Response object containing:
            - anonymized_prompt: The processed text (anonymized or original based on detection_only)
            - highlighted_original_prompt: Original text with PII highlighted
            - highlighted_anonymized_prompt: Anonymized text with replacements highlighted
            - pii_list: List of detected PII entities with their types and positions
            - pii_entities: List of PII entity types that were searched for
            - safe_guard_error_message: Any safeguard-related error messages
            - file_location: Path to processed file (if file was uploaded)
            - file_pii_array: Array of PII detected in uploaded file
            
    Raises:
        Exception: If processing fails, details logged via logger
        
    API Stability:
        This function signature is stable and the detection_only parameter
        is guaranteed to be supported in zt-guardrails-lib v0.1.3+
        
    Example:
        ```python
        # For full anonymization
        result = await get_anonymize_prompt_strict_gliner(form_data)
        
        # For detection only
        result = await get_anonymize_prompt_strict_gliner(form_data, detection_only=True)
        ```
    """
    # Initialize dictionary to store PII detection results from the uploaded file
    pii_result_of_file: dict = dict()

    # Variable to store file location of the anonymized content
    file_location: str = str()

    try:
        # Extract values from form data
        prompt = form_data.prompt
        pii_entities = form_data.pii_entities
        anonymize_keywords = form_data.anonymize_keywords
        deanonymize_keywords = form_data.deanonymize_keywords
        keyword_safeguard = form_data.keyword_safeguard
        uploaded_file = form_data.uploaded_file

        logger.info("Received strict anonymization request for prompt and file.")

        # If a file is uploaded, process it
        if uploaded_file:
            logger.info("Processing uploaded file for PII detection and anonymization.")

            # Extract text content from the uploaded file
            extracted_text = extract_text_from_file(uploaded_file)

            # Check for safeguard keywords in the file
            file_safeguard_result = check_safeguard_keyword(
                extracted_text, keyword_safeguard
            )

            # If safeguard keywords are found, return an error response
            if file_safeguard_result:
                logger.warning(
                    f"Safeguard keyword detected in uploaded file: {file_safeguard_result}"
                )
                response = AnonymizedPromptResponse()
                response.safe_guard_error_message = f"Your organization's AI policy prevents the use of the following keywords: {file_safeguard_result}. Contact your administrator if you have any questions."
                return response

            logger.info("Anonymizing file content using strict GLiNER model.")
            # Get PII from the file content and anonymize it using strict GLiNER
            pii_result_of_file = await get_pii_from_file_content_strict_gliner(
                extracted_text, anonymize_keywords, pii_entities, preserve_keywords=deanonymize_keywords
            )

            # Combine PII from file
            combined_file_pii = []
            if "detected_pii_in_file" in pii_result_of_file:
                combined_file_pii.extend(pii_result_of_file["detected_pii_in_file"])
            if "detected_custom_pii_file" in pii_result_of_file:
                combined_file_pii.extend(pii_result_of_file["detected_custom_pii_file"])

            # Process the file content based on detection_only flag
            if detection_only:
                # Only detection - save original file content
                file_location = await save_anonymized_content_to_file(extracted_text)
            else:
                # Full anonymization - anonymize the file content
                if combined_file_pii:
                    processed_file_pii = process_pii(combined_file_pii, detection_only=False)
                    anonymized_file_result = anonymize_prompt_and_highlight(extracted_text, processed_file_pii)
                    anonymized_file_content = anonymized_file_result["anonymized_prompt"]
                    
                    # Save the anonymized file content
                    file_location = await save_anonymized_content_to_file(anonymized_file_content)
                else:
                    file_location = await save_anonymized_content_to_file(extracted_text)

        # Check for safeguard keywords in the prompt
        prompt_safeguard_result = check_safeguard_keyword(prompt, keyword_safeguard)

        # If safeguard keywords are found, return an error response
        if prompt_safeguard_result:
            logger.warning(
                f"Safeguard keyword detected in prompt: {prompt_safeguard_result}"
            )
            response = AnonymizedPromptResponse()
            response.safe_guard_error_message = f"Your organization's AI policy prevents the use of the following keywords: {prompt_safeguard_result}. Contact your administrator if you have any questions."
            return response

        logger.info("Anonymizing prompt using strict GLiNER model.")
        
        # Get PII from the prompt and anonymize it using strict GLiNER
        pii_result_of_prompt = await get_pii_from_user_prompt_strict_gliner(
            prompt, anonymize_keywords, pii_entities, preserve_keywords=deanonymize_keywords
        )

        # Combine PII from prompt
        combined_prompt_pii = []
        if "detected_pii_in_prompt" in pii_result_of_prompt:
            combined_prompt_pii.extend(pii_result_of_prompt["detected_pii_in_prompt"])
        if "detected_custom_pii_prompt" in pii_result_of_prompt:
            combined_prompt_pii.extend(pii_result_of_prompt["detected_custom_pii_prompt"])

        # Process the prompt based on detection_only flag
        if detection_only:
            # Only detection - return the detected PII with generic tags
            if combined_prompt_pii:
                # Convert [text, <LABEL>] format to detection format with generic tags
                processed_pii = process_pii(combined_prompt_pii, detection_only=True)
                anonymized_prompt_result = {
                    "anonymized_prompt": prompt,  # Keep original prompt
                    "highlighted_original_prompt": prompt,
                    "highlighted_anonymized_prompt": prompt,
                    "pii_list": [[item["Original"], item["Anonymized"]] for item in processed_pii],
                    "pii_entities": [[item["Original"], item["PII_Type"]] for item in processed_pii]  # Keep [text, type] format for API compatibility
                }
            else:
                # No PII found, return original prompt
                anonymized_prompt_result = {
                    "anonymized_prompt": prompt,
                    "highlighted_original_prompt": prompt,
                    "highlighted_anonymized_prompt": prompt,
                    "pii_list": [],
                    "pii_entities": []
                }
        else:
            # Full anonymization - convert PII to anonymized format and replace in text
            if combined_prompt_pii:
                # Convert [text, <LABEL>] format to anonymized format
                processed_pii = process_pii(combined_prompt_pii, detection_only=False)
                anonymized_prompt_result = anonymize_prompt_and_highlight(prompt, processed_pii)
            else:
                # No PII found, return original prompt
                anonymized_prompt_result = {
                    "anonymized_prompt": prompt,
                    "highlighted_original_prompt": prompt,
                    "highlighted_anonymized_prompt": prompt,
                    "pii_list": [],
                    "pii_entities": [],
                }

        # Prepare the response
        response = AnonymizedPromptResponse()
        response.anonymized_prompt = anonymized_prompt_result["anonymized_prompt"]
        response.highlighted_original_prompt = anonymized_prompt_result["highlighted_original_prompt"]
        response.highlighted_anonymized_prompt = anonymized_prompt_result["highlighted_anonymized_prompt"]
        response.pii_list = anonymized_prompt_result["pii_list"]
        response.pii_entities = anonymized_prompt_result["pii_entities"]
        response.file_location = file_location

        # Add file PII data if available
        if pii_result_of_file:
            # Combine PII from file
            combined_file_pii = []
            if "detected_pii_in_file" in pii_result_of_file:
                combined_file_pii.extend(pii_result_of_file["detected_pii_in_file"])
            if "detected_custom_pii_file" in pii_result_of_file:
                combined_file_pii.extend(pii_result_of_file["detected_custom_pii_file"])
            
            # Process the PII to get anonymization pairs
            if combined_file_pii:
                processed_file_pii = process_pii(combined_file_pii, detection_only=detection_only)
                # Extract the [original, anonymized] pairs for file_pii_array
                file_pii_data = [[item["Original"], item["Anonymized"]] for item in processed_file_pii]
                response.file_pii_array = file_pii_data
            else:
                response.file_pii_array = []

        logger.info("Strict anonymization process completed successfully.")
        return response

    except Exception as e:
        logger.error(f"Error occurred during strict anonymization: {e}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        response = AnonymizedPromptResponse()
        response.safe_guard_error_message = f"Error during processing: {str(e)}"
        return response