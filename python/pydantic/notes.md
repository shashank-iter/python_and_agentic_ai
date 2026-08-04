Pydantic provides:

- Data Validation
- Setting Management
- Data Parsing and Validation
- API development
- Configuration Management
- Data Serialization/De-serialization
- Stops from data interchangability for variables, TS for Python
- Best Practices
- Define leaf model first: Model with no dependencies
- Build Upwards: from leaf to root
- Use Clear naming: make relationship obivious
- Group Related Models: together

# Performance Considerations
- Deep nestig impacts performance - Keep reasonable depth
- Large list of nested model: consider pagination
- circular references- use carefully, can cause memory issues
- lazy loading - consider for expansive nested computations
- don't overuse computed fields too much, get calculated each time

# Data Modelling Tips
- Model-Real World relationships
- use optional appropiately: not all realationship are required
- consider Union type: for polymorphic relationship
- validate business rules: use model validators for cross model logic, business rules come over performance
