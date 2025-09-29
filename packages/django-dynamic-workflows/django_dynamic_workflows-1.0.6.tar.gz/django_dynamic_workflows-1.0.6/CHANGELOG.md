# Changelog

All notable changes to django-dynamic-workflows will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.6] - 2025-09-28

### 🔧 DRF Spectacular Compatibility Fixes
- **Fixed type hint warnings**: Added `@extend_schema_field` decorators to all SerializerMethodField methods in serializers
- **Resolved GenericForeignKey warnings**: Created custom `GenericForeignKeyField` to properly handle Pipeline.department field serialization
- **Enhanced API documentation**: All serializer method fields now have proper type annotations for OpenAPI schema generation
- **Improved field resolution**: Replaced direct department field usage with department_detail field using custom serializer

### 📋 Technical Improvements
- **Added drf-spectacular import**: Imported extend_schema_field decorator for type hint support
- **Custom field implementation**: Created GenericForeignKeyField class for consistent GenericForeignKey serialization
- **Type safety**: All SerializerMethodField methods now have explicit return type declarations
- **Schema compliance**: Full compatibility with drf-spectacular OpenAPI schema generation

### 🚫 Resolved Warnings
- Fixed "unable to resolve type hint" warnings for all serializer method fields
- Resolved Pipeline.department model field resolution issues
- Eliminated DRF Spectacular W001 warnings across all serializers

## [1.0.5] - 2025-09-28

### 🚀 Complete Resubmission & Delegation Implementation
- **Enhanced resubmission logic**: Implemented proper `after_resubmission` handler with stage transitions and workflow event triggers
- **Added delegation logic**: New `after_delegate` handler with delegate user assignment and workflow event integration
- **WorkflowApprovalSerializer integration**: All approval actions (approve, reject, delegate, resubmission) now use `advance_flow` with proper parameter passing
- **Comprehensive test coverage**: Completely rewritten flow tests using WorkflowApprovalSerializer instead of manual assignment

### 🔧 Workflow Engine Improvements
- **Handler integration**: Added `ActionType.AFTER_DELEGATE` and `ActionType.AFTER_RESUBMISSION` workflow event triggers
- **Stage transition logic**: Resubmission properly updates workflow attachment to target resubmission stage
- **Metadata tracking**: Resubmission steps include `resubmission_stage_id` in extra_fields for audit trail
- **Error handling**: Improved error handling and validation in serializer save method

### 📋 Testing & Validation
- **advance_flow integration tests**: Added comprehensive mocking tests to verify correct parameter passing to approval workflow
- **End-to-end flow tests**: New tests validate complete approval progression using proper serializer patterns
- **Real workflow simulation**: Tests now use actual WorkflowApprovalSerializer patterns from production implementations

### 📚 Documentation Updates
- **Feature highlights**: Updated README with new resubmission and delegation capabilities
- **Implementation notes**: Added documentation about workflow event triggers and stage transitions
- **Known limitations**: Documented step number conflict issue in approval workflow package for resubmission edge cases

## [1.0.4] - 2025-09-27

### 🔄 Clone Tracking & API Improvements
- **Added `cloned_from` field**: All workflow models (WorkFlow, Pipeline, Stage) now automatically track their clone origin
- **Enhanced clone functionality**: Base clone method automatically sets clone relationships and handles field copying
- **Improved API consistency**: Renamed `department_object_id` to `department_id` for cleaner, more intuitive API

### 📚 Configuration Documentation
- **Comprehensive configuration guide**: Added detailed DEPARTMENT_MODEL setting documentation to README
- **Flexible department mapping**: Document support for mapping departments to any model (custom models, auth.Group, etc.)
- **Developer-friendly examples**: Enhanced configuration examples with real-world use cases

### 🛠 Technical Improvements
- **Optimized service functions**: Enhanced workflow data retrieval functions with better performance
- **Updated migrations**: Clean field renaming with proper migration handling
- **Code quality**: Applied formatting improvements with isort and black

### 📋 Migration Notes
- **Seamless upgrade**: Field rename handled transparently in migrations
- **No breaking changes**: All existing functionality preserved
- **130 tests passing**: Full test coverage maintained

---

## [1.0.3] - 2025-09-27

### 🔧 Model Updates
- Allowed `null=True` on timestamp and related fields to improve migration flexibility
- Ensures smoother installation on existing databases without requiring defaults

### 🛠 Migration Notes
- If upgrading from `1.0.2`, run migrations to apply the `null=True` changes
- New installs are not affected

---

## [1.0.2] - 2025-07-15

### 🚀 Enhancements
- **Refactored Department** to be fully generic and non-blocking for developer usage
- **Updated Company model**: defaults to `AUTH_USER_MODEL` for better integration
- **Optimized service helpers**: added utilities such as `get_detailed_workflow_data` with focus on performance
- **Developer support APIs**: ready-made endpoints to simplify implementation and accelerate onboarding

