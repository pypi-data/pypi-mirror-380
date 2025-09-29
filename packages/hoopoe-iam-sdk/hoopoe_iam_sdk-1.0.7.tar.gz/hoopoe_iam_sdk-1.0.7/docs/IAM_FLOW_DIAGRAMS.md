# Hoopoe IAM Service - Comprehensive Flow Diagrams

This document provides comprehensive flow diagrams for the Hoopoe IAM Service, illustrating the relationships and data flows between different components.

## Overview

The Hoopoe IAM Service provides Identity and Access Management capabilities with the following key flows:
1. **Administrative Setup Flow**: Admin → Organization → Application → API Keys
2. **User Authentication & Authorization Flow**: Client/App → User → Roles → Permissions
3. **Login & Session Management Flow**: User → Login → Devices → Tokens

---

## 1. Administrative Setup Flow

```mermaid
graph TB
    A[Admin User] --> B[Create Organization]
    B --> C[Organization Created]
    C --> D[Create Application]
    D --> E[Application Created]
    E --> F[Generate API Keys]
    F --> G[Access Key + Secret Key]

    subgraph "Database Tables"
        H[iam_organizations]
        I[iam_applications]
        J[iam_api_keys]
    end

    B --> H
    D --> I
    F --> J

    subgraph "API Endpoints"
        K[POST /admin/organizations]
        L[POST /admin/applications]
        M[POST /admin/api-keys]
    end

    B --> K
    D --> L
    F --> M

    style A fill:#e1f5fe
    style G fill:#c8e6c9
```

### Administrative Setup Process:

1. **Admin Authentication**: Admin uses bearer token authentication with `IAM_ADMIN_API_KEY`
2. **Organization Creation**: Admin creates organization through `/admin/organizations` endpoint
3. **Application Registration**: Admin creates application under organization via `/admin/applications`
4. **API Key Generation**: Admin generates access/secret key pairs for application authentication

### Key Database Tables:
- **iam_organizations**: Stores organization metadata and settings
- **iam_applications**: Stores application configurations linked to organizations
- **iam_api_keys**: Stores AWS-style access/secret key pairs for application authentication

---

## 2. User Authentication & Authorization Flow

```mermaid
graph TB
    A[Client Application] --> B[Authenticate with API Keys]
    B --> C[User Registration/Login]
    C --> D[User Account Created]
    D --> E[Role Assignment]
    E --> F[Permission Mapping]
    F --> G[Access Control]

    subgraph "Authentication Methods"
        H[X-IAM-Access-Key]
        I[X-IAM-Secret-Key]
        J[Bearer Token]
    end

    subgraph "Database Tables"
        K[iam_users]
        L[iam_accounts]
        M[iam_roles]
        N[iam_role_assignments]
        O[iam_permissions]
        P[iam_permission_grants]
    end

    subgraph "API Endpoints"
        Q[POST /users/register]
        R[POST /auth/login]
        S[POST /admin/roles]
        T[POST /admin/role-assignments]
    end

    B --> H
    B --> I
    C --> J

    C --> K
    D --> L
    E --> M
    E --> N
    F --> O
    F --> P

    C --> Q
    C --> R
    E --> S
    E --> T

    style A fill:#e1f5fe
    style G fill:#c8e6c9
```

### User Authentication Process:

1. **Application Authentication**: Client app authenticates using API access/secret keys
2. **User Operations**: App can register users or facilitate user login
3. **Account Creation**: Each user gets an account per application/organization
4. **Role Assignment**: Users are assigned roles (e.g., premium-user, moderator, admin)
5. **Permission Mapping**: Roles are mapped to specific permissions
6. **Access Control**: System enforces permissions for resource access

### Key Database Tables:
- **iam_users**: Global user records with credentials
- **iam_accounts**: User accounts scoped to specific app/organization combinations
- **iam_roles**: Role definitions with scope and level
- **iam_role_assignments**: Links users to roles within organizations
- **iam_permissions**: Permission definitions for various resources
- **iam_permission_grants**: Grants specific permissions to users or roles

---

## 3. Login & Session Management Flow

```mermaid
graph TB
    A[User Login Request] --> B[Credentials Validation]
    B --> C[Password Verification]
    C --> D[Account Status Check]
    D --> E[Role Collection]
    E --> F[JWT Token Generation]
    F --> G[Session Creation]
    G --> H[Device Registration]
    H --> I[Audit Logging]
    I --> J[Token Response]

    subgraph "Token Types"
        K[Access Token]
        L[Refresh Token]
        M[Token Cache]
    end

    subgraph "Database Tables"
        N[iam_token_sessions]
        O[iam_user_devices]
        P[iam_audit_logs]
        Q[iam_access_controls]
    end

    subgraph "Security Features"
        R[Failed Login Tracking]
        S[Account Locking]
        T[IP Monitoring]
        U[Risk Scoring]
    end

    F --> K
    F --> L
    F --> M

    G --> N
    H --> O
    I --> P
    I --> Q

    B --> R
    C --> S
    I --> T
    I --> U

    style A fill:#e1f5fe
    style J fill:#c8e6c9
```

### Login Session Process:

