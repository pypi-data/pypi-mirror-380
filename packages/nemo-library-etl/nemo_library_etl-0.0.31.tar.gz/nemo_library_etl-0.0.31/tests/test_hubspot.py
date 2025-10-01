from nemo_library_etl.adapter.hubspot.flow import hubspot_flow


HS_PROJECT_NAME = "gs_unit_test_HubSpot"

def test_hubspot() -> None:

    hubspot_flow()