### 🛠 Technical Improvements
- Refined model structure for clarity and future-proofing
- Improved separation between workflow orchestration and developer integration layers

### 📋 Migration Notes
- Fully backward compatible
- Developers can now use generic departments without schema changes

---

## [1.0.1] - 2024-12-27

### 🎉 Production-Ready Release
This release marks the completion of extensive testing, optimization, and internationalization work, making django-dynamic-workflows fully production-ready for enterprise deployment.

### ✅ Test Coverage & Quality Improvements
- **Achieved 100% test pass rate**: Fixed all 58 failing tests, now 69/69 tests pass
- **Added comprehensive test mocking**: Optimized test execution speed by 43% (70s → 40s)
- **Enhanced test reliability**: Added proper fixtures and database optimization
- **Improved error handling**: Better validation and error messages throughout

### 🌍 Internationalization & Localization
- **Full Arabic translation support**: Complete translation of all user-facing text
- **Enhanced English translations**: Refined and standardized all English text
- **RTL support**: Right-to-left text rendering for Arabic interface
- **Dynamic language switching**: API responses adapt to request language headers
- **Translated components**:
  - Model verbose names and field labels
  - Validation error messages and API responses
  - Email templates and notifications
  - Admin interface and help text

### 📊 Advanced Logging & Monitoring
- **Structured logging system**: Comprehensive workflow operation tracking
- **Performance monitoring**: Execution time tracking for optimization
- **Contextual logging**: Rich metadata for debugging and analysis
- **Workflow event tracking**: Complete audit trail of all workflow operations
- **Error tracking**: Detailed error logging with context information

### 🚀 Performance Optimizations
- **Faster test execution**: Comprehensive mocking strategy for slow operations
- **Database optimizations**: Reduced query count and improved caching
- **Email backend mocking**: Eliminated slow email operations in tests
- **Memory usage improvements**: Optimized object creation and cleanup

### 🔧 Developer Experience Enhancements
- **Better error messages**: Clear, actionable error descriptions in both languages
- **Improved documentation**: Enhanced README with clearer examples
- **Translation management**: Added management commands for translation compilation
- **Development tools**: Optimized pytest configuration and test fixtures

### 📦 Package Improvements
- **Updated dependencies**: Removed version pinning for latest compatibility
- **Enhanced metadata**: Improved package description and keywords
- **Better structure**: Organized code with clear separation of concerns
- **Documentation updates**: Added TRANSLATIONS.md with comprehensive i18n guide

### 🛠 Technical Improvements
- **Serializer enhancements**: Better validation logic and error handling
- **Service layer optimization**: More efficient workflow operations
- **Model improvements**: Enhanced progress calculation and status management
- **API refinements**: More robust request/response handling

### 📋 Migration Notes
- All existing functionality remains backward compatible
- New translation files need to be compiled: `python manage.py compilemessages`
- Recommended to update to latest dependency versions
- Enhanced logging may increase log volume (configure appropriately)

### 🎯 Use Case Validation
Successfully tested for:
- CRM workflow replacement scenarios
- Multi-tenant enterprise applications
- High-volume workflow processing
- International deployments requiring Arabic/English support
- Complex approval processes with multiple stages

---

## [1.0.0] - 2024-09-26

### Added
- Initial release of Django Dynamic Workflows
- Generic workflow attachment system for any Django model
- Database-stored configurable actions with inheritance system
- Integration with django-approval-workflow package
- WorkFlow, Pipeline, Stage hierarchical structure
- WorkflowAction model with database-stored function paths
- Action inheritance: Stage → Pipeline → Workflow → Default
- Default email actions for all workflow events
- WorkflowAttachment model for generic model binding
- WorkflowConfiguration for model registration
- Comprehensive admin interface
- Action types: AFTER_APPROVE, AFTER_REJECT, AFTER_RESUBMISSION, AFTER_DELEGATE, AFTER_MOVE_STAGE, AFTER_MOVE_PIPELINE, ON_WORKFLOW_START, ON_WORKFLOW_COMPLETE
- Dynamic function execution system
- Rich context passing to action functions
- Progress tracking and status management
- API serializers for workflow approval actions
- Comprehensive usage examples and documentation

### Features
- Attach workflows to any model without hardcoded relationships
- Configure workflow actions dynamically in database
- Execute Python functions by database-stored paths
- Smart email notifications with automatic recipient detection
- Workflow progression through approval actions only
- Error resilient action execution with logging
- Django admin integration with rich interfaces
- Support for metadata and custom parameters

### Dependencies
- Django >= 4.0
- django-approval-workflow >= 0.8.0