1. **Authentication**: User provides identifier (email/username) and password
2. **Validation**: System verifies credentials and checks account status
3. **Security Checks**: Failed login tracking, account locking, risk assessment
4. **Role Resolution**: Collect user roles for the specific application/organization
5. **Token Generation**: Create JWT access and refresh tokens with role claims
6. **Session Tracking**: Store session information with JTI tracking
7. **Device Registration**: Track device information for security monitoring
8. **Audit Logging**: Log all authentication events with risk scores
9. **Response**: Return tokens and user/account information

### Key Database Tables:
- **iam_token_sessions**: JWT session tracking with access/refresh JTIs
- **iam_user_devices**: Device fingerprinting and tracking
- **iam_audit_logs**: Comprehensive authentication and authorization audit trail
- **iam_access_controls**: Real-time access control rules and violations

---

## 4. Complete System Architecture

```mermaid
graph TB
    subgraph "Admin Layer"
        A1[System Admin]
        A2[Organization Admin]
    end

    subgraph "Application Layer"
        B1[Client Applications]
        B2[Hoopoe IAM SDK]
        B3[API Authentication]
    end

    subgraph "IAM Service Core"
        C1[Authentication Service]
        C2[Authorization Service]
        C3[User Management]
        C4[Session Management]
        C5[Audit Service]
    end

    subgraph "Database Layer"
        D1[Organizations & Applications]
        D2[Users & Accounts]
        D3[Roles & Permissions]
        D4[Sessions & Devices]
        D5[Audit & Security]
    end

    subgraph "Security Features"
        E1[JWT Token Management]
        E2[Rate Limiting]
        E3[Risk Assessment]
        E4[Device Tracking]
        E5[Audit Logging]
    end

    A1 --> C3
    A2 --> C3
    B1 --> B2
    B2 --> B3
    B3 --> C1
    C1 --> C2
    C1 --> C4
    C1 --> C5
    C2 --> C5
    C3 --> D2
    C1 --> D4
    C2 --> D3
    C4 --> D4
    C5 --> D5

    C1 --> E1
    C1 --> E3
    C4 --> E4
    C5 --> E5

    style A1 fill:#ffebee
    style A2 fill:#ffebee
    style B1 fill:#e3f2fd
    style C1 fill:#e8f5e8
    style D1 fill:#fff3e0
    style E1 fill:#f3e5f5
```

---

## 5. Data Flow Summary

### Administrative Flow:
1. **Admin** → Creates **Organization** → Creates **Application** → Generates **API Keys**
2. Database: `iam_organizations` → `iam_applications` → `iam_api_keys`

### Application Authentication Flow:
1. **Client App** → Authenticates with **API Keys** → Accesses **IAM Endpoints**
2. Headers: `X-IAM-Access-Key` + `X-IAM-Secret-Key` or `Authorization: Bearer {token}`

### User Lifecycle Flow:
1. **User Registration** → **Account Creation** → **Role Assignment** → **Permission Mapping**
2. Database: `iam_users` → `iam_accounts` → `iam_role_assignments` → `iam_permission_grants`

### Login Session Flow:
1. **Login Request** → **Authentication** → **Token Generation** → **Session Creation** → **Device Tracking**
2. Database: `iam_token_sessions` + `iam_user_devices` + `iam_audit_logs`

### Security & Audit Flow:
1. **All Operations** → **Risk Assessment** → **Audit Logging** → **Access Control** → **Monitoring**
2. Database: `iam_audit_logs` + `iam_access_controls` + security metrics

---

## 6. Database Table Relationships

```mermaid
erDiagram
    IAM_ORGANIZATIONS ||--o{ IAM_APPLICATIONS : contains
    IAM_APPLICATIONS ||--o{ IAM_API_KEYS : has
    IAM_APPLICATIONS ||--o{ IAM_ACCOUNTS : scoped_to
    IAM_ORGANIZATIONS ||--o{ IAM_ACCOUNTS : belongs_to

    IAM_USERS ||--o{ IAM_ACCOUNTS : has
    IAM_USERS ||--o{ IAM_TOKEN_SESSIONS : owns
    IAM_USERS ||--o{ IAM_USER_DEVICES : registers
    IAM_USERS ||--o{ IAM_AUDIT_LOGS : subject_of

    IAM_ACCOUNTS ||--o{ IAM_ROLE_ASSIGNMENTS : assigned
    IAM_ROLES ||--o{ IAM_ROLE_ASSIGNMENTS : defines
    IAM_ROLES ||--o{ IAM_PERMISSION_GRANTS : grants
    IAM_PERMISSIONS ||--o{ IAM_PERMISSION_GRANTS : granted

    IAM_TOKEN_SESSIONS ||--o{ IAM_AUDIT_LOGS : triggers
    IAM_USER_DEVICES ||--o{ IAM_AUDIT_LOGS : tracked_in
    IAM_ACCESS_CONTROLS ||--o{ IAM_AUDIT_LOGS : enforces
```

---

## Implementation Notes

### Security Considerations:
- All passwords are hashed using bcrypt
- JWT tokens include expiration and role-based claims
- Failed login attempts trigger account locking
- All operations are audit logged with risk scoring
- Device fingerprinting helps detect suspicious activities

### Scalability Features:
- Token caching for improved performance
- Async database operations using SQLAlchemy
- Connection pooling for database efficiency
- Modular service architecture for horizontal scaling

### Integration Points:
- RESTful API endpoints for all operations
- Python SDK for easy integration
- Standardized error responses
- Comprehensive audit trail for compliance

This comprehensive flow documentation should help understand the complete IAM system architecture and data flows within the Hoopoe IAM Service.
