# Contributing Guide

Thank you for your interest in contributing to SamaBrains AI projects.

## Code Standards

### Python Style

- Follow PEP 8.
- Use type hints for function signatures.
- Keep functions focused and testable.
- Add docstrings when they provide useful context.

### Comments

- Comment why something is done, not what each line does.
- Explain important assumptions and limitations.
- Keep comments short and useful.

### Testing

- Test new behavior when practical.
- Cover important happy paths and error cases.
- Use descriptive test names.

## Development Setup

```bash
git clone <repository>
cd <project>
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

## Making Changes

1. Create a branch:

   ```bash
   git checkout -b feature/description
   ```

2. Make focused changes and test them locally.

3. Open a pull request with a clear summary and testing notes.

## Commit Message Format

```text
type(scope): brief description

Optional details about the change.
```

Common types:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation change
- `refactor`: Code restructuring
- `test`: Test additions or updates
- `perf`: Performance improvement

## Code Review Checklist

- [ ] Code follows the project style.
- [ ] Documentation is updated where needed.
- [ ] Tests or manual verification were completed.
- [ ] No unnecessary dependencies were added.
- [ ] Error handling is appropriate.
- [ ] No hardcoded secrets or credentials were introduced.

## Reporting Issues

When reporting bugs, include:

- Python version
- Operating system
- Steps to reproduce
- Expected behavior
- Actual behavior
- Relevant logs or error messages

## License

By contributing, you agree that your contributions are licensed under the MIT
License.

## Questions

Contact [contact@samabrains.com](mailto:contact@samabrains.com).
