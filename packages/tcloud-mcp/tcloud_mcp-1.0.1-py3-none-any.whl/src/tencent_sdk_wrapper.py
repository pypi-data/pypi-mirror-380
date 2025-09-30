"""
Tencent Cloud SDK Wrapper

Direct SDK integration without requiring TCCLI installation.
Uses the same tencentcloud-sdk-python that TCCLI depends on.
"""

import json
import logging
import os
from typing import Dict, Any, Optional, List
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

# Import commonly used services
from tencentcloud.cvm.v20170312 import cvm_client, models as cvm_models
from tencentcloud.vpc.v20170312 import vpc_client, models as vpc_models
from tencentcloud.cbs.v20170312 import cbs_client, models as cbs_models
from tencentcloud.cls.v20201016 import cls_client, models as cls_models
from tencentcloud.clb.v20180317 import clb_client, models as clb_models
from tencentcloud.monitor.v20180724 import monitor_client, models as monitor_models

# Import TCCLI service loader
from .tccli_service_loader import TCCLIServiceLoader

logger = logging.getLogger(__name__)


class TencentSDKWrapper:
    """Direct SDK wrapper for Tencent Cloud services."""

    # Service mappings
    SERVICE_MAPPINGS = {
        'cvm': {
            'client_class': cvm_client.CvmClient,
            'models': cvm_models,
            'endpoint': 'cvm.tencentcloudapi.com'
        },
        'vpc': {
            'client_class': vpc_client.VpcClient,
            'models': vpc_models,
            'endpoint': 'vpc.tencentcloudapi.com'
        },
        'cbs': {
            'client_class': cbs_client.CbsClient,
            'models': cbs_models,
            'endpoint': 'cbs.tencentcloudapi.com'
        },
        'cls': {
            'client_class': cls_client.ClsClient,
            'models': cls_models,
            'endpoint': 'cls.tencentcloudapi.com'
        },
        'clb': {
            'client_class': clb_client.ClbClient,
            'models': clb_models,
            'endpoint': 'clb.tencentcloudapi.com'
        },
        'monitor': {
            'client_class': monitor_client.MonitorClient,
            'models': monitor_models,
            'endpoint': 'monitor.tencentcloudapi.com'
        }
    }

    def __init__(self, secret_id: str = None, secret_key: str = None, region: str = "ap-guangzhou"):
        """Initialize SDK wrapper.

        Args:
            secret_id: Tencent Cloud Secret ID
            secret_key: Tencent Cloud Secret Key
            region: Default region
        """
        self.secret_id = secret_id or os.environ.get('TENCENTCLOUD_SECRET_ID')
        self.secret_key = secret_key or os.environ.get('TENCENTCLOUD_SECRET_KEY')
        self.default_region = region or os.environ.get('TENCENTCLOUD_REGION', 'ap-guangzhou')

        if not self.secret_id or not self.secret_key:
            raise ValueError("Missing Tencent Cloud credentials. Please set TENCENTCLOUD_SECRET_ID and TENCENTCLOUD_SECRET_KEY environment variables.")

        self.cred = credential.Credential(self.secret_id, self.secret_key)
        self.clients = {}  # Cache for clients

        # Initialize TCCLI service loader
        self.service_loader = TCCLIServiceLoader()

    def _get_client(self, service: str, region: str = None):
        """Get or create client for a service."""
        region = region or self.default_region
        cache_key = f"{service}_{region}"

        if cache_key in self.clients:
            return self.clients[cache_key]

        if service not in self.SERVICE_MAPPINGS:
            raise ValueError(f"Unsupported service: {service}")

        service_info = self.SERVICE_MAPPINGS[service]

        # Create HTTP profile
        httpProfile = HttpProfile()
        httpProfile.endpoint = service_info['endpoint']

        # Create client profile
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile

        # Create client
        client = service_info['client_class'](self.cred, region, clientProfile)
        self.clients[cache_key] = client

        return client

    async def call_api(self, service: str, action: str,
                      parameters: Optional[Dict[str, Any]] = None,
                      region: Optional[str] = None) -> Dict[str, Any]:
        """Call Tencent Cloud API.

        Args:
            service: Service name (e.g., 'cvm', 'vpc')
            action: API action (e.g., 'DescribeInstances')
            parameters: API parameters
            region: Target region

        Returns:
            API response as dictionary
        """
        try:
            client = self._get_client(service, region)
            service_info = self.SERVICE_MAPPINGS[service]

            # Get request model class
            request_class_name = f"{action}Request"
            if not hasattr(service_info['models'], request_class_name):
                raise ValueError(f"Unknown action: {action} for service: {service}")

            request_class = getattr(service_info['models'], request_class_name)

            # Create request object
            if parameters:
                # Convert parameters to JSON string and back to handle nested objects
                params_json = json.dumps(parameters, ensure_ascii=False)
                request = request_class()
                request.from_json_string(params_json)
            else:
                request = request_class()

            # Call API
            response = getattr(client, action)(request)

            # Convert response to dict
            response_dict = json.loads(response.to_json_string())

            return response_dict

        except TencentCloudSDKException as e:
            logger.error(f"SDK error: {e}")
            raise Exception(f"Tencent Cloud API error: {e.message}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise

    async def get_regions(self) -> List[Dict[str, str]]:
        """Get available regions."""
        try:
            result = await self.call_api('cvm', 'DescribeRegions')
            return result.get('RegionSet', [])
        except Exception as e:
            logger.error(f"Failed to get regions: {e}")
            return []

    async def get_available_services(self) -> List[str]:
        """Get list of supported services from TCCLI and SDK."""
        # Get services from TCCLI definitions
        tccli_services = set(self.service_loader.get_available_services())

        # Get services from SDK mappings
        sdk_services = set(self.SERVICE_MAPPINGS.keys())

        # Return union of both
        return sorted(tccli_services.union(sdk_services))

    def search_actions(self, query: str, service: str = None) -> List[Dict[str, Any]]:
        """Search for actions matching the query."""
        return self.service_loader.search_actions(query, service)

    def get_service_info(self, service: str) -> Dict[str, Any]:
        """Get information about a service using TCCLI definitions."""
        # First try to get info from TCCLI service definitions
        tccli_info = self.service_loader.get_service_info(service)

        if "error" not in tccli_info:
            # Enhance with SDK info if available
            if service in self.SERVICE_MAPPINGS:
                service_mapping = self.SERVICE_MAPPINGS[service]
                tccli_info["endpoint"] = service_mapping['endpoint']
                tccli_info["sdk_supported"] = True
            else:
                tccli_info["sdk_supported"] = False
            return tccli_info

        # Fallback to SDK-only info
        if service not in self.SERVICE_MAPPINGS:
            return {"error": f"Service {service} not found in both TCCLI definitions and SDK mappings"}

        service_info = self.SERVICE_MAPPINGS[service]
        models_module = service_info['models']

        # Get all available actions
        actions = []
        for attr_name in dir(models_module):
            if attr_name.endswith('Request'):
                action_name = attr_name[:-7]  # Remove 'Request' suffix
                actions.append(action_name)

        return {
            "service": service,
            "endpoint": service_info['endpoint'],
            "available_actions": sorted(actions),
            "total_actions": len(actions),
            "sdk_supported": True,
            "source": "SDK only"
        }

    def get_action_info(self, service: str, action: str) -> Dict[str, Any]:
        """Get information about a specific action using TCCLI definitions."""
        # First try to get info from TCCLI service definitions
        tccli_info = self.service_loader.get_action_info(service, action)

        if "error" not in tccli_info:
            # Enhance with SDK info if available
            if service in self.SERVICE_MAPPINGS:
                service_info = self.SERVICE_MAPPINGS[service]
                models_module = service_info['models']
                request_class_name = f"{action}Request"
                response_class_name = f"{action}Response"

                tccli_info["request_class"] = request_class_name
                tccli_info["response_class"] = response_class_name

                # Check if action exists in SDK
                if hasattr(models_module, request_class_name):
                    request_class = getattr(models_module, request_class_name)
                    tccli_info["sdk_available"] = True

                    # Try to create a sample request to see its structure
                    try:
                        sample_request = request_class()
                        tccli_info["sdk_sample_request"] = sample_request.to_json_string()
                    except:
                        tccli_info["sdk_sample_request"] = "{}"
                else:
                    tccli_info["sdk_available"] = False
            else:
                tccli_info["sdk_available"] = False

            return tccli_info

        # Fallback to SDK-only info
        if service not in self.SERVICE_MAPPINGS:
            return {"error": f"Service {service} not found in both TCCLI definitions and SDK mappings"}

        service_info = self.SERVICE_MAPPINGS[service]
        models_module = service_info['models']

        request_class_name = f"{action}Request"
        response_class_name = f"{action}Response"

        info = {
            "service": service,
            "action": action,
            "request_class": request_class_name,
            "response_class": response_class_name,
            "source": "SDK only"
        }

        # Check if action exists
        if hasattr(models_module, request_class_name):
            request_class = getattr(models_module, request_class_name)

            info["sdk_available"] = True

            # Try to create a sample request to see its structure
            try:
                sample_request = request_class()
                info["sdk_sample_request"] = sample_request.to_json_string()
            except:
                info["sdk_sample_request"] = "{}"
        else:
            info["sdk_available"] = False
            info["error"] = f"Action {action} not found in service {service}"

        return info