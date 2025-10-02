"""Main client for the Vaults.fyi SDK."""

import json
from typing import Dict, Any, Optional, List
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .exceptions import HttpResponseError, AuthenticationError, ForbiddenError, RateLimitError, NetworkError
from .utils import generate_query_params


class VaultsSdk:
    """Python SDK for interacting with the Vaults.fyi API."""
    
    def __init__(
        self, 
        api_key: str, 
        api_base_url: str = "https://api.vaults.fyi",
        timeout: int = 30,
        max_retries: int = 3
    ):
        """Initialize the Vaults.fyi SDK client.
        
        Args:
            api_key: Your Vaults.fyi API key
            api_base_url: Base URL for the API (default: https://api.vaults.fyi)
            timeout: Request timeout in seconds (default: 30)
            max_retries: Maximum number of retries for failed requests (default: 3)
        """
        self.api_key = api_key
        self.api_base_url = api_base_url.rstrip('/')
        self.timeout = timeout
        
        # Configure session with retry strategy
        self.session = requests.Session()
        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS"],
            backoff_factor=1
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
    
    def _make_request(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        method: str = "GET"
    ) -> Dict[str, Any]:
        """Make HTTP request to the API.
        
        Args:
            endpoint: API endpoint path
            params: Request parameters (path and query params)
            method: HTTP method (GET or POST)
            
        Returns:
            JSON response data
            
        Raises:
            HttpResponseError: When API returns an error
            AuthenticationError: When API key is invalid
            RateLimitError: When rate limit is exceeded
            NetworkError: When network/connection issues occur
        """
        # Extract query parameters
        query_params = params.get('query', {}) if params else {}
        query_string = generate_query_params(query_params)
        
        # Build full URL
        url = f"{self.api_base_url}{endpoint}{query_string}"
        
        # Prepare headers
        headers = {
            "Content-Type": "application/json",
            "x-api-key": self.api_key,
        }
        
        # Prepare request body for POST requests
        body = None
        if method == "POST" and params and 'body' in params:
            body = json.dumps(params['body'])
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                headers=headers,
                data=body,
                timeout=self.timeout
            )
            
            # Handle different status codes
            if response.status_code == 401:
                try:
                    error_data = response.json()
                    error_message = error_data.get('message', 'API key required')
                    error_id = error_data.get('errorId')
                    raise AuthenticationError(error_message, error_id)
                except (ValueError, KeyError):
                    raise AuthenticationError("Invalid API key")
            elif response.status_code == 403:
                try:
                    error_data = response.json()
                    error_message = error_data.get('message', 'Forbidden - insufficient permissions or credits exhausted')
                    error_id = error_data.get('errorId')
                    raise ForbiddenError(error_message, error_id)
                except (ValueError, KeyError):
                    raise ForbiddenError("Forbidden - insufficient permissions or credits exhausted")
            elif response.status_code == 429:
                raise RateLimitError("API rate limit exceeded")
            elif not response.ok:
                try:
                    error_data = response.json()
                    error_message = error_data.get('message', f'HTTP {response.status_code}')
                except:
                    error_message = f'HTTP {response.status_code}: {response.text}'
                
                raise HttpResponseError(
                    error_message, 
                    status_code=response.status_code,
                    response_data=error_data if 'error_data' in locals() else None
                )
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error: {str(e)}")
    
    # V2 API Methods - Health & Basic Data

    def get_health(self) -> Dict[str, Any]:
        """Get API health status.

        Returns:
            API health status
        """
        endpoint = "/v2/health"
        return self._make_request(endpoint)

    def get_vaults(
        self,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        network: Optional[str] = None,
        asset_symbol: Optional[str] = None,
        only_transactional: Optional[bool] = None,
        only_app_featured: Optional[bool] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Get basic list of vaults with simple filtering.

        Args:
            page: Page number (starting from 0)
            per_page: Number of items per page
            network: Network name filter
            asset_symbol: Asset symbol filter
            only_transactional: Filter for transactional vaults only
            only_app_featured: Filter for app-featured vaults only
            **kwargs: Additional query parameters

        Returns:
            Basic vaults list
        """
        endpoint = "/v2/vaults"
        query_params = {}

        if page is not None:
            query_params['page'] = page
        if per_page is not None:
            query_params['perPage'] = per_page
        if network is not None:
            query_params['network'] = network
        if asset_symbol is not None:
            query_params['assetSymbol'] = asset_symbol
        if only_transactional is not None:
            query_params['onlyTransactional'] = only_transactional
        if only_app_featured is not None:
            query_params['onlyAppFeatured'] = only_app_featured

        query_params.update(kwargs)
        params = {"query": query_params} if query_params else None
        return self._make_request(endpoint, params)

    def get_assets(
        self,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        network: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Get list of supported assets.

        Args:
            page: Page number (starting from 0)
            per_page: Number of items per page
            network: Network name filter
            **kwargs: Additional query parameters

        Returns:
            List of supported assets
        """
        endpoint = "/v2/assets"
        query_params = {}

        if page is not None:
            query_params['page'] = page
        if per_page is not None:
            query_params['perPage'] = per_page
        if network is not None:
            query_params['network'] = network

        query_params.update(kwargs)
        params = {"query": query_params} if query_params else None
        return self._make_request(endpoint, params)

    def get_networks(self, **kwargs) -> Dict[str, Any]:
        """Get list of supported blockchain networks.

        Args:
            **kwargs: Additional query parameters

        Returns:
            List of supported networks
        """
        endpoint = "/v2/networks"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)

    def get_tags(self, **kwargs) -> Dict[str, Any]:
        """Get list of vault categorization tags.

        Args:
            **kwargs: Additional query parameters

        Returns:
            List of vault tags
        """
        endpoint = "/v2/tags"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)

    # V2 API Methods - Benchmarks
    
    def get_benchmarks(
        self,
        network: str,
        code: str
    ) -> Dict[str, Any]:
        """Get benchmark APY data for a specific network and benchmark code.
        
        Args:
            network: Network name (e.g., 'mainnet', 'base', 'arbitrum')
            code: Benchmark code ('usd' or 'eth')
            
        Returns:
            Benchmark APY data with timestamp
        """
        endpoint = f"/v2/benchmarks/{network}"
        params = {"query": {"code": code}}
        return self._make_request(endpoint, params)
    
    def get_historical_benchmarks(
        self,
        network: str,
        code: str,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        from_timestamp: Optional[int] = None,
        to_timestamp: Optional[int] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Get historical benchmark APY data with pagination.
        
        Args:
            network: Network name (e.g., 'mainnet', 'base', 'arbitrum')
            code: Benchmark code ('usd' or 'eth')
            page: Page number (starting from 0)
            per_page: Number of items per page
            from_timestamp: Start timestamp for filtering
            to_timestamp: End timestamp for filtering
            **kwargs: Additional query parameters
            
        Returns:
            Paginated historical benchmark data
        """
        endpoint = f"/v2/historical-benchmarks/{network}"
        query_params = {"code": code}
        
        if page is not None:
            query_params['page'] = page
        if per_page is not None:
            query_params['perPage'] = per_page
        if from_timestamp is not None:
            query_params['fromTimestamp'] = from_timestamp
        if to_timestamp is not None:
            query_params['toTimestamp'] = to_timestamp
        
        # Add any additional kwargs
        query_params.update(kwargs)
        
        params = {"query": query_params}
        return self._make_request(endpoint, params)
    
    # V2 API Methods - Portfolio & Vaults
    
    def get_vault_historical_data(
        self,
        network: str,
        vault_address: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Get historical data for a specific vault.

        Args:
            network: Network name (e.g., 'mainnet', 'base', 'arbitrum')
            vault_address: Vault contract address
            **kwargs: Additional query parameters

        Returns:
            Historical vault data
        """
        endpoint = f"/v2/historical/{network}/{vault_address}"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)

    def get_vault_historical_apy(
        self,
        network: str,
        vault_address: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Get historical APY data for a specific vault.

        Args:
            network: Network name
            vault_address: Vault contract address
            **kwargs: Additional query parameters

        Returns:
            Historical APY data
        """
        endpoint = f"/v2/historical/{network}/{vault_address}/apy"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)

    def get_vault_historical_tvl(
        self,
        network: str,
        vault_address: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Get historical TVL data for a specific vault.

        Args:
            network: Network name
            vault_address: Vault contract address
            **kwargs: Additional query parameters

        Returns:
            Historical TVL data
        """
        endpoint = f"/v2/historical/{network}/{vault_address}/tvl"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)

    def get_vault_historical_share_price(
        self,
        network: str,
        vault_address: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Get historical share price data for a specific vault.

        Args:
            network: Network name
            vault_address: Vault contract address
            **kwargs: Additional query parameters

        Returns:
            Historical share price data
        """
        endpoint = f"/v2/historical/{network}/{vault_address}/sharePrice"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)
    
    def get_vault_total_returns(
        self,
        user_address: str,
        network: str,
        vault_address: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Get total returns for a user in a specific vault.

        Args:
            user_address: User's wallet address
            network: Network name
            vault_address: Vault contract address
            **kwargs: Additional query parameters

        Returns:
            Total returns data
        """
        endpoint = f"/v2/portfolio/total-returns/{user_address}/{network}/{vault_address}"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)
    
    def get_positions(self, user_address: str, **kwargs) -> Dict[str, Any]:
        """Get all positions for a user.

        Args:
            user_address: User's wallet address
            **kwargs: Additional query parameters

        Returns:
            User positions data
        """
        endpoint = f"/v2/portfolio/positions/{user_address}"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)

    def get_position(
        self,
        user_address: str,
        network: str,
        vault_address: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Get a specific position for a user in a vault.

        Args:
            user_address: User's wallet address
            network: Network name
            vault_address: Vault contract address
            **kwargs: Additional query parameters

        Returns:
            Single position data
        """
        endpoint = f"/v2/portfolio/positions/{user_address}/{network}/{vault_address}"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)

    def get_best_vault(self, user_address: str, **kwargs) -> Dict[str, Any]:
        """Get the best vault opportunity for a user.

        Args:
            user_address: User's wallet address
            **kwargs: Additional query parameters

        Returns:
            Best vault recommendation data
        """
        endpoint = f"/v2/portfolio/best-vault/{user_address}"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)
    
    def get_deposit_options(
        self, 
        user_address: str, 
        allowed_assets: Optional[List[str]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Get best deposit options for a user.
        
        Args:
            user_address: User's wallet address
            allowed_assets: List of allowed asset symbols (e.g., ['USDC', 'USDS'])
            **kwargs: Additional query parameters
            
        Returns:
            Best deposit options data
        """
        endpoint = f"/v2/portfolio/best-deposit-options/{user_address}"
        query_params = kwargs.copy()
        if allowed_assets:
            query_params['allowedAssets'] = allowed_assets
        
        params = {"query": query_params} if query_params else None
        return self._make_request(endpoint, params)
    
    def get_vault_holder_events(
        self,
        user_address: str,
        network: str,
        vault_address: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Get events for a vault holder.
        
        Args:
            user_address: User's wallet address
            network: Network name
            vault_address: Vault contract address
            **kwargs: Additional query parameters
            
        Returns:
            Vault holder events data
        """
        endpoint = f"/v2/portfolio/events/{user_address}/{network}/{vault_address}"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)
    
    def get_all_vaults(self, **kwargs) -> Dict[str, Any]:
        """Get all available vaults.
        
        Args:
            **kwargs: Query parameters for filtering
            
        Returns:
            All vaults data
        """
        endpoint = "/v2/detailed-vaults"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)
    
    def get_vault(self, network: str, vault_address: str, **kwargs) -> Dict[str, Any]:
        """Get detailed information for a specific vault.

        Args:
            network: Network name
            vault_address: Vault contract address
            **kwargs: Additional query parameters

        Returns:
            Detailed vault data
        """
        endpoint = f"/v2/detailed-vaults/{network}/{vault_address}"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)

    def get_vault_apy_breakdown(
        self,
        network: str,
        vault_address: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Get APY breakdown for a specific vault.

        Args:
            network: Network name
            vault_address: Vault contract address
            **kwargs: Additional query parameters

        Returns:
            Vault APY breakdown data
        """
        endpoint = f"/v2/detailed-vaults/{network}/{vault_address}/apy"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)

    def get_vault_tvl_breakdown(
        self,
        network: str,
        vault_address: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Get TVL breakdown for a specific vault.

        Args:
            network: Network name
            vault_address: Vault contract address
            **kwargs: Additional query parameters

        Returns:
            Vault TVL breakdown data
        """
        endpoint = f"/v2/detailed-vaults/{network}/{vault_address}/tvl"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)
    
    def get_idle_assets(self, user_address: str, **kwargs) -> Dict[str, Any]:
        """Get idle assets for a user.
        
        Args:
            user_address: User's wallet address
            **kwargs: Additional query parameters
            
        Returns:
            Idle assets data
        """
        endpoint = f"/v2/portfolio/idle-assets/{user_address}"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)
    
    def get_transactions_context(
        self,
        user_address: str,
        network: str,
        vault_address: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Get transaction context for a user and vault.
        
        Args:
            user_address: User's wallet address
            network: Network name
            vault_address: Vault contract address
            **kwargs: Additional query parameters
            
        Returns:
            Transaction context data
        """
        endpoint = f"/v2/transactions/context/{user_address}/{network}/{vault_address}"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)
    
    def get_actions(
        self,
        action: str,
        user_address: str,
        network: str,
        vault_address: str,
        amount: Optional[str] = None,
        asset_address: Optional[str] = None,
        simulate: bool = False,
        **kwargs
    ) -> Dict[str, Any]:
        """Get transaction actions for deposit/withdraw operations.

        Args:
            action: Action type ('deposit', 'redeem', etc.)
            user_address: User's wallet address
            network: Network name
            vault_address: Vault contract address
            amount: Amount for the transaction
            asset_address: Asset contract address
            simulate: Whether to simulate the transaction
            **kwargs: Additional query parameters

        Returns:
            Transaction action data
        """
        endpoint = f"/v2/transactions/{action}/{user_address}/{network}/{vault_address}"

        query_params = kwargs.copy()
        if amount is not None:
            query_params['amount'] = amount
        if asset_address is not None:
            query_params['assetAddress'] = asset_address
        query_params['simulate'] = simulate

        params = {"query": query_params} if query_params else None
        return self._make_request(endpoint, params)

    # V2 API Methods - Rewards

    def get_rewards_context(self, user_address: str, **kwargs) -> Dict[str, Any]:
        """Get rewards context for a user.

        Args:
            user_address: User's wallet address
            **kwargs: Additional query parameters

        Returns:
            Rewards context data
        """
        endpoint = f"/v2/transactions/rewards/context/{user_address}"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)

    def get_rewards_claim(self, user_address: str, **kwargs) -> Dict[str, Any]:
        """Get rewards claim transaction data for a user.

        Args:
            user_address: User's wallet address
            **kwargs: Additional query parameters

        Returns:
            Rewards claim transaction data
        """
        endpoint = f"/v2/transactions/rewards/claim/{user_address}"
        params = {"query": kwargs} if kwargs else None
        return self._make_request(endpoint, params)