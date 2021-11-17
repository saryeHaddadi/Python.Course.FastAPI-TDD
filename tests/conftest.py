import sys
from pathlib import Path

# Add src folder to Python Path
# Inside src, all imports are made relatively to src, ie. not prefixed by 'src.'
# and thus can not be resolved here. 
sys.path.append(str(Path(Path(), 'src').resolve()))

import os
import pytest
from starlette.testclient import TestClient

from src import main


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))

@pytest.fixture(scope="module")
def test_app():
    # set up
    main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:

        # testing
        yield test_client

    # tear down
