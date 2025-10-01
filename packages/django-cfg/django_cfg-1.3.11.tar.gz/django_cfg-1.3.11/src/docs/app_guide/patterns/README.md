# 🎯 Django-CFG Development Patterns %%PRIORITY:HIGH%%

## 🎯 Quick Summary
- Architecture patterns and best practices for Django-CFG applications
- Manager-based business logic and URL routing patterns
- Admin interface customization and middleware integration
- Type-safe development with proper separation of concerns

## 📋 Table of Contents
1. [Architecture](architecture.md) - Project structure and layer separation
2. [Configuration](configuration.md) - Configuration management patterns
3. [Managers](managers.md) - ORM managers and business logic patterns
4. [Routing](routing.md) - URL routing and API design
5. [Admin Interface](admin-interface.md) - Unfold admin customization
6. [Modules](modules.md) - Django-CFG modules and integrations

## 🔑 Key Concepts at a Glance
- **Layered Architecture**: Models → Managers → Services → Views → Admin
- **Business Logic in Managers**: Models for schema, managers for operations
- **Type Safety First**: Pydantic 2 for services, Django ORM for CRUD
- **URL Separation**: Public API vs Admin endpoints
- **Auto-Configuration**: Middleware and features based on enabled apps

## 🚀 Quick Start
```python
# Layered architecture example
# models/payment.py - Schema only
class Payment(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    status = models.CharField(max_length=20)
    
    # Manager assignment
    objects = PaymentManager()

# managers/payment_managers.py - Business logic
class PaymentManager(models.Manager):
    def create_payment(self, user, amount_usd: float) -> 'Payment':
        # Business logic here
        return self.create(user=user, amount_usd=amount_usd)

# services/payment_service.py - Pydantic validation
class PaymentService:
    def create_payment(self, data: PaymentRequest) -> PaymentResponse:
        # Use manager for business logic
        payment = Payment.objects.create_payment(data.user, data.amount_usd)
        return PaymentResponse.from_orm(payment)
```

## 🏷️ Metadata
**Tags**: `patterns, architecture, managers, routing, admin`
**Status**: %%ACTIVE%%
**Complexity**: %%COMPREHENSIVE%%
**Max Lines**: 400 (this file: 80 lines)

---

## 🏗️ Architecture Patterns

### Layered Architecture
- **Models**: Database schema and relationships only
- **Managers**: Complex queries and business operations
- **Services**: Business logic with Pydantic validation
- **Views**: HTTP handling and serialization
- **Admin**: Custom admin interfaces and actions

### Type Safety Strategy
- **Django ORM**: For database operations and CRUD
- **Pydantic 2**: For service layer and API validation
- **Zero Raw JSON**: All data structures properly typed

### URL Structure
- **`urls.py`**: Public API for Revolution client generation
- **`urls_admin.py`**: Internal admin interfaces and management

## 🎯 Development Philosophy

### Business Logic Placement
```python
# ✅ CORRECT: Business logic in managers
class PaymentManager(models.Manager):
    def create_payment(self, user, amount: float) -> 'Payment':
        # Validation and business logic
        if amount < 1.0:
            raise ValidationError("Minimum amount is $1.00")
        return self.create(user=user, amount=amount)

# ❌ WRONG: Business logic in models
class Payment(models.Model):
    def create_payment(self, amount):  # Don't do this
        pass
```

### Service Layer Pattern
```python
# ✅ CORRECT: Services orchestrate managers
class PaymentService:
    def create_payment(self, data: PaymentRequest) -> PaymentResponse:
        # Use manager for business logic
        payment = Payment.objects.create_payment(data.user, data.amount)
        
        # Convert to Pydantic response
        return PaymentResponse.from_orm(payment)
```

### Admin Integration
```python
# ✅ CORRECT: Rich admin interfaces
@admin.register(Payment)
class PaymentAdmin(ModelAdmin):
    list_display = ['id', 'amount', 'status', 'created_at']
    actions = ['process_payments']
    
    def process_payments(self, request, queryset):
        # Use manager for business operations
        for payment in queryset:
            Payment.objects.process_payment(payment)
```

---

Navigate to specific pattern documentation for detailed examples and best practices.
