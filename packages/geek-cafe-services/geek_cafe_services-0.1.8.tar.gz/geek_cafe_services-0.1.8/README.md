# Geek Cafe Services

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![DynamoDB](https://img.shields.io/badge/database-DynamoDB-orange.svg)](https://aws.amazon.com/dynamodb/)
[![AWS Lambda](https://img.shields.io/badge/runtime-AWS%20Lambda-yellow.svg)](https://aws.amazon.com/lambda/)

## Description

**Geek Cafe Services** is a production-ready, enterprise-grade library that provides reusable database services specifically designed for multi-tenant SaaS applications. Built on top of AWS DynamoDB, this library offers a prescriptive approach to building scalable, maintainable backend services with consistent patterns and best practices.

### Why Geek Cafe Services?

🏗️ **Consistent Architecture**: All services follow the same proven patterns for CRUD operations, error handling, and access control  
🔒 **Multi-Tenant by Design**: Built-in tenant isolation ensures secure data separation across customers  
⚡ **DynamoDB Optimized**: Leverages DynamoDB's strengths with efficient GSI indexes and query patterns  
🛡️ **Production Ready**: Comprehensive error handling, logging, pagination, and batch operations  
🧪 **Fully Tested**: 100% test coverage with comprehensive test suites for reliability  
📖 **Well Documented**: Extensive documentation with practical examples and best practices  

### Perfect For

- **SaaS Applications** requiring multi-tenant data isolation
- **Serverless Architectures** built on AWS Lambda and DynamoDB
- **Teams** wanting consistent, proven patterns across services
- **Rapid Development** with pre-built, tested service components

## Installation

```bash
# Clone the repository
git clone https://github.com/geekcafe/geek-cafe-services.git
cd geek-cafe-services

# Setup the development environment
./pysetup.sh

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

```python
from geek_cafe_services.message_service import MessageService

# Initialize service
service = MessageService()

# Create a message
result = service.create(
    tenant_id="your_tenant",
    user_id="your_user",
    type="notification",
    content={"title": "Welcome!", "body": "Thanks for joining us."}
)

if result.success:
    print(f"Created message: {result.data.id}")
```

## Available Services

### 📧 MessageService
**Purpose**: Complete message and notification management system

**Key Capabilities**:
- ✅ Full CRUD operations with tenant isolation
- ✅ Flexible JSON content storage for any message type
- ✅ Efficient querying by user, tenant, and message type
- ✅ Automatic audit trails and timestamps
- ✅ Built-in access control and validation

**Use Cases**: User notifications, system alerts, communication logs, announcement management

### 🗳️ Voting Services Suite
**Purpose**: Complete voting and rating system with real-time aggregation

**Architecture**: Three interconnected services working together:

#### VoteService
- ✅ Individual vote management with automatic upsert behavior
- ✅ One vote per user per target enforcement
- ✅ Support for up/down votes or custom vote types
- ✅ Comprehensive querying by user, target, and tenant

#### VoteSummaryService  
- ✅ Pre-calculated vote totals for instant retrieval
- ✅ Target-based optimization for high-performance lookups
- ✅ Metadata tracking (last tallied timestamp, vote counts)
- ✅ Tenant-scoped summary management

#### VoteTallyService
- ✅ Intelligent vote aggregation with pagination support
- ✅ Batch processing for multiple targets
- ✅ Stale target detection and automated re-tallying
- ✅ Comprehensive error handling and resilience

**Use Cases**: Product ratings, content voting, feedback systems, community polls, recommendation engines

## Documentation

📖 **[Complete Documentation](./docs/services_overview.md)**

- [Services Overview](./docs/services_overview.md) - Architecture and common patterns
- [MessageService](./docs/message_service.md) - Message management API
- [Voting Services](./docs/voting_services.md) - Complete voting system documentation
- [A/B Testing Guide](./docs/ab_testing_guide.md) - Using voting services for A/B testing and experimentation
- [Development Roadmap](./docs/roadmap.md) - Planned improvements and enhancements

## Core Features

### 🏛️ **Enterprise Architecture**
- **Multi-Tenant by Design**: Complete tenant isolation with automatic access control
- **Consistent Patterns**: All services follow identical CRUD interfaces and conventions
- **Scalable Design**: Built for high-throughput, multi-customer SaaS applications

### 🔧 **Developer Experience**
- **Type Safety**: Full Python type hints for better IDE support and fewer bugs
- **Comprehensive Testing**: 100% test coverage with realistic test scenarios
- **Rich Documentation**: Detailed API docs, examples, and best practices
- **Easy Integration**: Simple initialization and consistent error handling

### ⚡ **Performance & Reliability**
- **DynamoDB Optimized**: Efficient GSI indexes and query patterns for fast operations
- **Pagination Support**: Handle large datasets without memory issues
- **Batch Operations**: Process multiple items efficiently
- **Error Resilience**: Graceful handling of partial failures and edge cases

### 🛡️ **Production Ready**
- **Structured Logging**: AWS Lambda Powertools integration for observability
- **Comprehensive Validation**: Input validation with detailed error messages  
- **Access Control**: Automatic tenant and user-based security enforcement
- **Audit Trails**: Complete tracking of who did what and when

## Environment Setup

```bash
# Required environment variables
export DYNAMODB_TABLE_NAME=your_table_name

# Optional AWS configuration (if not using IAM roles)
export AWS_REGION=us-east-1
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
```

## Testing

```bash
# Run all tests
pytest tests/ -v

# Run specific service tests
pytest tests/test_message_service.py -v
pytest tests/test_vote_*_service.py -v

# Run with coverage
pytest tests/ --cov=geek_cafe_services --cov-report=html
```

## Project Structure

```
geek-cafe-services/
├── src/geek_cafe_services/
│   ├── models/              # Data models with DynamoDB mapping
│   ├── *_service.py         # Service implementations
│   ├── database_service.py  # Base service class
│   └── service_result.py    # Standardized response wrapper
├── tests/                   # Comprehensive test suite
├── docs/                    # Detailed documentation
└── README.md               # This file
```

## Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository** and create a feature branch
2. **Follow the existing patterns** - consistency is key
3. **Add comprehensive tests** for any new functionality  
4. **Update documentation** for API changes
5. **Submit a Pull Request** with a clear description

### Development Guidelines

- Follow existing code style and patterns
- Maintain 100% test coverage for new code
- Update documentation for any API changes
- Use meaningful commit messages
- Test against multiple Python versions if possible

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 📖 **Documentation**: [Complete docs](./docs/services_overview.md)
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/geekcafe/geek-cafe-services/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/geekcafe/geek-cafe-services/discussions)
- 📧 **Questions**: Create an issue with the "question" label

---

**Built with ❤️ for the SaaS development community**
