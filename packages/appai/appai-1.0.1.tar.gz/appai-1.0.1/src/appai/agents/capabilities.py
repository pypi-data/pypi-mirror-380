"""Agent capabilities enum for capability-based task assignment."""

from enum import Enum


class AgentCapability(str, Enum):
    """Agent capabilities for task matching."""

    # Django
    DJANGO_MODELS = "django_models"
    DJANGO_VIEWS = "django_views"
    DJANGO_ADMIN = "django_admin"
    DJANGO_FORMS = "django_forms"

    # DRF
    DRF_SERIALIZERS = "drf_serializers"
    DRF_VIEWSETS = "drf_viewsets"
    DRF_PERMISSIONS = "drf_permissions"

    # Testing
    TESTING = "testing"
    TEST_FIXTURES = "test_fixtures"

    # Quality
    CODE_REVIEW = "code_review"
    OPTIMIZATION = "optimization"

    # Architecture
    ARCHITECTURE = "architecture"
    DATABASE_DESIGN = "database_design"

    # General
    DOCUMENTATION = "documentation"
    DEBUGGING = "debugging"
