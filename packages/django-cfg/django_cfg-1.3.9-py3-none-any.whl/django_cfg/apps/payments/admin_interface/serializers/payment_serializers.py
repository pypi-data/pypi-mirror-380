"""
Payment Serializers for Admin Interface.

DRF serializers for payment management in admin dashboard.
"""

from rest_framework import serializers
from django.contrib.auth import get_user_model
from ...models import UniversalPayment

User = get_user_model()


class AdminUserSerializer(serializers.ModelSerializer):
    """
    Simplified user serializer for admin interface.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active']
        read_only_fields = fields


class AdminPaymentListSerializer(serializers.Serializer):
    """
    Serializer for payment list in admin interface.
    Uses UniversalPayment only for data extraction.
    """
    id = serializers.UUIDField(read_only=True)
    user = AdminUserSerializer(read_only=True)
    amount_usd = serializers.FloatField(read_only=True)
    currency_code = serializers.SerializerMethodField()
    currency_name = serializers.SerializerMethodField()
    provider = serializers.CharField(read_only=True)
    provider_display = serializers.SerializerMethodField()
    status = serializers.CharField(read_only=True)
    status_display = serializers.SerializerMethodField()
    pay_amount = serializers.DecimalField(max_digits=20, decimal_places=8, read_only=True)
    pay_address = serializers.CharField(read_only=True)
    transaction_hash = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    description = serializers.CharField(read_only=True)
    age = serializers.SerializerMethodField()
    
    def get_currency_code(self, obj):
        """Get currency code from related Currency model."""
        return obj.currency.code if obj.currency else None
    
    def get_currency_name(self, obj):
        """Get currency name from related Currency model."""
        return obj.currency.name if obj.currency else None
    
    def get_provider_display(self, obj):
        """Get human-readable provider name."""
        return obj.get_provider_display()
    
    def get_status_display(self, obj):
        """Get human-readable status."""
        return obj.get_status_display()
    
    def get_age(self, obj):
        """Get human-readable age of payment."""
        from django.contrib.humanize.templatetags.humanize import naturaltime
        return naturaltime(obj.created_at)


class AdminPaymentDetailSerializer(serializers.Serializer):
    """
    Detailed serializer for individual payment in admin interface.
    Uses UniversalPayment only for data extraction.
    """
    id = serializers.UUIDField(read_only=True)
    user = AdminUserSerializer(read_only=True)
    internal_payment_id = serializers.CharField(read_only=True)
    amount_usd = serializers.FloatField(read_only=True)
    actual_amount_usd = serializers.FloatField(read_only=True)
    fee_amount_usd = serializers.FloatField(read_only=True)
    currency_code = serializers.SerializerMethodField()
    currency_name = serializers.SerializerMethodField()
    provider = serializers.CharField(read_only=True)
    provider_display = serializers.SerializerMethodField()
    status = serializers.CharField(read_only=True)
    status_display = serializers.SerializerMethodField()
    pay_amount = serializers.DecimalField(max_digits=20, decimal_places=8, read_only=True)
    pay_address = serializers.CharField(read_only=True)
    payment_url = serializers.URLField(read_only=True)
    transaction_hash = serializers.CharField(read_only=True)
    confirmations_count = serializers.IntegerField(read_only=True)
    security_nonce = serializers.CharField(read_only=True)
    expires_at = serializers.DateTimeField(read_only=True)
    completed_at = serializers.DateTimeField(read_only=True)
    description = serializers.CharField(read_only=True)
    callback_url = serializers.URLField(read_only=True)
    cancel_url = serializers.URLField(read_only=True)
    provider_data = serializers.JSONField(read_only=True)
    webhook_data = serializers.JSONField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    age = serializers.SerializerMethodField()
    
    def get_currency_code(self, obj):
        """Get currency code from related Currency model."""
        return obj.currency.code if obj.currency else None
    
    def get_currency_name(self, obj):
        """Get currency name from related Currency model."""
        return obj.currency.name if obj.currency else None
    
    def get_provider_display(self, obj):
        """Get human-readable provider name."""
        return obj.get_provider_display()
    
    def get_status_display(self, obj):
        """Get human-readable status."""
        return obj.get_status_display()
    
    def get_age(self, obj):
        """Get human-readable age of payment."""
        from django.contrib.humanize.templatetags.humanize import naturaltime
        return naturaltime(obj.created_at)


class AdminPaymentCreateSerializer(serializers.Serializer):
    """
    Serializer for creating payments in admin interface.
    Uses UniversalPayment only for data creation.
    """
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    amount_usd = serializers.FloatField(min_value=1.0, max_value=100000.0)
    currency_code = serializers.CharField(max_length=10, help_text="Currency code (e.g., BTC, ETH)")
    provider = serializers.CharField(max_length=50)
    description = serializers.CharField(required=False, allow_blank=True)
    callback_url = serializers.URLField(required=False, allow_blank=True)
    cancel_url = serializers.URLField(required=False, allow_blank=True)
    
    def validate_amount_usd(self, value):
        """Validate USD amount."""
        if value <= 0:
            raise serializers.ValidationError("Amount must be positive")
        if value > 100000:  # Max $100k per payment
            raise serializers.ValidationError("Amount exceeds maximum limit")
        return value
    
    def create(self, validated_data):
        """Create payment with currency lookup."""
        from django_cfg.apps.payments.models.currencies import Currency
        import uuid
        
        # Extract currency_code and find Currency object
        currency_code = validated_data.pop('currency_code')
        try:
            currency = Currency.objects.get(code=currency_code)
        except Currency.DoesNotExist:
            raise serializers.ValidationError(f"Currency {currency_code} not found")
        
        # Generate internal payment ID and create payment
        validated_data['currency'] = currency
        validated_data['internal_payment_id'] = f"PAY-{uuid.uuid4().hex[:12].upper()}"
        
        return UniversalPayment.objects.create(**validated_data)


class AdminPaymentUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating payments in admin interface.
    """
    class Meta:
        model = UniversalPayment
        fields = [
            'status', 'description', 'callback_url', 'cancel_url',
            'provider_data', 'webhook_data'
        ]
    
    def validate_status(self, value):
        """Validate status transitions."""
        if self.instance and self.instance.status == UniversalPayment.PaymentStatus.COMPLETED:
            if value != UniversalPayment.PaymentStatus.COMPLETED:
                raise serializers.ValidationError("Cannot change status of completed payment")
        return value


class AdminPaymentStatsSerializer(serializers.Serializer):
    """
    Serializer for payment statistics in admin interface.
    """
    total_payments = serializers.IntegerField()
    total_amount_usd = serializers.FloatField()
    successful_payments = serializers.IntegerField()
    failed_payments = serializers.IntegerField()
    pending_payments = serializers.IntegerField()
    success_rate = serializers.FloatField()
    
    # Provider breakdown
    by_provider = serializers.DictField(
        child=serializers.DictField(),
        help_text="Statistics by provider"
    )
    
    # Currency breakdown
    by_currency = serializers.DictField(
        child=serializers.DictField(),
        help_text="Statistics by currency"
    )
    
    # Time-based stats
    last_24h = serializers.DictField(
        child=serializers.IntegerField(),
        help_text="Payments in last 24 hours"
    )
    
    last_7d = serializers.DictField(
        child=serializers.IntegerField(),
        help_text="Payments in last 7 days"
    )
    
    last_30d = serializers.DictField(
        child=serializers.IntegerField(),
        help_text="Payments in last 30 days"
    )
