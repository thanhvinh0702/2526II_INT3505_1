# API Deprecation Notice — Payment API v1

## Overview

The Payment API `v1` has been officially deprecated and will be sunset on **2026-12-01**.

Developers are strongly encouraged to migrate to **API v2** as soon as possible to ensure uninterrupted service.

---

## Important Dates

| Event | Date |
|---|---|
| Deprecation Announcement | 2026-08-01 |
| API v1 Sunset Date | 2026-12-01 |

After the sunset date, all requests to:

/api/v1/payment

may stop functioning or return errors.

---

# Why We Introduced v2

API v2 improves:

- Data consistency
- Validation rules
- Transaction tracking
- Future extensibility
- Payment auditing support

---

# What Happens in v1

All responses from API v1 now include deprecation metadata in both:

- HTTP Headers
- JSON Response Body

Example headers:

```http
Deprecation: true
Sunset: 2026-12-01
Warning: 299 - "API v1 is deprecated. Please migrate to API v2 before 2026-12-01"
Link: </api/docs/v2-migration>; rel="deprecation"; type="text/html"
```
Example response body:

```
{
  "version": "v1",
  "status": "success",
  "message": "Payment processed",
  "deprecated": true,
  "deprecation_notice": {
    "deprecated_since": "2026-08-01",
    "sunset_date": "2026-12-01",
    "migration_guide": "/api/docs/v2-migration"
  }
}
```

# Migration Guide
Migration documentation is available at:
```
GET /api/docs/v2-migration
```

# Breaking Changes in v2

| Field | v1 | v2 |
|---|---|---|
| amount | string | integer |
| currency | optional | required |
| transaction_id | unavailable | included in response |

# Example API Usage
## v1 Request

```
POST /api/v1/payment
Content-Type: application/json
```

```
{
  "amount": "1000"
}
```

## v2 Request
```
POST /api/v2/payment
Content-Type: application/json
```

```
{
  "amount": 1000,
  "currency": "USD"
}
```

## v2 Response
```
{
  "version": "v2",
  "status": "success",
  "transaction_id": "TXN-123456",
  "processed_at": "2026-05-07T12:00:00",
  "message": "Payment processed successfully"
}
```

# Support
If you encounter migration issues, contact:
```
support@payment-api.local
```
or refer to the migration guide endpoint.