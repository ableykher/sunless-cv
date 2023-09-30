"""Module with identifiers of Sunless CV."""

import enum


class LocationId(enum.Enum):
    """Enumeration with location ids."""
    HOME = "home"
    MAZE = "maze"
    HALLWAY = "hallway"
    PROFESSION = "profession"
    PERSONALITY = "personality"
    TECHNOLOGY = "technology"
    COMPANY = "company"


class CompetenceId(enum.Enum):
    """Enumeration with competence ids."""
    AGILE = "agile"
    API = "API"
    BDD = "BDD"
    CI = "continuus integration"
    CONTAINER = "containers"
    JAVA = "java"
    LOAD_TESTING = "load testing"
    PROTOCOL = "protocols"
    PYTHON = "python"
    QA = "quality assurance"
    REPORT = "reporting"
    RISK_ASSESSMENT = "product risk assessment"
    SELENIUM = "selenium"
    STANDALONE_APPLICATION = "standalone application"
    TEST_AUTOMATION = "test automation"
    TEST_DESIGN = "test design"
    TMS = "test management system"
    VIRTUAL_MACHINE = "virtual machines"
    WEB_APPLICATION = "web application"
