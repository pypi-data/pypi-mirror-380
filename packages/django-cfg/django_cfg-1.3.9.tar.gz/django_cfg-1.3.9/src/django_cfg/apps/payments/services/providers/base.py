"""
Base provider class for the Universal Payment System v2.0.

Abstract base class for all payment providers with unified interface.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from decimal import Decimal
from django_cfg.modules.django_logger import get_logger
from ..types import ProviderResponse, ServiceOperationResult
from .models import ProviderConfig, PaymentRequest


class BaseProvider(ABC):
    """
    Abstract base class for payment providers.
    
    Defines the unified interface that all providers must implement.
    """
    
    def __init__(self, config: ProviderConfig):
        """
        Initialize provider with configuration.
        
        Args:
            config: Provider configuration
        """
        self.config = config
        self.logger = get_logger(f"providers.{config.provider_name}")
        self._session = None
    
    @property
    def name(self) -> str:
        """Get provider name."""
        return self.config.provider_name
    
    @property
    def is_sandbox(self) -> bool:
        """Check if provider is in sandbox mode."""
        return self.config.sandbox
    
    # Provider configuration methods (to be overridden by specific providers)
    def get_fee_percentage(self, currency_code: str = None, currency_type: str = None) -> Decimal:
        """
        Get fee percentage for currency.
        
        Args:
            currency_code: Currency code (e.g., 'BTC', 'ETH')
            currency_type: Currency type ('fiat', 'crypto')
            
        Returns:
            Fee percentage as decimal (0.005 = 0.5%)
        """
        return Decimal('0.005')  # Default 0.5%
    
    def get_fixed_fee_usd(self, currency_code: str = None, currency_type: str = None) -> Decimal:
        """
        Get fixed fee in USD for currency.
        
        Args:
            currency_code: Currency code (e.g., 'BTC', 'ETH')
            currency_type: Currency type ('fiat', 'crypto')
            
        Returns:
            Fixed fee in USD
        """
        return Decimal('0.0')  # Default no fixed fee
    
    def get_min_amount_usd(self, currency_code: str = None, currency_type: str = None, is_stable: bool = False) -> Decimal:
        """
        Get minimum amount in USD for currency.
        
        Args:
            currency_code: Currency code (e.g., 'BTC', 'ETH')
            currency_type: Currency type ('fiat', 'crypto')
            is_stable: Whether currency is a stablecoin
            
        Returns:
            Minimum amount in USD
        """
        if currency_type == 'fiat':
            return Decimal('1.0')
        elif is_stable:
            return Decimal('0.01')
        else:
            return Decimal('0.000001')
    
    def get_max_amount_usd(self, currency_code: str = None, currency_type: str = None) -> Decimal:
        """
        Get maximum amount in USD for currency.
        
        Args:
            currency_code: Currency code (e.g., 'BTC', 'ETH')
            currency_type: Currency type ('fiat', 'crypto')
            
        Returns:
            Maximum amount in USD
        """
        return Decimal('1000000.0')  # Default 1M USD
    
    def get_confirmation_blocks(self, network_code: str) -> int:
        """
        Get confirmation blocks for network.
        
        Args:
            network_code: Network code (e.g., 'btc', 'eth')
            
        Returns:
            Number of confirmation blocks
        """
        return 1  # Default 1 confirmation
    
    def get_network_name(self, network_code: str) -> str:
        """
        Get human-readable network name.
        
        Args:
            network_code: Network code (e.g., 'btc', 'eth')
            
        Returns:
            Human-readable network name
        """
        return network_code.upper() if network_code else 'Unknown'
    
    @abstractmethod
    def create_payment(self, request: PaymentRequest) -> ProviderResponse:
        """
        Create payment with provider.
        
        Args:
            request: Payment creation request
            
        Returns:
            ProviderResponse: Provider response with payment details
        """
        pass
    
    @abstractmethod
    def get_payment_status(self, provider_payment_id: str) -> ProviderResponse:
        """
        Get payment status from provider.
        
        Args:
            provider_payment_id: Provider's payment ID
            
        Returns:
            ProviderResponse: Current payment status
        """
        pass
    
    @abstractmethod
    def get_supported_currencies(self) -> ServiceOperationResult:
        """
        Get list of supported currencies from provider.
        
        Returns:
            ServiceOperationResult: List of supported currencies
        """
        pass
    
    @abstractmethod
    def sync_currencies_to_db(self):
        """
        Sync currencies from provider API to database.
        
        Returns:
            CurrencySyncResult: Synchronization result
        """
        pass
    
    @abstractmethod
    def validate_webhook(self, payload: Dict[str, Any], signature: str = None) -> ServiceOperationResult:
        """
        Validate webhook from provider.
        
        Args:
            payload: Webhook payload
            signature: Webhook signature (if any)
            
        Returns:
            ServiceOperationResult: Validation result
        """
        pass
    
    def get_exchange_rate(self, from_currency: str, to_currency: str) -> ServiceOperationResult:
        """
        Get exchange rate from provider (optional).
        
        Args:
            from_currency: Source currency
            to_currency: Target currency
            
        Returns:
            ServiceOperationResult: Exchange rate or not supported
        """
        return ServiceOperationResult(
            success=False,
            message=f"Exchange rates not supported by {self.name}",
            error_code="not_supported"
        )
    
    def health_check(self) -> ServiceOperationResult:
        """
        Perform provider health check.
        
        Returns:
            ServiceOperationResult: Health check result
        """
        try:
            # Basic connectivity test - can be overridden by providers
            result = self.get_supported_currencies()
            
            if result.success:
                return ServiceOperationResult(
                    success=True,
                    message=f"{self.name} provider is healthy",
                    data={
                        'provider': self.name,
                        'sandbox': self.is_sandbox,
                        'api_url': self.config.api_url,
                        'supported_currencies_count': len(result.data.get('currencies', []))
                    }
                )
            else:
                return ServiceOperationResult(
                    success=False,
                    message=f"{self.name} provider health check failed",
                    error_code="health_check_failed",
                    data={'provider': self.name, 'error': result.message}
                )
                
        except Exception as e:
            self.logger.error(f"Health check failed for {self.name}: {e}")
            return ServiceOperationResult(
                success=False,
                message=f"{self.name} provider health check error: {e}",
                error_code="health_check_error",
                data={'provider': self.name}
            )
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """
        Make HTTP request to provider API.
        
        Args:
            method: HTTP method
            endpoint: API endpoint
            data: Request data
            headers: Request headers
            
        Returns:
            Dict[str, Any]: Response data
            
        Raises:
            Exception: If request fails
        """
        import requests
        from requests.adapters import HTTPAdapter
        from urllib3.util.retry import Retry
        
        # Create session if not exists
        if self._session is None:
            self._session = requests.Session()
            
            # Configure retries
            retry_strategy = Retry(
                total=self.config.retry_attempts,
                backoff_factor=self.config.retry_delay,
                status_forcelist=[429, 500, 502, 503, 504],
            )
            adapter = HTTPAdapter(max_retries=retry_strategy)
            self._session.mount("http://", adapter)
            self._session.mount("https://", adapter)
        
        # Build URL
        url = f"{self.config.api_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        # Prepare headers
        request_headers = {
            'Content-Type': 'application/json',
            'User-Agent': f'django-cfg-payments/2.0 ({self.name})',
        }
        if headers:
            request_headers.update(headers)
        
        # Log request
        self.logger.debug(f"Making {method} request to {url}", extra={
            'method': method,
            'url': url,
            'has_data': bool(data)
        })
        
        # Make request
        response = self._session.request(
            method=method,
            url=url,
            json=data if data else None,
            headers=request_headers,
            timeout=self.config.timeout
        )
        
        # Log response
        self.logger.debug(f"Received response: {response.status_code}", extra={
            'status_code': response.status_code,
            'response_size': len(response.content)
        })
        
        # Handle response
        response.raise_for_status()
        
        try:
            return response.json()
        except ValueError:
            # Non-JSON response
            return {'raw_response': response.text, 'status_code': response.status_code}
    
    def _create_provider_response(
        self,
        success: bool,
        raw_response: Dict[str, Any],
        **kwargs
    ) -> ProviderResponse:
        """
        Create standardized provider response.
        
        Args:
            success: Operation success
            raw_response: Raw provider response
            **kwargs: Additional response fields
            
        Returns:
            ProviderResponse: Standardized response
        """
        return ProviderResponse(
            provider=self.name,
            success=success,
            raw_response=raw_response,
            **kwargs
        )
    
    def __str__(self) -> str:
        """String representation."""
        return f"{self.name}Provider(sandbox={self.is_sandbox})"
    
    def __repr__(self) -> str:
        """Detailed representation."""
        return f"{self.__class__.__name__}(name='{self.name}', sandbox={self.is_sandbox}, api_url='{self.config.api_url}')"
