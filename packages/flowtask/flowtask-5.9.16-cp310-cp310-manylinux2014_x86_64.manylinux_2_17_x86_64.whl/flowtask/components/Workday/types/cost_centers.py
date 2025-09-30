import asyncio
import math
from typing import List, Optional
import pandas as pd
from datetime import date, datetime

from .base import WorkdayTypeBase
from ..models.cost_center import CostCenter
from ..parsers.cost_center_parsers import parse_cost_center_data
from ..utils import safe_serialize


class CostCenterType(WorkdayTypeBase):
    """Handler for the Workday Get_Cost_Centers operation."""

    def _get_default_payload(self) -> dict:
        """
        Payload base específico para cost centers.
        """
        return {
            "Response_Filter": {},
            "Response_Group": {
                "Include_Reference": True,
                "Include_Cost_Center_Data": True,
                "Include_Simple_Cost_Center_Data": False,
            },
        }

    async def execute(self, **kwargs) -> pd.DataFrame:
        """
        Execute the Get_Cost_Centers operation and return a pandas DataFrame.

        Supported parameters:
        - cost_center_id: Specific cost center ID to fetch (uses Request_References)
        - cost_center_id_type: Type of cost center ID (WID, Cost_Center_Reference_ID, etc.)
        - updated_from_date: Filter by updates from this date
        - updated_to_date: Filter by updates to this date
        - include_inactive: Include inactive cost centers (True/False)
        """
        # Extract parameters
        cost_center_id = kwargs.pop("cost_center_id", None)
        cost_center_id_type = kwargs.pop("cost_center_id_type", "Cost_Center_Reference_ID")
        updated_from_date = kwargs.pop("updated_from_date", None)
        updated_to_date = kwargs.pop("updated_to_date", None)
        include_inactive = kwargs.pop("include_inactive", None)

        # Build request payload
        payload = {**self.request_payload}

        # Add Request_References for specific cost center
        if cost_center_id:
            payload["Request_References"] = {
                "Cost_Center_Reference": [
                    {
                        "ID": [
                            {
                                "type": cost_center_id_type,
                                "_value_1": cost_center_id
                            }
                        ]
                    }
                ]
            }

        # Add Request_Criteria for filtering
        criteria = {}
        
        if updated_from_date or updated_to_date:
            criteria["Updated_From_Date"] = updated_from_date
            criteria["Updated_To_Date"] = updated_to_date
            
        if include_inactive is not None:
            criteria["Include_Inactive"] = include_inactive

        if criteria:
            payload["Request_Criteria"] = criteria

        self._logger.info(f"Executing Get_Cost_Centers with payload: {payload}")

        try:
            # Execute the SOAP call
            response = await self.component.run(
                operation="Get_Cost_Centers",
                **payload
            )

            # Debug: Log the full response structure
            self._logger.debug(f"Raw SOAP response type: {type(response)}")
            
            # Serialize the response to a dictionary
            serialized = self.component.serialize_object(response)
            self._logger.debug(f"Serialized response keys: {list(serialized.keys()) if isinstance(serialized, dict) else 'Not a dict'}")

            # Navigate to the cost center data
            cost_centers_raw = []
            
            if "Response_Data" in serialized and serialized["Response_Data"]:
                response_data = serialized["Response_Data"]
                
                # Extract Cost_Center elements - they might be nested
                if "Cost_Center" in response_data:
                    # Cost centers can be in a list or single item
                    cost_center_data = response_data["Cost_Center"]
                    if isinstance(cost_center_data, list):
                        cost_centers_raw = cost_center_data
                    else:
                        # Single cost center case
                        cost_centers_raw = [cost_center_data]
                else:
                    # Fallback: maybe the response_data is already the cost centers list
                    if isinstance(response_data, list):
                        cost_centers_raw = response_data
                    else:
                        cost_centers_raw = [response_data]

            self._logger.info(f"Found {len(cost_centers_raw)} cost centers in response")

            # Process each cost center
            cost_centers_processed = []
            for i, cc in enumerate(cost_centers_raw):
                try:
                    # Parse the cost center data - it should already be extracted
                    parsed_cc = parse_cost_center_data(cc)
                    
                    # Create CostCenter model instance for validation
                    cost_center_model = CostCenter(**parsed_cc)
                    
                    # Convert to dict for DataFrame
                    cost_centers_processed.append(cost_center_model.dict())
                    
                except Exception as e:
                    self._logger.error(f"Error processing cost center {i}: {e}")
                    self._logger.debug(f"Cost center data keys: {list(cc.keys()) if isinstance(cc, dict) else 'Not a dict'}")
                    # Log a sample of the problematic data (first 200 chars to avoid spam)
                    cc_str = str(cc)
                    self._logger.debug(f"Problematic cost center data sample: {cc_str[:200]}...")
                    continue

            # Convert to DataFrame
            if cost_centers_processed:
                df = pd.DataFrame(cost_centers_processed)
                
                # Log DataFrame info
                self._logger.info(f"Created DataFrame with {len(df)} rows and {len(df.columns)} columns")
                self._logger.debug(f"DataFrame columns: {list(df.columns)}")
                
                return df
            else:
                self._logger.warning("No cost centers found or processed successfully")
                # Return empty DataFrame with expected columns
                return pd.DataFrame(columns=[
                    'cost_center_id', 'cost_center_wid', 'cost_center_name', 'cost_center_code',
                    'organization_id', 'organization_name', 'organization_code', 'organization_type',
                    'effective_date', 'availability_date', 'inactive'
                ])

        except Exception as e:
            self._logger.error(f"Error in Get_Cost_Centers operation: {e}")
            raise


    async def get_all_cost_centers(self, **kwargs) -> pd.DataFrame:
        """
        Get all cost centers with pagination support.
        
        Returns:
            DataFrame with all cost centers
        """
        self._logger.info("Starting Get_All_Cost_Centers operation")
        
        # Start with first page
        page = 1
        page_size = kwargs.get('page_size', 500)  # Default page size
        all_cost_centers = []
        
        while True:
            try:
                # Add pagination to payload
                current_kwargs = {**kwargs}
                current_kwargs.update({
                    'page': page,
                    'page_size': page_size
                })
                
                # Get current page
                page_df = await self.execute(**current_kwargs)
                
                if page_df.empty:
                    self._logger.info(f"No more cost centers found at page {page}")
                    break
                    
                all_cost_centers.append(page_df)
                self._logger.info(f"Retrieved {len(page_df)} cost centers from page {page}")
                
                # Check if we got less than page_size (last page)
                if len(page_df) < page_size:
                    self._logger.info(f"Reached last page {page}")
                    break
                    
                page += 1
                
                # Safety limit to prevent infinite loops
                if page > 1000:
                    self._logger.warning("Reached maximum page limit (1000)")
                    break
                    
            except Exception as e:
                self._logger.error(f"Error retrieving page {page}: {e}")
                break
        
        # Combine all pages
        if all_cost_centers:
            combined_df = pd.concat(all_cost_centers, ignore_index=True)
            self._logger.info(f"Combined total: {len(combined_df)} cost centers")
            return combined_df
        else:
            self._logger.warning("No cost centers retrieved")
            return pd.DataFrame() 